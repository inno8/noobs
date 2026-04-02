var result = 0;
var history = [];

function add(a, b) {
    result = a + b;
    history.push(a + "+" + b + "=" + result);
    document.getElementById("result").innerHTML = result;
}

function subtract(a, b) {
    result = a - b;
    history.push(a + "-" + b + "=" + result);
    document.getElementById("result").innerHTML = result;
}

function multiply(a, b) {
    result = a * b;
    history.push(a + "*" + b + "=" + result);
    document.getElementById("result").innerHTML = result;
}

function divide(a, b) {
    result = a / b;
    history.push(a + "/" + b + "=" + result);
    document.getElementById("result").innerHTML = result;
}

function showHistory() {
    var html = "";
    for (var i = 0; i < history.length; i++) {
        html = html + "<p>" + history[i] + "</p>";
    }
    document.getElementById("history").innerHTML = html;
}

function clearAll() {
    result = 0;
    history = [];
    document.getElementById("result").innerHTML = "";
    document.getElementById("history").innerHTML = "";
}

function calculate() {
    var num1 = document.getElementById("num1").value;
    var num2 = document.getElementById("num2").value;
    var op = document.getElementById("op").value;
    if (op == "add") add(num1, num2);
    if (op == "subtract") subtract(num1, num2);
    if (op == "multiply") multiply(num1, num2);
    if (op == "divide") divide(num1, num2);
}
