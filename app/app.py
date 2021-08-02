from flask import Flask, make_response, request, jsonify, render_template, redirect, url_for
from forms import ContactForm
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__, instance_relative_config=False)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    my_dict = {'key': 'dictionary value'}
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(my_dict), 200, headers)


nav = [
    {'name': 'Home', 'url': 'https://example.com/1'},
    {'name': 'About', 'url': 'https://example.com/2'},
    {'name': 'Pics', 'url': 'https://example.com/3'}
]


@app.route('/home')
def home():
    """Landing page."""
    return render_template(
        'home.html',
        nav=nav,
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja."
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2", nav=nav,
        form=form,
        template="form-template"
    )


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
