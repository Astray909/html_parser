from bs4 import BeautifulSoup

def extract_text_from_html(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as html_file:
        # Parse the file using 'html.parser'
        soup = BeautifulSoup(html_file, 'html.parser')
        
        # Get all the text from the parsed HTML file
        text = soup.get_text(separator=' ')
        
        return text

# Use the function on your file
html_text = extract_text_from_html('parse.html')

# Open a new text file in write mode
with open('output.txt', 'w') as output_file:
    # Write the extracted text to the file
    output_file.write(html_text)

print("Text has been written to output.txt")
