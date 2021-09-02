from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# 1. localhost:5000/ - have it say "Hello World!"
@app.route('/')
def hello_world():
    return "Hello World!"

# 2. localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

# 3. Create one url pattern and function that can handle the following examples:
# w/NINJA BONUS: Ensure the names provided in the 3rd task are strings
@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name}!"

# 4. Create one url pattern and function that can handle the following examples 
# (HINT: int() will come in handy! For example int("35") returns 35):
# w/NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer, 
# and the 3rd element is a string
@app.route('/repeat/<int:num>/<string:item>')
def repeat(num, item):
    return f"{item * num}"

# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, 
# they receive an error message saying "Sorry! No response. Try again."
@app.errorhandler(404)
def wrong_route(e):
    return "Sorry! No response. Try again."


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.