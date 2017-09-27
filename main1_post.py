from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir), autoescape=True)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    template = jinja_env.get_template("hello_form.html")
    return template.render()

@app.route("/hello", methods=["POST"])
def hello():
    first_name = request.form["first_name"]
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(name=first_name)

@app.route("/validate-time")
def display_time_form():
    templete = jinja_env.get_template("time_form.html")
    return template.render()

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/validate-time", methods=["POST"])
def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = "hours value out of range (0-23)"
            hours = ""

    if not is_integer(hours):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or hours < 0:
            minutes_error = "hours value out of range (0-59)"
            minutes = ""

    if not minutes_error and not hours_error:
        time = str(hours) + ":" + str(minutes)
    else:
        time = hours_error + " " +  minutes_error 
    
    return time

@app.route("/form-inputs")
def display_form_inputs():
    return """
    <style>
    br {margin-bottom: 20px;}
    </style>
    <form method="POST">

        <!--<label for="name"> <input name="name" type="text /> *optional format-->

        <label>type=text
            <input name="user-name" type="text" />
        </label>

        <br>

        <label>type=password
            <input name="user-password" type="password" />
        </label>

        <br>

        <label>type=email
            <input name="user-email" type="email" />
        </label>

        <br>

        <label>Ketchup
            <input type="checkbox" name="cb1" value="first-cb" />
        </label>

        <br>

        <label>mustard
            <input name="cb2" type="checkbox" value="second-cb" />
        </label>

        <br>

        <label>Small
            <input type="radio" name="coffee_size" value="sm" />
        </label>

        <br>

        <label>Medium
            <input type="radio" name="coffee_size" value="md" />
        </label>

        <br>

        <label>Large
            <input type="radio" name="coffee_size" value="lg" />
        </label>

        <br>

        <label>Your life story
            <textarea name="life-story"></textarea>
        </label>

        <br>

            <label>LaunchCode Hub
                <select name="lc-hub">
                    <option value="kc">Kansas City</option>
                    <option value="mia">Miami</option>
                    <option value="ri">Providence</option>
                    <option value="sea">Seattle</option>
                    <option value="pdx">Portland</option>
                </select>
            </label>
    """
@app.route("/form-inputs", methods=["POST"])
def print_form_values():
    resp = ""
    for field in request.form.keys():
        resp += "<b>{key}</b>: {value}<br>".format(key=field,
        value=request.form[field])

    return cgi.escape(resp)


app.run()