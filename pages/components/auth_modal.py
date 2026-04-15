from selenium.webdriver.common.by import By


class AuthModal:
    EMAIL_INPUT = (By.ID, "email")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    PASSWORD_INPUT = (By.ID, "password")
    REPEAT_PASSWORD_INPUT = (By.ID, "repeatPassword")
    SUBMIT_BUTTON = (By.XPATH, "//button[@class='greenStyle']")

    EMAIL_ERROR = (By.ID, "email-err-msg")
    USERNAME_ERROR = (By.ID, "firstname-err-msg")
    PASSWORD_ERROR = (By.CSS_SELECTOR, ".form-content-container >  .password-not-valid")
    CONFIRM_PASSWORD_ERROR = (By.ID, "confirm-err-msg")

    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, ".close-modal-window > .cross-btn")

    def __init__(self, page):
        self.page = page

    def enter_email(self, email):
        self.page.type(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.page.type(self.PASSWORD_INPUT, password)

    def enter_repeat_password(self, password):
        self.page.type(self.REPEAT_PASSWORD_INPUT, password)

    def enter_username(self, username):
        self.page.type(self.FIRST_NAME_INPUT, username)

    def submit(self):
        self.page.click(self.SUBMIT_BUTTON)

    def sign_in(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.submit()

    def sign_up(self, email, username, password, repeat_password=None):
        self.enter_email(email)
        self.enter_username(username)
        self.enter_password(password)
        if repeat_password:
            self.enter_repeat_password(repeat_password)
        else:
            self.enter_repeat_password(password)

    def get_email_error(self):
        return self.page.find(self.EMAIL_ERROR).text

    def get_username_error(self):
        return self.page.find(self.USERNAME_ERROR).text

    def get_password_error(self):
        return self.page.find(self.PASSWORD_ERROR).text

    def get_confirm_password_error(self):
        return self.page.find(self.CONFIRM_PASSWORD_ERROR).text

    def is_submit_disabled(self):
        return self.page.is_disabled(self.SUBMIT_BUTTON)

    def close_modal(self):
        self.page.click(self.CLOSE_MODAL_BUTTON)
