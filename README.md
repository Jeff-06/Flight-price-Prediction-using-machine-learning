# ✈️ Flight Price Predictor

A Machine Learning-powered web application that predicts airline ticket prices based on travel details such as airline, source city, destination city, departure time, arrival time, number of stops, travel duration, and days left before departure.

## 🚀 Features

- Predict flight ticket prices instantly
- Interactive web interface built with Flask
- Machine Learning model trained on real flight data
- REST API endpoint for predictions
- Responsive and modern UI
- Random Forest Regressor model

## 📊 Model Performance

| Metric | Value |
|----------|----------|
| MAE | 1789 |
| RMSE | 3437 |
| R² Score | 0.977 |
| Cross Validation RMSE | 5048 |

## 🛠️ Tech Stack

- Python
- Flask
- Scikit-Learn
- Pandas
- NumPy
- HTML
- CSS
- JavaScript

## 📁 Project Structure

```text
FlightPrice/
│
├── app.py
├── airfare_predictornew.pkl
├── Clean_Dataset.csv
│
├── templates/
│   └── index.html
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Jeff-06/Flight-price-Prediction-using-machine-learning.git
```

Move into the project directory:

```bash
cd Flight-price-Prediction-using-machine-learning
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
flask run
```

Open:

```text
http://127.0.0.1:5000
```

## 🔌 API Usage

### Endpoint

```http
POST /predict
```

### Example Request

```json
{
  "airline": "Air_India",
  "source_city": "Delhi",
  "destination_city": "Mumbai",
  "departure_time": "Night",
  "arrival_time": "Morning",
  "stops": "one",
  "class": "Economy",
  "duration": 11.25,
  "days_left": 39
}
```

### Example Response

```json
{
  "predicted_price": 2903.26
}
```

## 📷 Screenshots

Add screenshots of:
<img width="1919" height="935" alt="image" src="https://github.com/user-attachments/assets/e26d65c0-73b1-4338-96c7-758487e87738" />

<img width="1919" height="944" alt="image" src="https://github.com/user-attachments/assets/5179a10f-4092-43d3-a79b-95704bf793a1" />

<img width="1227" height="656" alt="image" src="https://github.com/user-attachments/assets/335e225d-d58e-4f27-9af6-f2f9ff29789c" />


## 👨‍💻 Author

Jeffrey Jaijo

CS Engineering Student

---

If you found this project useful, consider giving it a ⭐ on GitHub.
