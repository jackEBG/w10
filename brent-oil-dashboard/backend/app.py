from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Sample data loading function (replace with your actual data source)
def load_data():
    # Load your analysis results here
    return pd.read_csv('data/merged_data.csv')

@app.route('/api/oil-prices', methods=['GET'])
def get_oil_prices():
    data = load_data()
    # Convert DataFrame to JSON (customize as needed)
    return jsonify(data.to_dict(orient='records'))

@app.route('/api/event-impact', methods=['GET'])
def get_event_impact():
    # Analyze and return how events impact prices
    return jsonify({"event": "Sample Event", "impact": "Increase"})

if __name__ == '__main__':
    app.run(debug=True)