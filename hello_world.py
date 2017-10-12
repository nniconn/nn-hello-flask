from flask import Flask
from os import environ

app = Flask(__name__)

# @app.route("/")
# @app.route("/hello")
# @app.route("/hello/<name>")
@app.route("/jedi/<firstname>/<lastname>")

# def say_hi():
#     return "Hello World!"
    
# def hi_person(name):
    # return "Hello {}!".format(name.title())
    
# def hello_person(name):
#     html = """
#         <h1>
#             Hello {}!
#         </h1>
#         <p>
#             Here's a picture of a kitten. Awww...
#             </p>
#             <img src="http://placekitten.com/g/200/300">
#     """
#     return html.format(name.title())
    
def hello_jedi(lastname,firstname):
    url = 'https://nn-hello-flask-niconguyen.c9users.io/<firstname>/<lastname>'
    if url.endswith('/<lastname>/<firstname>'):
        url = lastname[0:3], firstname[0:2] 
    return "Hello, {}"
    
if __name__ == "__main__":
    app.run(host=environ['IP'],
        port=int(environ['PORT']))