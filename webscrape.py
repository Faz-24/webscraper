import os 
import requests
from bs4 import BeautifulSoup
from docx import Document

# URL of the webpage to scrape
urls = ["https://www.novelcool.com/chapter/Damn-Reincarnation-Chapter-82/8690734/"]

while len(urls) > 0:
# Send an HTTP GET request to the URL
    response = requests.get(urls[0])

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
        output_file = os.path.join(destination_folder, "output82b.docx")

        # Save the document to the specified folder and file
        doc.save(output_file)
        print(f"Word document saved in '{output_file}'")
    
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
