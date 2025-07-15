from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import re
import math

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('advanced_calculator.html', version='2.0')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        
        # Clean the expression and validate
        expression = expression.replace('×', '*').replace('÷', '/')
        
        # Remove any characters that aren't numbers, operators, or parentheses
        expression = re.sub(r'[^0-9+\-*/().]', '', expression)
        
        # Basic validation
        if not expression or len(expression) > 100:
            return jsonify({'error': 'Invalid expression'}), 400
        
        # Check for division by zero
        if '/0' in expression and not re.search(r'/0[^.]', expression):
            return jsonify({'error': 'Division by zero'}), 400
        
        # Evaluate the expression
        result = eval(expression)
        
        # Format result
        if isinstance(result, (int, float)):
            if result == int(result):
                result = int(result)
            else:
                result = round(result, 8)  # Limit decimal places
        
        return jsonify({'result': str(result)})
        
    except ZeroDivisionError:
        return jsonify({'error': 'Division by zero'}), 400
    except Exception as e:
        return jsonify({'error': 'Invalid expression'}), 400

@app.route('/calculate-emi', methods=['POST'])
def calculate_emi():
    try:
        data = request.get_json()
        principal = float(data.get('principal', 0))
        rate = float(data.get('rate', 0))
        tenure = float(data.get('tenure', 0))
        
        if principal <= 0 or rate <= 0 or tenure <= 0:
            return jsonify({'error': 'Invalid input values'}), 400
        
        # Calculate EMI
        monthly_rate = rate / 12 / 100
        total_months = tenure * 12
        
        if monthly_rate == 0:
            emi = principal / total_months
        else:
            emi = principal * monthly_rate * (1 + monthly_rate) ** total_months / ((1 + monthly_rate) ** total_months - 1)
        
        total_amount = emi * total_months
        total_interest = total_amount - principal
        
        return jsonify({
            'emi': round(emi, 2),
            'totalAmount': round(total_amount, 2),
            'totalInterest': round(total_interest, 2),
            'principal': principal
        })
        
    except Exception as e:
        return jsonify({'error': 'Calculation error'}), 400

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000, use_reloader=False)