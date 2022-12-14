from flask import jsonify, Flask,  request, render_template, redirect, session, url_for,  make_response, Blueprint
from flask_cors import CORS
import secrets
from route.attraction import attraction_api
from route.member import member_api
from route.booking import booking_api
from route.order import order_api

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/static",
)

app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True

key=secrets.token_urlsafe(16)
app.secret_key="key"

CORS(app)

# Pages
@app.route("/")
def index():
	return render_template("index.html")
@app.route("/attraction/<id>")
def attraction(id):
	return render_template("attraction.html")
@app.route("/booking")
def booking():
	return render_template("booking.html")
@app.route("/thankyou")
def thankyou():
	return render_template("thankyou.html")

@app.route("/member")
def member():
	return render_template("member.html")

app.register_blueprint(attraction_api)
app.register_blueprint(member_api)
app.register_blueprint(booking_api)
app.register_blueprint(order_api)

if __name__=="__main__":
	app.run(host='0.0.0.0', port=3000)