


 You can work with Classic UI sections in Freedom UI in the following ways:
 


* Move a Classic UI section to Freedom UI.
 [Read more >>>](#title-2619-5)
* Bind a Classic UI section to the Freedom UI app.
 [Read more >>>](#title-2619-6)



 Move a Classic UI section to Freedom UI
-----------------------------------------



 To move a Classic UI section to Freedom UI, set up a Freedom UI section for an object that already has a Classic UI section. You can add a section to a new or existing app. In general, the setup procedure comprises the following steps:
 


1. Create an app based on the section object.
 [Read more >>>](#title-2619-1)
2. Customize the app pages.
 [Read more >>>](#title-2619-2)
3. Replace the Classic UI section with the Freedom UI section in workplaces.
 [Read more >>>](#title-2619-3)
4. Ensure the Creatio always opens Freedom UI form pages for the section object.
 [Read more >>>](#title-2619-4)





 Example.
 
 Create a Freedom UI section for a custom
 
 Requests
 
 object that has a Classic UI section.
 



### 
 Step 1. Create an app based on the section object


1. Click
 ![btn_system_designer.png](/docs/sites/en/files/images/NoCodePlatform/move_a_classic_ui_section_to_freedom_ui/btn_system_designer.png)
 to open the System Designer → “Application Management” →
 
 Application Hub
 
 .
2. Click
 
 New application
 
 →
 
 Records & Business processes
 
 template →
 
 Select
 
 .
3. Select the app icon and color. For this example, select the
 ![icn_requests.png](/docs/sites/en/files/images/NoCodePlatform/move_a_classic_ui_section_to_freedom_ui/icn_requests.png)
 icon and orange color (Fig. 1).
4. Enter the app name in the
 
 Application name
 
 field. For this example, enter “Requests.”
5. Click
 
 Advanced parameters
 
 →
 
 Link to an existing object
 
 . This brings up the object selection field.
6. Select the “Requests” object in the
 
 Object
 
 field.
7. Click “Create.”




 Fig. 1 Create an app
 

![scr_create_an_app.png](/docs/sites/en/files/images/NoCodePlatform/move_a_classic_ui_section_to_freedom_ui/scr_create_an_app.png)



 As a result, Creatio will add the
 
 Requests
 
 app that contains the
 
 Requests
 
 section and add the section to the “My applications” workplace. The section will have the same icon, color, and name as the app, but you will be able to change them for the section. Learn more about managing the app in a separate article:
 [Manage apps](https://academy.creatio.com/documents?id=2444) 
 .
 



 Since the app does not contain the needed functionality at this step, we recommend ensuring only the system administrators have permissions to access the “My applications” workplace. Learn more about setting up workplace permissions in a separate article:
 [Set up workplaces](https://academy.creatio.com/documents?id=1248#title-1730-4) 
 .
 



 You can add more sections based on new or existing objects to the app if needed. Learn more:
 [Manage app elements in the No-Code Designer](https://academy.creatio.com/documents?id=2418#title-2533-2) 
 ,
 [Set up the app UI](https://academy.creatio.com/documents?id=2379#title-2231-1) 
 .
 





 Note.
 
 When you create an app, Creatio adds base packages and the package that contains the object as dependencies. Creatio can add more dependencies when you customize the app pages. We recommend keeping track of app dependencies if you are going to transfer the app to other environments.
 



### 
 Step 2. Customize the section pages



 The page customization you need to perform on this step depends on the Classic UI section and your business goals. You can follow these best practices when setting up the pages:
 


* You can recreate the functionality of the Classic UI section in the Freedom UI Designer or enhance the functionality using advanced Freedom UI capabilities.
* Developers can implement custom functionality using custom code.
* You can recreate or set up new page or element business rules.
* If the object has a dynamic case connected to it, Creatio adds it automatically when you add an
 
 Action Dashboard
 
 component. You can also create new cases when you edit pages.
* If the Classic UI section has custom lookups, add them to the needed Freedom UI pages manually in the Freedom UI Designer.
* If the app has customizations and you are going to transfer it to a different environment, bind the packages that contain customizations to the app. You can do this via lookups.
* You can localize Freedom UI elements as part of the page setup.



 Learn more about customizing Freedom UI pages in separate articles:
 [Freedom UI Designer](https://academy.creatio.com/documents?id=2376) 
 ,
 [Implement a custom component,](https://academy.creatio.com/documents?id=15002) 
[Implement a remote module](https://academy.creatio.com/documents?id=15017) 
 ,
 [Set up business rules](https://academy.creatio.com/documents?id=2409) 
 ,
 [Localize a Freedom UI element](https://academy.creatio.com/documents?id=2441) 
 .
 


### 
 Step 3. Replace the Classic UI section with the Freedom UI section in workplaces


1. Click
 ![btn_system_designer.png](/docs/sites/en/files/images/NoCodePlatform/move_a_classic_ui_section_to_freedom_ui/btn_system_designer.png)
 to open the System Designer → “Set up view” →
 
 Workplace setup
 
 .
2. Select the needed workplace and click
 
 Open
 
 . For this example, select the “Service” workplace.
3. Add the Freedom UI
 
 Requests
 
 section. To do this:
	1. Click the
	 ![btn_add.png](/docs/sites/en/files/images/NoCodePlatform/move_a_classic_ui_section_to_freedom_ui/btn_add.png)
	 button on the
	 
	 Sections
	 
	 detail. This opens a window.
	2. Select the “Requests” section →
	 
	 Select
	 
	 (Fig. 2).
	 
	
	
	
	
	 Fig. 2 Select a section
	 
	
	![scr_select_a_section.png](/docs/sites/en/files/images/NoCodePlatform/move_a_classic_ui_section_to_freedom_ui/scr_select_a_section.png)
4. Remove the Classic UI
 
 Requests
 
 section. To do this:
 


	1. Select the section on the
	 
	 Sections
	 
	 detail.
	2. Click the
	 ![btn_context_menu.png](/docs/sites/en/files/images/NoCodePlatform/move_a_classic_ui_section_to_freedom_ui/btn_context_menu.png)
	 button →
	 
	 Delete
	 
	 .
5. Repeat the steps 1–4 for other relevant workplaces.



 As a result, users will be able to use the new section in Creatio. You can also leave the Classic UI section in workplaces for certain roles. For example, this is useful for A/B testing. Learn more about managing workplaces in a separate article:
 [Set up workplaces](https://academy.creatio.com/documents?id=1248) 
 .
 



 The section will open the Freedom UI form page when users add, view, edit, or copy records. Proceed to step 4 to ensure the section opens Freedom UI form pages in other cases as well. You can skip step 4 if you already have Freedom UI turned on.
 


### 
 Step 4. Ensure the app opens Freedom UI form pages for the section object



 If an object has both Classic UI and Freedom UI form pages, Freedom UI sections always open Freedom UI form pages when users add, view, edit, or copy records. To ensure the section opens Freedom UI form pages in other cases, take any of the following steps:
 


* Replace the Classic UI section with the Freedom UI section in the workplace settings. That way, the new section will open Freedom UI form pages for the object that has both Classic UI and Freedom UI form pages.
* Change system setting values. That way, Creatio will open Freedom UI form pages for all objects that have both Classic UI and Freedom UI form pages.
* Add the object as an exception to system setting values to a lookup. That way, Creatio will open Freedom UI form pages only for the object of your section.



 Learn more in a separate article:
 [Manage the form pages in the Freedom UI and Classic UI](https://academy.creatio.com/documents?id=2413) 
 .
 



 Bind a Classic UI section to the Freedom UI app
-------------------------------------------------



 If the current Freedom UI tools do not let you move all customizations of the Classic UI section to Freedom UI, you can bind an existing Classic UI section to the Freedom UI app. You can do it in the following ways:
 


* Move the Classic UI section schemas to the app package using Creatio IDE. Learn more:
 [Operations in Creatio IDE](https://academy.creatio.com/documents?id=15104&anchor=title-2093-19) 
 .
* Bind the package that implements the Classic UI section to the app.



 To
 **bind the package** 
 that implements the Classic UI section to the app:
 


1. Click
 ![](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “System setup” → “Lookups.”
2. Click
 
 New lookup
 
 on the
 
 Lookups
 
 section toolbar and fill out the
 **lookup properties** 
 :
 


	* Enter an arbitrary name in the
	 
	 Name
	 
	 property. For example, “App package.”
	* Select “Package in installed application” in the
	 
	 Object
	 
	 property.
3. Click
 
 Save
 
 on the lookup setup page's toolbar.
4. Open the
 
 App package
 
 lookup.
5. Add a filter “Installed application = [Name of the app to change the primary app package].”
6. Select an arbitrary record in the lookup list and click
 ![](/docs/sites/en/files/images/NoCodePlatform/move_a_classic_ui_section_to_freedom_ui/btn_copy_record.png)
 .
7. Select the package that implements the Classic UI section in the
 
 Package
 
 column. For example, bind the “UsrExpensesPackage” package that includes the
 
 Expenses
 
 Classic UI section to the
 
 Requests
 
 Freedom UI app. To do this, select the “UsrExpensesPackage” package in the
 
 Package
 
 column (Fig. 3).
 




 Fig. 3 Select a package
 

![scr_select_a_package.png](/docs/sites/en/files/images/NoCodePlatform/move_a_classic_ui_section_to_freedom_ui/scr_select_a_package.png)
8. Save the changes.



 As a result, Creatio will bind the “UsrExpensesPackage” package that includes the
 
 Expenses
 
 Classic UI section to the
 
 Requests
 
 Freedom UI app (Fig. 4).
 




 Fig. 4
 
 Advanced settings
 
 tab of
 
 Requests
 
 app
 

![scr_view_advanced_settings_tab.png](/docs/sites/en/files/images/NoCodePlatform/move_a_classic_ui_section_to_freedom_ui/scr_view_advanced_settings_tab.png)




