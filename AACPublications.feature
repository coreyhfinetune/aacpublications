Feature: Search and Select American Alpine Club Publications
http://publications.americanalpineclub.org/
As a user searching for publications by the American Alpine Club, I should be able to search, select, and view a publication

Background:
Given I navigate to the American Alpine Club Publications page

Scenario: User can search for publications without specifying search parameters
	When I search for all articles
	Then the list of articles are displayed 

Scenario: User can search for publications using search parameters
	When I search for "Rainier Kautz Route"
	Then the Records Found count is greater than zero
	And the list of articles are displayed 

Scenario: User can filter the search by the specific journals
	When I search for "Rainier Kautz Route" using the following filters:
	| JournalName | SearchExactMatch |
	| AAJ 		  | FALSE			 |
	Then the list of articles are displayed 
	And the Records Found count is greater than zero

Scenario: User is displayed the proper messaging when searching for an article that does not exist
	When I search for "Kelso Ridge"
	Then the Records Found count is "0"
	And the "No data available in table" message is displayed

Scenario: User can select an article
	When I search for "Kilimanjaro: The White Roof of Africa"
	And I select the article "Kilimanjaro: The White Roof of Africa"
	Then the article "Kilimanjaro: The White Roof of Africa" is displayed





