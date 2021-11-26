import allure
from playwright.sync_api import Page

from page_objects.components.barbora_login_modal import BarboraLoginModal
from page_objects.components.barbora_clear_cart_modal import BarboraClearCartModal


class BarboraFrontPage:
    login_modal: BarboraLoginModal
    clear_cart: BarboraClearCartModal

    vilniusCountyButton = 'button[data-county="vilnius"]'
    standardBarboraEshopButton = 'button[class="link-to-page-btn "]'
    allowCookiesButton = 'id=CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll'
    loginLink = 'button.b-login-register--login'
    buyButton = 'div.b-sidebar-bottom button.b-sidebar-bottom--purchase-btn'
    searchInput = 'header input.b-search'

    def __init__(self, page: Page):
        self.page = page
        self.login_modal = BarboraLoginModal(self.page)
        self.clear_cart = BarboraClearCartModal(self.page)

    @allure.step('Accept cookies')
    def accept_all_cookies(self):
        self.page.locator(self.allowCookiesButton).click()

    @allure.step('Click login')
    def click_login_link(self):
        self.page.locator(self.loginLink).nth(1).click()

    @allure.step('Click buy')
    def click_buy_button(self):
        self.page.locator(self.buyButton).click()

    @allure.step('Search for: {1}')
    def search_for(self, product: str):
        self.page.locator(self.searchInput).fill(product)
        self.page.locator(self.searchInput).press('Enter')
