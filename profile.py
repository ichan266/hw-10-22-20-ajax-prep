import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""
    return render_template("index.html")



@app.route('/api/profile', methods=['POST'])
def profile():
    """Return results from profile form."""

    fullname = request.form['name']
    age = request.form['age']
    occupation = request.form['occupation']
    # salary = request.form['salary']
    # education_level = request.form['education']
    # state = request.form['state']
    # city = request.form['city']
    # gardening = request.form['garden']
    # tv_hours = request.form['tv']

    # TODO: get the values from the rest of the form
    # Add them to jsonify
    
    return jsonify({'fullname': fullname,
                    'age': age,
                    'occupation': occupation,})





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")