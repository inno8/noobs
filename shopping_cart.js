// Shopping cart functionality
var cart = [];
var TAX_RATE = 0.1;

function addItem(name, price, quantity) {
    for (var i = 0; i < cart.length; i++) {
        if (cart[i].name == name) {
            cart[i].quantity = cart[i].quantity + quantity;
            updateDisplay();
            return;
        }
    }
    cart.push({name: name, price: price, quantity: quantity});
    updateDisplay();
}

function removeItem(name) {
    for (var i = 0; i < cart.length; i++) {
        if (cart[i].name == name) {
            cart.splice(i, 1);
            updateDisplay();
            return;
        }
    }
}

function getTotal() {
    var total = 0;
    for (var i = 0; i < cart.length; i++) {
        total = total + (cart[i].price * cart[i].quantity);
    }
    return total;
}

function getTax() {
    return getTotal() * TAX_RATE;
}

function getGrandTotal() {
    return getTotal() + getTax();
}

function updateDisplay() {
    var html = "<table>";
    html = html + "<tr><th>Item</th><th>Price</th><th>Qty</th><th>Subtotal</th><th></th></tr>";
    for (var i = 0; i < cart.length; i++) {
        html = html + "<tr>";
        html = html + "<td>" + cart[i].name + "</td>";
        html = html + "<td>$" + cart[i].price + "</td>";
        html = html + "<td>" + cart[i].quantity + "</td>";
        html = html + "<td>$" + (cart[i].price * cart[i].quantity) + "</td>";
        html = html + "<td><button onclick='removeItem(\"" + cart[i].name + "\")'>Remove</button></td>";
        html = html + "</tr>";
    }
    html = html + "</table>";
    html = html + "<p>Subtotal: $" + getTotal() + "</p>";
    html = html + "<p>Tax: $" + getTax() + "</p>";
    html = html + "<p>Total: $" + getGrandTotal() + "</p>";
    document.getElementById("cart-display").innerHTML = html;
}

function checkout() {
    if (cart.length == 0) {
        alert("Cart is empty!");
        return;
    }
    var total = getGrandTotal();
    alert("Order placed! Total: $" + total);
    cart = [];
    updateDisplay();
}
