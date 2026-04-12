from selenium.webdriver.common.by import By


class HeaderComponent:
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-in-link")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, ".header_sign-up-link > .header_sign-up-btn")
    EVENTS_LINK = (
        By.XPATH,
        "//header//a[contains(@class, 'url-name') and contains(., 'Події') or contains(., 'Events')]"
    )

    def __init__(self, page):
        self.page = page

    def open_sign_in(self):
        self.page.click(self.SIGN_IN_BUTTON)

    def open_sign_up(self):
        self.page.click(self.SIGN_UP_BUTTON)

    def go_to_events(self):
        self.page.click(self.EVENTS_LINK)
