from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up the WebDriver (make sure you have the correct path to your WebDriver)
driver_path = 'path/to/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)

# URL of the scholarship page
url = 'https://www.example.com/scholarships'

# Function to extract scholarship data
def extract_scholarship_data(soup):
    scholarships = []
    # Example structure of scholarships on the page
    scholarship_elements = soup.find_all('div', class_='scholarship-item')
    for elem in scholarship_elements:
        title = elem.find('h2').text
        description = elem.find('p', class_='description').text
        deadline = elem.find('span', class_='deadline').text
        scholarships.append({
            'title': title,
            'description': description,
            'deadline': deadline
        })
    return scholarships

# Navigate to the scholarship page
driver.get(url)
time.sleep(5)  # Wait for the page to load

# Get the page source and parse it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Extract scholarship data
scholarship_data = extract_scholarship_data(soup)

# Print the extracted data
for scholarship in scholarship_data:
    print(f"Title: {scholarship['title']}")
    print(f"Description: {scholarship['description']}")
    print(f"Deadline: {scholarship['deadline']}")
    print()

# Close the browser
driver.quit()
