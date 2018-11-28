from flask import Flask, render_template
import os


app = Flask(__name__)

from rdkit import Chem
from rdkit.Chem import Draw

@app.route('/')
@app.route('/index')
def drawMolecule():
	molString = "CCOCCNSC=O"
	mol = Chem.MolFromSmiles(molString)
	img = Draw.MolToFile(mol, 'static/mol_img/mol.png')
	return render_template("index.html")