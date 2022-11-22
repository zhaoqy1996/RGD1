## Reaction Graph Depth 1 (RGD1) database
This reaction database is generated by manuscript "[Comprehensive exploration of graphically defined reaction spaces](https://chemrxiv.org/engage/chemrxiv/article-details/6377f78974b7b66185035734)."

The additional data files are provided on [FigShare](https://figshare.com/articles/dataset/model_reaction_database/21066901). The csv file named as RGD1CHNO_smiles.csv contains atom-mapped SMILES, activation energies, and enthalpies of formation for each reaction. The HDF5 file contains the geometry information and can be iterated by a python script (parse\_data.py). An additional csv file (DFT_reaction_info.csv) is supplied to reproduce figures in the article.

* **Usage of python code**
    - parse\_data.py: This script parses all of the model reactions stored in a HDF5 file which can be freely downloaded from figshare.

    - make\_stat\_plots.py: This script parses the a csv file of reaction features and makes bar plots of different reaction features as DE\_break\_dist.pdf

    - draw\_violin.py: This script parses csv files of reaction features and DFT energies and makes violin plots of the activation energy distribution of different reaction types as reaction\_stat.pdf
