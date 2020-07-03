#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import socket
from flask import Flask, render_template, request, redirect, url_for, Markup, abort, session
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sqlite3
import cgitb, math, re
import rdkit 
#from sklearn.externals import joblib
import joblib
from sklearn import linear_model,cross_decomposition
from sklearn.model_selection import cross_val_score,cross_val_predict
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


gp=joblib.load('gpr200703')
def predicter(smis,solv=None,return_std=False):
    if type(smis) is str: smis=[smis]
    ms=[Chem.MolFromSmiles(s) for s in smis]
    fp = [pyAvalonTools.GetAvalonFP(m) for m in ms]
    if not solv: solv=np.outer(np.ones(len(smis)),[1,0,0])
    x = np.hstack([fp,solv])
    return gp.predict(x,return_std=return_std)

app = Flask(__name__)
app.secret_key='HUHU9'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/go', methods=['GET', 'POST'])
def qy():
    smi=request.form["smi"]
    try:
        qy=round(predicter(smi)[0],2)
    except:
        qy='Not available!'
    return render_template('index.html',smi=smi,qy=qy)
@app.route('/<string:page>/')
def render_static(page):
    return render_template('%s.html' % page,title=page)

@app.route('/favicon.ico/',methods=['GET'])
def favicon():
    return('', 204)

if __name__ == '__main__':
    app.debug = True
    host = socket.gethostname()
#    app.run(host='localhost',port=8090)
    app.run(host='165.242.106.75',port=8090)
