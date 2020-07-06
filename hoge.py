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
    if request.method == 'GET': return redirect(url_for("index"))
    smi=request.form["smi"]
    ppsq=pred.psq(smi)
    ppsq.submit()
    mol=Chem.MolFromSmiles(smi)
    sqls=pred.rank()
    return render_template('index.html',smi=smi,ppsq=ppsq,sqls=sqls)

@app.route('/qy', methods=['GET', 'POST'])
def qy():
    if request.method == 'GET': return redirect(url_for("index"))
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
    from os import getenv
    app.debug = True
    host = getenv('HHost')
    port = getenv('HPort')
    if port and host:
        try:
            app.run(host=host,port=port)
        except:
            host=socket.gethostname()
            app.run(host=host,port=port)
    else:
        app.run()
