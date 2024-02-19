import json
import re
import requests
from bs4 import BeautifulSoup


class UrlTemplate:
    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers or {}
        self.metadata = None

    def get_metadata(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        schemaorg_elements = soup.find_all('script', {'type': 'application/ld+json'})

        # Create an empty list to store product metadata
        metadata = []

        # Iterate over elements containing scripts with schema.org metadata
        for element in schemaorg_elements:
            # Clean the text of the element from control characters
            cleaned_text = self.clean_control_characters(element.text)

            # Parse the cleaned text into a JSON object
            json_data = json.loads(cleaned_text)

            # Check for the presence of the "@type" key and its value being "Product"
            if "@type" in json_data and json_data["@type"] == "Product":
                # If the condition is met, add the metadata to the list
                metadata.append(json_data)

        if len(metadata) > 1:
            raise ValueError("Error: More than one script with '@type': 'Product' found. Please ensure only one is present.")

        self.metadata = metadata[0] if metadata else None

    def clean_control_characters(self, text):
        return re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)

    def check_required_keys(self):
        required_keys = ["@context", "@type", "name", "image", "description", "sku", "brand", "offers", "aggregateRating"]

        for key in required_keys:
            if key not in self.metadata:
                print(f"Error: Required key '{key}' is missing in metadata for {self.url}.")
