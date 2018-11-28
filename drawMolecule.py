from flask import Flask, render_template, request

app = Flask(__name__)

from rdkit import Chem
from rdkit.Chem import Draw

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def input_post():
	text = request.form['text']
	mol = Chem.MolFromSmiles(text)
	path = 'static/mol_img/{}.png'.format(text)
	img = Draw.MolToFile(mol, path)
	return render_template("index.html", path = path)
