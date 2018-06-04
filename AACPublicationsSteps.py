# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import *

# Given Steps

@given('I navigate to the American Alpine Club Publications page')
# This step could be moved to a before_scenario function. It seems more clear to add it here for contextual purposes.
def step_impl(context):
    context.browser.get("http://publications.americanalpineclub.org/")
    if not "AAC Publications" in context.browser.title:
		    raise Exception("Unable to load the American Alpine Publications page!")

# When Steps
@when('I search for all articles')
def step_impl(context):
	#Select the search button
    context.browser.find_element_by_css_selector(".no_radius[value='SEARCH']").click()

@when('I search for "{searchText}"')
def step_impl(context, searchText):
	#Enter search text and select the search option
    context.browser.find_element_by_name("all").send_keys(searchText)
    context.browser.find_element_by_css_selector(".no_radius[value='SEARCH']").click()
   
@when('I search for "{searchText}" using the following filters')
def step_impl(context, searchText):
	# Enter search text, select the journal, and select the search option 
	context.browser.find_element_by_name("all").send_keys(searchText)

	for row in context.table:
		
		journalName = str(row['JournalName']).upper()
		exactMatchChecked = str(row['SearchExactMatch']).upper()

		if journalName == "AAJ":
			context.browser.find_element_by_css_selector(".pub_type[value='aaj']").click()
		elif journalName == "ACCIDENTS":
			context.browser.find_element_by_css_selector(".pub_type[value='anam']").click()
		elif journalName == "ALPINA AMERICANA":
			context.browser.find_element_by_css_selector(".pub_type[value='aa']").click()
		else:
			context.browser.find_element_by_css_selector(".pub_type[value='both']").click()
			break

		context.browser.find_element_by_css_selector(".no_radius[value='SEARCH']").click()


@when('I select the article "{articleName}"')
def step_impl(context, articleName):
    try:
    	#Attempting to find and click the link using the variable specified
    	context.browser.find_element_by_css_selector("a:contains('%s')" % articleName).click()
    except:
    	raise Exception("Unable to find the specified publication!")

# Then Steps

@then('the list of articles are displayed')
def step_impl(context):
	# Verify that rows are returned
	actualRowCount = len(context.browser.find_elements_by_xpath("//table[@id='DataTables_Table_0']/tbody/tr"))
	assert actualRowCount > 0

@then('the Records Found count is greater than zero')
def step_impl(context):
	#Attemtping to find the h4 element, grab its text, and parse it to pull out the record count
	recordsFoundString = context.browser.find_element_by_tag_name('h4').text.split()
	actualNumRecordsFound = recordsFoundString[1]
	assert int(actualNumRecordsFound)>0     

@then('the Records Found count is "{expectedRecordCount}"')
def step_impl(context, expectedRecordCount):
	#Attemtping to find the h4 element, grab its text, and parse it to pull out the record count
	recordsFoundString = context.browser.find_element_by_tag_name('h4').text.split()
	actualNumRecordsFound = recordsFoundString[1]
	assert int(actualNumRecordsFound) == int(expectedRecordCount)

@then('the article "{expectedArticleName}" is displayed')
def step_impl(context, expectedArticleName):
	#Not Implemented: Need to verify the article I'm expecting to be returned is in the table
	actual = context.browser.find_elements_by_xpath("//table[@id='DataTables_Table_0']/tbody/tr/td")

@then('the "{expectedMessageText}" message is displayed')
	# Attempting to validate the 'no data in table' message text on the page 
def step_impl(context, expectedMessageText):
	foundMessage = context.browser.find_element_by_xpath("//table[@id='DataTables_Table_0']/tbody/tr/td")
	print (foundMessage)
	assert foundMessage == expectedMessageText

  

