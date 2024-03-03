# Delivering Locally Sourced Nutritious Food to Indian Households
___

# NOTE TO SELF:
- tell sanchita about using softmax
- ask about rice + wheat. Include? Not include?
- revisit the terminology "bin-packing". Is this really a bin-packing problem? The baskets are designed with
continuous (not discrete) amounts of each crop. 


# for sanchita
- Figure out units for production file (same as consumption?)
- Per household minimum (pulse vs millet)
- Check replicability + correctness of ode (after it's finished)

# for reuben
- Make algebraic forulation of both problems (see if they agree with each other)
- Add legend to cluster map (in general make it readable)
- Seed clustering so it's reproducible
- Get everything ready for the big model



## Replication instructions
*Rough outline*
1. Dependencies + environment
    1. Python packages: sklearn, matplotlib, numpy, pandas
    2. CPLEX runtimes: Basket Design, Distribution
2. Preference Clustering
    1. Run clustering.py to assign clusters and preferenes
    2. Visualize data with explore_consumption.ipynb
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
- /basket_design
    - connect to output of /clustering
    - add postprocessing
- / distribution
    - clean up unused parts
    - change to real travel distance times (tt_ij from google maps)
