from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import IPAddress

class InputServerIP(FlaskForm):
    server_ip = StringField(
        label = "Server IP Address",
        validators = [IPAddress()],
        description = "Please enter the IP Address of the server"
                      "where EZVIDIA is installed."
    )