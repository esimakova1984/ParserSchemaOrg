
from schema_comparer import SchemaComparer
from url_parser import UrlTemplate

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url_template = UrlTemplate(
    "https://www.shopper.shop/store/zoo-eretz-rosh-haayin/product/%d7%9e%d7%a9%d7%9e%d7%a8%d7%99-%d7%9e%d7%a0%d7%92%d7%95-%d7%9c%d7%9b%d7%9c%d7%91%d7%99%d7%9d-100-%d7%92%d7%a8%d7%9d-%d7%91%d7%98%d7%a2%d7%9d-%d7%98%d7%a8%d7%a7%d7%99"
)
url_compare = UrlTemplate(
    "https://www.shopper.shop/store/medika-pharmacy/product/%d7%97%d7%99%d7%9c%d7%91%d7%94-%d7%90%d7%9c%d7%98%d7%9e%d7%9f-2"
)

schema_comparer = SchemaComparer(url_template.url, url_compare.url, headers=headers)
schema_comparer.compare_schemas()
