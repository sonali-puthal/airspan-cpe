

from selenium import webdriver
from selenium.webdriver import Keys

from app.core.airspan.element_locators import DeviceATCommandPageLocators
from app.core.browsers.chrome import ChromeBrowser


class DeviceATCommandPage:
    """
    Page object model for the Airspan CPE Login Page
    """

    def __init__(self, browser: ChromeBrowser or None, url: str = None):
        self.browser = browser
        self.driver: webdriver.Chrome = browser.get_driver()
        self.url = 'https://10.0.11.145/web_shell.html' if url is None else url

        self.locators = DeviceATCommandPageLocators()

    def enter_command_textbox(self, shell=str):
        self.driver.get(self.url)
        command_text_box = self.driver.find_element(*self.locators.command_text_box)
        #command_text_box.send_keys(command_text_box, Keys.ENTER)
        save_button = self.driver.find_element(*self.locators.save_button)
        save_button.click


