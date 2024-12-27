import requests
from bs4 import BeautifulSoup
import os

def get_links(url):
    """
    Scrapes a webpage to find all links.
    :param url: The URL of the webpage to scrape.
    :return: A list of links.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL {url}: {e}")
        return []

def download_file(url, save_dir="downloads"):
    """
    Downloads a file from a URL and saves it locally.
    :param url: The URL of the file to download.
    :param save_dir: The directory to save the downloaded file.
    """
    try:
        os.makedirs(save_dir, exist_ok=True)
        local_filename = os.path.join(save_dir, url.split('/')[-1])
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Downloaded file: {local_filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file {url}: {e}")

def download_html(url, save_dir="html_pages"):
    """
    Downloads the HTML content of a page from a URL and saves it locally.
    :param url: The URL of the page to download.
    :param save_dir: The directory to save the HTML content.
    """
    try:
        os.makedirs(save_dir, exist_ok=True)
        local_filename = os.path.join(save_dir, f"{url.split('//')[-1].replace('/', '_')}.html")
        response = requests.get(url)
        response.raise_for_status()
        with open(local_filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"Downloaded HTML: {local_filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the HTML from {url}: {e}")

def process_links(base_url, save_dir="downloads"):
    """
    Processes links from a webpage. Downloads files for '/download' links
    and saves HTML for other links.
    :param base_url: The URL of the page to scrape and process.
    :param save_dir: The directory to save the files and HTML.
    """
    print(f"Processing links from: {base_url}")
    links = get_links(base_url)

    if not links:
        print("No links found.")
        return

    for link in links:
        # Ensure the link is complete
        if not link.startswith("http"):
            link = requests.compat.urljoin(base_url, link)
        
        if "/download" in link:
            print(f"Found download link: {link}")
            download_file(link, save_dir)
        else:
            print(f"Found page link: {link}")
            download_html(link, save_dir)

def main():
    """
    Main function to run the script.
    """
    target_url = "a website with a lot of ads"  # Replace with your target URL
    downloads_dir = "downloads"         # Directory for downloaded files
    process_links(target_url, downloads_dir)

if __name__ == "__main__":
    main()
