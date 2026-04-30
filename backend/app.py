from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

orders = []
order_id = 1

PRICE_LIST = {
    "Shirt": 50,
    "Pants": 70,
    "Saree": 100
}

# ---------------------------
# Home Route
# ---------------------------
@app.route('/')
def home():
    return "Laundry API is Running 🚀"


# ---------------------------
# Create Order
# ---------------------------
@app.route('/create-order', methods=['POST'])
def create_order():
    global order_id

    data = request.json
    items = data['items']

    total = 0
    for item in items:
        total += PRICE_LIST[item['type']] * item['qty']

    order = {
        "id": order_id,
        "customer_name": data['customer_name'],
        "phone": data['phone'],
        "items": items,
        "total": total,
        "status": "RECEIVED"
    }

    orders.append(order)
    order_id += 1

    return jsonify(order)


# ---------------------------
# Get Orders
# ---------------------------
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)


# ---------------------------
# Update Status
# ---------------------------
@app.route('/update-status/<int:id>', methods=['PUT'])
def update_status(id):
    data = request.json

    for order in orders:
        if order['id'] == id:
            order['status'] = data['status']
            return jsonify(order)

    return jsonify({"error": "Order not found"})


# ---------------------------
# Dashboard
# ---------------------------
@app.route('/dashboard', methods=['GET'])
def dashboard():
    total_orders = len(orders)
    total_revenue = sum(o['total'] for o in orders)

    status_count = {}
    for o in orders:
        status = o['status']
        status_count[status] = status_count.get(status, 0) + 1

    return jsonify({
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "status": status_count
    })


# ---------------------------
# Run Server
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)