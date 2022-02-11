from urllib import response
from flask import Flask, Blueprint, render_template, url_for, redirect, request
from chatbot import predict_class, get_response, intents
# a 'blueprint' of the website structure is created
views = Blueprint(__name__, "views")

# the fisle is a flask application and url prefix is set to "/"
app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/")
app.config['SECRET_KEY'] = "secret_key_Gaz69"

answer_list = []
chat_box = []
question_list = []

@app.route("/") # the page is accessed with the prefix "/"
def homepage():
    global answer_list
    answer_list.clear()
    return render_template("index.html", name = "Neuralidays")
# sets the homepage to "index.html" in the "templates" folder

@app.route("/services")
def service_page():
    return render_template("services.html")

@app.route("/aboutus")
def aboutus_page():
    return render_template("aboutus.html")

@app.route("/contactus")
def contactus_page():
    return render_template("contactus.html")

@app.route("/index")
def index_page():
    return render_template("index.html")

@app.route("/home")
def home_redirect():
    return redirect(url_for("homepage"))
# "/home" will redirect to the same location as the homepage function.

@app.errorhandler(404)
def page_not_found(e):
    return render_template("page_not_found.html"), 404
# error 404 handler

@app.errorhandler(500)
def pinternal_server_error(e):
    return render_template("internal_server_error.html"), 500
# error 500 handler

@app.route('/chatbot', methods=["POST", "GET"])
def chatbot():
    global answer_list
    if request.method == "POST":
        message = request.form['message']
        ints = predict_class(message)
        response = get_response(ints, intents)
        chat_box.append(message)
        chat_box.append(response)
        answer_list.append(response)
        question_list.append(message)
        print(chat_box)
        if len(chat_box) > 8:
            chat_box.remove(chat_box[0])
            chat_box.remove(chat_box[0])
        return render_template('chatbot.html', message=message, answer_list=answer_list, question_list=question_list, chat_box=chat_box )
    return render_template('chatbot.html', message="", answer_list="")

if __name__ == "__main__":
    app.run(debug=True, port=8000)

