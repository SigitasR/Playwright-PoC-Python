import allure
from playwright.sync_api import Page


class BarboraLoginModal:
    emailInput = 'id=email'
    passwordInput = 'id=password'
    loginModalButton = 'button[type=submit]'

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Enter email: {1}')
    def fill_email(self, email: str):
        self.page.locator(self.emailInput).fill(email)

    @allure.step('Enter password: ***')
    def fill_password(self, password: str):
        self.page.locator(self.passwordInput).fill(password)

    @allure.step('Click login button')
    def click_login_button(self):
        self.page.locator(self.loginModalButton).click()
        self.page.wait_for_selector(self.loginModalButton, state="detached")
