
// 🔥 CREATE ORDER
function createOrder() {

    const name = document.getElementById("name").value;
    const phone = document.getElementById("phone").value;
    const type = document.getElementById("type").value;
    const qty = document.getElementById("qty").value;

    fetch("http://127.0.0.1:5000/create-order", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            customer_name: name,
            phone: phone,
            items: [
                {
                    type: type,
                    qty: parseInt(qty)
                }
            ]
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML =
            `✅ Order Created! <br>
             Order ID: ${data.id} <br>
             Total: ₹${data.total} <br>
             Status: ${data.status}`;
    })
    .catch(err => {
        document.getElementById("result").innerHTML = "❌ Error creating order";
    });
}


// 📦 GET ALL ORDERS (Dashboard)
function getOrders() {

    fetch("http://127.0.0.1:5000/orders")
    .then(res => res.json())
    .then(data => {

        let html = "";

        data.forEach(order => {
            html += `
                <div class="card">
                    <b>Order ID:</b> ${order.id} <br>
                    <b>Name:</b> ${order.customer_name} <br>
                    <b>Phone:</b> ${order.phone} <br>
                    <b>Total:</b> ₹${order.total} <br>
                    <b>Status:</b> ${order.status}
                </div>
                <br>
            `;
        });

        document.getElementById("orders").innerHTML = html;

    })
    .catch(err => {
        document.getElementById("orders").innerHTML = "❌ Error loading orders";
    });
}