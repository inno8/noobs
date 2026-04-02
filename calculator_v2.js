/**
 * Calculator v2 - Improved version with less duplication
 * and better practices
 */

class Calculator {
  constructor() {
    this.result = 0;
    this.history = [];
  }

  calculate(a, b, operator) {
    const num1 = parseFloat(a);
    const num2 = parseFloat(b);

    if (isNaN(num1) || isNaN(num2)) {
      throw new Error("Invalid numbers provided");
    }

    let result;
    switch (operator) {
      case "add":
        result = num1 + num2;
        break;
      case "subtract":
        result = num1 - num2;
        break;
      case "multiply":
        result = num1 * num2;
        break;
      case "divide":
        if (num2 === 0) throw new Error("Cannot divide by zero");
        result = num1 / num2;
        break;
      default:
        throw new Error("Unknown operator: " + operator);
    }

    this.result = result;
    this.history.push({
      operation: `${num1} ${operator} ${num2} = ${result}`,
      timestamp: new Date().toISOString(),
    });
    return result;
  }

  getHistory() {
    return this.history;
  }

  clearHistory() {
    this.history = [];
    this.result = 0;
  }
}

// Usage
const calc = new Calculator();
