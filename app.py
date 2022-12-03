import os
import socket

from flask import Flask, render_template, request
from form import *

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

class EzvidiaResponse():
    def __init__(self, ip=None, port=48541):
        self.options = []
        self.ip = ip
        self.port = port
        self.list_message = "LIST"
        self.apply_message = "APPLY "
        self.current_status = "Disconnected"
        self.sock = None
    
    def test_connection(self):
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )
        try:
            sock.connect((self.ip, self.port))
            print("Connected!")
            self.current_status = "Connected"
        except:
            print("Cannot connect.")
            self.current_status = "Error"
            return
        sock.send(self.list_message.encode())
        resp = sock.recv(8192).decode()
        configs = resp.split(";;")
        self.options = configs
        self.sock = sock
    
    def change_config(self, config_option):
        if config_option not in self.options:
            print("Option does not exist")
            return '500 (Option does not exist)'
        if not self.sock:
            print("Not connected")
            return '500 (Not connected)'

        self.sock.send(f"{self.apply_message}{config_option}".encode())
        

ez = EzvidiaResponse()

@app.route("/", methods=["GET","POST"])
def index():
    ip_form = InputServerIP()
    if ip_form.validate_on_submit():
        captured_ip = ip_form.server_ip.data
        ez.ip = captured_ip
        ez.test_connection()
        print(ez.options)
        return render_template(
            'index.html',
            form=ip_form,
            ezobj=ez
        ) 
    return render_template(
        'index.html', 
        form=ip_form, 
        ezobj=ez
    )
    
@app.route("/setconfig", methods=["GET","POST"])
def setconfig():
    requested_config = eval(request.data.decode())
    ez.change_config(requested_config)
    
    return "200"