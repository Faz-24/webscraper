import requests
from bs4 import BeautifulSoup
from docx import Document

# URL of the webpage to scrape
url = "https://www.novelcool.com/chapter/Damn-Reincarnation-CH-0/8786442/"

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page 
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the <p> tags on the page
    p_tags = soup.find_all('p')

    # Specify the destination folder path
    destination_folder = "\Documents\3. Python"

    # Creates a new Word document
    doc = Document()
    
    # Add the text content of each <p> tag to the document
    for p_tag in p_tags:
        doc.add_paragraph(p_tag.get_text())

    # Save the document to a file
    doc.save("fahimscrape.docx")
    print("Word document saved as 'fahimscrape.docx'")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
