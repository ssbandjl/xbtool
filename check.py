#!/usr/bin/env python3
from flask import Flask, request, Response, jsonify
import logging
import hashlib
api = Flask(__name__)
UPLOAD_FOLDER = './upload/'


@api.route("/")
def hello():
    return "Hello API version 1.0"


@api.route("/api/get/<filename>")
def getFile(filename):
    resp = Response(open(filename, encoding="utf-8").read(),
                    mimetype="text/plain")
    resp.headers["Content-Type"] = "text/plain;charset=UTF-8"
    fileObj = hashlib.md5()
    fileObj.update(open(filename, "rb").read())
    fileHash = fileObj.hexdigest()
    resp.headers["X-Shell-MD5"] = fileHash
    print(resp)
    return resp


@api.route("/api/upload", methods=["POST"])
def uploadFile():
    file = request.files["file"]
    file.save(UPLOAD_FOLDER+file.filename)
    return jsonify({"status": "Success"})


if __name__ == "__main__":
    api.debug = True
    api.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    api.run(host='0.0.0.0')
