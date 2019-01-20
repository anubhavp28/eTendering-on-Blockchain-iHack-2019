from app import app, db, bdb
import json
from app import ipfs
from flask import render_template, jsonify, url_for, request


@app.route('/create_govt_dept')
def create_govt_dept():
    from bigchaindb_driver.crypto import generate_keypair
    new_user = generate_keypair()

    acc_data = {
        'data': {
            'profile': {
                "dept_id": 8332,
                "dept_name": "Govt College of Engineering Kalyani",
                "dept_city": "Kolkata",
                "dept_state": "West Bengal",
                "dept_publicKey": new_user.public_key,
            },
        },
    }

    prepared_token_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=new_user.public_key,
        asset=acc_data,
        metadata={
            "ego": "true"
        })

    fulfilled_token_tx = bdb.transactions.fulfill(
        prepared_token_tx,
        private_keys=new_user.private_key)
    bdb.transactions.send_commit(fulfilled_token_tx)

    acc_data['dept_privateKey'] = new_user.private_key
    db.dept.insert(acc_data)

    return 'done'


@app.route('/create_seller')
def create_seller_id():
    from bigchaindb_driver.crypto import generate_keypair
    new_user = generate_keypair()

    acc_data = {
        'data': {
            'profile': {
                "seller_id": 8332,
                "seller_name": "Baba Stationary Store",
                "seller_city": "Kolkata",
                "seller_state": "West Bengal",
                "seller_publicKey": new_user.public_key,
            },
        },
    }

    prepared_token_tx = bdb.transactions.prepare(
        operation='CREATE',
        signers=new_user.public_key,
        asset=acc_data,
        metadata={
            "ego": "true"
        })

    fulfilled_token_tx = bdb.transactions.fulfill(
        prepared_token_tx,
        private_keys=new_user.private_key)
    bdb.transactions.send_commit(fulfilled_token_tx)

    acc_data['seller_privateKey'] = new_user.private_key
    db.sellers.insert(acc_data)

    return 'done'


@app.route('/create_tender')
def create_tender():
    return render_template('create_tender.html')


@app.route('/execute_create_tender', methods=['POST'])
def execute_create_tender():
    return jsonify(request.form)


@app.route('/')
def index():
    return render_template('index.html')


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


@app.route('/test')
def test():
    return json.dumps(db.test.find()[0]["name"])
