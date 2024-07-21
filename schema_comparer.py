# import json
#
# from temlate_schema import TemplateSchema
# from url_parser import UrlTemplate
#
#
# class SchemaComparer:
#     def __init__(self, url_compare, headers=None):
#         self.template_schema = TemplateSchema.get_template()
#         self.url_compare = UrlTemplate(url_compare, headers=headers)
#
#     def find_missing_keys(self, obj1, obj2, path=""):
#         missing_keys = []
#
#         if isinstance(obj2, dict):
#             for key in obj2.keys():
#                 new_path = f"{path}.{key}" if path else key
#                 if key not in obj1:
#                     missing_keys.append(new_path)
#                 elif isinstance(obj1[key], (dict, list)) and isinstance(obj2[key], (dict, list)):
#                     missing_keys.extend(self.find_missing_keys(obj1[key], obj2[key], path=new_path))
#
#         elif isinstance(obj2, list) and isinstance(obj1, list):
#             for i, (item1, item2) in enumerate(zip(obj1, obj2)):
#                 missing_keys.extend(self.find_missing_keys(item1, item2, path=f"{path}[{i}]"))
#
#         return missing_keys
#
#     def find_empty_values(self, obj, path=""):
#         empty_keys = []
#
#         if isinstance(obj, dict):
#             for key, value in obj.items():
#                 new_path = f"{path}.{key}" if path else key
#                 if not value:
#                     empty_keys.append(new_path)
#                 elif isinstance(value, (dict, list)):
#                     empty_keys.extend(self.find_empty_values(value, path=new_path))
#
#         elif isinstance(obj, list):
#             for i, item in enumerate(obj):
#                 empty_keys.extend(self.find_empty_values(item, path=f"{path}[{i}]"))
#
#         return empty_keys
#
#     def compare_schemas(self):
#         self.template_schema.get_metadata()
#         self.url_compare.get_metadata()
#
#         self.template_schema.check_required_keys()
#
#         print(f"\nMetadata for {self.template_schema.url} (Product type):")
#         print(json.dumps(self.template_schema.metadata, indent=2))
#
#         print(f"\nMetadata for {self.url_compare.url} (Product type):")
#         print(json.dumps(self.url_compare.metadata, indent=2))
#
#         if self.template_schema.metadata and self.url_compare.metadata:
#             missing_keys_template = self.find_missing_keys(self.template_schema.metadata, self.url_compare.metadata)
#             missing_keys_compare = self.find_missing_keys(self.url_compare.metadata, self.template_schema.metadata)
#
#             print(f"\nMissing Keys in {self.template_schema.url} compared to {self.url_compare.url}:")
#             print(missing_keys_template)
#             empty_keys_template = self.find_empty_values(self.template_schema.metadata)
#             if empty_keys_template:
#                 print("\nKeys with empty values:")
#                 print(empty_keys_template)
#
#             print(f"\nMissing Keys in {self.url_compare.url} compared to {self.template_schema.url}:")
#             print(missing_keys_compare)
#             empty_keys_compare = self.find_empty_values(self.url_compare.metadata)
#             if empty_keys_compare:
#                 print("\nKeys with empty values:")
#                 print(empty_keys_compare)
#         else:
#             print("\nUnable to compare metadata. One or both URLs do not contain metadata of type 'Product'.")


import json

from temlate_schema import TemplateSchema
from url_parser import UrlTemplate


# Импортируем наш новый класс

class SchemaComparer:
    def __init__(self, url_compare, headers=None):
        self.url_compare = UrlTemplate(url_compare, headers=headers)
        self.template_schema = TemplateSchema.get_template()  # Получаем эталонную схему как словарь

    def find_missing_keys(self, obj1, obj2, path=""):
        missing_keys = []

        if isinstance(obj2, dict):
            for key in obj2.keys():
                new_path = f"{path}.{key}" if path else key
                if key not in obj1:
                    missing_keys.append(new_path)
                elif isinstance(obj1[key], (dict, list)) and isinstance(obj2[key], (dict, list)):
                    missing_keys.extend(self.find_missing_keys(obj1[key], obj2[key], path=new_path))

        elif isinstance(obj2, list) and isinstance(obj1, list):
            for i, (item1, item2) in enumerate(zip(obj1, obj2)):
                missing_keys.extend(self.find_missing_keys(item1, item2, path=f"{path}[{i}]"))

        return missing_keys

    def find_empty_values(self, obj, path=""):
        empty_keys = []

        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = f"{path}.{key}" if path else key
                if not value:
                    empty_keys.append(new_path)
                elif isinstance(value, (dict, list)):
                    empty_keys.extend(self.find_empty_values(value, path=new_path))

        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                empty_keys.extend(self.find_empty_values(item, path=f"{path}[i]"))

        return empty_keys

    def compare_schemas(self):
        self.url_compare.get_metadata()  # Получаем метаданные только для объекта UrlTemplate

        print(f"\nMetadata for {self.url_compare.url} (Product type):")
        print(json.dumps(self.url_compare.metadata, indent=2))

        if self.url_compare.metadata:
            missing_keys_compare = self.find_missing_keys(self.template_schema, self.url_compare.metadata)

            print(f"\nMissing Keys in {self.url_compare.url} compared to template schema:")
            print(missing_keys_compare)
            empty_keys_compare = self.find_empty_values(self.url_compare.metadata)
            if empty_keys_compare:
                print("\nKeys with empty values:")
                print(empty_keys_compare)
        else:
            print("\nUnable to compare metadata. URL does not contain metadata of type 'Product'.")
