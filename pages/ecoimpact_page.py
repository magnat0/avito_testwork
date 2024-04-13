from playwright.sync_api import Page
import config
import json


class EcoImpactPage:

    def open_index_page(self, page: Page, indicator: any, screen_name : str) -> None:
        
        def handle_request(route):
                
                with open('data.json', 'r') as f:
                    json_data = json.load(f) 

                for key in json_data['result']['blocks']['personalImpact']['data'].keys():
                    json_data['result']['blocks']['personalImpact']['data'][key] = indicator
                route.fulfill(json=json_data)

        page.route(config.api.DOMAIN, handle_request)
        page.goto(config.url.DOMAIN)
        page.wait_for_selector(config.screen_selector) 

        self.make_screenshot_page(page, config.screen_selector, screen_name)

    def make_screenshot_page(self, page : Page, selector, screen_name : str) -> None:
        element = page.query_selector(selector) 
        element.screenshot(path=f'output/{screen_name}.jpg')