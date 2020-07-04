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
from rdkit import Chem
import pred
app = Flask(__name__)
app.secret_key='HUHU9'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/psq', methods=['GET', 'POST'])
def psq():
    smi=request.form["smi"]
    try:
        lp,r=pred.psq(smi)
        mol=Chem.MolFromSmiles(smi)
    except:
        lp='Not available!'
        r='Not available!'
        mol=''
    return render_template('index.html',smi=smi,lp=lp,r=r,mol=mol)

@app.route('/qy', methods=['GET', 'POST'])
def qy():
    smi=request.form["smi"]
    print(smi)
    try:
        qy=round(pred.qy(smi)[0],3)
        mol=Chem.MolFromSmiles(smi)
    except:
        qy='Not available!'
        mol=''
    return render_template('index.html',smi=smi,qy=qy,mol=mol)
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
