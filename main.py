from flask import Flask, request
from caesar import rotate_string

app = Flask('app')

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
<form action="/do" method="POST">
		<label for="rot">Rotate By:</label>
		<input type="text" name="rot" id="rot" value=0>  <br>
		<textarea name="text" >{0}</textarea><br>
		<input type="submit" value="Encrypt Text">
</form>
    </body>
</html>
"""

@app.route('/')
def index():
  return form.format(" ")

@app.route("/do", methods=["POST"])
def encrypt():
    x = request.form["text"]
    y = int(request.form["rot"])
    z = rotate_string(x, y)
    return form.format(z)



app.run(host='0.0.0.0', port=8080)