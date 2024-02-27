# ----------------------->> without pagination (single page)
# import scrapy
# import json
# import os

# class MyfontsSpider(scrapy.Spider):
#     name = "myfonts"
#     start_urls = [
#         'https://p11uzvl396-dsn.algolia.net/1/indexes/*/queries'
#     ]
    
#     headers = {
#         'X-Algolia-Agent': 'Algolia for JavaScript (4.20.0); Browser (lite); JS Helper (3.14.0); react (17.0.2); react-instantsearch (6.40.4)',
#         'Content-Type': 'application/json',
#         'X-Algolia-API-Key': '084aa805a4e8f0f531b540c0c29887ce',
#         'X-Algolia-Application-Id': 'P11UZVL396'
#     }
    
#     form_data = {
#         "requests": [
#             {
#                 "indexName": "universal_search_data",
#                 "params": "analyticsTags=foundry_myfonts&attributesToHighlight=%5B%5D&attributesToRetrieve=%5B%22font_count%22%2C%22family_id%22%2C%22foundry_handle%22%2C%22foundry_name%22%2C%22foundry_title%22%2C%22foundry_logo%22%2C%22foundry_location%22%2C%22foundry_image_urls%22%2C%22foundry_description%22%2C%22handle%22%2C%22has_free%22%2C%22image_urls%22%2C%22font_data.file_type%22%2C%22font_data.handle%22%2C%22font_data.md5%22%2C%22font_data.name%22%2C%22font_data.pim_style_id%22%2C%22name%22%2C%22prices%22%2C%22public_tags%22%2C%22_tags%22%2C%22_tags_de%22%2C%22_tags_es%22%2C%22_tags_fr%22%2C%22_tags_pt%22%2C%22render_text%22%2C%22title%22%2C%22included_packages%22%5D&facets=%5B%22*%22%5D&filters=foundry_handle%3Afontfabric-foundry&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&hitsPerPage=20&maxValuesPerFacet=200&page=3&query=&ruleContexts=foundry_myfonts&tagFilters=&clickAnalytics=true&analytics=true&userToken=anonymous-105ac04a-4638-47fd-a95f-e0f04ff2e34b&facetFilters=%5B%5D"
#             }
#         ]
#     }
    
#     base_url = "https://cdn.myfonts.net/cdn-cgi/image/width=400,height=auto,fit=contain,format=auto/images/pim/"
#     output_dir = "downloaded_images4"
    
#     def start_requests(self):
#         for url in self.start_urls:
#             yield scrapy.Request(url, method='POST', headers=self.headers, body=json.dumps(self.form_data), callback=self.parse_json)
    
#     def parse_json(self, response):
#         if response.status == 404:
#             self.logger.error("404 Error: Page not found")
#             return
#         elif response.status == 403:
#             self.logger.error("403 Error: Forbidden access")
#             return
        
#         try:
#             json_data = response.json()
#             image_urls_by_name = self.get_image_urls_by_name(json_data)
#             for name, urls in image_urls_by_name.items():
#                 folder_path = os.path.join(self.output_dir, name)
#                 if not os.path.exists(folder_path):
#                     os.makedirs(folder_path)
#                 for idx, url in enumerate(urls, 1):
#                     yield scrapy.Request(url, meta={'name': name, 'idx': idx}, callback=self.save_image)
#         except Exception as e:
#             self.logger.error(f"Error occurred while parsing JSON: {e}")
    
#     def get_image_urls_by_name(self, json_data):
#         image_urls_by_name = {}
#         if 'results' in json_data:
#             for result in json_data['results']:
#                 if 'hits' in result:
#                     for hit in result['hits']:
#                         name = hit.get('name')
#                         if name and 'image_urls' in hit:
#                             image_urls = [self.base_url + url for url in hit['image_urls']]
#                             image_urls_by_name.setdefault(name, []).extend(image_urls)
#         return image_urls_by_name
    
#     def save_image(self, response):
#         try:
#             name = response.meta['name']
#             idx = response.meta['idx']
#             image_name = f"image_{idx}.png"
#             folder_path = os.path.join(self.output_dir, name)
#             image_path = os.path.join(folder_path, image_name)
#             with open(image_path, 'wb') as f:
#                 f.write(response.body)
#             self.logger.info(f"Image {idx} for {name} downloaded successfully: {image_path}")
#         except Exception as e:
#             self.logger.error(f"Error occurred while saving image {idx} for {name}: {e}")

#  ------------------------------------->> with pagination
# import scrapy
# import json
# import os

# class MyfontsSpider(scrapy.Spider):
#     name = "myfonts"
#     start_urls = [
#         'https://p11uzvl396-dsn.algolia.net/1/indexes/*/queries'
#     ]
    
#     headers = {
#         'X-Algolia-Agent': 'Algolia for JavaScript (4.20.0); Browser (lite); JS Helper (3.14.0); react (17.0.2); react-instantsearch (6.40.4)',
#         'Content-Type': 'application/json',
#         'X-Algolia-API-Key': '084aa805a4e8f0f531b540c0c29887ce',
#         'X-Algolia-Application-Id': 'P11UZVL396'
#     }
    
#     base_url = "https://cdn.myfonts.net/cdn-cgi/image/width=600,height=auto,fit=contain,format=auto/images/pim/"
#     output_dir = "downloaded_imagezz2"
    
#     def start_requests(self):
#         for page_num in range(4):  # Loop through pages 0, 1, 2, 3
#             form_data = {
#                 "requests": [
#                     {
#                         "indexName": "universal_search_data",
#                         "params": f"analyticsTags=foundry_myfonts&attributesToHighlight=%5B%5D&attributesToRetrieve=%5B%22font_count%22%2C%22family_id%22%2C%22foundry_handle%22%2C%22foundry_name%22%2C%22foundry_title%22%2C%22foundry_logo%22%2C%22foundry_location%22%2C%22foundry_image_urls%22%2C%22foundry_description%22%2C%22handle%22%2C%22has_free%22%2C%22image_urls%22%2C%22font_data.file_type%22%2C%22font_data.handle%22%2C%22font_data.md5%22%2C%22font_data.name%22%2C%22font_data.pim_style_id%22%2C%22name%22%2C%22prices%22%2C%22public_tags%22%2C%22_tags%22%2C%22_tags_de%22%2C%22_tags_es%22%2C%22_tags_fr%22%2C%22_tags_pt%22%2C%22render_text%22%2C%22title%22%2C%22included_packages%22%5D&facets=%5B%22*%22%5D&filters=foundry_handle%3Acultivated-mind-foundry&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&hitsPerPage=20&maxValuesPerFacet=200&page={page_num}&query=&ruleContexts=foundry_myfonts&tagFilters=&clickAnalytics=true&analytics=true&userToken=anonymous-105ac04a-4638-47fd-a95f-e0f04ff2e34b&facetFilters=%5B%5D"
#                     }
#                 ]
#             }
#             yield scrapy.Request(url=self.start_urls[0], method='POST', headers=self.headers, body=json.dumps(form_data), callback=self.parse_json)
    
#     def parse_json(self, response):
#         if response.status == 404:
#             self.logger.error("404 Error: Page not found")
#             return
#         elif response.status == 403:
#             self.logger.error("403 Error: Forbidden access")
#             return
        
#         try:
#             json_data = response.json()
#             image_urls_by_name = self.get_image_urls_by_name(json_data)
#             for name, urls in image_urls_by_name.items():
#                 folder_path = os.path.join(self.output_dir, name)
#                 if not os.path.exists(folder_path):
#                     os.makedirs(folder_path)
#                 for idx, url in enumerate(urls, 1):
#                     yield scrapy.Request(url, meta={'name': name, 'idx': idx}, callback=self.save_image)
#         except Exception as e:
#             self.logger.error(f"Error occurred while parsing JSON: {e}")
    
#     def get_image_urls_by_name(self, json_data):
#         image_urls_by_name = {}
#         if 'results' in json_data:
#             for result in json_data['results']:
#                 if 'hits' in result:
#                     for hit in result['hits']:
#                         name = hit.get('name')
#                         if name and 'image_urls' in hit:
#                             image_urls = [self.base_url + url for url in hit['image_urls']]
#                             image_urls_by_name.setdefault(name, []).extend(image_urls)
#         return image_urls_by_name
    
#     def save_image(self, response):
#         try:
#             name = response.meta['name']
#             idx = response.meta['idx']
#             image_name = f"image_{idx}.png"
#             folder_path = os.path.join(self.output_dir, name)
#             image_path = os.path.join(folder_path, image_name)
#             with open(image_path, 'wb') as f:
#                 f.write(response.body)
#             self.logger.info(f"Image {idx} for {name} downloaded successfully: {image_path}")
#         except Exception as e:
#             self.logger.error(f"Error occurred while saving image {idx} for {name}: {e}")
#------------------------------->> foundry --> User Input
import scrapy
import json
import os

class MyfontsSpider(scrapy.Spider):
    name = "myfonts"
    start_urls = [
        'https://p11uzvl396-dsn.algolia.net/1/indexes/*/queries'
    ]
    
    headers = {
        'X-Algolia-Agent': 'Algolia for JavaScript (4.20.0); Browser (lite); JS Helper (3.14.0); react (17.0.2); react-instantsearch (6.40.4)',
        'Content-Type': 'application/json',
        'X-Algolia-API-Key': '084aa805a4e8f0f531b540c0c29887ce',
        'X-Algolia-Application-Id': 'P11UZVL396'
    }
    
    base_url = "https://cdn.myfonts.net/cdn-cgi/image/width=400,height=auto,fit=contain,format=auto/images/pim/"
    output_dir = "downloaded_imagezz3"
    
    def start_requests(self):
        foundry_name = input("Enter foundry name: ")
        form_data_list = self.construct_form_data(foundry_name)
        for form_data in form_data_list:
            yield scrapy.Request(url=self.start_urls[0], method='POST', headers=self.headers, body=json.dumps(form_data), callback=self.parse_json)
    
    def construct_form_data(self, foundry_name):
        form_data_list = []
        for page_num in range(4):
            form_data = {
                "requests": [
                    {
                        "indexName": "universal_search_data",
                        "params": f"analyticsTags=foundry_myfonts&attributesToHighlight=%5B%5D&attributesToRetrieve=%5B%22font_count%22%2C%22family_id%22%2C%22foundry_handle%22%2C%22foundry_name%22%2C%22foundry_title%22%2C%22foundry_logo%22%2C%22foundry_location%22%2C%22foundry_image_urls%22%2C%22foundry_description%22%2C%22handle%22%2C%22has_free%22%2C%22image_urls%22%2C%22font_data.file_type%22%2C%22font_data.handle%22%2C%22font_data.md5%22%2C%22font_data.name%22%2C%22font_data.pim_style_id%22%2C%22name%22%2C%22prices%22%2C%22public_tags%22%2C%22_tags%22%2C%22_tags_de%22%2C%22_tags_es%22%2C%22_tags_fr%22%2C%22_tags_pt%22%2C%22render_text%22%2C%22title%22%2C%22included_packages%22%5D&facets=%5B%22*%22%5D&filters=foundry_handle%3A{foundry_name}&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&hitsPerPage=20&maxValuesPerFacet=200&page={page_num}&query=&ruleContexts=foundry_myfonts&tagFilters=&clickAnalytics=true&analytics=true&userToken=anonymous-105ac04a-4638-47fd-a95f-e0f04ff2e34b&facetFilters=%5B%5D"
                    }
                ]
            }
            form_data_list.append(form_data)
        
        return form_data_list
    
    def parse_json(self, response):
        if response.status == 404:
            self.logger.error("404 Error: Page not found")
            return
        elif response.status == 403:
            self.logger.error("403 Error: Forbidden access")
            return
        
        try:
            json_data = response.json()
            image_urls_by_name = self.get_image_urls_by_name(json_data)
            for name, urls in image_urls_by_name.items():
                folder_path = os.path.join(self.output_dir, name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                for idx, url in enumerate(urls, 1):
                    yield scrapy.Request(url, meta={'name': name, 'idx': idx}, callback=self.save_image)
        except Exception as e:
            self.logger.error(f"Error occurred while parsing JSON: {e}")
    
    def get_image_urls_by_name(self, json_data):
        image_urls_by_name = {}
        if 'results' in json_data:
            for result in json_data['results']:
                if 'hits' in result:
                    for hit in result['hits']:
                        name = hit.get('name')
                        if name and 'image_urls' in hit:
                            image_urls = [self.base_url + url for url in hit['image_urls']]
                            image_urls_by_name.setdefault(name, []).extend(image_urls)
        return image_urls_by_name
    
    def save_image(self, response):
        try:
            name = response.meta['name']
            idx = response.meta['idx']
            image_name = f"image_{idx}.png"
            folder_path = os.path.join(self.output_dir, name)
            image_path = os.path.join(folder_path, image_name)
            with open(image_path, 'wb') as f:
                f.write(response.body)
            self.logger.info(f"Image {idx} for {name} downloaded successfully: {image_path}")
        except Exception as e:
            self.logger.error(f"Error occurred while saving image {idx} for {name}: {e}")


