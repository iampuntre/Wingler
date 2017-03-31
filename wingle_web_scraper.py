from selenium import webdriver
import logging
from time import sleep


def restart_script():
    logging.basicConfig()
    logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
    logger.setLevel(logging.DEBUG)
    ip_address = "http://192.168.8.1"
    try:
        browser.get(ip_address)
        logger.info("Browser visits the address")

        sleep(40)
        reset_btn= browser.find_element_by_id("mobile_connect_btn")
        reset_btn.click()
        logger.info("Restart Button Clicked")
        logger.info("Waiting for Response from Button")
        sleep(20)
        user_name = browser.find_element_by_id("username").send_keys("admin")
        password = browser.find_element_by_id("password").send_keys("admin")
        login_btn = browser.find_element_by_id("pop_login").click()
        sleep(20)
        logger.info("Logged In")
        logger.info("Waiting for Response from Log In button")
        status = browser.find_element_by_id("index_connection_status").text.split('\n')
        if status[0] == 'Disconnected':
            reset_btn.click()
            logger.info("Restarting")
            logger.info("Waiting for Response from Restart button")
            sleep(20)
        status = browser.find_element_by_id("index_connection_status").text.split('\n')
        logger.info(status[0])
        browser.close()
        return status[0]
    except:
        return "Error"

browser = webdriver.PhantomJS()

status = restart_script()
print status
