import allure
from playwright.sync_api import Page


class BarboraClearCartModal:
    confirm_button = 'div.modal-dialog div.modal-content button[title="Patvirtinti"]'

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Click confirm in clear cart modal')
    def click_confirm(self):
        self.page.locator(self.confirm_button).click()
