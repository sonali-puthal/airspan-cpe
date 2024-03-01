from app.core.airspan.element_locators import DeviceStataticsPageLocators
from app.core.browsers.chrome import ChromeBrowser


class DeviceStataticsPage:
    """
    Page object model for the Airspan CPE Device View Page
    """

    def __init__(self, browser: ChromeBrowser or None, url: str = None):
        self.browser = browser
        self.driver = browser.get_driver()
        self.url = 'https://10.0.11.145/statistical_data.html' if url is None else url

        self.locators = DeviceStataticsPageLocators()

    def get_details(self, shell=str):
        self.driver.get(self.url)
        details = {
            'APN_List': self.browser.wait_for_element_and_get_text(*self.locators.APN_List),
        }
        return details
