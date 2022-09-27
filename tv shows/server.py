from flask_app import app
from flask_app.controllers import login_reg
from flask_app.controllers import shows

if __name__ == "__main__":
    app.run(debug=True, port=5120)