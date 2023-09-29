


 In Creatio, you can manage the communication options and addresses of contacts and accounts using the
 
 General information
 
 tab on their pages. Add addresses and communication options, look them up on a map, and restrict the usage of specific communication options.
 



 Add a communication option
----------------------------



 Use the
 
 Communication options
 
 detail to specify the communication options of a contact or account. To do this:
 


1. Go to the
 
 Contacts
 
 or
 
 Accounts
 
 section and open the needed record.
2. Click
 
 General information
 
 →
 
 Operations
 
 →
 ![btn_chapter_mobile_wizard_new_role.png](/docs/sites/default/files/2020-11/btn_chapter_mobile_wizard_new_role.png)
 .
3. Select communication option to add:
	* Business phone
	 
	 ,
	 
	 Mobile phone
	 
	 ,
	 
	 Home phone
	 
	 . Phone numbers that can be used to contact the person. Communication option types are defined when a record is added. You can change the options later. The fields are available for contact profiles.
	* Primary phone
	 
	 ,
	 
	 Alternate phone
	 
	 ,
	 
	 Fax
	 
	 . Phone numbers that can be used to contact the company. Communication option types are defined when a record is added. You can change the options later. The fields are available for account profiles.
	* Web
	 
	 ,
	 
	 Email
	 
	 . Website and email addresses of the contact. The record list displays the last of the entered email addresses of the contact or account.
	* Facebook
	 
	 ,
	 
	 Twitter
	 
	 . Social network profiles of the contact or account. A separate page is used to link social network profiles to accounts or contacts.
	* Skype
	 
	 . The contact's Skype account. The field is available for contact profiles.
4. Enter the data using the standard format for this communication option.
5. Click
 
 Save
 
 .



 You can use default types of communication options or add custom ones. Use the
 
 Communication option types
 
 lookup to add custom types of communication options. Custom communication option types fall into one of the pre-set communication types, such as Email, Phone, Skype, SMS, Social network, or Web. Be sure to select one when adding a custom communication option type.
 





 Attention.
 
 If the Microsoft Exchange integration is configured, it is not recommended to change default communication option types, since this may lead to
 [synchronization](/docs/7-18/user/setup_and_administration/base_integrations/microsoft_email_contacts_and_calendar/set_up_microsoft_exchange_and_office_365/set_up_the_ms_exchange_and_microsoft_365_services) 
 errors.
 



### 
 Restrict the usage of a contact's communication options



 If a contact prefers some communication options and finds the usage of the other options unacceptable, you can display this information on the
 
 Communication options
 
 detail. To do this, click
 ![btn_chapter_mobile_wizard_new_role.png](/docs/sites/default/files/2020-11/btn_chapter_mobile_wizard_new_role.png)
 →
 
 Do not use
 
 → select the needed option.
 


* Do not use email
* Do not use phone
* Do not use SMS
* Do not use mail
* Do not use fax



 Checkboxes signify which communication options cannot be used to contact the person. For example, if a contact does not wish to receive mails, select the
 
 Do not use mail
 
 checkbox. For example, if a contact did not consent to receive emails, select the
 
 Do not use Email
 
 checkbox.
 



 If the “Unsubscribe user from all bulk emails” system setting is enabled, the
 
 Do not use email
 
 option box will be automatically checked for all contacts who unsubscribed from bulk emails. This functionality is available in Sales Creatio and Marketing Creatio.
 



 When sending bulk emails via the
 
 Send email
 
 element in the business process or case, Creatio ignores the
 
 Do not use email
 
 checkbox selected in the
 
 Communication options
 
 detail.
 



 You can also tag a communication option as invalid. This functionality is available in Marketing Creatio:
 


* Invalid
 
 . If a communication option is currently not used, it becomes invalid. The “invalid” status appears automatically when the
 
 Valid
 
 option is not checked for the selected communication option. It is not displayed on the
 
 Communication options
 
 detail but can be used when setting up filters for folders.
* Reason for irrelevance
 
 . The reason why the selected communication option is invalid: “Hard bounce” or “Manual setting.” The field is populated automatically. It is not displayed on the
 
 Communication options
 
 detail but can be used when setting up filters for folders.
* Invalid from
 
 . Date from which the selected communication option becomes invalid. The field is populated automatically. It is not displayed on the
 
 Communication options
 
 detail but can be used when setting up filters for folders.



 Add address
-------------



 Use the
 
 Addresses
 
 detail to specify the addresses of a contact or account. To do this:
 


1. Go to the
 
 Contacts
 
 or
 
 Accounts
 
 section and open the needed record.
2. Click
 
 General information
 
 →
 
 Addresses
 
 →
 ![btn_chapter_mobile_wizard_new_role.png](/docs/sites/default/files/2020-11/btn_chapter_mobile_wizard_new_role.png)
 .
3. Select the type of address to add.
4. Fill out the following fields on the page that opens:
	* Address type
	 
	 . Type of address of the contact or account. For example, “Home” or “Work” for a contact, “Legal” or “Actual” for an account. Address types are defined when a record is added. You can change the types later.
	* Primary
	 
	 . Indicates the primary address. Select this checkbox to display this address in the contact or account profile. By default, the
	 
	 Primary
	 
	 checkbox is selected for the first address added to the
	 
	 Addresses
	 
	 detail, but you can select this checkbox for a different address at any time. The checkbox in the original record will be cleared.
	* Address
	 
	 . Street, building, and apartment or office number. The list displays the account or contact’s primary address.
	* City
	 
	 ,
	 
	 Country
	 
	 . The location of the contact or account. The
	 
	 State/province
	 
	 and
	 
	 City
	 
	 fields are connected to the
	 
	 Country
	 
	 field. For example, the
	 
	 Country
	 
	 field will be populated automatically when you populate the
	 
	 City
	 
	 field. Similarly, if you enter a province in the
	 
	 State/province
	 
	 , the
	 
	 Country
	 
	 field will be populated automatically. When you fill out the
	 
	 Country
	 
	 field, the
	 
	 State/province
	 
	 and
	 
	 City
	 
	 fields will display only those regions and cities, which correspond to the selected country. You can associate a region with a certain country in the
	 
	 States/provinces
	 
	 lookup, and associate a city with a country in the
	 
	 Cities
	 
	 lookup.
	* ZIP
	 
	 . ZIP or postal code of the account or contact.



 After populating one or several addresses, the
 
 Show on map
 
 section action becomes available. Use it to display the location of the selected accounts on the map. If an account has several addresses populated, e. g., physical address and delivery address, the map displays all of the specified addresses. To view the detailed description, click one of the addresses.
 



 The address of an account also displays after clicking on the needed entry in the
 
 Addresses
 
 detail. If the location of the account on the map is not correct, move the marker to the correct position and save the changes.
 





 Attention.
 
 Creatio displays addresses using the OpenStreetMap service integration. The service is developed and maintained by a third party. Creatio assumes no responsibility for the operation of the service and the content of OpenStreetMap maps.
 





