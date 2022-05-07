from behave import *
from selenium import webdriver
# from selenium import *


@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when('I open hegic Homepage')
def step_impl(context):
    context.driver.get("https://hegic.portal.camcom.ai/login")


@when('Enter valid username "user" and password "pwd"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_xpath("//input[@type='email']").send_keys(user)
    context.driver.find_element_by_xpath("//input[@type='password']").send_keys(pwd)
    # context
@when('Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("login").click()

@then('User must successfully login to the homepage')
def step_impl(context):
    text = context.driver.find_element_by_xpath(("/html[1]/body[1]/div[3]/button[2]")).text()
    assert text == "Claims"
    context.driver.close()
