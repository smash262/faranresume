from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/calculator/')
def calculator():
    return render_template("calculator.html")

@app.route('/weather/')
def weather():
    return render_template("weather.html")

if __name__=="__main__":
    app.run(debug=True)

