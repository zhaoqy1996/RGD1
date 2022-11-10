import h5py
import numpy as np

hf = h5py.File('RGD1_CHNO.h5', 'r')

# convert number to symbok
num2element = {1:'H', 6:'C', 7:'N', 8:'O', 9:'F'}

for Rind,Rxn in hf.items():

    print("Paring Reaction {}".format(Rind))

    # parse SPE
    R_E,P_E,TS_E = np.array(Rxn.get('R_E')),np.array(Rxn.get('P_E')),np.array(Rxn.get('TS_E'))

    # parse enthalpy
    R_H,P_H,TS_H = np.array(Rxn.get('R_H')),np.array(Rxn.get('P_H')),np.array(Rxn.get('TS_H'))
    
    # parse Gibbs free energy
    R_F,P_F,TS_F = np.array(Rxn.get('R_F')),np.array(Rxn.get('P_F')),np.array(Rxn.get('TS_F'))
    
    # parse smiles
    Rsmiles,Psmiles = str(np.array(Rxn.get('Rsmiles'))),str(np.array(Rxn.get('Psmiles')))

    # parse elements
    elements = [num2element[Ei] for Ei in np.array(Rxn.get('elements'))]
    
    # parse geometries
    TS_G = np.array(Rxn.get('TSG'))    
    R_G = np.array(Rxn.get('RG'))
    P_G = np.array(Rxn.get('PG'))

