from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def stock_data():
    tesla = yf.Ticker("TSLA")
    df = tesla.history(period="max")
    df = df.tail(120)
    return render_template("stock_data.html", data=df.to_html())

if __name__ == "__main__":
    app.run(debug=True)