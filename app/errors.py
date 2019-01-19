from flask import jsonify, request

def bad_request(message):
    response = jsonify({ "status" : "error", "error" : message })
    response.status_code = 400
    return response

def notfound_404(message):
    response = jsonify({ "status" : "error", "error" : message })
    response.status_code = 404
    return response