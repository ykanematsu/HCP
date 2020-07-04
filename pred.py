import rdkit 
#from sklearn.externals import joblib
import joblib
import numpy as np
import pandas as pd
from sklearn import linear_model,cross_decomposition
from scipy.stats import binom_test
from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem.Descriptors import *
#from rdkit.Chem.rdMolDescriptors import BCUT2D
from rdkit.Chem import AllChem, rdPartialCharges
import openpyxl
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.gaussian_process import kernels as sk_kern
from sklearn.gaussian_process.kernels import ConstantKernel as C
from sklearn.gaussian_process import GaussianProcessRegressor as GPR
from sklearn.feature_selection import SelectKBest, f_regression
from rdkit.Avalon import pyAvalonTools
import pubchempy as pcp
from rdkit.Chem.PandasTools import ChangeMoleculeRendering
ChangeMoleculeRendering(renderer='PNG')

gp=joblib.load('gpr200703')
lmlp=joblib.load('Lp200704')
lmr=joblib.load('R200704')
def sigmoid(x):
    return 1/(1+np.exp(-x))

def psq(sma):
    smi_c=sma.replace('([R])','').replace('[R]','').replace('([*])','').replace('[*]','').replace('(*)','').replace('*','')
    smi_r=sma.replace('([R])','C').replace('[R]','C').replace('([*])','C').replace('[*]','C').replace('(*)','C').replace('*','C')
    morg=Chem.MolFromSmarts(sma)
    mrot=Chem.MolFromSmiles(smi_r)
    m=Chem.MolFromSmiles(smi_c)
    si=[at.GetIdx() for at in morg.GetAtoms() if at.GetSymbol()=='*']
    tmp=pd.Series(dtype='float64')
    tmp['nbridge']=len(Chem.rdmolops.GetShortestPath(morg,si[0],si[1]))-1
    tmp['nrot']=NumRotatableBonds(mrot)
    a=pcp.get_compounds(smi_c,'smiles')[0]
    fs=['molecular_weight','xlogp','h_bond_donor_count','h_bond_acceptor_count','rotatable_bond_count','tpsa','complexity']
    for f in fs:
        tmp[f]=eval('a.'+f)
    X_lp=[tmp[['molecular_weight','xlogp','h_bond_acceptor_count','tpsa']]]
    X_R=[tmp[['molecular_weight','xlogp','h_bond_acceptor_count','nrot','nbridge']]]
    return round(10**lmlp.predict(X_lp)[0],3),round(sigmoid(lmr.predict(X_R)[0]),3)

def qy(smis,solv=None,return_std=False):
    if type(smis) is str: smis=[smis]
    ms=[Chem.MolFromSmiles(s) for s in smis]
    fp = [pyAvalonTools.GetAvalonFP(m) for m in ms]
    if not solv: solv=np.outer(np.ones(len(smis)),[1,0,0])
    x = np.hstack([fp,solv])
    return gp.predict(x,return_std=return_std)
if __name__=='__main__':
    print(psq('*CC*'))
