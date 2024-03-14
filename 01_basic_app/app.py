# importing flask
from flask import  Flask

# initiate the flask class 
app = Flask(__name__)

# app route for home page
@app.route('/')  #

# function name for home page
def helloworld():  #
    return "<p>Hello, World!</p>"  # return a string to be displayed on the webpage

   

    
if __name__ == "__main__":
    app.run(debug=True)