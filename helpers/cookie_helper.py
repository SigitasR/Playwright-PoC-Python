from playwright.sync_api import Page


class Cookie:
    @staticmethod
    def set_region_cookie(page: Page, region=''):
        page.context.add_cookies([{
            'name': 'region',
            'value': f'{region.lower()}.barbora.lt',
            'path': '/',
            'domain': '.barbora.lt'
        }])
