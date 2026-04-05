import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


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
        self.login()

    def test_successful_sign_up(self):
        sign_up_selector = ".header_sign-up-link > .header_sign-up-btn"
        sign_up_button = self.wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, sign_up_selector))
        )
        sign_up_button.click()

        email_input = self.wait.until(
            expected_conditions.visibility_of_element_located((By.ID, "email"))
        )
        email_input.send_keys(self.generate_email())

        first_name_input = self.driver.find_element(By.ID, "firstName")
        first_name_input.send_keys(self.NEW_USER_USERNAME)

        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(self.NEW_USER_PASSWORD)

        repeat_password_input = self.driver.find_element(By.ID, "repeatPassword")
        repeat_password_input.send_keys(self.NEW_USER_PASSWORD)

        sign_up_button = self.driver.find_element(By.XPATH, "//button[@class='greenStyle']")
        sign_up_button.click()

        modal_invisible = self.wait.until(
            expected_conditions.invisibility_of_element_located((By.XPATH, self.modal_xpath))
        )
        self.assertTrue(modal_invisible, "Modal should disappear after sign up")

    def test_successful_create_event(self):
        self.login()
        self.driver.get(self.BASE_URL)

        create_event_selector = ".create > .secondary-global-button"
        create_event_button = self.wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, create_event_selector))
        )
        create_event_button.click()

        self.wait.until(
            expected_conditions.url_contains("/events/create-update-event")
        )
        self.assertIn("/events/create-update-event", self.driver.current_url)

    def login(self):
        sign_in_selector = ".header_navigation-menu-right-list > .header_sign-in-link"
        sign_in_button = self.wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, sign_in_selector))
        )
        sign_in_button.click()

        email_input = self.wait.until(
            expected_conditions.visibility_of_element_located((By.ID, "email"))
        )
        email_input.send_keys(self.LOGIN_EMAIL)

        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(self.LOGIN_PASSWORD)

        sign_in_button = self.driver.find_element(By.XPATH, "//button[@class='greenStyle']")
        sign_in_button.click()

        self.wait.until(expected_conditions.url_contains("/profile/"))
        self.assertIn("/profile/", self.driver.current_url)

    def generate_email(self):
        return f"test{int(time.time())}@example.com"


if __name__ == "__main__":
    unittest.main()

