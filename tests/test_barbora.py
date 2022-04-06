import os

import pytest
from playwright.sync_api import Page
from pytest import mark

from helpers.api_helper import Api
from helpers.cookie_helper import Cookie
from page_objects.barbora_front_page import BarboraFrontPage
from page_objects.barbora_product_page import BarboraProductPage
from page_objects.components.barbora_cart_sidebar import BarboraCartSidebar
from page_objects.components.barbora_product_list import BarboraProductList


@mark.api_login
class TestBarbora:
    front: BarboraFrontPage
    product_list: BarboraProductList
    product_page: BarboraProductPage
    cart_sidebar: BarboraCartSidebar

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.front = BarboraFrontPage(page)
        self.product_list = BarboraProductList(page)
        self.product_page = BarboraProductPage(page)
        self.cart_sidebar = BarboraCartSidebar(page)
        Cookie.set_region_cookie(page)
        page.goto('/')
        Api.login(page, os.environ['EMAIL'], os.environ['PASS'])
        Api.clear_cart(page)
        page.reload()

    def test_barbora(self):
        search_term = 'grimbergen'
        self.front.search_for(search_term)
        self.product_list.click_product()
        self.product_page.age_modal.click_over_20_button()
        self.product_page.click_add_to_cart()
        self.product_page.age_modal.click_over_20_button()
        self.cart_sidebar.check_first_item_in_cart(search_term)
