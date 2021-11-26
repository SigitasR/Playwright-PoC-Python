from typing import List

import allure
from assertpy import assert_that
from playwright.sync_api import Page


class BarboraCheckoutPage:
    checkoutNextButton = '.b-checkout--continue-btn'
    checkoutCartTable = 'table.b-checkout--tableview'
    checkoutDeliveryTable = 'div.b-deliverytime--body-checkout'

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Click Next button')
    def click_next_button(self):
        self.page.locator(self.checkoutNextButton).click()

    @allure.step('Look for cart table')
    def look_for_cart_table(self):
        assert_that(self.page.wait_for_selector(self.checkoutCartTable).is_visible()).is_true()

    @allure.step('Check delivery times table')
    def check_delivery_table(self):
        table_texts = self.get_delivery_time_table_texts()
        assert_that(any('€' in text for text in table_texts)).is_true()

    def get_delivery_time_table_texts(self) -> List[str]:
        columns = self.page.wait_for_selector(self.checkoutDeliveryTable).query_selector_all(
            '//div[@class="b-deliverytime--col"]//div')
        table_texts: List[str] = []
        for i in range(0, len(columns)):
            table_texts.append(columns[i].text_content())

        return table_texts
