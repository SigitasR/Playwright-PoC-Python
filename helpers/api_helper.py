from playwright.sync_api import Page


class Api:
    token = 'Basic YXBpa2V5OlNlY3JldEtleQ=='

    @staticmethod
    def login(page: Page, email: str, password: str):
        page.context.request.post(url='/api/eshop/v1/user/login',
                                  headers={'Authorization': Api.token},
                                  data={'rememberMe': True, 'email': email, 'password': password})

    @staticmethod
    def clear_cart(page: Page):
        page.context.request.delete(url='/api/eshop/v1/cart/removeallitems',
                                    headers={'Authorization': Api.token})
