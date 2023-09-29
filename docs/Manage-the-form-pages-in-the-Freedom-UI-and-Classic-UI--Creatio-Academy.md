



 This functionality is available for Creatio 8.0.6 and later.
 




 Creatio objects can have both a Freedom UI and Classic UI form page. For example, the “Contact” object has a Freedom UI form page in the
 
 Customer 360
 
 app as well as a Classic form page in the
 
 Contacts
 
 Classic UI section.
 



 If the object has both form pages, Freedom UI sections always open Freedom UI form pages when you add, view, edit, or copy a record. In other cases, system administrator can specify which page to open. This makes a transition to composable architecture easy and comfortable for users.
 



 To manage the form pages to display, turn on the Freedom UI. Learn more in a separate article:
 [Turn on the Freedom UI](https://academy.creatio.com/documents?id=2446) 
 .
 



 In general, the mechanism that determines the form page to display in the Freedom UI and Classic UI works as follows (Fig. 1):
 




 Fig. 1 Mechanism that determines the form page to display in the Freedom UI and Classic UI
 

![](/sites/default/files/documentation/sdk/ru/BPMonlineWebSDK/Screenshots/ManageTheDisplayOfPages/8.0/scr_process_of_opening_the_pages.png)



 You can specify the form page to open sitewide or add exceptions for specific objects.
 



 Specify the form page to open sitewide
----------------------------------------



 To specify the form page to open sitewide, use the following
 **system settings** 
 :
 


* “Default form page in the Freedom UI shell” (EditPagesUITypeForFreedomHost code) for the Freedom UI. Set
 
 Default value
 
 property to “Freedom UI pages” or “Classic UI pages.”
* “Default form page in the Classic UI shell” (EditPagesUITypeForEXTHost code) for the Classic UI. Set
 
 Default value
 
 property to “Freedom UI pages” or “Classic UI pages.”



 To apply the changes, log out of and log back in to Creatio.
 



 Add exceptions for specific Creatio objects
---------------------------------------------



 Use
 **exceptions** 
 if you set up a form page in another UI or want to use a different UI for a specific page for A/B testing.
 



 For example, you want to open
 
 Contacts
 
 section in Classic UI. To do this:
 


1. Click
 ![btn_sys_designer.png](/docs/sites/en/files/images/NoCodePlatform/ApplicationHub/btn_sys_designer.png)
 to open the System Designer.
2. Click
 **“Lookups”** 
 in the “System setup” block.
3. Open the
 
 Object-specific form page interface in the Freedom and Classic UI shell
 
 lookup. This opens a lookup content page.
4. Click
 
 New
 
 .
5. Populate the required fields (Fig. 2):
 


	* Set
	 
	 Object code
	 
	 to "Contact."
	* Set
	 
	 Freedom UI shell
	 
	 to "Classic UI pages."

 Fig. 2
 
 Contacts
 
 page settings in the Freedom UI and Classic UI
 

![](/sites/default/files/documentation/sdk/ru/BPMonlineWebSDK/Screenshots/ManageTheDisplayOfPages/8.0/src_lookup_setting.png)
6. Click
 ![](/sites/default/files/documentation/sdk/ru/BPMonlineWebSDK/Screenshots/ManageTheDisplayOfPages/8.0/scr_checkbox.png)
 to save changes.





 Attention.
 
 The priority of the
 
 Object-specific form page interface in the Freedom and Classic UI shell
 
 lookup is higher than the priority of the “Default form page in the Freedom UI shell” (EditPagesUITypeForFreedomHost code) and “Default form page in the Classic UI shell” (EditPagesUITypeForEXTHost code) system settings.
 




 If an object has both Freedom UI and Classic UI sections, only one is displayed in the
 
 All apps
 
 workspace. Manage the section to display in the “Default form page in the Freedom UI shell” (EditPagesUITypeForFreedomHost code) system setting and
 
 Object-specific form page interface in the Freedom and Classic UI shell
 
 lookup.
 



 Setup examples
----------------





 Example 1.
 
 Turn on
 
 Customer 360
 
 app for newly installed Creatio 8.0.6 and later.
 




**Setup** 
 : install the
 
 Customer 360
 
 app if you use Studio Creatio. Otherwise,
 
 Customer 360
 
 app is installed by default.
 



**Results** 
 :
 


* Creatio will open Freedom UI sections if they exist.
* Creatio will open Freedom UI pages if they exist and no exceptions are specified.





 Example 2.
 
 Turn on
 
 Contacts
 
 Classic UI section for newly installed Creatio 8.0.6 and later.
 




**Setup** 
 :
 


1. Add a record to the
 
 Object-specific form page interface in the Freedom and Classic UI shell
 
 lookup.
2. Set
 
 Object code
 
 to "Contact."
3. Set
 
 Freedom UI shell
 
 to "Classic UI pages."
4. Add
 
 Contacts
 
 Classic UI section to a workplace. To do this, follow instructions in a separate article:
 [Set up workplaces](https://academy.creatio.com/documents?id=1248) 
 .



**Results** 
 :
 


* “Contact” object will use the Classic UI section.
* Other objects will use Freedom UI sections.





 Example 3.
 
 Turn on
 
 Contacts
 
 Freedom UI section for an existing Creatio instance that was updated to 8.0.6 and later.
 




**Setup** 
 :
 


1. Add a record to the
 
 Object-specific form page interface in the Freedom and Classic UI shell
 
 lookup.
2. Set
 
 Object code
 
 to "Contact."
3. Set
 
 Freedom UI shell
 
 to "Freedom UI pages."
4. Add
 
 Contacts
 
 Freedom UI section to a workplace. To do this, follow instructions in a separate article:
 [Set up workplaces](https://academy.creatio.com/documents?id=1248) 
 .



**Results** 
 :
 


* Creatio will use the Classic UI.
* “Contact” object will use the Freedom UI section and Freedom UI form pages.
* Other objects will also use Freedom UI form pages if they exist and no exceptions are specified.





 Example 4.
 
 Open Freedom UI contact pages from
 
 Contacts
 
 Classic UI section for an existing Creatio instance that was updated to 8.0.6 and later.
 




**Setup** 
 : set
 
 Default value
 
 property of the “Default form page in the Classic UI shell” (EditPagesUITypeForEXTHost code) system setting to "Freedom UI pages."
 



**Results** 
 :
 


* Creatio will use the Classic UI.
* “Contact” object will use the Classic UI section and Freedom UI form pages.
* Other objects will also use Freedom UI form pages if they exist and no exceptions are specified.





 Example 5.
 
 Turn on the Freedom UI and open Freedom UI sections for an existing Creatio instance that was updated to 8.0.6 and later. Set up for the current user.
 




**Setup** 
 :
 


1. Select the
 
 Default value
 
 checkbox of the “Use Freedom UI interface” (UseNewShell code) system setting.
2. Select the
 
 Save value for current user
 
 checkbox of the “Use Freedom UI interface” (UseNewShell code) system setting.
3. Set
 
 Default value
 
 property of the “Default form page in the Freedom UI shell” (EditPagesUITypeForFreedomHost code) system setting to "Freedom UI pages."
4. Set
 
 Default value
 
 property of the “Default form page in the Classic UI shell” (EditPagesUITypeForEXTHost code) system setting to "Freedom UI pages."



**Results** 
 :
 


* Creatio will use the Freedom UI for the current user and the Classic UI for other users.
* Creatio will open Freedom UI sections if they exist for the current user and Classic UI sections for other users.
* Creatio will open Freedom UI pages if they exist and no exceptions are specified for the current user and Classic UI pages for other users.





 Example 6.
 
 Turn on the Freedom UI and open Freedom UI sections for an existing Creatio instance that was updated to 8.0.6 and later. Set up for all users.
 




**Setup** 
 :
 


1. Select the
 
 Default value
 
 checkbox of the “Use Freedom UI interface” (UseNewShell code) system setting.
2. Clear the
 
 Save value for current user
 
 checkbox of the “Use Freedom UI interface” (UseNewShell code) system setting.
3. Set
 
 Default value
 
 property of the “Default form page in the Freedom UI shell” (EditPagesUITypeForFreedomHost code) system setting to "Freedom UI pages."
4. Set
 
 Default value
 
 property of the “Default form page in the Classic UI shell” (EditPagesUITypeForEXTHost code) system setting to "Freedom UI pages."



**Results** 
 :
 


* Creatio will use the Freedom UI.
* Creatio will open Freedom UI sections if they exist.
* Creatio will open Freedom UI pages if they exist and no exceptions are specified.





 Example 7.
 
 Turn on
 
 Customer 360
 
 app for an existing Creatio instance that was updated to 8.0.6 and later. Set up for all users.
 




**Setup** 
 :
 


1. Select the
 
 Default value
 
 checkbox of the “Use Freedom UI interface” (UseNewShell code) system setting.
2. Clear the
 
 Save value for current user
 
 checkbox of the “Use Freedom UI interface” (UseNewShell code) system setting.



**Results** 
 :
 


* Creatio will use the Freedom UI.
* Creatio will Freedom UI sections if they exist.
* Creatio will open Freedom UI pages if they exist and no exceptions are specified.




