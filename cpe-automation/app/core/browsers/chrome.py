"""
Webdriver class for Chrome interactions
"""
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pathlib
import logging

logger = logging.getLogger(__name__)

# TODO: Move the following to a config file?
# https://googlechromelabs.github.io/chrome-for-testing/#stable
# download the latest chromedriver from the above link and mention its path below
dir_path = pathlib.Path(__file__).parent.absolute()

CHROMEDRIVER_DEFAULT_PATH = dir_path / pathlib.Path("chrome/chromedriver")


class ChromeBrowser:
    def __init__(
        self, chromedriver_path: str = None, debug: bool = False, headless: bool = True
    ):
        """
        :param chromedriver_path: Relative path to the chrome driver
        :param debug: If True, keeps the browser open on encountering exceptions
        :param headless: If True and debug is False then disables the UI of browser
        """

        self.get_details = None
        self.chromedriver_path = (
            chromedriver_path
            if chromedriver_path is not None
            else CHROMEDRIVER_DEFAULT_PATH
        )
        self.service = Service(executable_path=self.chromedriver_path)
        self.options = webdriver.ChromeOptions()
        self.configure_options(debug, headless)
        self.driver = None

    def configure_options(self, debug: bool, headless: bool):
        self.options.accept_insecure_certs = True
        # Disable the banner "Chrome is being controlled via automation"
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        if headless:
            self.options.add_argument('--headless=new')
        if debug:
            self.options.add_experimental_option("detach", True)

    def open(self):
        """
        Opens the Chrome webdriver and returns a driver instance
        """
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        return self.driver

    def get_driver(self):
        """
        :return: an instance of driver if it exists otherwise opens one and return it
        """
        if self.driver is None:
            return self.open()
        else:
            return self.driver

    def close(self):
        self.driver.quit()

    def hover(self, *locator):
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_for_element(self, *locator):
        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(
                f'Timeout occurred while trying to locate the element "{locator[1]}" by "{locator[0]}"'
            )
            return None

    def wait_for_element_and_get_text(self, *locator):
        element = self.wait_for_element(*locator)
        if element is not None:
            return element.text
        else:
            return None

    def __del__(self):
        self.close()
