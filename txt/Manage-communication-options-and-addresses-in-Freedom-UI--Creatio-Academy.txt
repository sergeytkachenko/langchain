



 This functionality is available in Creatio version 8.0.9 and later.
 




 In Creatio, you can manage the communication options and addresses of contacts and accounts on their form pages in the
 
 Customer 360
 
 app. Manage the communication options in the top left and manage the addresses on the
 
 Contact info
 
 tab.
 



 You can use
 **default types** 
 of communication options or add
 **custom types** 
 . Use the
 
 Communication option types
 
 lookup to add custom types of communication options. Custom communication option types fall into one of the pre-set communication types specified on the page of the individual lookup record: “Email,” “Phone,” “SMS,” “Social network,” and “Web.” Specify the needed communication type when adding a custom communication option.
 





 Attention.
 
 If Microsoft Exchange integration is configured, we do not recommend changing the default communication option types, since this might lead to synchronization errors.
 




 Communication options can have various
 **display formats** 
 . The format determines the
 **action** 
 executed when you click the communication option, for example, opening the email client. The following display formats are available:
 


* text
* phone
* email
* web
* skype
* twitter
* linkedin
* google
* facebook



 Creatio sets the display format for new communication options to “text”
 **automatically** 
 . You can change the format
 **manually** 
 in the
 
 Communication option types
 
 lookup if needed.
 



 Add a communication option
----------------------------



 Use the
 
 Communication options
 
 component and the
 
 Add communication option
 
 button to specify the communication options of a contact or account. To do this:
 





 Fig. 1
 
 Communication options
 
 component
 




![scr_communication_options_component.png](/docs/sites/en/files/images/CRM_Tools/communications_and_addresses_in_freedom_ui/scr_communication_options_component.png)



 Mark a communication option as primary
----------------------------------------



 Creatio marks one communication option per option type as
 **primary** 
 . When a communication option is marked as primary, its value is synchronized with the corresponding object field if it exists, for example,
 
 Email
 
 . The first added communication option is marked as primary
 **automatically** 
 . Creatio does not mark any other options of the same type you add later as primary. You can change the primary communication option
 **manually** 
 if needed. To do this:
 



**As a result** 
 , Creatio will mark the communication option as primary and remove the mark from the original primary communication option.
 



 If you
 **delete** 
 a primary communication option and other options of the same type exist, Creatio marks the newest communication option as primary.
 



 Keep communication options valid
----------------------------------



 Creatio marks newly added communication options as
 **valid** 
 automatically. You can also mark communication options as
 **invalid** 
 or valid manually if needed. For example, if the email address of the customer changes, you can add a new address to the detail component and mark the previous address as invalid manually. To do this:
 



**As a result** 
 , Creatio will add “invalid” next to the field name (Fig. 4)
 





 Fig. 4 Invalid communication option
 




![scr_invalid_communication_option.png](/docs/sites/en/files/images/CRM_Tools/communications_and_addresses_in_freedom_ui/scr_invalid_communication_option.png)



 Depending on the received email responses in Marketing Creatio, Creatio can
 **mark an email address as invalid automatically** 
 . This occurs if the sent emails received “Hard Bounce” response 5 times in a row for any of the following reasons:
 



 If Creatio receives the “Hard Bounce” response for the “Recipient Blocked” reason, the email address is marked as invalid immediately.
 



 To view the reasons for the response, open the email page → the
 
 Audience
 
 tab → the
 
 Response reason
 
 column.
 



 Add an address
----------------



 Use the
 
 Addresses
 
 expanded list to specify the addresses of a contact or account. To do this:
 



 You can open an account address to
 **view it on the map** 
 . If the location of the account on the map is not correct, drag the marker to the correct position and save the changes.
 





 Attention.
 
 Creatio displays addresses using the OpenStreetMap service integration. The service is developed and maintained by a third party. Creatio assumes no responsibility for the operation of the service and the content of OpenStreetMap maps.
 



1. Go to the
 
 Contacts
 
 or
 
 Accounts
 
 section and
 **open the needed record** 
 .
2. Click the
 
 Add communication option
 
 button and
 **select the option to add** 
 :
	* Twitter
	 
	 ,
	 
	 LinkedIn
	 
	 ,
	 
	 Facebook
	 
	 . Social network profiles of the contact or account.
	* Web
	 
	 . Website of the contact or account.
	* Skype
	 
	 . The contact’s Skype account. The field is available for contact profiles.
	* Other phone
	 
	 ,
	 
	 Extension phone
	 
	 ,
	 
	 Business phone
	 
	 ,
	 
	 Mobile phone
	 
	 ,
	 
	 Home phone
	 
	 . Phone numbers that can be used to contact the person. The fields are available for contact profiles.
	* Fax
	 
	 ,
	 
	 Phone
	 
	 ,
	 
	 Alternate phone
	 
	 . Phone numbers that can be used to contact the company. The fields are available for account profiles.
	* Email
	 
	 . Email address of the contact or account.
3. **Enter data** 
 using the standard format for this communication option.
4. **Save the changes** 
 .
	1. Go to the
	 
	 Contacts
	 
	 or
	 
	 Accounts
	 
	 section and
	 **open the needed record** 
	 .
	2. Hold the pointer over the needed communication option in the
	 
	 Communication options
	 
	 component →
	 ![btn_context_menu.png](/docs/sites/en/files/images/CRM_Tools/communications_and_addresses_in_freedom_ui/btn_context_menu.png)
	**button** 
	 . This opens the record edit menu.
	3. **Click “Set as primary”** 
	 (Fig 2).
	 
	
	
	 Fig. 2 Set a communication option as primary
	 
	
	
	
	
	![scr_set_communication_option_as_primary.png](/docs/sites/en/files/images/CRM_Tools/communications_and_addresses_in_freedom_ui/scr_set_communication_option_as_primary.png)
	1. Go to the
	 
	 Contacts
	 
	 or
	 
	 Accounts
	 
	 section and
	 **open the needed record** 
	 .
	2. Hold the pointer over an invalid email in the
	 
	 Communication options
	 
	 component → the
	 ![btn_context_menu.png](/docs/sites/en/files/images/CRM_Tools/communications_and_addresses_in_freedom_ui/btn_context_menu.png)
	**button** 
	 . This opens the record edit menu.
	3. **Click “Mark as invalid”** 
	 (Fig. 3).
	 
	
	
	 Fig. 3 Mark a communication option as invalid
	 
	
	
	
	
	![scr_mark_communication_option_as_invalid.png](/docs/sites/en/files/images/CRM_Tools/communications_and_addresses_in_freedom_ui/scr_mark_communication_option_as_invalid.png)
	4. **Save the changes** 
	 .
	* Unknown Recipient
	* Mailbox Problem
	* Spam Reject
	* Domain Not Found
	1. Go to the
	 
	 Contacts
	 
	 or
	 
	 Accounts
	 
	 section and
	 **open the needed record** 
	 .
	2. Open the
	 
	 Contact info
	 
	 or
	 
	 Account info
	 
	 tab →
	 
	 Addresses
	 
	 expanded list →
	 ![btn_add_an_address.png](/docs/sites/en/files/images/CRM_Tools/communications_and_addresses_in_freedom_ui/btn_add_an_address.png)
	**button** 
	 . This opens a page.
	3. Fill out the following fields on the page that opens:
		1. **Specify the type of the contact or account address** 
		 in the
		 
		 Address type
		 
		 field. For example, “Home” or “Business” for a contact, “Legal” or “Actual” for an account. Address types are defined when a record is added, but you can change them later.
		2. **Select the
		 
		 Primary
		 
		 checkbox** 
		 if the address is primary. By default, the
		 
		 Primary
		 
		 checkbox is selected for the first address added to the
		 
		 Addresses
		 
		 detail, but you can select this checkbox for a different address at any time.
		3. **Enter the street, building, and apartment or office number** 
		 in the
		 
		 Address
		 
		 field.
		4. **Select the contact or account location** 
		 in the
		 
		 City
		 
		 and
		 
		 Country
		 
		 fields. The
		 
		 State/province
		 
		 and
		 
		 City
		 
		 fields are connected to the
		 
		 Country
		 
		 field. For example, if a city is located in a certain country, then when you populate the
		 
		 City
		 
		 field, Creatio populates the
		 
		 Country
		 
		 field automatically. Similarly, if you enter a province in the
		 
		 State/province
		 
		 field, Creatio populates the
		 
		 Country
		 
		 field automatically. When you fill out the
		 
		 Country
		 
		 field, the
		 
		 State/province
		 
		 and
		 
		 City
		 
		 fields display only the regions and cities connected to the selected country. You can connect a region to a specific country in the
		 
		 States/provinces
		 
		 lookup, and connect a city to a country in the
		 
		 Cities
		 
		 lookup.
		5. **Enter the ZIP or postal code** 
		 of the account or contact in the
		 
		 ZIP/postal code
		 
		 field.




