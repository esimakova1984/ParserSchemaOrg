class TemplateSchema:
    @staticmethod
    def get_template():
        return {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": "Example Product – Amazing Toy – Speaks Example Language",
            "image": "https://www.example.com/wp-content/uploads/2024/04/example-image.png",
            "description": "An amazing toy that speaks Example Language, perfect for kids.",
            "sku": "1234567890",
            "brand": {
                "@type": "Brand",
                "name": "ExampleBrand"
            },
            "offers": {
                "@type": "Offer",
                "priceCurrency": "USD",
                "price": "19.99",
                "priceValidUntil": "2025-12-31",
                "availability": "https://schema.org/InStock",
                "seller": {
                    "@type": "Organization",
                    "name": "Example Toy Store",
                    "image": "https://www.example.com/wp-content/uploads/2022/06/example-store.jpeg",
                    "description": "Example store description with hours and services.",
                    "telephone": "123-456-7890",
                    "url": "https://www.example.com/store/example-toy-store",
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": "123 Example Street",
                        "addressLocality": "Example City",
                        "addressRegion": "EX",
                        "postalCode": "12345",
                        "addressCountry": "USA"
                    }
                }
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "4.5",
                "reviewCount": "100"
            },
            "review": [
                {
                    "@type": "Review",
                    "author": "Jane Doe",
                    "datePublished": "2023-01-01",
                    "description": "My kids love this toy!",
                    "reviewRating": {
                        "@type": "Rating",
                        "ratingValue": "5"
                    }
                },
                {
                    "@type": "Review",
                    "author": "John Smith",
                    "datePublished": "2023-02-15",
                    "description": "Good quality, but a bit pricey.",
                    "reviewRating": {
                        "@type": "Rating",
                        "ratingValue": "4"
                    }
                }
            ],
            "sameAs": [
                "https://www.instagram.com/example_store/",
                "https://www.facebook.com/example_store/"
            ]
        }