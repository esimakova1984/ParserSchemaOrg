from schema_comparer import SchemaComparer

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url_compare = "https://www.shopper.shop/store/s-phone/product/%d7%9b%d7%99%d7%a1%d7%95%d7%99-%d7%a9%d7%a7%d7%95%d7%a3-skech-magsafe"

schema_comparer = SchemaComparer(url_compare, headers=headers)
schema_comparer.compare_schemas()