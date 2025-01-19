from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import json

# Configure Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Use WebDriver Manager to automatically download and set up the correct ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to extract reviews from a given URL
def extract_reviews(url):
    # Open the URL
    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "styles_reviewCardInner__UZk1x"))
    )

    reviews = []
    while True:
        for _ in range(5):
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            time.sleep(2)  # Wait for content to load

        # Find all review cards
        review_cards = driver.find_elements(By.CLASS_NAME, "styles_reviewCardInner__UZk1x")

        for card in review_cards:
            try:
        # Extract reviewer name (default to empty string if not found)
                try:
                    reviewer = card.find_element(By.CSS_SELECTOR, "[data-consumer-name-typography='true']").text.strip()
                except Exception:
                    reviewer = "" 

        # Extract review title (default to empty string if not found)
                try:
                    title = card.find_element(By.CSS_SELECTOR, "[data-service-review-title-typography='true']").text.strip()
                except Exception:
                    title = ""  

                try:
                    body = card.find_element(By.CSS_SELECTOR, "[data-service-review-text-typography='true']").text.strip()
                except Exception:
                    body = ""  

        # Extract rating (default to 0 if not found)
                try:
                    rating_alt = card.find_element(By.CSS_SELECTOR, "div.star-rating_starRating__sdbkn img").get_attribute("alt")
                    rating = int(rating_alt.split()[1])  # Extract rating number
                except Exception:
                    rating = 0  

        # Append to the reviews list
                reviews.append({
                    "title": title,
                    "body": body,
                    "rating": rating,
                    "reviewer": reviewer
                })

            except Exception as e:
                print(f"Error extracting a review: {e}")


        # Check if there is a "Next Page" button
        try:
            # Wait for the "Next Page" button to be clickable
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Next page"]'))
            )

            # Scroll to the "Next Page" button to ensure it's in view
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            time.sleep(1)  # Wait for smooth scrolling

            # Click the "Next Page" button using JavaScript to bypass the "click intercepted" issue
            driver.execute_script("arguments[0].click();", next_button)

            # Wait for the page to load
            WebDriverWait(driver, 10).until(EC.staleness_of(next_button))

        except Exception as e:
            print(f"No more pages or error encountered: {e}")
            break
    
    driver.quit()

    review_data = {
        "review_counts": len(reviews),
        "reviews": reviews
    }
    return json.dumps(review_data)




# try:
#     url = "https://www.trustpilot.com/review/maxiscoot.com"  
#     review_data = extract_reviews(url)
#     with open("reviews.json", "w", encoding="utf-8") as f:
#         json.dump(review_data, f, ensure_ascii=False, indent=4)

#     print("Reviews successfully saved to reviews.json")

# finally:
#     driver.quit()


#print(extract_reviews("https://www.trustpilot.com/review/maxiscoot.com"))