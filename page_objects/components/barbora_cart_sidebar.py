from assertpy import assert_that
from playwright.sync_api import Page

from page_objects.components.barbora_clear_cart_modal import BarboraClearCartModal


class BarboraCartSidebar:
    confirm_modal: BarboraClearCartModal

    cart_sidebar = 'div.b-cart--scrollable-blocks-wrap--cart-content'
    clear_cart_button = 'div.b-cart--scrollable-blocks-wrap--cart-header button'
    cart_items = 'div.b-next-cart-item'
    buy_button = 'div.b-sidebar-bottom button.b-sidebar-bottom--purchase-btn'

    def __init__(self, page: Page):
        self.page = page
        self.confirm_modal = BarboraClearCartModal(self.page)

    def check_first_item_in_cart(self, text: str):
        sidebar = self.page.wait_for_selector(self.cart_sidebar)
        assert_that(sidebar.query_selector(self.cart_items).text_content().lower()).contains_ignoring_case(text)

    def click_buy_button(self):
        self.page.locator(self.buy_button).click()

    def click_clear_cart(self):
        self.page.locator(self.clear_cart_button).click()
