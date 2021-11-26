from typing import List

from playwright.sync_api import Page


class BarboraCheckoutPage:
    checkoutNextButton = '.b-checkout--continue-btn'
    checkoutCartTable = 'table.b-checkout--tableview'
    checkoutDeliveryTable = 'div.b-deliverytime--body-checkout'

    def __init__(self, page: Page):
        self.page = page

    def click_next_button(self):
        self.page.locator(self.checkoutNextButton).click()

    def look_for_cart_table(self):
        assert self.page.locator(self.checkoutCartTable).is_visible() is True

    def check_delivery_table(self):
        table_texts = self.get_delivery_time_table_texts()
        assert any('€' in text for text in table_texts) is True

    def get_delivery_time_table_texts(self) -> List[str]:
        columns = self.page.wait_for_selector(self.checkoutDeliveryTable).query_selector_all(
            '//div[@class="b-deliverytime--col"]//div')
        table_texts: List[str]
        for i in range(0, len(columns)):
            table_texts.append(columns[i].text_content())

        return table_texts
