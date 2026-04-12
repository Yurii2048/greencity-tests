from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.components.auth_modal import AuthModal
from pages.components.header_component import HeaderComponent


class EventsPage(BasePage):
    EVENTS_URL = "https://www.greencity.cx.ua/#/greenCity/events"
    CREATE_EVENT_BUTTON = (By.CSS_SELECTOR, ".create > .secondary-global-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.auth_modal = AuthModal(self)
        self.header = HeaderComponent(self)

    def open_page(self):
        self.open(self.EVENTS_URL)

    def login(self, email, password):
        self.header.open_sign_in()
        self.auth_modal.sign_in(email, password)

    def register(self, email, password, username):
        self.header.open_sign_up()
        self.auth_modal.sign_up(email, password, username)

    def go_to_events(self):
        self.header.go_to_events()

    def open_create_event_page(self):
        self.click(self.CREATE_EVENT_BUTTON)
