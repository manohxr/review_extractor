from flask import Flask, request, jsonify
from review_extraction import extract_reviews
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    url = request.args.get('page')
    if not url:
        return jsonify({"error": "URL parameter 'page' is required"}), 400
    
    try:
        # Extract reviews from the provided URL
        reviews_data = extract_reviews(url)
        
        # Parse the reviews data from JSON string to dictionary
        review_data_dict = json.loads(reviews_data)
        
        # Return the data in a structured format
        return jsonify({
            "review_count": review_data_dict["review_counts"],
            "reviews": review_data_dict["reviews"]
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
