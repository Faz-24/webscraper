import os 
import requests
from bs4 import BeautifulSoup
from docx import Document
import time

# URL of the webpage to scrape
urls = ["https://www.novelcool.com/chapter/Damn-Reincarnation-Chapter-80/8690732/"]
counter = 0 
while len(urls) > 0:
# Send an HTTP GET request to the URL
    counter += 1
    
    response = requests.get(urls[0])
    time.sleep(10)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the <p> tags on the page
        p_tags = soup.find_all('p')

        # Specify the destination folder path
        destination_folder = "/Users/f.shahriyar/Documents"

        # Create a new Word document
        doc = Document()

        # Add the text content of each <p> tag to the document
        for p_tag in p_tags:
            doc.add_paragraph(p_tag.get_text())

        # Specify the full path to the output file in the destination folder
        output_file = os.path.join(destination_folder, f"output-{counter}.docx")

        # Save the document to the specified folder and file
        doc.save(output_file)
        print(f"Word document saved in chapter'{output_file}'")
    
    #find the url for next chap
        div_element = soup.find('div', class_='dis-hide', id='next_chp_url')

    # Extract the URL from the div element
        if div_element:
            url = div_element.text.strip()
            urls.pop()
            urls.append(url)
        else:
            print('URL not found')
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
