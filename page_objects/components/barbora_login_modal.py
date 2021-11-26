from playwright.sync_api import Page


class BarboraLoginModal:
    emailInput = 'id=email'
    passwordInput = 'id=password'
    loginModalButton = 'button[type=submit]'

    def __init__(self, page: Page):
        self.page = page

    def fill_email(self, email: str):
        self.page.locator(self.emailInput).fill(email)

    def fill_password(self, password: str):
        self.page.locator(self.passwordInput).fill(password)

    def click_login_button(self):
        self.page.locator(self.loginModalButton).click()
        self.page.wait_for_selector(self.loginModalButton, state="detached")
