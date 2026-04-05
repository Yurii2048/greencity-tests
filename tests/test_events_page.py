import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from tests.utils import open_sign_up_modal, fill_sign_up_form, click_submit_button, open_sign_in_modal, \
    fill_sign_in_form, click_create_event_button, generate_email


class TestEventsPage(unittest.TestCase):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"
    modal_xpath = "//app-auth-modal"

    LOGIN_EMAIL = "yuyurara1919@gmail.com"
    LOGIN_PASSWORD = "Qwerty1!"

    NEW_USER_PASSWORD = "Qwerty1!"
    NEW_USER_USERNAME = "example"

    def setUp(self):
        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_window_size(1920, 1080)
        self.driver.get(self.BASE_URL)
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_successful_sign_in(self):
        open_sign_in_modal(self.wait)
        fill_sign_in_form(self.driver, self.wait, self.LOGIN_EMAIL, self.LOGIN_PASSWORD)
        click_submit_button(self.driver)

        self.wait.until(expected_conditions.url_contains("/profile/"))
        self.assertIn("/profile/", self.driver.current_url)

    def test_successful_sign_up(self):
        open_sign_up_modal(self.wait)
        fill_sign_up_form(self.driver, self.wait, generate_email(), self.NEW_USER_USERNAME, self.NEW_USER_PASSWORD)
        click_submit_button(self.driver)

        modal_invisible = self.wait.until(
            expected_conditions.invisibility_of_element_located((By.XPATH, self.modal_xpath)))
        self.assertTrue(modal_invisible, "Modal should disappear after sign up")

    def test_successful_create_event(self):
        open_sign_in_modal(self.wait)
        fill_sign_in_form(self.driver, self.wait, self.LOGIN_EMAIL, self.LOGIN_PASSWORD)
        click_submit_button(self.driver)
        self.wait.until(expected_conditions.url_contains("/profile/"))
        self.driver.get(self.BASE_URL)

        click_create_event_button(self.driver, self.wait)

        self.wait.until(expected_conditions.url_contains("/events/create-update-event"))
        self.assertIn("/events/create-update-event", self.driver.current_url)


if __name__ == "__main__":
    unittest.main()
