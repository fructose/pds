# Delivering Locally Sourced Nutritious Food to Indian Households
___
## Replication instructions
*Rough outline*
1. Dependencies + environment
    1. Python packages: sklearn, matplotlib, numpy, pandas
    2. CPLEX runtimes: Basket Design, Distribution
2. Preference Clustering
    1. kmeans.ipynb walkthrough (including postprocessing)
    2. visualize with cluster_analysis
3. Basket Design
    1. CPLEX walkthrough
    2. postprocess walkthrough
4. Distribution

## Data explanation
1. Consumption
2. Travel Times
3. Production

## References

## License

## TODO:
- /data
    - clean up unused parts of 2011.xlsx
- /clustering
    - Add kmeans.ipynb
        - connect to new data location (/data/consumption.csv)
        - add postprocessing to kmeans.ipynb
    - Write cluster_analysis.py
- /basket_design
    - add postprocessing
- / distribution
    - change to real travel distance times (tt_ij from google maps)
