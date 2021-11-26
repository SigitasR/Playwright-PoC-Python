import allure
from playwright.sync_api import Page


class BarboraAgeModal:
    modal_body = 'div.b-alert--modal div.modal-content'
    over_20_button = 'button.c-btn'

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Click age confirmation button')
    def click_over_20_button(self):
        self.page.locator(self.modal_body).locator(self.over_20_button).nth(0).click()
        self.page.wait_for_selector(self.modal_body, state="detached")
