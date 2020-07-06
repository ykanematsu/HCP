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
lmLp=joblib.load('Lp200704')
lmR=joblib.load('R200704')
f_pc_all=['molecular_weight','xlogp','h_bond_donor_count','h_bond_acceptor_count','rotatable_bond_count','tpsa','complexity']

def sigmoid(x):
    return 1/(1+np.exp(-x))

class psq():
    def __init__(self,sma):
        self.f_pc_Lp=['molecular_weight','xlogp','h_bond_acceptor_count','tpsa']
        self.f_pc_R=['molecular_weight','xlogp','h_bond_acceptor_count','nrot','nbridge']
        try:
            smi_c=sma.replace('([R])','').replace('[R]','').replace('([*])','').replace('[*]','').replace('(*)','').replace('*','')
            smi_r=sma.replace('([R])','C').replace('[R]','C').replace('([*])','C').replace('[*]','C').replace('(*)','C').replace('*','C')
            morg=Chem.MolFromSmarts(sma)
            self.mol=Chem.MolFromSmiles(sma)
            mrot=Chem.MolFromSmiles(smi_r)
            m=Chem.MolFromSmiles(smi_c)
            si=[at.GetIdx() for at in morg.GetAtoms() if at.GetSymbol()=='*']
            tmp=pd.Series(dtype='float64')
            tmp['nbridge']=len(Chem.rdmolops.GetShortestPath(morg,si[0],si[1]))-1
            tmp['nrot']=NumRotatableBonds(mrot)
            a=pcp.get_compounds(smi_c,'smiles')[0]
            fs=f_pc_all
            for f in fs:
                tmp[f]=eval('a.'+f)
            X_Lp=[tmp[self.f_pc_Lp]]
            X_R=[tmp[self.f_pc_R]]
            self.Lp=round(10**lmLp.predict(X_Lp)[0],3)
            self.R=round(sigmoid(lmR.predict(X_R)[0]),3)
            self.Lp_coef=lmLp.coef_
            self.X_Lp=X_Lp[0]
        except:
            self.Lp='Not available!'
            self.R='Not available!'
            self.mol=''

def qy(smis,solv=None,return_std=False):
    if type(smis) is str: smis=[smis]
    ms=[Chem.MolFromSmiles(s) for s in smis]
    fp = [pyAvalonTools.GetAvalonFP(m) for m in ms]
    if not solv: solv=np.outer(np.ones(len(smis)),[1,0,0])
    x = np.hstack([fp,solv])
    return gp.predict(x,return_std=return_std)
if __name__=='__main__':
    print(psq('*CC*'))
