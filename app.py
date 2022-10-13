#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import socket
from flask import Flask, render_template, request, redirect, url_for, Markup, abort, session
from jinja2 import TemplateNotFound
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

@app.post('/psq')
def psq():
    smi=request.form["smi"]
    ppsq=pred.psq(smi)
    ppsq.submit()
    mol=Chem.MolFromSmiles(smi)
    sqls=pred.rank()
    return render_template('psq.htm',smi=smi,ppsq=ppsq,sqls=sqls)

@app.post('/qy')
def qy():
    smi=request.form["smi"]
    print(smi)
    try:
        qy=round(pred.qy(smi)[0],3)
        mol=Chem.MolFromSmiles(smi)
    except:
        qy='Not available!'
        mol=''
    return render_template('qy.htm',smi=smi,qy=qy,mol=mol)
@app.route('/<string:page>')
def render_static(page):
    try:
      return render_template('%s.html' % page,title=page)
    except TemplateNotFound:
      abort(404)

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
