import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def open_sign_up_modal(wait):
    sign_up_selector = ".header_sign-up-link > .header_sign-up-btn"
    sign_up_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, sign_up_selector)))
    sign_up_button.click()


def open_sign_in_modal(wait):
    sign_in_selector = ".header_navigation-menu-right-list > .header_sign-in-link"
    sign_in_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, sign_in_selector)))
    sign_in_button.click()


def fill_sign_up_form(driver, wait, email, username, password):
    email_input = wait.until(expected_conditions.visibility_of_element_located((By.ID, "email")))
    email_input.send_keys(email)
    driver.find_element(By.ID, "firstName").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "repeatPassword").send_keys(password)


def fill_sign_in_form(driver, wait, email, password):
    email_input = wait.until(expected_conditions.visibility_of_element_located((By.ID, "email")))
    email_input.send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)


def click_submit_button(driver):
    driver.find_element(By.XPATH, "//button[@class='greenStyle']").click()


def click_create_event_button(driver, wait):
    create_event_selector = ".create > .secondary-global-button"
    create_event_button = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, create_event_selector)))
    create_event_button.click()


def generate_email():
    return f"test{int(time.time())}@example.com"
