from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

class WeightConverter:
    @staticmethod
    def validate_weight(weight):
        """Validate weight input"""
        try:
            weight_float = float(weight)
            if weight_float <= 0:
                return False, "Weight must be a positive number"
            if weight_float > 1000:
                return False, "Weight must be less than 1000"
            return True, weight_float
        except (ValueError, TypeError):
            return False, "Weight must be a valid number"
    
    @staticmethod
    def validate_unit(unit):
        """Validate unit input"""
        if not unit or unit.lower() not in ['p', 'k', 'pounds', 'kilograms']:
            return False, "Unit must be 'p', 'k', 'pounds', or 'kilograms'"
        return True, unit.lower()
    
    @staticmethod
    def convert_weight(weight, from_unit):
        """Convert weight between pounds and kilograms"""
        if from_unit in ['p', 'pounds']:
            # Convert pounds to kilograms
            converted_weight = weight * 0.453592
            return {
                'original_weight': weight,
                'original_unit': 'pounds',
                'converted_weight': round(converted_weight, 2),
                'converted_unit': 'kilograms'
            }
        elif from_unit in ['k', 'kilograms']:
            # Convert kilograms to pounds
            converted_weight = weight / 0.453592
            return {
                'original_weight': weight,
                'original_unit': 'kilograms',
                'converted_weight': round(converted_weight, 2),
                'converted_unit': 'pounds'
            }

@app.route('/', methods=['GET'])
def home():
    """Health check endpoint"""
    return jsonify({
        'message': 'Weight Converter API is running!',
        'version': '1.0.0',
        'endpoints': {
            'convert': '/api/convert (POST)',
            'health': '/ (GET)'
        }
    })

@app.route('/api/convert', methods=['POST'])
def convert_weight():
    """Convert weight between pounds and kilograms"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Extract data
        name = data.get('name', '').strip()
        weight = data.get('weight')
        unit = data.get('unit', '').strip()
        
        # Validate name
        if not name:
            return jsonify({'error': 'Name is required and cannot be empty'}), 400
        
        # Validate weight
        weight_valid, weight_result = WeightConverter.validate_weight(weight)
        if not weight_valid:
            return jsonify({'error': weight_result}), 400
        
        # Validate unit
        unit_valid, unit_result = WeightConverter.validate_unit(unit)
        if not unit_valid:
            return jsonify({'error': unit_result}), 400
        
        # Convert weight
        conversion_result = WeightConverter.convert_weight(weight_result, unit_result)
        
        # Add user info to response
        response = {
            'user': name,
            'conversion': conversion_result,
            'message': f"Hi {name}! Your weight has been successfully converted."
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Detailed health check"""
    return jsonify({
        'status': 'healthy',
        'service': 'Weight Converter API',
        'timestamp': '2025-07-02'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
