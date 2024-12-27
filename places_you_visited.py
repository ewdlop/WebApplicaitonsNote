from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (make sure you have the correct path to your WebDriver)
driver_path = 'path/to/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)

# List of resource URLs
urls = {
    "Mental Health Resources": "https://www.mentalhealth.gov/",
    "Hospital Resources": "https://www.hospitalsafetygrade.org/",
    "Government Resources": "https://www.usa.gov/",
    "School Resources": "https://www.ed.gov/"
}

# Function to navigate to a URL and wait for some time
def navigate_to_url(url):
    driver.get(url)
    time.sleep(5)  # Wait for 5 seconds to load the page

# Navigate to each resource
for resource, url in urls.items():
    print(f"Navigating to {resource}: {url}")
    navigate_to_url(url)

# Close the browser
driver.quit()
