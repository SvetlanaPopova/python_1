Scenario Outline: Add new contact
	Given a contact list
	Given a contact with <firstname>, <lastname>, <address> and <mobilephone>
	When I add the contact to the list
	Then the new contact list is equal to the old contact list with the added contact

	Examples:
	| firstname  | lastname  | address  | mobilephone  |
	| firstname1 | lastname1 | address1 | mobilephone1 |
	#| firstname2 | lastname2 | address2 | mobilephone2 |

Scenario: Delete a contact
	Given a non-empty contact list
	Given a random contact from the list
	When I delete the contact from the list
	Then the new contact list is equal to the old contact list without the contact

Scenario Outline: Modify a contact
    Given a contact with <firstname>, <lastname>, <address> and <mobilephone>
	Given a non-empty contact list
	Given a random contact from the list
	When I modify the contact from the list
	Then the new contact list is equal to the old contact list with the modified contact

    Examples:
	| firstname        | lastname        | address        | mobilephone        |
    | firstname_modify | lastname_modify | address_modify | mobilephone_modify |