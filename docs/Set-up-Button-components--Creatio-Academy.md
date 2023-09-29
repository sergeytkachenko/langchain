


 Use
 
 Button
 
 components to enable users to take a wide variety of actions, from opening record pages to setting up access permissions.
 



 Set up a button that executes a single action
-----------------------------------------------





 Example.
 
 Set up the
 
 Workflow
 
 button on the request page. The button must open the page that displays the request workflow and have an easily noticeable icon.
 





 Fig. 1 Button that executes a single action
 

![scr_single_action_button.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_single_action_button.png)


1. Drag a
 
 Button
 
 component to the canvas and open the component setup area.
2. Enter “Workflow” in the
 
 Title
 
 parameter. You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/set_title_field_localization.png)
 button to the right to localize the title to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article.
3. Specify the visual design of the button in the
 
 Style
 
 parameter. For this example, select “Primary.”
4. Set the button size in the
 
 Size
 
 parameter. For this example, select “L.”
5. Specify the button action to execute in the
 
 Action
 
 parameter. For this example, select “Open specific page.” This brings up the
 
 Which page to open?
 
 parameter. Other parameter values bring up similar parameters that let you customize the action.
6. Select the page to open in the
 
 Which page to open?
 
 parameter or click
 ![btn_new_page.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_new_page.png)
 next to the parameter to create and set up a new page. For this example, create and set up a “Workflow” page based on the “Blank” template.
7. Click
 ![scr_add_menu_item_button.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_add_menu_item_button.png)
 in the
 
 Menu items
 
 group to add another action to the button as a menu item. For this example, do not add any items. Learn more about setting up button menus in different sections:
 [Set up a button that executes multiple common actions](#title-2377-2) 
 ,
 [Set up a button that contains submenus](#title-2377-3) 
 .
8. Click the
 ![btn_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_visible.png)
 or
 ![btn_not_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_not_visible.png)
 button in the
 
 Visibility
 
 group to make the component visible or invisible by default on the page, respectively. For this example, leave the component visible.
9. Click
 
 Setup conditions
 
 in the
 
 Visibility
 
 group to set up element business rules. For this example, do not add business rules. Learn more about setting up business rules in a separate article:
 [Set up business rules](https://academy.creatio.com/documents?id=2409) 
 .
10. Click the
 
 Use icon
 
 toggle to add an icon to the button. This brings up button setup parameters.
11. Select the
 ![icn_info.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_info.png)
 information icon in the
 
 Icon
 
 parameter.
12. Specify the button position or toggle the button caption in the
 
 Position
 
 parameter. For this example, place the icon to the left of the caption.
13. View the unique component code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar components on the page. For this example, leave the code as is.




 Fig. 2 Set up a button that executes a single action
 

![scr_single_action_button_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_single_action_button_setup_area.png)



 As a result, Creatio will add the
 
 Workflow
 
 button to the request page. The button will open the page the displays the request workflow and have an
 ![icn_info.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_info.png)
 icon to the left of its caption.
 



 Set up a button that executes multiple common actions
-------------------------------------------------------



 To keep the page UI lean, you can combine similar button actions, for example, saving the record, canceling changes, or closing the page, into the drop-down menu of a single button.
 





 Example.
 
 Set up the
 
 Save and close
 
 button on the request page toolbar. The button must save the changes and close the page simultaneously. The
 
 Close
 
 item of the drop-down button menu must close the page without saving the changes.
 





 Fig. 3 Button that executes multiple common actions
 

![scr_multiple_action_button.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_multiple_action_button.png)


1. Open the setup area of the
 
 Save
 
 button included in the page template by default.
2. Enter “Save and close” in the
 
 Title
 
 parameter. You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/set_title_field_localization.png)
 button to the right to localize the title to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article.
3. Add a drop-down menu with the action that closes the page.
 


	1. Click
	 ![](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_add_menu_item_button.png)
	 in the
	 
	 Menu items
	 
	 block. This opens the setup area of the menu item.
	2. Set the base menu item parameters in the setup area:
	 
	
	
		1. Enter “Close” in the
		 
		 Title
		 
		 parameter. You can localize the parameter similarly to the
		 
		 Title
		 
		 parameter.
		2. Select “Close page” in the
		 
		 Action
		 
		 parameter.




 Fig. 4 Set up the button that executes multiple common actions
 

![scr_multiple_action_button_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_multiple_action_button_setup_area.png)



 As a result, Creatio will add the
 
 Save and close
 
 button to the record page. Click the button to save the changes and open the section list. Select the
 
 Close
 
 menu item in the button drop-down menu to close the page without saving the changes.
 



 Set up a button that contains submenus
----------------------------------------



 To make the app workflow as flexible as possible, you can add buttons that contain submenus with various actions users might require on different process stages.
 





 Example.
 
 Set up the
 
 Actions
 
 button on the list page toolbar. The button must contain an embedded menu with the following items:
 
 Open homepage
 
 and
 
 Add record
 
 . Items of the
 
 Open homepage
 
 submenu must open “HR” and “Finance” homepages. Items of the
 
 Add record
 
 submenu must add new expense and business trip records.
 





 Fig. 5 Button that contains submenus
 

![scr_submenu_button.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_submenu_button.png)


1. Drag a
 
 Button
 
 component to the canvas and open the component setup area.
2. Enter “Actions” in the
 
 Title
 
 parameter. You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/set_title_field_localization.png)
 button to the right to localize the title to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article.
3. Select “Primary” in the
 
 Style
 
 parameter.
4. Set up the submenu with actions that open pages.
 


	1. Add an item that will contain the submenu.
	 
	
	
		1. Click
		 ![](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_add_menu_item_button.png)
		 in the
		 
		 Menu items
		 
		 block.
		2. Enter “Open homepage” in the
		 
		 Title
		 
		 parameter. You can localize the parameter similarly to the first
		 
		 Title
		 
		 parameter.
	2. Add an item that opens the “HR” homepage to the
	 
	 Open homepage
	 
	 submenu.
	 
	
	
		1. Click the
		 
		 Open homepage
		 
		 menu item to open its settings.
		2. Click
		 ![](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_add_menu_item_button.png)
		 in the
		 
		 Menu items
		 
		 block.
		3. Set the base menu item parameters in the setup area:
		 
		
		
			1. Set
			 
			 Action
			 
			 to “Open specific page.”
			2. Enter “HR” in the
			 
			 Title
			 
			 parameter. You can localize the parameter similarly to the first
			 
			 Title
			 
			 parameter.
			3. Select the page to open in the
			 
			 Which page to open?
			 
			 parameter or click
			 ![btn_new_page.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_new_page.png)
			 next to the parameter to create and set up a new page. For this example, create and set up an “HR” homepage based on the “Dashboards” template.
	3. Repeat steps a-c for the submenu item that opens the “Finance” homepage.
5. Set up the submenu whose items add expense and business trip records in a similar way.




 Fig. 6 Set up the button that contains submenus
 

![scr_submenu_button_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_submenu_button_setup_area.png)



 As a result, Creatio will add the
 
 Actions
 
 button to the toolbar of the list page. You will be able to run the following actions using the button menu:
 


* Open HR homepage.
* Open Finance homepage.
* Add an expense record.
* Add a business trip record.



 Set up a button that runs business processes in a section
-----------------------------------------------------------



 In Creatio, you can set up a business process that runs for a specific section record. You can run business processes in any Freedom UI object using a button.
 





 Example.
 
 Set up the
 
 Run process
 
 button on the record page toolbar. The button must run the
 
 Actualize contact age process
 
 and
 
 Update the profile data population
 
 business processes.
 





 Fig. 7 Button that runs a business process
 

![scr_process_button.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_process_button.png)


1. Drag a
 
 Button
 
 component to the canvas and open the component setup area.
2. Enter “Run process” in the
 
 Title
 
 parameter. You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/set_title_field_localization.png)
 button to the right to localize the title to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article.
3. Set
 
 Style
 
 to “Primary.”
4. Add an item that runs the
 
 Actualize contact age process
 
 process.
 


	1. Click
	 ![](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_add_menu_item_button.png)
	 in the
	 
	 Menu items
	 
	 block.
	2. Set the base menu item parameters in the setup area:
	 
	
	
		1. Enter “Actualize contact age process” in the
		 
		 Title
		 
		 parameter. You can localize the parameter similarly to the first
		 
		 Title
		 
		 parameter.
		2. Select “Run process” in the
		 
		 Action
		 
		 parameter.
		3. Select “Actualize contact age process” in the
		 
		 Which process to run?
		 
		 parameter.
5. Add an item that runs the
 
 Update the profile data population
 
 process in a similar way.




 Fig. 8 Set up the button that runs business processes
 

![scr_process_button_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_process_button_setup_area.png)



 As a result, you will be able to run the
 
 Actualize contact age process
 
 and
 
 Update the profile data population
 
 business processes using the
 
 Run process
 
 button on the section page.
 




