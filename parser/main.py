from parser.url_parser import UrlTemplate
from parser.schema_comparer import SchemaComparer

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url_template = UrlTemplate(
    "https://www.shopper.shop/store/deli-top-rosh-haayin/product/%d7%a0%d7%a7%d7%a0%d7%99%d7%a7%d7%99%d7%95%d7%aa-%d7%92%d7%93%d7%99%d7%a1-%d7%91%d7%a7%d7%a8-%d7%a2%d7%9d-%d7%a6%d7%a0%d7%95%d7%91%d7%a8%d7%99%d7%9d-%d7%a7%d7%a9%d7%99%d7%95-%d7%95%d7%91%d7%94%d7%a8"
)
url_compare = UrlTemplate(
    "https://www.shopper.shop/store/jaffa-fish-shoham/product/%d7%9b%d7%99%d7%a1%d7%95%d7%a0%d7%99%d7%9d-%d7%a7%d7%a4%d7%95%d7%90%d7%99%d7%9d-%d7%a4%d7%95%d7%a0%d7%92%d7%b3%d7%91%d7%99-%d7%a1%d7%9e%d7%95%d7%a1%d7%94"
)

schema_comparer = SchemaComparer(url_template.url, url_compare.url, headers=headers)
schema_comparer.compare_schemas()
