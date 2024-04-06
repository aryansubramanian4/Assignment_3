from flask import Flask, render_template, request
import mbta_helper

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', location = None, station = None)

@app.route("/search", methods = ['GET']) # Used get to request data
def search():
    location = request.args.get('location') 
    if location:
        station = mbta_helper.find_stop_near(location)
        if station:
            return render_template('index.html', location = location, station = station)
        else:
            return render_template('index.html', location = location, error = "Unfortunately, no nearby stations found.")
    else:
        return render_template('index.html', error="Please enter a correct location.")

if __name__ == "__main__":
    app.run(debug=True)