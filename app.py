from flask import Flask, jsonify

# Dictionary of Justice League
justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

#################################################
# Flask Setup
app= Flask(__name__)
#################################################
# @TODO: Initialize your Flask app here
# YOUR CODE GOES HERE
@app.route("/")
def home():
	print("Welcome to the Justice Leagee Home page...")
	return "Welcome to Justice Leagee Home page!"
	return "/api/v1.0/justice-league"
#################################################
# Flask Routes

@app.route("/about")
def about():
	return "Welcome to George Oddoye's wonderful About page!"
	
@app.route("/contact")
def contact():
	return "This website was created by George Oddoye. You can contact him in Duluth,Ga"
	
@app.route("/justice-league")
def justice_league():
	return jsonify(justice_league_members )

#################################################

# @TODO: Complete the routes for your app here
# YOUR CODE GOES HERE

if __name__ == "__main__":
	app.run(debug=True)
    # @TODO: Create your app.run statement here
    # YOUR CODE GOES HERE
