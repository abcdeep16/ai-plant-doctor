import os
import google.generativeai as genai
import PIL.Image
from flask import Flask, request, jsonify, render_template

# 1. CONFIGURE GEMINI AND FLASK APP
# Configure Gemini with your API key
# Important: For a real project, store this securely in an environment variable
genai.configure(api_key="AIzaSyBkPvd8RzEXLRMmFP3qLu8hhPIw7sHws9Q") 

# 2. DEFINE THE MODEL GLOBALLY
# This is the fix for the "name 'model' is not defined" error.
# The model is created once when the app starts.
model = genai.GenerativeModel('gemini-1.5-flash-latest')

app = Flask(__name__)

@app.route('/')
def index():
    # Renders the HTML file for the frontend
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_plant():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image']
    
    if image_file.filename == '':
        return jsonify({'error': 'No selected image'}), 400

    try:
        # Open the image using Pillow (PIL)
        img = PIL.Image.open(image_file)
        
        # 3. THE PROMPT FOR GEMINI
        # The prompt is a key part of your API. It tells the model what to do.
        # You can make this more specific for better results.
        prompt = """
        Analyze the condition of this plant in the image. Identify any potential diseases, pests, or nutrient deficiencies.
        Provide a clear and concise diagnosis. If a problem is found, suggest a simple, actionable organic treatment.
        If the plant appears healthy, state so.
        """
        
        # 4. USE THE MODEL TO GENERATE CONTENT
        # The 'model' variable is now accessible because it's defined globally.
        response = model.generate_content([prompt, img])
        
        # Return the generated text as a JSON response
        return jsonify({'analysis': response.text})

    except Exception as e:
        # This will help you catch any other errors that might occur
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)