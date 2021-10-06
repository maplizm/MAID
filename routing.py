import os
import bottle
from bottle import run, get, post, static_file, template, request
import data_register
import data_compare

@get("/")
def index():
        return template("index", result="")

@post("/")
def api_call():
        # 受信データとDBに保存されたデータを比較する関数
        compareResults=data_compare.recvDataCompare()
        # DBに受信データを格納する関数
        data_register.recvDataRegister()
        return template("index", result=str(compareResults + request.forms.send_data))
@get("/static/<static:path>")
def get_static(static):
        return static_file(static,root="static")
@get("/ssdeep/ssdeep.js")
def get_ssdeep():
        return static_file("ssdeep.js",root="ssdeep")
if __name__ == "__main__":
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

app = bottle.default_app()
