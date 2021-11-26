from playwright.sync_api import Page


class BarboraProductList:
    productListWrapper = 'div.b-products-list--wrapper'
    productItems = 'div.b-product--wrap'

    def __init__(self, page: Page):
        self.page = page

    def click_product(self, product_number = 0):
        wrapper = self.page.wait_for_selector(self.productListWrapper)
        wrapper.query_selector_all(self.productItems)[product_number].click()
