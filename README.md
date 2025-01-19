Review Extractor Project
This project allows users to extract product reviews from a given URL using Selenium and Flask. The frontend allows users to input a product page URL, and it will display the reviews extracted from that URL.

Features
Allows users to input a URL and fetch reviews from that product page.
Extracts review titles, bodies, ratings, and reviewer names.
Handles infinite scroll and pagination for continuous loading of reviews.
Displays the total number of reviews and review details.
Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Flask (Python)
Web Scraping: Selenium, WebDriver Manager
Browser Automation: Chrome WebDriver
API: Flask API for fetching reviews

Setup Instructions
1. Clone the repository
Start by cloning the repository to your local machine:

2. Install dependencies
To set up the environment, install the necessary dependencies. It is recommended to use a virtual environment:

For Windows:
python -m venv venv
.\venv\Scripts\activate

For macOS/Linux:
python3 -m venv venv
source venv/bin/activate

Once inside the virtual environment, install the required Python packages:
pip install -r requirements.txt
The requirements.txt file should include all the necessary dependencies.

3. Install Chrome and ChromeDriver
Since this project uses Selenium for web scraping, it requires Google Chrome and the correct version of ChromeDriver.

Install WebDriver Manager: The project uses webdriver-manager, which automates downloading the correct version of ChromeDriver for your system. This is already handled by the requirements.txt file.

4. Run the Flask application
Once all dependencies are installed, run the Flask app with the following command:
python app.py
The Flask server will start and be available at http://127.0.0.1:5000/.

5. Open the web interface
Open a web browser and navigate to http://127.0.0.1:5000/. You will see the review extractor interface. Enter a product page URL and click the Get Reviews button to fetch reviews from the page.

6. Endpoints
The Flask API has the following endpoint for fetching reviews:

GET /api/reviews?page={url}:
Query parameter: page (The product page URL)
Response:
review_count: The number of reviews on the product page.
reviews: A list of extracted reviews, each containing:
title: The title of the review.
body: The body/content of the review.
rating: The rating out of 5 stars.
reviewer: The name of the reviewer (if available).

7. Example Usage
In the browser, input a product URL, such as:
https://www.trustpilot.com/review/travelexinsurance.com

Click the Get Reviews button. The system will fetch the reviews and display them on the page, including the title, body, rating, and reviewer name (if available).