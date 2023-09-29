



 This functionality is available for Creatio 8.0.9 and later.
 




 Turn on Freedom UI for external users in Portal Creatio
---------------------------------------------------------



 Freedom UI is turned on for external users in new Creatio instances by default.
 



 We recommend turning on Freedom UI for external users in existing instances only after you check whether the existing portal customizations are compatible with Freedom UI. Learn more:
 [Turn on Freedom UI](https://academy.creatio.com/documents?id=2446#title-2605-2) 
 .
 



 Create external Freedom UI pages
----------------------------------



 To set up Freedom UI form pages available for external users:
 


1. Create the Freedom UI app. Instructions:
 [Manage apps](https://academy.creatio.com/documents?id=2444)
2. Set up the external page for the app object. Instructions:
 [Set up the app UI](https://academy.creatio.com/documents?id=2379&anchor=title-2231-2)
3. Set up access permissions to the object for external users. Instructions:
 [Object operation permissions](https://academy.creatio.com/documents?id=250&anchor=title-2265-1)
4. Add the section to the external workplace. Instructions:
 [Customize Portal Creatio](https://academy.creatio.com/documents?id=2002&anchor=title-2088-44)



 You can set up Freedom UI form pages available for external users for any out-of-the-box or custom portal section in an editable app using no-code tools. This can be done in multiple ways:
 


* Set up pages while setting up the
 
 Button
 
 Freedom UI component.
 [Read more >>>](#title-2776-2)
* Set up pages in an app data model.
 [Read more >>>](#title-2776-3)



 Creatio stores the custom Freedom UI form page in the app where you created it. The page is bound to the object via the
 
 Addon
 
 type configuration element stored in the app where you bound the page to the object. The app, page, and configuration element must be present in the environment for the functionality to operate as intended.
 


### 
 Set up Freedom UI form pages for external users while setting up Freedom UI button



 You can set up Freedom UI form pages for external users while setting up the
 [Button](https://academy.creatio.com/documents?id=2376&anchor=title-2230-17)
 Freedom UI component. For example, this is useful if you need to use the same list page both for main Creatio and Portal Creatio sections. To do this:
 


1. Click
 ![btn_system_designer_8_shell.png](/docs/sites/en/files/images/NoCode_Customization/portal_pages_setup/btn_system_designer_8_shell.png)
 in the top right →
 
 Application Hub
 
 .
2. Open the relevant app.
3. Open the list page.
4. Select the
 
 New
 
 button and click
 ![btn_properties.png](/docs/sites/en/files/images/NoCode_Customization/portal_pages_setup/btn_properties.png)
 .
5. Go to the
 
 Action
 
 block. Click
 ![btn_page_setup.png](/docs/sites/en/files/images/NoCode_Customization/portal_pages_setup/btn_page_setup.png)
 to the right of the
 
 Which form to create?
 
 field. This opens the pages setup window (Fig. 1).
 




 Fig. 1 Page setup window
 

![scr_pages_setup_window.png](/docs/sites/en/files/images/NoCode_Customization/portal_pages_setup/scr_pages_setup_window.png)
6. Take the following steps in the the
 
 Pages setup for external users
 
 block:
 


	* Select an existing Freedom UI page in the
	 
	 Default page
	 
	 field or click
	 ![btn_add.png](/docs/sites/en/files/images/NoCodePlatform/custom_form_pages/btn_add.png)
	 to the right of the field to create and set up a new page.
	* Select an existing Freedom UI page in the
	 
	 Add page
	 
	 field or click
	 ![btn_add.png](/docs/sites/en/files/images/NoCodePlatform/custom_form_pages/btn_add.png)
	 to the right of the field to create and set up a new page (optional).
7. Click
 
 Save
 
 .
8. Save the list page.



**As a result** 
 , Creatio will use the specified pages to display records in Portal Creatio.
 


### 
 Set up Freedom UI form pages for external users in an app data model



 You can set up Freedom UI form pages for external users in a data model of an editable app. For example, this is useful if you need to create a custom form page for an out-of-the-box Creatio object and the page is the only Freedom UI functionality required. To do this:
 


1. Click
 ![btn_system_designer_8_shell.png](/docs/sites/en/files/images/NoCode_Customization/portal_pages_setup/btn_system_designer_8_shell.png)
 in the top right →
 
 Application Hub
 
 .
2. Open an existing app or create a new app. Learn more:
 [Manage apps](https://academy.creatio.com/documents?id=2444#title-2232-6) 
 .
3. Open the
 
 Data models
 
 tab.
4. Click the app data model connected to the relevant object.
5. Open the
 
 Pages
 
 tab →
 
 Pages setup for external users
 
 block.
6. Select an existing Freedom UI page in the
 
 Default page
 
 field or click
 ![btn_add_data_model.png](/docs/sites/en/files/images/NoCodePlatform/custom_form_pages/btn_add_data_model.png)
 to the right of the field to create and set up a new page.
7. Select an existing Freedom UI page in the
 
 Add page
 
 field or click
 ![btn_add.png](/docs/sites/en/files/images/NoCodePlatform/custom_form_pages/btn_add.png)
 to the right of the field to create and set up a new page (optional).
 




 Fig. 2 Set up Freedom UI form pages for external users in the data model
 

![scr_data_model_pages_settings.png](/docs/sites/en/files/images/NoCode_Customization/portal_pages_setup/scr_data_model_pages_settings.png)
8. Click
 
 Save
 
 .



**As a result** 
 , Creatio will use the specified pages to display records in Portal Creatio.
 




