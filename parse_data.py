import h5py
import numpy as np

# load in h5 files
rxns= h5py.File('XXX/RGD1_CHNO.h5', 'r')
RPs = h5py.File('XXX/RGD1_RPs.h5', 'r')

# load in molecule dictionary
lines = open('XXX/RandP_smiles.txt', 'r', encoding="utf-8").readlines()
RP_dict = dict()
for lc,line in enumerate(lines):
    if lc == 0: continue
    RP_dict[line.split()[0]] = line.split()[1]

# convert number to symbol
num2element = {1:'H', 6:'C', 7:'N', 8:'O', 9:'F'}

missing_mols,missing_rxns = [],[]
for Rind,Rxn in rxns.items():

    #print(f"Paring Reaction {Rind}")

    # parse SPE
    R_E,P_E,TS_E = np.array(Rxn.get('R_E')),np.array(Rxn.get('P_E')),np.array(Rxn.get('TS_E'))

    # parse enthalpy
    R_H,P_H,TS_H = np.array(Rxn.get('R_H')),np.array(Rxn.get('P_H')),np.array(Rxn.get('TS_H'))
    
    # parse Gibbs free energy
    R_F,P_F,TS_F = np.array(Rxn.get('R_F')),np.array(Rxn.get('P_F')),np.array(Rxn.get('TS_F'))
    
    # parse smiles
    Rsmiles,Psmiles = Rxn.get('Rsmiles')[()].decode('utf-8'), Rxn.get('Psmiles')[()].decode('utf-8') 

    # parse elements
    elements = [num2element[Ei] for Ei in np.array(Rxn.get('elements'))]
    
    # parse geometries
    TS_G = np.array(Rxn.get('TSG'))    
    R_G = np.array(Rxn.get('RG'))
    P_G = np.array(Rxn.get('PG'))
    # Note: RP and PG are unoptimized

    # load in seperated reactant/product molecules
    Rmols = [RP_dict[i] for i in Rsmiles.split('.')]
    Pmols = [RP_dict[i] for i in Rsmiles.split('.')]
    for mol in Rmols+Pmols:
        # obtain the corresponding molecule
        try:
            molecule = RPs[mol]
            # obtain DFT level energy and geometry
            DFT_G = np.array(molecule.get('DFTG'))
            DFT_SPE = np.array(molecule.get('DFT_SPE'))
            # note: other keys are '_id', 'elements', 'xTBG', 'xTB_SPE'
        except:
            print(f"In rxn {Rind}, molecule {mol} info is missing")
            missing_mols.append(mol)
            missing_rxns.append(Rind)

