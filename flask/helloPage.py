from flask import Flask

app=Flask(__name__)
app.debug=True

@app.route("/")
@app.route("/index")
def index():
    return "hello flask"

@app.route("/hello")
def hello():
    return "<html><head><title>Hi there!</title></head><body>Hello World!</body></html>",200

if __name__ == '__main__':
    app.run()
    
