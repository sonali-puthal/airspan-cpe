from app.core.airspan.element_locators import HomePageLocators
from app.core.browsers.chrome import ChromeBrowser


class HomePage:
    """
    Page object model for the Airspan CPE Device View Page
    """

    def __init__(self, browser: ChromeBrowser or None, url: str = None):
        self.browser = browser
        self.driver = browser.get_driver()
        self.url = 'https://10.0.11.145/home.html' if url is None else url

        self.locators = HomePageLocators()

    def get_details(self):
        self.driver.get(self.url)
        details = {
            'cellular_network': {
                'status': self.browser.wait_for_element_and_get_text(*self.locators.lte_main_status),
                'operator': self.browser.wait_for_element_and_get_text(*self.locators.lte_operator_plmn),
                'mode': self.browser.wait_for_element_and_get_text(*self.locators.lte_mode),
                '5g_cell_id': self.browser.wait_for_element_and_get_text(*self.locators.lte_cell_id_5g),
                '5g_rsrp': self.browser.wait_for_element_and_get_text(*self.locators.lte_rsrp_5g),
                '5g_rsrq': self.browser.wait_for_element_and_get_text(*self.locators.lte_rsrq_5g),
                '5g_snir': self.browser.wait_for_element_and_get_text(*self.locators.lte_sinr_5g),
            },
            'wan_status': {
                'connect_method': self.browser.wait_for_element_and_get_text(*self.locators.lte_network),
                'connect_mode': self.browser.wait_for_element_and_get_text(*self.locators.network_wan_settings_mode),
                'ip_address': self.browser.wait_for_element_and_get_text(*self.locators.network_wan_settings_ip),
                'subnet_mask': self.browser.wait_for_element_and_get_text(*self.locators.network_wan_settings_mask),
                'primary_dns_server': self.browser.wait_for_element_and_get_text(
                    *self.locators.network_wan_settings_dns_bak),
                'secondary_dns_server': self.browser.wait_for_element_and_get_text(
                    *self.locators.network_wan_settings_dns_bak_secondary),
            },
        }
        return details
