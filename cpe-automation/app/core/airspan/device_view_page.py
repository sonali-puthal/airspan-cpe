from app.core.airspan.element_locators import DeviceViewPageLocators
from app.core.browsers.chrome import ChromeBrowser


class DeviceViewPage:
    """
    Page object model for the Airspan CPE Device View Page
    """

    def __init__(self, browser: ChromeBrowser or None, url: str = None):
        self.browser = browser
        self.driver = browser.get_driver()
        self.url = 'https://10.0.11.145/index.html' if url is None else url

        self.locators = DeviceViewPageLocators()

    def get_details(self):
        self.driver.get(self.url)
        details = {
            'system_product_model': self.browser.wait_for_element_and_get_text(*self.locators.system_product_model),
            'system_version_hw': self.browser.wait_for_element_and_get_text(*self.locators.system_version_hw),
            'system_version_running': self.browser.wait_for_element_and_get_text(*self.locators.system_version_running),
            'system_version_uboot': self.browser.wait_for_element_and_get_text(*self.locators.system_version_uboot),
            'system_version_sn': self.browser.wait_for_element_and_get_text(*self.locators.system_version_sn),
            'lte_imei': self.browser.wait_for_element_and_get_text(*self.locators.lte_imei),
            'lte_imsi': self.browser.wait_for_element_and_get_text(*self.locators.lte_imsi),
            'network_lan_settings_mac': self.browser.wait_for_element_and_get_text(*self.locators.network_lan_settings_mac),
            'network_lan_setting_ip': self.browser.wait_for_element_and_get_text(*self.locators.network_lan_setting_ip),
            'network_lan_setting_mask': self.browser.wait_for_element_and_get_text(*self.locators.network_lan_setting_mask),
        }
        return details



