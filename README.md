# Delivering Locally Sourced Nutritious Food to Indian Households
___

# NOTE TO SELF:
## tell sanchita about using softmax

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
