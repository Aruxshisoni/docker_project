from flask import Flask
myapp= Flask(__name__)
@myapp.route("/search")
def lwinfo():
    print("i am arushi")
    return "i am arshi"
myapp.run()
