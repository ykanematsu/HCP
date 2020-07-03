import rdkit 
from sklearn.externals import joblib
import numpy as np
import pandas as pd
from sklearn import linear_model,cross_decomposition
from sklearn.model_selection import cross_val_score,cross_val_predict
from scipy.stats import binom_test
from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem.Descriptors import *
#from rdkit.Chem.rdMolDescriptors import BCUT2D
from rdkit.Chem import AllChem, rdPartialCharges
import matplotlib.pyplot as plt
import openpyxl
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.gaussian_process import kernels as sk_kern
from sklearn.gaussian_process.kernels import ConstantKernel as C
from sklearn.gaussian_process import GaussianProcessRegressor as GPR
from sklearn.feature_selection import SelectKBest, f_regression
from rdkit.Avalon import pyAvalonTools


gp=joblib.load('gpr200703')
def predicter(smis,solv=None,return_std=False):
    if type(smis) is str: smis=[smis]
    ms=[Chem.MolFromSmiles(s) for s in smis]
    fp = [pyAvalonTools.GetAvalonFP(m) for m in ms]
    if not solv: solv=np.outer(np.ones(len(smis)),[1,0,0])
    x = np.hstack([fp,solv])
    return gp.predict(x,return_std=return_std)

smi='CC'
print(predicter(smi,solv=[[0,0,1]],return_std=True))

