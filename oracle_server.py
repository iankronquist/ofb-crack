from operator import operator+
from os import environ
from flask import Flask, request, render_template, flash, redirect, url_for, g
import ofbmode

key = environ['CRYPTO_KEY']
app = Flask(__name__)
app.secret_key = environ['APP_KEY']

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/null', methods=['POST'])
def null_byte_oracle():
    ciphertext = request.form['ciphertext']
    plaintext = reduce(operator+, ofbmode.ofb_crypt_str(ciphertext, key))
    if '\0' in plaintext:
        return 400
    else:
        return 200

@app.route('/padding', methods=['POST'])
def null_byte_oracle():
    ciphertext = request.form['ciphertext']
    plaintext = reduce(operator+, ofbmode.ofb_crypt_str(ciphertext, key))
    padding_len = ord(plaintext[-1])
    if any(map(lambda a: a != '\0', plaintext[-padding_len:-1]:
        return 400
    else:
        return 200
