


 A
 **detail** 
 is a page element that displays records of an object linked to the current record. Use details to display data from another object that is connected to the current record. For example, a contact’s noteworthy events or an account’s addresses. The majority of details come with their own record list. The detail only displays entries connected to the current section record. The connection is usually established via the record page object (most often the section object) selected in the detail’s lookup field. Use developer tools to create details with editable fields or custom data, such as
 
 Attachments
 
 , as well as details not directly connected to the current record. Learn more in the development guide:
 [Detail](/docs/7-16/developer/interface_elements/detail/overview) 
 .
 





 Note.
 
 Note. Learn more about objects in the
 [Creatio object model](https://academy.creatio.com/node/531086/takecourse) 
 course.
 




 For example, the
 
 Activity participants
 
 detail shows the participant list of the current activity. The
 
 Activities
 
 detail (Fig. 1) shows the list of activities linked to the current account, contact, etc.
 




 Fig. 1 Record filtering on the
 
 Activities
 
 detail
 



![scr_record_filtering_on_activities_detail.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/scr_record_filtering_on_activities_detail.png)



 You can create a detail in the Section wizard during the page setup or use the Detail wizard. Creatio adds details created in the Section wizard to the relevant section page automatically. You have to add details created in the Detail wizard to the section page manually. Learn more:
 [Add an existing detail on a record page](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/set_up_a_detail/add_an_existing_detail_on_a_record_page) 




 You can create a detail:
 


* Based on an
 **existing** 
 object. For example, display new custom section’s data as a detail in other sections. You can also use this option to add multiple unique details created from the same object to section pages.
 [Read more >>>](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/create_a_detail/create_new_detail#title-150-1)
* Using a
 **new** 
 object. For example, display the list of medical documents for employees’ sick leave applications in the custom
 
 Requests
 
 section. Use this option when the object whose data you would like to use does not exist yet.
 [Read more >>>](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/create_a_detail/create_new_detail#title-150-2)



 All objects and schemas created in the Section or Detail wizard are bound to a specific package. If you plan to transfer changes between environments, create a custom package before creating the detail. Then, set this package as the new destination for custom objects.
 



 Add a detail based on an existing object
------------------------------------------



 You can use Creatio sections or lookups to create a detail. To ensure the transferability of new packages, check the package bindings before starting the setup:
 


* When creating a detail based on a
 **custom** 
 object, make sure that your current changes are saved to the same or dependent package.
* When creating a detail based on a
 **base** 
 object, make sure that your current package is dependent on the package with the base object (usually the Base package or a product functionality package, such as “SalesEnterprise”).



 Learn more about packages in the
 [Get started with packages](/docs/7-17/developer/development_tools/packages/packages) 
 developer documentation article.
 





 Example.
 
 Create a detail that will display a list of the contact’s requests on their page.
 




 This example will create a detail from an object of a custom
 
 Requests
 
 section. Learn more about adding custom sections in the
 [Create a new section](https://academy.creatio.com/documents?product=base&ver=7&id=1397) 
 article.
 


1. Open a section, e. g.,
 
 Contacts
 
 .
2. Click
 
 View
 
 →
 
 Open Section Wizard
 
 .
3. In the
 
 Section pages
 
 block of the Section Wizard:
	* click
	 
	 Edit page
	 
	 if you have only one edit page in the section
	* click
	 **the link to the relevant page** 
	 if there are several pages in the section.
4. Navigate to the tab where you would like to place the detail.
5. Click
 
 New detail
 
 .
6. Click the
 ![btn_add.png](/docs/sites/default/files/images/NoCode_Customization/section_wizard/btn_add.png)
 button to the right of the
 
 Detail
 
 field in the detail setup window.
7. Select
 
 Add based on existing object
 
 in the menu that pops up (Fig. 2).
 

 Fig. 2 Adding a detail based on an existing object
 

![scr_create_detail_from_section_wizard.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/scr_create_detail_from_section_wizard.png)
8. In the pop-up window (Fig. 3):
	1. Specify which
	 **object’s** 
	 data the detail will use. In our case, it is “
	 **Requests** 
	 .”
	2. Specify the detail
	 **title** 
	 that will help you find it in the object list. In our case, it is “
	 **Contact requests** 
	 .”
	3. Add
	 **translations** 
	 for the title if necessary. Learn more about translations in the following article:
	 [Add new element translations](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/translations/add_new_element_translations) 
	 .
	4. Select the
	 
	 Make the list editable
	 
	 checkbox to make the detail’s data editable directly from the list without the need to open a new page.
	5. Click
	 
	 Save
	 
	 .
	 
	
	 Fig. 3 Setting up a detail based on an existing object in the Section wizard
	 
	
	![scr_set_detail_from_existing_object_in_section_wizard.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/scr_set_detail_from_existing_object_in_section_wizard.png)
9. Set up how the detail will display the records of the
 
 Requests
 
 section in the
 
 What records to show on the page?
 
 block:
	1. The
	 
	 Where detail column
	 
	 field specifies the detail object’s column the value of which Creatio will use to check whether to display the record. In our case, it is the “
	 **Created by** 
	 ” column.
	2. The
	 
	 Equals to page column
	 
	 field specifies the current section’s page column the value of which Creatio will compare to the value of the column specified in the
	 
	 Where detail column
	 
	 field. In our case, it is the “
	 **Id** 
	 ” column.
	   
	
	 As a result, the contact page will only display those records of the
	 
	 Requests
	 
	 section where the
	 
	 Created by
	 
	 field matches the specified contact.
10. Click
 
 Save
 
 .
11. Save the changes in the window and in the Section Wizard.



 As a result, a new schema and detail page will be available. Creatio will register the new detail and add it to the record page. The detail’s edit page is identical to the page from the custom
 
 Requests
 
 section. All changes made on the detail page will also be available on the section page. The new detail’s schema (the client module) and data will be available in the package to which the changes are saved. The
 
 Contacts
 
 section’s updated object, schema, and an edit page will also be available in the package.
 



 You can also implement this example in the Detail wizard. As a result, Creatio will register a new detail and display it in the detail list in the section wizard. You will be able to add the detail to section pages. Learn more:
 [Create a detail to add it to a record page](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/create_a_detail/create_new_detail#title-150-3) 
 The new detail’s schema (the client module) and data will be available in the package to which the changes are saved.
 



 Add a detail based on a new object
------------------------------------





 Example.
 
 Create a new detail for medical documents in the
 
 Requests
 
 custom section. The documents serve as grounds to approve employee requests for sick or maternity leaves.
 






 Note.
 
 Learn more about adding a custom section in the
 [Create a new section](https://academy.creatio.com/documents?product=base&ver=7&id=1397) 
 article.
 



1. Open a section, e. g.,
 
 Cases
 
 .
2. Click
 
 View
 
 →
 
 Open Section Wizard
 
 .
3. In the
 
 Section pages
 
 block of the Section Wizard:
	* Click
	 
	 Edit page
	 
	 if you have only one edit page in your section.
	* Click
	 **the link to the relevant page** 
	 if there are several pages in the section.
4. Navigate to the tab where you would like to place the detail.
5. Click
 
 New detail
 
 .
6. Click the
 ![btn_add.png](/docs/sites/default/files/images/NoCode_Customization/section_wizard/btn_add.png)
 button to the right of the
 
 Detail
 
 field in the detail setup window.
7. Select
 
 Add using new existing object
 
 in the menu that pops up (Fig. 4).
 

 Fig. 4 Adding a detail using a new object
 

![scr_create_new_detail_from_section_wizard.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/scr_create_new_detail_from_section_wizard.png)
8. Specify the following in the pop-up (Fig. 5):
	1. The
	 **object title** 
	 in the configuration object list. In our case, it is “
	 **Medical documents** 
	 .”
	2. The
	 **detail title** 
	 to help you find the detail in the Section wizard’s object list. In our case, it is “
	 **Medical documents** 
	 .”
	3. A unique
	 **code** 
	 that displays in the configuration object list. The code must contain a prefix that identifies the creator of the object. The prefix is specified in the “Prefix for object name” system setting. In our case, the code is “
	 **UsrMedicalDocuments** 
	 .”
	4. Select the
	 
	 Make the list editable
	 
	 checkbox to make the detail’s data editable directly from the list without the need to open a new page.
	5. Creatio will populate the data in the
	 
	 How to connect detail to current page?
	 
	 block automatically.
	6. Click
	 
	 Save
	 
	 .
	 
	
	 Fig. 5 Filling out a new detail’s parameters
	 
	
	![scr_add_new_detail_from_section_wizard.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/scr_add_new_detail_from_section_wizard.png)
9. Creatio will populate all parameters in the detail setup window automatically. Click
 
 Save
 
 .
10. Save the changes in the window and in the Section Wizard.



 As a result, a new object, schema, and detail page will be available. Creatio will register the new detail and add it to the page of the custom
 
 Requests
 
 section.
 



 The detail will be also available in the section wizard’s detail list. You can add the detail to any section page that can be connected to the detail. The detail page will display the
 
 Name
 
 field (required) and the
 
 Requests
 
 field used to match the detail records to the current section record. Edit the detail page to add other fields. Learn more:
 [Add an existing detail to a record page](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/set_up_a_detail/add_an_existing_detail_on_a_record_page) 
 . The new detail’s object, page, and schemas (the client module) will be available in the package to which the changes are saved. If the section where you added the new detail is saved in a different package, saving the changes in the Section wizard will also save the updated object, schema, and section edit page to your package.
 



 You can also implement this example in the Detail wizard. As a result, the detail will become available in the section wizard’s detail list. You will be able to add the detail to the section page. Learn more:
 [Create a detail for subsequent adding to a record page](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/create_a_detail/create_new_detail#title-150-3) 




 Create a detail to add it to a record page
--------------------------------------------



 You can create and set up a detail in the Detail wizard. This is useful for such things as collaboration on no-code customization. The new detail will be available in the section wizard’s detail list and the
 
 Advanced settings
 
 section. You can add the detail to any section page that can be connected to the detail as well as transfer it to another environment. You can follow the same procedure as in the section wizard to create details based on new or existing Creatio objects in the detail wizard. We will explain how to work with the detail wizard by using a custom detail based on a new object as an example.
 





 Example.
 
 Create a new
 
 Registration documents
 
 custom detail that displays contacts’ ID cards.
 



1. Click
 ![btn_system_designer.png](/guides/sites/default/files/documentation/user/ru/ui_business_logic_customization/BPMonlineHelp/create_new_detail/btn_system_designer.png)
 →
 
 System Designer
 
 .
2. In the
 
 System setup
 
 block, click
 
 Detail wizard
 
 .
3. On the opened page (Fig. 4):
	1. Select “
	 **Create new object** 
	 ” in the
	 
	 How to create detail?
	 
	 block.
	2. Specify the new detail’s
	 **title** 
	 to display in the Section Wizard’s detail list. In our case, it is “
	 **Registration documents** 
	 .”
	3. Specify the new object’s
	 **title and unique code** 
	 that will help you find the object in the configuration element list. In our case, it is “
	 **Registration documents** 
	 ” and “
	 **UsrRegistrationDocuments** 
	 ” respectively.
	 
	
	 Fig. 6 Setting up a detail based on a new object
	 
	
	![scr_detail_wizard_add_detail_new_object.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/scr_detail_wizard_add_detail_new_object.png)
4. Connect the new detail to the
 
 Contacts
 
 section object. To do so:
	1. Click
	 
	 Page
	 
	 to set up the detail’s record page (Fig. 7).
	 
	
	 Fig. 7 Navigating to editing the page
	 
	
	![scr_open_page_tab_in_detail_wizard.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/scr_open_page_tab_in_detail_wizard.png)
	2. Drag the
	 
	 Lookup
	 
	 field from the
	 
	 New column
	 
	 list on the left to the workspace on the right (Fig. 8). A
	 
	 New column
	 
	 pop-up will appear.
	 
	
	
	
	
	 Fig. 8 Creating a lookup field
	 
	
	![gif_drag_lookup_in_detail_wizard.gif](/docs/sites/en/files/images/NoCode_Customization/page_layout/gif_drag_lookup_in_detail_wizard.gif)
	3. Fill out the properties in the
	 
	 New column
	 
	 pop-up.
	 
	
	
		1. In the
		 
		 Title
		 
		 field, specify the display name of the new field, e. g., “
		 **Contact.** 
		 ”
		2. In the
		 
		 Code
		 
		 field, specify the unique name for the field in the database, preceded by a prefix, e.g., “
		 **UsrContact.** 
		 ”
		 
		
		
		
		
		
		 Attention.
		 
		 The
		 
		 Code
		 
		 field must contain a prefix that identifies the author of the configuration changes. The prefix is specified in the “Prefix for object name” system setting. By default, the “Usr” value is used.
		3. In the
		 
		 Lookup
		 
		 field,
		 **select the section object** 
		 , to which the detail must be linked. For example, to link the detail to the records of the
		 
		 Contacts
		 
		 section, select the “
		 **Contact** 
		 ” object as the lookup.
		 
		
		
		
		
		 Fig. 9 Setting up a lookup column that links a detail to a section
		 
		
		![scr_lookup_detail.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/scr_lookup_detail.png)
		4. To delete all detail records when the connected record is deleted, select the
		 
		 Delete records from Detail schema
		 
		 option (Fig. 10).
		 
		
		
		
		
		 Fig. 10 Blocking the record deletion
		 
		
		![scr_block_deleting_records.png](/docs/sites/en/files/images/NoCode_Customization/page_layout/scr_block_deleting_records.png)
		5. Save the changes in the
		 
		 New column
		 
		 pop-up.
5. Set up the detail page. Add fields and field groups to store the registration documents. In our case, these are
 
 Document type
 
 ,
 
 Series
 
 ,
 
 Number
 
 ,
 
 Issued by
 
 . Working with column properties on a detail is similar to that of the regular page. Learn more:
 [Set up page fields](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/fields/set_up_page_fields) 
 .
6. Click
 
 Save
 
 to save the detail.



 As a result, a new object, schema, and detail page will be available. Creatio will register the new detail. The detail will be available in the section wizard’s detail list. You can add the detail to any section page that can be connected to the detail. For example,
 
 Contacts
 
 ,
 
 Employees
 
 , or
 
 Accounts
 
 . Learn more:
 [Add an existing detail on a record page](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/set_up_a_detail/add_an_existing_detail_on_a_record_page) 
 . The new detail’s object, page, and schemas (the client module) will be available in the package to which the changes are saved.
 




