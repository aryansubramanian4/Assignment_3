# from flask import Flask, render_template, request


# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html', location = None)

# @app.route("/search", methods = ['GET']) # to accept only https GET requests
# def search():
#     location = request.args.get('location')
#     return render_template('index.html', location=location)

# if __name__ == "__main__":
#     app.run(debug=True)
