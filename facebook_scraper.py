import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ----------------------------
# Configuration
# ----------------------------
USERNAME = 'parasjadhav6666@gmail.com'  # Your email
PASSWORD = '9673670666'                   # Your password
CHROME_DRIVER_PATH = r'C:\Users\DevRahul\Downloads\chrome-win64\chrome-win64\chromedriver.exe'
SCREENSHOTS_DIR = 'screenshots'
REPORTS_DIR = 'reports'
PDF_REPORT_PATH = os.path.join(REPORTS_DIR, 'SocialMediaReport.pdf')

# Ensure directories exist
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

# ----------------------------
# Initialize WebDriver
# ----------------------------
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')
service = Service(CHROME_DRIVER_PATH)  # Use Service to specify the driver path
driver = webdriver.Chrome(service=service, options=options)

# ----------------------------
# Helper Functions
# ----------------------------

def login_facebook(username, password):
    driver.get('https://www.facebook.com/')
    time.sleep(3)  # Wait for the page to load

    # Enter username
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys(username)

    # Enter password
    password_input = driver.find_element(By.ID, 'pass')
    password_input.send_keys(password)

    # Click login
    login_button = driver.find_element(By.NAME, 'login')
    login_button.click()
    time.sleep(5)  # Wait for login to complete

def navigate_to_profile():
    # Navigate to user's profile
    driver.get('https://www.facebook.com/me/')
    time.sleep(5)

def extract_posts():
    posts = []
    SCROLL_PAUSE_TIME = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    while len(posts) < 10:  # Limit to first 10 posts for demonstration
        # Extract posts
        post_elements = driver.find_elements(By.XPATH, '//div[@data-ad-preview="message"]')
        for elem in post_elements:
            try:
                content = elem.text
                if content and content not in posts:
                    posts.append(content)
                    # Take screenshot of the post
                    location = elem.location
                    size = elem.size
                    screenshot_path = os.path.join(SCREENSHOTS_DIR, f'post_{len(posts)}.png')
                    driver.save_screenshot(screenshot_path)
                    # Crop the screenshot to the post element
                    image = Image.open(screenshot_path)
                    left = location['x']
                    top = location['y']
                    right = location['x'] + size['width']
                    bottom = location['y'] + size['height']
                    image = image.crop((left, top, right, bottom))
                    image.save(screenshot_path)
                    print(f'Captured post {len(posts)}')
            except Exception as e:
                print(f'Error capturing post: {e}')
        
        # Scroll down to load more posts
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # No more posts to load
        last_height = new_height

    return posts

def generate_pdf_report(posts):
    c = canvas.Canvas(PDF_REPORT_PATH, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 14)
    c.drawString(50, height - 50, "Social Media Report")
    c.setFont("Helvetica", 12)
    y_position = height - 80

    for idx, post in enumerate(posts, start=1):
        if y_position < 150:
            c.showPage()
            y_position = height - 50
        c.drawString(50, y_position, f"Post {idx}:")
        y_position -= 20
        text = c.beginText(70, y_position)
        for line in post.split('\n'):
            text.textLine(line)
            y_position -= 15
            if y_position < 100:
                break
        c.drawText(text)
        # Add screenshot
        screenshot_path = os.path.join(SCREENSHOTS_DIR, f'post_{idx}.png')
        if os.path.exists(screenshot_path):
            c.drawImage(screenshot_path, 50, y_position - 200, width=500, height=200)
            y_position -= 220
    c.save()
    print(f'PDF report generated at {PDF_REPORT_PATH}')

# ----------------------------
# Main Workflow
# ----------------------------
try:
    login_facebook(USERNAME, PASSWORD)
    navigate_to_profile()
    posts = extract_posts()
    generate_pdf_report(posts)
except NoSuchElementException as e:
    print(f'Element not found: {e}')
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    driver.quit()
