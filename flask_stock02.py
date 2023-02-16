from flask import Flask, render_template
import yfinance as yf
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/")
def stock_data():
    tesla = yf.Ticker("TSLA")
    df = tesla.history(period="max")
    df = df.tail(120)
    
    # Find the average value of 30 days and 60 days.
    df['30_day_MA'] = df['Close'].rolling(window=30).mean()
    df['60_day_MA'] = df['Close'].rolling(window=60).mean()
    
    # Visualize the average value.
    plt.plot(df['Close'], label='Close')
    plt.plot(df['30_day_MA'], label='30_day_MA')
    plt.plot(df['60_day_MA'], label='60_day_MA')
    plt.legend(loc='upper left')
    
    # Save the plot to the buffer in png file format.
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    # Encode the image to base64.
    image_base64 = base64.b64encode(image_png).decode('utf-8')
    image_data = 'data:image/png;base64,{}'.format(image_base64)
    
    return render_template("stock_data.html", data=df.to_html(), image_data=image_data)

if __name__ == "__main__":
    app.run(debug=True)