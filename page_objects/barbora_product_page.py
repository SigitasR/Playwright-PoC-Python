from playwright.sync_api import Page

from page_objects.components.barbora_age_modal import BarboraAgeModal


class BarboraProductPage:
    age_modal: BarboraAgeModal

    item_price = 'div.b-product-info--price-and-quantity span[itemprop="price"]'
    add_to_cart_button = 'div.b-product-info--price-and-quantity div.b-product-cart-link button.c-btn--brand-primary'

    def __init__(self, page: Page):
        self.page = page
        self.age_modal = BarboraAgeModal(self.page)

    def click_add_to_cart(self):
        self.page.locator(self.add_to_cart_button).click()
