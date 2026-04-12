from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def wait_for_visible(self, locator):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def wait_for_invisible(self, locator):
        return self.wait.until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def find(self, locator):
        return self.wait_for_visible(locator)

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def type(self, locator, text):
        self.wait_for_visible(locator).send_keys(text)

    def wait_for_url_contains(self, text):
        self.wait.until(expected_conditions.url_contains(text))

    def is_disabled(self, locator):
        return not self.find(locator).is_enabled()
