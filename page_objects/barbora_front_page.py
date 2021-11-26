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

    def accept_all_cookies(self):
        self.page.locator(self.allowCookiesButton).click()

    def click_login_link(self):
        self.page.locator(self.loginLink).nth(1).click()

    def search_for(self, product: str):
        self.page.locator(self.searchInput).fill(product)
        self.page.locator(self.searchInput).press('Enter')
