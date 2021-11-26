import os

import pytest
from playwright.sync_api import Page
from pytest import mark

from helpers.cookie_helper import Cookie
from page_objects.barbora_checkout_page import BarboraCheckoutPage
from page_objects.barbora_front_page import BarboraFrontPage
from page_objects.barbora_product_page import BarboraProductPage
from page_objects.components.barbora_cart_sidebar import BarboraCartSidebar
from page_objects.components.barbora_product_list import BarboraProductList


@mark.full_flow
class TestBarboraFlow:
    front: BarboraFrontPage
    product_list: BarboraProductList
    product_page: BarboraProductPage
    cart_sidebar: BarboraCartSidebar
    checkout: BarboraCheckoutPage

    @pytest.fixture(autouse=True)
    def setup_teardown(self, page: Page):
        self.front = BarboraFrontPage(page)
        self.product_list = BarboraProductList(page)
        self.product_page = BarboraProductPage(page)
        self.cart_sidebar = BarboraCartSidebar(page)
        self.checkout = BarboraCheckoutPage(page)
        Cookie.set_region_cookie(page)
        page.goto('/')
        yield
        page.goto('https://pagrindinis.barbora.lt')
        self.cart_sidebar.click_clear_cart()
        self.cart_sidebar.confirm_modal.click_confirm()

    def test_barbora_full_flow(self):
        self.front.accept_all_cookies()
        self.front.click_login_link()
        self.front.login_modal.fill_email(os.environ['EMAIL'])
        self.front.login_modal.fill_password(os.environ['PASS'])
        self.front.login_modal.click_login_button()

        self.front.search_for('fujimi')
        self.product_list.click_product()
        self.product_page.age_modal.click_over_20_button()
        self.product_page.click_add_to_cart()
        self.product_page.age_modal.click_over_20_button()

        self.front.search_for('jautiena')
        self.product_list.click_product()
        self.product_page.click_add_to_cart()

        self.front.search_for('duona')
        self.product_list.click_product()
        self.product_page.click_add_to_cart()

        self.cart_sidebar.check_first_item_in_cart('duona')

        self.front.click_button_button()
        self.checkout.click_next_button()

        self.checkout.look_for_cart_table()
        self.checkout.click_next_button()
        self.checkout.check_delivery_table()

