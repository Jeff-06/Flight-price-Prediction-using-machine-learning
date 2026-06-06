from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load model artifacts
saved = joblib.load("airfare_predictor.pkl")

model = saved["model"]
scaler = saved["scaler"]
columns = saved["columns"]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()
    print("Received data:")
    print(data)

    # Create empty dataframe with training columns
    df = pd.DataFrame(0, index=[0], columns=columns)

    # Scale numerical features
    scaled = scaler.transform([[
        data["duration"],
        data["days_left"]
    ]])

    df["duration"] = scaled[0][0]
    df["days_left"] = scaled[0][1]

    # Airline
    airline_col = f'airline_{data["airline"].replace(" ", "_")}'
    if airline_col in df.columns:
        df[airline_col] = 1

    # Source city
    source_col = f'source_city_{data["source_city"]}'
    if source_col in df.columns:
        df[source_col] = 1

    # Departure time
    departure_col = f'departure_time_{data["departure_time"]}'
    if departure_col in df.columns:
        df[departure_col] = 1

    # Stops
    stops_col = f'stops_{data["stops"]}'
    if stops_col in df.columns:
        df[stops_col] = 1

    # Arrival time
    arrival_col = f'arrival_time_{data["arrival_time"]}'
    if arrival_col in df.columns:
        df[arrival_col] = 1

    # Destination city
    destination_col = f'destination_city_{data["destination_city"]}'
    if destination_col in df.columns:
        df[destination_col] = 1

    # Class
    class_col = f'class_{data["class"]}'
    if class_col in df.columns:
        df[class_col] = 1

    print(df.T)
    prediction = model.predict(df)[0]

    return jsonify({
        "predicted_price": round(float(prediction), 2)
    })


if __name__ == "__main__":
    app.run(debug=True)