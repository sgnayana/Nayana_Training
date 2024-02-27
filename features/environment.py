from selenium import webdriver
import allure
from allure_commons.types import AttachmentType


def before_all(context):
    context.driver = webdriver.Edge()
    # context.text_value = 10

# def after_step(context, step):
#     if step.status == "failed" or "passed":
#         allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

def after_scenario(context, scenario):
    if scenario.status == "failed" or "passed":
        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    
def after_all(context):
    context.driver.close()
