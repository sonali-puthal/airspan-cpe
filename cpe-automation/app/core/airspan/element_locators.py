"""
Module contains all the element locators for various pages in Airspan CPE as separate classes
"""

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    def __init__(self):
        self.username = (By.ID, "username")


class DeviceViewPageLocators(object):
    def __init__(self):
        self.system_product_model = (By.ID, 'systemProductModel')
        self.system_version_hw = (By.ID, 'systemVersionHw')
        self.system_version_running = (By.ID, 'systemVersionRunning')
        self.system_version_uboot = (By.ID, 'systemVersionUboot')
        self.system_version_sn = (By.ID, 'systemVersionSn')
        self.lte_imei = (By.ID, 'lteImei')
        self.lte_imsi = (By.ID, 'lteImsi')
        self.network_lan_settings_mac = (By.ID, 'networkLanSettingsMac')
        self.network_lan_setting_ip = (By.ID, 'networkLanSettingIp')
        self.network_lan_setting_mask = (By.ID, 'networkLanSettingMask')


class HomePageLocators(object):
    def __init__(self):
        self.lte_main_status = (By.ID, 'lteMainStatusGet')
        self.lte_operator_plmn = (By.ID, 'lteOperatorGet')
        self.lte_mode = (By.ID, 'lteModeGet')
        self.lte_cell_id_5g = (By.ID, 'lteCellidGet_5g')
        self.lte_rsrp_5g = (By.ID, 'lteRsrp0_5g')
        self.lte_rsrq_5g = (By.ID, 'lteRsrq_5g')
        self.lte_sinr_5g = (By.ID, 'lteSinr_5g')
        self.lte_network = (By.ID, 'lteNetwork')
        self.network_wan_settings_mode = (By.ID, 'networkWanSettingsMode')
        self.network_wan_settings_ip = (By.ID, 'networkWanSettingsIp')
        self.network_wan_settings_mask = (By.ID, 'networkWanSettingsMask')
        self.network_wan_settings_dns_bak = (By.ID, 'networkWanSettingsDns_bak')
        self.network_wan_settings_dns_bak_secondary = (By.ID, 'networkWanSettingsDns_bak_Secondary')


class DeviceATCommandPageLocators(object):
    def __int__(self):
        self.command_text_box = (By.NAME, 'webshell_name')
        self.command_text_box.send_keys("command_text_box")
        self.command_text_box.send_keys(Keys.RETURN)
        self.save_button = (By.ID, "SubmitBtn")


class DeviceStataticsPageLocators(object):
    def __init__(self):
        self.APN_List = (By.XPATH, '//*[@id="wantable"]')
