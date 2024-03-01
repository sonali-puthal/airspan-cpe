import logging
from pprint import pformat
from telnetlib import EC
from turtledemo.chaos import f
from urllib import response

import fastapi
from h11 import Response
from selenium.webdriver.support.wait import WebDriverWait

from app.core.airspan.device_AT_command_page import DeviceATCommandPage
from app.core.airspan.device_view_page import DeviceViewPage
from app.core.airspan.home_page import HomePage
from app.core.airspan.login_page import LoginPage
from app.core.airspan.statatics import DeviceStataticsPage
from app.core.browsers.chrome import ChromeBrowser, CHROMEDRIVER_DEFAULT_PATH
from selenium.webdriver.common.by import By

router = fastapi.APIRouter(tags=["airspan-cpe"], responses={404: {"description": "Not found"}})

logger = logging.getLogger(__name__)
browser = None
driver = None

# TODO: Move the following to a config file
AIRSPAN_CPE = {
    "login_url": "https://10.0.11.145/pub/login.html",
    "username": "admin",
    "password": "admin",
    "command_text_box": "AT+CGMI"  # TODO: properly take password from environment variable or a config file.
}


@router.get("/login")
def login():
    global browser, driver
    logger.info("Starting browser")
    logger.debug(f"Chrome driver path: {CHROMEDRIVER_DEFAULT_PATH}")

    if browser is None:
        browser = ChromeBrowser(chromedriver_path=CHROMEDRIVER_DEFAULT_PATH, debug=False, headless=False)
        driver = browser.get_driver()

    login_page = LoginPage(browser=browser, url=AIRSPAN_CPE["login_url"])
    login_page.enter_username_and_password(AIRSPAN_CPE["username"], AIRSPAN_CPE["password"])


@router.get("/cpe-status")
def cpe_status():
    global browser, driver
    logger.info("Starting browser")
    logger.debug(f"Chrome driver path: {CHROMEDRIVER_DEFAULT_PATH}")

    if browser is None:
        browser = ChromeBrowser(chromedriver_path=CHROMEDRIVER_DEFAULT_PATH, debug=False, headless=False)
        driver = browser.get_driver()

    login_page = LoginPage(browser=browser, url=AIRSPAN_CPE["login_url"])
    login_page.enter_username_and_password(AIRSPAN_CPE["username"], AIRSPAN_CPE["password"])
    driver.maximize_window()

    home_page = HomePage(browser)
    logger.debug('Collecting cellular network status from home page')
    cellular_network_details = home_page.get_details()
    logger.info(f'cellular_network_details:\n{pformat(cellular_network_details, sort_dicts=False)}')
    # return cellular_network_details

    cellular_network = cellular_network_details["cellular_network"]

    return cellular_network["status"]


@router.post("/viewpage")
def viewpage():
    global browser, driver
    logger.info("Starting browser")
    logger.debug(f"Chrome driver path: {CHROMEDRIVER_DEFAULT_PATH}")

    if browser is None:
        browser = ChromeBrowser(
            chromedriver_path=CHROMEDRIVER_DEFAULT_PATH, debug=False, headless=True
        )
        driver = browser.get_driver()

    login_page = LoginPage(browser=browser, url=AIRSPAN_CPE["login_url"])
    login_page.enter_username_and_password(
        AIRSPAN_CPE["username"], AIRSPAN_CPE["password"]
    )
    driver.maximize_window()

    admin_setting_link = driver.find_element(By.XPATH, "//*[@id='advanced']")
    admin_setting_link.click()

    device_view_page = DeviceViewPage(browser)
    device_details = device_view_page.get_details()

    print(f"device_details:\n{pformat(device_details, sort_dicts=False)}")
    Version_Information = device_details["Version_Information"]

    # return Version_Information["lte_imsi"]

    response = Response()
    if Version_Information["lte_imsi"]:
        response.status_code = 200
        return {"RESULT": "0", "returnValue": Version_Information["lte_imsi"]}
    else:
        response.status_code = 401
        logger.debug("Failed to get imsi value")
        return {"RESULT": "1", "returnValue": "Failed"}


@router.get("/AT_command")
def AT_command(details: dict = None):
    """
    Logs in to the Airspan CPE UI and returns a response with status code 200 if successful

    :return: Response with status code 200 if successful, else 401
    """
    global browser, driver
    logger.info("Starting browser")
    logger.debug(f"Chrome driver path: {CHROMEDRIVER_DEFAULT_PATH}")

    if browser is None:
        browser = ChromeBrowser(
            chromedriver_path=CHROMEDRIVER_DEFAULT_PATH, debug=False, headless=False
        )
        driver = browser.get_driver()

    login_page = LoginPage(browser=browser)
    login_page.enter_username_and_password(
        AIRSPAN_CPE["username"], AIRSPAN_CPE["password"]
    )
    device_AT_command_page = DeviceATCommandPage(browser)
    device_AT_command_page.enter_command_text_box(AIRSPAN_CPE["command_text_box"])


@router.post("/Statistics")
def cpe_status(logged_in: bool = False):
    """
    Reads all the details from the Airspan CPE UI and returns a response with status code 200 if successful

    :param logged_in: If True, assumes that the user is already logged in to the UI
    :return: Response with status code 200 if successful, else 401
    """
    global browser, driver

    if browser is None:
        logger.info("Starting browser")
        logger.debug(f"Chrome driver path: {CHROMEDRIVER_DEFAULT_PATH}")
        browser = ChromeBrowser(
            chromedriver_path=CHROMEDRIVER_DEFAULT_PATH, debug=False, headless=True)
        driver = browser.get_driver()

    logger.debug(f"Query parameter logged_in received as '{logged_in}'")
    if not logged_in:
        login_page = LoginPage(browser=browser, url=AIRSPAN_CPE["login_url"])
        login_page.enter_username_and_password(
            AIRSPAN_CPE["username"], AIRSPAN_CPE["password"]
        )

        driver.maximize_window()


    statatics_page = DeviceStataticsPage(browser)
    statatics_page_details = statatics_page.get_details()

    print(f"statatics_page_details:\n{pformat(statatics_page_details, sort_dicts=False)}")

