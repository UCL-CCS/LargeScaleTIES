# LargeScaleTIES 

Input structures and parameters included for each protein system.
The directory structure is $PROTEIN/$LIGAND-PAIR/com/* and $PROTEIN/$LIGAND-PAIR/lig/*.
The former contains AMBER input files used for our simulations for complex simulations, whereas the latter contains the same for the ligand simulations.

Input for simulations using RESP charges for all 60 ligand pairs is also included in the directory called "RESP".
There are two subdirectories named "rand1" and "rand2" that contain input for each subset of 30 ligand pairs separately.
The directory structure in these subdirectories is identical to the one described above for individual protein systems.

Please note that the input structures and parameters used for REST2 simulations were the same as those of the standard TIES simulations.

"ddGs" directory contains ddG values for all ligand pairs using the standard TIES protocol as well as those for the various subsets of ligand pairs studied using RESP, REST2, large ensembles, etc. More details in "ddGs/README.txt".

"Figs_2_3" directory contains all data used to generate Figures 2 and 3. Description of the various files in this directory is available in "Figs_2_3/README.txt".
