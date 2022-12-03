from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import IPAddress

class InputServerIP(FlaskForm):
    server_ip = StringField(
        default="192.168.1.4",
        label = "Server IP Address",
        validators = [IPAddress()],
        description = "Please enter the IP Address of the server"
                      "where EZVIDIA is installed."
    )