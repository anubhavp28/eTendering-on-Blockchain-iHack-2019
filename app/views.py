from app import app, db
import json

@app.route('/test')
def test():
    return json.dumps(db.test.find()[0]["name"])




    
