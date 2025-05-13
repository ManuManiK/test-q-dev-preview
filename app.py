from flask import Flask, request, jsonify
import test_branch as calculator
import logging
import os
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Get configuration from environment variables
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', 5000))

@app.route('/api/add', methods=['POST'])
def add():
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({"error": "Missing required parameters 'a' and 'b'"}), 400
        
        a = float(data['a'])
        b = float(data['b'])
        result = calculator.add(a, b)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/subtract', methods=['POST'])
def subtract():
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({"error": "Missing required parameters 'a' and 'b'"}), 400
        
        a = float(data['a'])
        b = float(data['b'])
        result = calculator.subtract(a, b)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/multiply', methods=['POST'])
def multiply():
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({"error": "Missing required parameters 'a' and 'b'"}), 400
        
        a = float(data['a'])
        b = float(data['b'])
        result = calculator.multiply(a, b)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/api/divide', methods=['POST'])
def divide():
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({"error": "Missing required parameters 'a' and 'b'"}), 400
        
        a = float(data['a'])
        b = float(data['b'])
        result = calculator.divide(a, b)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/', methods=['GET'])
def home():
    return """
    <html>
        <head>
            <title>Calculator API</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
                h1 { color: #333; }
                h2 { color: #444; }
                pre { background-color: #f4f4f4; padding: 10px; border-radius: 5px; }
                code { font-family: monospace; }
            </style>
        </head>
        <body>
            <h1>Calculator API</h1>
            <p>A simple calculator API with the following endpoints:</p>
            
            <h2>Addition</h2>
            <pre>POST /api/add
Content-Type: application/json

{
    "a": 10,
    "b": 5
}</pre>
            
            <h2>Subtraction</h2>
            <pre>POST /api/subtract
Content-Type: application/json

{
    "a": 10,
    "b": 5
}</pre>
            
            <h2>Multiplication</h2>
            <pre>POST /api/multiply
Content-Type: application/json

{
    "a": 10,
    "b": 5
}</pre>
            
            <h2>Division</h2>
            <pre>POST /api/divide
Content-Type: application/json

{
    "a": 10,
    "b": 5
}</pre>
        </body>
    </html>
    """

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

if __name__ == '__main__':
    logger.info(f"Starting Calculator App on {HOST}:{PORT}")
    app.run(host=HOST, port=PORT, debug=DEBUG)