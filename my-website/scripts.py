from flask import Flask

# instantiate the class
app=Flask(__name__)


# ROUTES
@app.route('/')
def home():
    return "Website content goes here!"


if __name__=='__main__':
    app.run(debug=True)