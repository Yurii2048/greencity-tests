import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.events_page import EventsPage
from tests.utils import generate_email


class TestEventsPage(unittest.TestCase):
    MODAL_XPATH = "//app-auth-modal"

    LOGIN_EMAIL = "yuyurara1919@gmail.com"
    LOGIN_PASSWORD = "Qwerty1!"

    NEW_USER_PASSWORD = "Qwerty1!"
    NEW_USER_USERNAME = "example"

    def setUp(self):
        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_window_size(1920, 1080)

        self.page = EventsPage(self.driver)
        self.page.open_page()

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_successful_sign_in(self):
        self.page.login(self.LOGIN_EMAIL, self.LOGIN_PASSWORD)

        self.page.wait_for_url_contains("/profile/")
        self.assertIn("/profile/", self.driver.current_url)

    def test_successful_sign_up(self):
        self.page.register(generate_email(), self.NEW_USER_USERNAME, self.NEW_USER_PASSWORD)

        modal_invisible = self.page.wait_for_invisible((By.XPATH, self.MODAL_XPATH))
        self.assertTrue(modal_invisible, "Modal should disappear after sign up")

    def test_successful_create_event(self):
        self.page.login(self.LOGIN_EMAIL, self.LOGIN_PASSWORD)
        self.page.wait_for_url_contains("/profile/")
        self.page.go_to_events()

        self.page.open_create_event_page()

        self.page.wait_for_url_contains("/events/create-update-event")
        self.assertIn("/events/create-update-event", self.driver.current_url)

    def test_registration_with_invalid_data(self):
        test_data = [
            {
                "email": "example.gmail.com",
                "username": "123",
                "password": "123",
                "repeat_password": "1234bbo"
            },
            {
                "email": "wrong@",
                "username": "1",
                "password": "qwe",
                "repeat_password": "qwer76r"
            }
        ]

        for data in test_data:
            with self.subTest(data=data):
                self.page.registration_with_invalid_data(data["email"], data["username"], data["password"],
                                                         data["repeat_password"])

                self.assertTrue(
                    self.page.auth_modal.is_submit_disabled(),
                    "Submit button should be disabled"
                )

                self.assertNotEqual(
                    self.page.auth_modal.get_email_error(), "",
                    "Email error should be displayed"
                )

                self.assertNotEqual(
                    self.page.auth_modal.get_username_error(), "",
                    "Username error should be displayed"
                )

                self.assertNotEqual(
                    self.page.auth_modal.get_password_error(), "",
                    "Password error should be displayed"
                )

                # self.assertNotEqual(
                #     self.page.auth_modal.get_confirm_password_error(), "",
                #     "Confirm password error should be displayed"
                # )

                self.page.auth_modal.close_modal()


if __name__ == "__main__":
    unittest.main()
