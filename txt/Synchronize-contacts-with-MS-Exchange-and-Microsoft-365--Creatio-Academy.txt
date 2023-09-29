



 Creatio 8.0 Atlas and later does not support contact synchronization with external applications.
 




 Use the mailbox synchronization setup page to set up synchronization of Creatio contacts with the Microsoft Exchange or Microsoft 365 contacts (Fig. 1). You can open the page in several ways:
 


* Click
 ![btn_com_roles_actions_menu.png](/guides/sites/en/files/documentation/user/en/base_integrations/BPMonlineHelp/synchronize_contacts_MSExchange_Microsoft/btn_com_roles_actions_menu.png)
 →
 
 Edit email accounts
 
 in the communication panel.
* Select
 
 Actions
 
 →
 
 Synchronize contacts
 
 →
 
 Set up...
 
 in the
 
 Contacts
 
 section.



 The command contains the name of the account, for example,
 
 Set up john.best@mycompany.com
 
 .
 




 Fig. 1 Set up the synchronization of Creatio contacts with Microsoft Exchange calendar
 

![scr_chapter_exchange_synchronisation_contacts_synch.png](/guides/sites/en/files/documentation/user/en/base_integrations/BPMonlineHelp/synchronize_contacts_MSExchange_Microsoft/scr_chapter_exchange_synchronisation_contacts_synch.png)



 Set up the import of contacts into Creatio
--------------------------------------------



 To set up the import of the Microsoft Exchange or Microsoft 365 contacts into Creatio:
 


1. Go to the
 
 Contacts
 
 tab of the mailbox synchronization setup page and enable the
 
 Import contacts
 
 toggle.
2. Select
 
 Import all contacts
 
 to import all records from the mailbox folders of the “Contacts” type.
 



 If you only want to import contacts from specific folders, select
 
 Import contacts from specific folders in MS Exchange
 
 . Click
 ![btn_com_add_tab.png](/guides/sites/en/files/documentation/user/en/base_integrations/BPMonlineHelp/synchronize_contacts_MSExchange_Microsoft/btn_com_add_tab.png)
 and select the checkboxes next to the needed folders.
3. Click
 
 Save
 
 .





 Note.
 
 Creatio links imported contacts to Creatio accounts automatically. If more than one account with the same name is found in Creatio, the contact is imported without an account connection. If the user who performs the import has access to one of these accounts, the contact is imported with the connection to this account.
 




 Set up the export of contacts from Creatio
--------------------------------------------



 To set up the export of Creatio contacts to Microsoft Exchange or Microsoft 365:
 


1. Go to the
 
 Contacts
 
 tab of the mailbox synchronization setup page and enable the
 
 Export contacts
 
 toggle.
2. Select
 
 Export all contacts
 
 to export all contacts to which you have access.
3. If you only want to export contacts of certain types or folders, select
 
 Export specific contacts
 
 .
	1. Select the
	 
	 Employees
	 
	 and/or
	 
	 Customers
	 
	 checkbox to export all contacts of the corresponding types during synchronization. Creatio exports only the contacts to which you have access.
	2. Select the
	 
	 From folders
	 
	 checkbox to export contacts included in particular folders, for example, “Employees.” Expand the index of folders and select the folders for synchronization.
4. Click
 
 Save
 
 .





 Note.
 
 Learn more about creating folders in a separate article:
 [Folders](https://academy.creatio.com/documents?id=1018) 
 .
 




 Synchronize contacts with Microsoft Exchange and Microsoft 365
----------------------------------------------------------------



 Creatio can synchronize contacts with the Exchange server automatically. To enable automatic synchronization, open the mailbox synchronization setup page and enable the
 
 Synchronize contacts automatically
 
 toggle. To perform the synchronization immediately, open the
 
 Contacts
 
 section, click
 
 Actions
 
 →
 
 Synchronize contacts
 
 →
 
 Synchronize now
 
 .
 




