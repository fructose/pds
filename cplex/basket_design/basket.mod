/*********************************************
 * OPL 22.1.1.0 Model
 * Author: reube
 * Creation Date: Jan 30, 2024 at 11:14:53 AM
 *********************************************/
range Clusters = 0..5;
range Crops = 1..16;
range Grains = 1..6;
range Pulses = 7..16;
range Districts = 1..625;

string crops[Crops] = ... ;

float preferences[Crops][Clusters] = ... ;

int households[Clusters] = ... ;

string districts[Districts] = ... ;

int households_district[Districts] = ... ;

int clusters_district[Districts] = ... ;


execute {
  writeln(preferences);
  writeln(households);
};

float available[Crops] = [3000,3000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000];

float min_grain = .00005 ; // Per household
float min_pulse = .00003 ; // Per household

dvar float+ basket[Crops][Clusters];

dexpr float utility = ( sum (crop in Crops, cluster in Clusters) (preferences[crop][cluster] * basket[crop][cluster]));

maximize utility ;

subject to {
  
  // Minimum basket content constraints
  forall ( cluster in Clusters ) {
    ct1: ( sum ( grain in Grains ) basket[grain][cluster] ) == min_grain * households[cluster];
    ct2: ( sum ( puls in Pulses) basket[puls][cluster] ) == min_pulse * households[cluster];
  }
  
  // Baskets do not exceed available
  forall ( crop in Crops ) {
    ct3: ( sum (cluster in Clusters) basket[crop][cluster] ) <= available[crop] ;
  }
  
}

// After solving the model, write demand by district to a csv file:

// We know the total population of a cluster, (households)
// and the assignment of crops to each cluster, (basket)
// and the population + cluster assignment of each district, (districts, households_district, clusters_district)
// I want to write it to a csv file with the first column 'district', and the other columns the strings in crops
// The values for each district should be the demand assigned to that district,
// cluster_total_demand * district_population / cluster_population
// for each crop


execute {
  var f = new IloOplOutputFile("../distribution/demand.csv");
  var header = "district"; // Start building the header string
  
  for(var c in Crops) {
    header += "," + crops[c]; // Append each crop name to the header
  }
  
  f.writeln(header); // Write the complete header to the file

  for(var d in Districts) {
    var districtName = districts[d];
    var demandLine = districtName; // Start line with district name
    
    for(var c in Crops) {
      var totalCropDemandInDistrict = 0;
      
      for(var cl in Clusters) {
        if(clusters_district[d] == cl) { // Assuming clusters_district[d] gives the cluster of district d
          var clusterTotalDemandForCrop = basket[c][cl];
          var districtPopulation = households_district[d];
          var clusterPopulation = households[cl];
          
          var districtDemandForCrop = (clusterTotalDemandForCrop * districtPopulation) / clusterPopulation;
          totalCropDemandInDistrict += districtDemandForCrop;
        }
      }
      
      demandLine += "," + totalCropDemandInDistrict;
    }
    
    f.writeln(demandLine); // Write the calculated demand for this district
  }
  
  f.close();
}
