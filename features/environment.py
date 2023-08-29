import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import Configreader


def before_scenario(context, driver):
    browser = Configreader.read_configuration("basic info", "browser")
    if browser.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(Configreader.read_configuration("basic info", "url"))


def after_scenario(context, driver):
    context.driver.quit()

def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),name="failed_screenshotFailed", attachment_type=AttachmentType.PNG)
