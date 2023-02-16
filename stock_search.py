from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("search.html")

@app.route("/result", methods=["POST"])
def result():
    stock_ticker = request.form["stock_ticker"]
    stock_data = yf.Ticker(stock_ticker).history(period="30d")
    
    return render_template("result.html", data=stock_data.to_html(classes="table table-striped"))

if __name__ == "__main__":
    app.run(debug=True)