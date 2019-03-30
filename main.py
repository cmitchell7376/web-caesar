from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea_{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form action="/caesar" method:"post">
                <label for="rot">
                    Rotate by:
                    <input  type="text" name="rot"/ value=0>
                </label>
                    <br>
                    <br>
                    <textarea name="text"></textarea>
                    <br>
                    <br>
                    <input type="submit" value="Submit Query"/>
            </form>
        </body>
    </html>
"""
@app.route("/caesar", methods=['POST'])
def encrypt():
   num = request.form['rot']
   text = request.form['text']

   return num
@app.route("/")
def index():
    return form

app.run()