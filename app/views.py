from app import app, db, bdb
import json
from app import ipfs
from flask import render_template, jsonify, url_for, request, session, redirect
from random import randint
import pymongo
from pymongo import MongoClient
from werkzeug import secure_filename

client = MongoClient()


@app.route('/create_govt_dept', methods=['POST'])
def create_govt_dept():
    from bigchaindb_driver.crypto import generate_keypair
    new_user = generate_keypair()

    acc_data = {
        'data': {
            'profile': {
                "dept_id": randint(1, 9999999999),
                "dept_name": request.form['dept-name'],
                "dept_city": request.form['dept-city'],
                "dept_state": request.form['dept-state'],
                "dept_publicKey": new_user.public_key,
            },
        },
    }

    prepared_token_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=new_user.public_key,
        asset=acc_data,
        metadata={
            "test": "true"
        })

    fulfilled_token_tx = bdb.transactions.fulfill(
        prepared_token_tx,
        private_keys=new_user.private_key)
    bdb.transactions.send_commit(fulfilled_token_tx)

    acc_data['data']['profile']['dept_privateKey'] = new_user.private_key
    db.dept.insert(acc_data['data']['profile'])

    return 'done'


@app.route('/login_dept', methods=['POST'])
def login_dept():
    select = list(db.dept.find(
        {"dept_publicKey": request.form['password']}))[0]
    print(select)
    select['_id'] = None
    if select:
        for key in select:
            session[key] = select[key]

    return redirect(url_for('dashboard'))

@app.route('/login_seller', methods=['POST'])
def login_seller():
    select = db.sellers.find(
        {"seller_publicKey": request.form['password']})
    print(select)
    if select:
        for key in select:
            session[key] = select[key]

    return redirect(url_for('dashboard'))


@app.route('/create_seller', methods=['POST'])
def create_seller_id():
    from bigchaindb_driver.crypto import generate_keypair
    new_user = generate_keypair()

    acc_data = {
        'data': {
            'profile': {
                "seller_id": randint(1, 9999999999),
                "seller_name": request.form['seller-name'],
                "seller_city": request.form['seller-city'],
                "seller_state": request.form['seller-state'],
                "seller_publicKey": new_user.public_key,
            },
        },
    }

    prepared_token_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=new_user.public_key,
        asset=acc_data,
        metadata={
            "test": "true"
        })

    fulfilled_token_tx = bdb.transactions.fulfill(
        prepared_token_tx,
        private_keys=new_user.private_key)
    bdb.transactions.send_commit(fulfilled_token_tx)

    acc_data['data']['profile']['seller_privateKey'] = new_user.private_key
    db.sellers.insert(acc_data['data']['profile'])

    return 'done'


@app.route('/create_tender')
def create_tender():
    return render_template('create_tender.html')


@app.route('/execute_create_bid')
def execute_create_bid():
    print(session['dept_id'], session['dept_publicKey'],
          session['dept_privateKey'])

    data = {
        'data': {
            'profile': {
                "seller_id": randint(1, 9999999999),
                "seller_name": request.form['seller-name'],
                "seller_city": request.form['seller-city'],
                "seller_state": request.form['seller-state'],
                "seller_publicKey": new_user.public_key,
            },
        },
    }

    from bigchaindb_driver.crypto import generate_keypair
    new_user = generate_keypair()

    prepared_token_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=new_user.public_key,
        asset=data,
        metadata={
            "test": "true"
        })

    fulfilled_token_tx = bdb.transactions.fulfill(
        prepared_token_tx,
        private_keys=new_user.private_key)
    bdb.transactions.send_commit(fulfilled_token_tx)


@app.route('/execute_create_tender', methods=['POST'])
def execute_create_tender():
    print(session['dept_id'], session['dept_publicKey'],
          session['dept_privateKey'])

    f = request.files['tender_pdf']
    f.save(secure_filename(f.filename))
    from app import ipfs

    from Crypto.PublicKey import RSA
    key = RSA.generate(2048)
    privateKey = key.exportKey('DER')
    publicKey = key.publickey().exportKey('DER')

    ipfs_hash = ipfs.upload(secure_filename(f.filename))

    with open('pp.txt', 'wb') as g:
        g.write(publicKey)

    ipfs_hash2 = ipfs.upload('pp.txt')

    data = {
        'data': {
            'tender': {
                "tender_id": randint(1, 9999999999),
                "tender_title": request.form['tender_title'],
                "tender_refNo": request.form['tender_refNo'],
                "tender_bidClosingDate": request.form['tender_bidClosingDate'],
                "tender_bidOpeningDate": request.form['tender_bidOpeningDate'],
                "tender_clauses": request.form['tender_clauses'],
                "tender_amount": request.form['tender_amount'],
                "tender_ipfs_address": ipfs_hash,
                "tender_filename": f.filename,
                "tender_publicKey_ipfs": ipfs_hash2,
            },
        },
    }

    from bigchaindb_driver.crypto import generate_keypair

    prepared_token_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=session['dept_publicKey'],
        asset=data,
        metadata={
            "asdsa": "asd"
            # "tender_publicKey": publicKey,
        })

    print(type(session['dept_privateKey']))
    fulfilled_token_tx = bdb.transactions.fulfill(
        prepared_token_tx,
        private_keys=session['dept_privateKey'])
    bdb.transactions.send_commit(fulfilled_token_tx)

    data['data']['tender']['tender_privateKey'] = privateKey
    data['data']['tender']['tender_publicKey'] = publicKey

    db.tender.insert(data['data']['tender'])
    return 'done'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/view_all_tenders')
def view_all_tenders():
    return render_template('view_all_tenders.html', tenders=client.ihack.tender.find())


@app.route('/view_tender', methods=['POST'])
def view_tender():
    tender = list(db.tender.find(
        {"tender_id": int(request.form['tender-id'])}))[0]
    print(tender)
    return render_template('view_tender.html', tender=tender)


@app.route('/execute_upload_tender')
def execute_upload_tender():
    data = {
        "tender_title": "GPU Server",
        "tender_refNo": 10032,
        "tender_bidClosingDate": "15.1.1998",
        "tender_bidOpeningDate": "01.1.1998",
        "tender_clauses": ["Test Clause 1", "Test Clause 2", "Test Clause 3"],
        "tender_subtasks": ["Test Clause 1", "Test Clause 2", "Test Clause 3"],
        "tender_taskdays": [7, 7, 7],
        "tender_amount": 39990,
        "tender_ipfs_address": ipfs.upload("/home/ghost/Desktop/resume.pdf")
    }
    db.tender.insert(data)
    return 'done'


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/test')
def test():
    return json.dumps(db.test.find()[0]["name"])
