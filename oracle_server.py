from operator import add
from os import environ, urandom
from flask import Flask, request, render_template, flash, redirect, url_for, g
import ofbmode

key = environ.get('CRYPTO_KEY') or urandom(ofbmode.BLOCK_SIZE)
app = Flask(__name__)

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/null', methods=['POST'])
def null_byte_oracle():
    ciphertext = request.form['ciphertext']
    plaintext = reduce(add, ofbmode.ofb_decrypt(ciphertext, key))
    if '\0' in plaintext:
        return 400
    else:
        return 200

@app.route('/padding', methods=['POST'])
def padding_oracle():
    ciphertext = request.form['ciphertext']
    plaintext = reduce(add, ofbmode.ofb_decrypt(ciphertext, key))
    padding_len = ord(plaintext[-1])
    if any(map(lambda a: a != '\0', plaintext[-padding_len:-1])):
        return 400
    else:
        return 200

if __name__ == '__main__':
    print 'app running'
    app.run(debug=True)
