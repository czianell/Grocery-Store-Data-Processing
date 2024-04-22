from flask import Flask, request, jsonify

app = Flask(__name__)

# Grocery Store Items
items = [
    {"item_sku": 100, "item_name": "Fresh Milk", "num_of_purchases": 20, "item_price": 2.58},
    {"item_sku": 101, "item_name": "Oat Milk", "num_of_purchases": 15, "item_price": 3.99},
    {"item_sku": 102, "item_name": "Almond Milk", "num_of_purchases": 7, "item_price": 3.25}
]

# Display home
@app.route("/")
def home():
  return "Grocery Store Sales"

# Get Grocery Store Items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)
  
if __name__ == "__main__":
  app.run(debug=True)