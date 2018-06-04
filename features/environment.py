# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Sauce Labs Configuration
#def before_all(context):
	# desired_cap = {
		# 'platform': "Mac OS X 10.13.4",
		# 'browserName': "chrome",
		# 'version': "31",
		# 'idleTimeout': 20,
		# 'commandTimeout': 20
		#}

	# Not sure if this needs to be shoved into the context.	
	# driver = webdriver.Remote(command_executor='http://USERNAME:ACCESSKEY@ondemand.saucelabs.com:80/wd/hub', desired_capabilities=desired_cap)
	# context.browser = webdriver.Remote(command_executor='http://USERNAME:ACCESSKEY@ondemand.saucelabs.com:80/wd/hub', desired_capabilities=desired_cap)

#def after_all(context):
#    driver.quit()
#    context.browser.quit()

# Local Configuration

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()