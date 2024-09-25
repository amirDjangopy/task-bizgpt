from bs4 import BeautifulSoup
import markdownify
from selenium import webdriver
from embeddings.embedding_processor import convert_markdown_to_embedding, save_embedding
import time
import os

# لیست URLهای سایت
urls = [
    "https://qavanin.ir/Report/BookView/189",
    "https://qavanin.ir/Law/?zone=160",
    "https://qavanin.ir/Law/TreeText/?IDS=15139854016332449699",
    "https://qavanin.ir/Report/BookView/195",
    "https://qavanin.ir/Law/TreeText/?IDS=11702863590443787747"
]

# تنظیمات WebDriver
driver = webdriver.Chrome() 


def crawl_and_save_to_markdown(url, filename):
    try:
        driver.get(url)
        time.sleep(5)  # Wait for 5 seconds for the page to load

        # Converting HTML to BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content = soup.find('body')

        if content:
            # Convert HTML to Markdown
            markdown_content = markdownify.markdownify(str(content), heading_style="ATX")

            # Create the "ali" folder if it doesn't exist
            ali_folder = "crawelMd"
            if not os.path.exists(ali_folder):
                os.makedirs(ali_folder)

            # Save content to a file within the "ali" folder
            with open(f"{ali_folder}/{filename}.md", "w", encoding="utf-8") as file:
                file.write(markdown_content)
            print(f"Saved: {ali_folder}/{filename}.md")

            # Convert Markdown to embedding and save (assuming defined functions)
            embedding = convert_markdown_to_embedding(markdown_content)
            if embedding is not None:
                save_embedding(filename, embedding)
        else:
            print(f"Content not found for {url}")
    except Exception as e:
        print(f"Error for {url}: {e}")
        
        
for idx, url in enumerate(urls, start=1):
    crawl_and_save_to_markdown(url, f"page_{idx} ")

driver.quit()
