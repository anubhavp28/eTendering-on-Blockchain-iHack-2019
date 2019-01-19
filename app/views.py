from app import app, db
import json
from app import ipfs


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
