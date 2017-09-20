from flask import Flask, request

app = Flask(__name__)


form_html = '''
<!DOCTYPE html)
<html>
  <body>
    <form method='POST' action="/hello">
      <input type="text" name="name" />
      <input type="Date" name="birthday" />
      <input type="submit" value="go" />
    </form>
  </body>
</html>  
'''

response_html = '''
<!DOCTYPE html)
<html>
    <head></head>
  <body>
    <h1>Hello {name}</h1>
    <span>Your birthday is {birthday}</span>
  </body>
</html>  
'''


@app.route("/")
def handle_stuff():
    return form_html

@app.route('/hello', methods=['POST'])
def handle_hello():
    return response_html.format(name=request.form['name']),
birthday.request.form['birthdate'])

if __name__ == '__main__'
app.run(debug=True)