# The standard format of all files is: Column I --> Ligand pair; Column II --> ddG_calc; Column III --> error bar on ddG_calc; Column IV --> ddG_exp
# All values are in kcal/mol

*_ddG.dat: Protein-wise ddG values for all ligand pairs using the standard TIES protocol.

RESP: ddGs for subsets "rand1" and "rand2" using the RESP charge model for ligands.

REST2: ddGs for subsets "rand1" and "rand2" using the enhanced sampling protocol REST2.

large-alch-diff: ddGs for the 43 ligand transformations with the difference between disappearing and appearing atoms of greater than 10.

large_ensembles: ddGs using large ensembles of sizes 10 or 20 for selected MCL1 and PTP1B ligand pairs. Also, contains ddGs for PTP1B ligand pairs using smaller alchemical region.

pde-tr-size: Contains ddGs separately for "s2s", "l2l" and "s2l" ligand pairs of PDE2 system.

