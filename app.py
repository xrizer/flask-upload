from flask import Flask, request, jsonify
import base64
import os
from datetime import datetime

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploaded_images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Check if image is in the request
        if 'image' not in data:
            return jsonify({
                'status': 'error',
                'message': 'No image found in request'
            }), 400
        
        # Get the base64 string
        base64_string = data['image']
        
        try:
            # Decode the base64 string
            image_data = base64.b64decode(base64_string)
            
            # Generate unique filename using timestamp
            filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            
            # Save the image
            with open(file_path, 'wb') as f:
                f.write(image_data)
            
            return jsonify({
                'status': 'ok'
            }), 200
            
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': 'Invalid base64 string'
            }), 400
            
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'Server error'
        }), 500

if __name__ == '__main__':
    # Changed this line to accept connections from any IP
    app.run(host='0.0.0.0', port=8080, debug=True)