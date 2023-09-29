


 You can import the contacts that are connected to various objects to the email audience. “Contact”, “Lead”, “Event participant” objects are available by default. You can also add new objects, such as “Account” or “Order”. If you add a new object, Creatio will add to the email audience the contacts connected to that object's records. Read more about forming the bulk email audience:
 [Add bulk email audience](/docs/7-16/user/marketing_tools/email_marketing/bulk_email/create_an_email/add_a_bulk_email#title-1551-5) 
 .
 



 To import contacts, you first need to specify the object used to form the audience and set up how the object is connected to Creatio contacts. Any Creatio user with permissions to “Access to “Lookups” section” (“CanManageLookups” code) system operation can perform the setup. Read more:
 [System operation permissions](/docs/7-16/user/setup_and_administration/user_and_access_management/access_management/system_operation_permissions_shortcut/system_operation_permissions) 
 .
 



 To add a new object:
 


1. Navigate to the
 
 Audience
 
 tab of the email page, click
 ![btn_com_add_tab](/docs/sites/en/files/inline-images/btn_com_add_tab_6.png)
 and select
 
 Manage objects
 
 .
2. Click
 
 New
 
 in the top left of the newly-opened page. This will add an empty record to the
 
 Manage objects for audience import
 
 lookup.
3. Fill out the new record's fields (Fig. 1):
 


	1. Object caption
	 
	 — specify the name to be used in the object list on the
	 
	 Audience
	 
	 tab of the email page. For example, “Account”.
	2. Entity object
	 
	 — select the Creatio object that will be used to form the email audience. For example, “Account”.
	3. Contact column path
	 
	 — select the object's field that contains the contact data. The contact specified in this field will receive the email. For instance, there is contact data in the
	 
	 Primary contact
	 
	 field of the “Account” object.
	4. Email column path
	 
	 — specify the path to the
	 
	 Email
	 
	 field of the contact page.




 Fig. 1
 

 Manage objects for audience import
 
 lookup
 

![import_audience.PNG](/docs/sites/en/files/images/Marketing_Tools/set_up_objects_that_form_email_audience/import_audience.PNG)



 The record is saved automatically. This will add a new audience-forming object to the
 ![btn_com_add_tab](/docs/sites/en/files/inline-images/btn_com_add_tab_6.png)
 button's menu on the
 
 Audience
 
 tab of the email page.
 




