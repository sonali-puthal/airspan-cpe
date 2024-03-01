from app.core.airspan.element_locators import LoginPageLocators
from selenium import webdriver
from selenium.webdriver import Keys
from app.core.browsers.chrome import ChromeBrowser


class LoginPage:
    """
    Page object model for the Airspan CPE Login Page
    """

    def __init__(self, browser: ChromeBrowser or None, url: str = None):
        self.browser = browser
        self.driver: webdriver.Chrome = browser.get_driver()
        self.url = 'https://10.0.11.145/pub/login.html' if url is None else url

        self.locators = LoginPageLocators()

    def enter_username_and_password(self, username, password):
        self.driver.get(self.url)
        username_text_box = self.driver.find_element(*self.locators.username)
        username_text_box.send_keys(username, Keys.TAB, password, Keys.ENTER)
