from flask import Flask, render_template, request, send_file
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("search.html")

@app.route("/result", methods=["POST"])
def result():
    stock_ticker = request.form["stock_ticker"]
    stock_data = yf.Ticker(stock_ticker).history(period="30d")
    
    # create excel file
    stock_data.to_excel("stock_data.xlsx", index=False)
    
    return render_template("result03.html", data=stock_data.to_html(classes="table table-striped"))

@app.route("/download_report")
def download_report():
    return send_file("stock_data.xlsx", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)