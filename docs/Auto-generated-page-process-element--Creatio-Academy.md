


 Open a page generated according to the specified parameters as part of the process using the
 
 Auto-generated page
 
 process element.
 



 For example, open a page with the preset list of elements, such as buttons or specific fields.
 



 Specify the auto-generated page parameters in the element setup area (Fig. 1).
 





 Fig. 1
 
 The
 
 Auto-generated page
 
 element setup area
 

![scr_chapter_process_designer_auto_page_7.18.png](/docs/sites/en/files/images/BPM_Tools/user_elements_bp/scr_chapter_process_designer_auto_page_7.18.png)



 Fill out the fields using the parameter value menu:
 


1. Enter the element caption at the top of the element setup area. Creatio will display the caption on the process diagram.
2. Page title
 
 – enter the name of the page to display.
3. Who performs the task?
 
 – select one of the options and fill out the field that opens:
	* “User” – specify the user who will see the page in the
	 
	 Contact
	 
	 field.
	* “Employee's manager” – specify the user whose manager will see the page in the
	 
	 Contact
	 
	 field.
	* “Role” – specify the role the users with which will see the page in the
	 
	 Role
	 
	 field.
	 
	
	
	
	 You can specify a dynamic parameter value or select a constant value in the parameter value box.
4. Show page automatically
 
 – select the checkbox to display the page automatically as soon as the process initiates the element.
5. Buttons
 
 – click
 ![btn_button_connections00006.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_button_connections00006.png)
 and enter the desired parameters (Fig. 2):
 


	1. Caption
	 
	 – specify the button caption. Required parameter.
	2. Code
	 
	 – enter the unique button name you can use when coding the business logic. Required parameter.
	3. Style
	 
	 – select one of the common Creatio button styles. Required parameter.
	4. Generate signal
	 
	 – enter the signal to generate once the button is clicked. For example, “Sent for approval.” You can add other items that wait for this signal further down the process.
	5. Select the
	 
	 Active
	 
	 checkbox if the button must be active when the page opens.
	6. Select the
	 
	 Performs value validation
	 
	 checkbox to check if the user filled out the required fields once the button is clicked. Click the
	 
	 Save
	 
	 button in the parameter value box.
	 
	
	
	
	 Clicking any button added to the page completes the element and determines its result. If you add outgoing conditional flows to the auto-generated page, the buttons will be available as flow completion conditions.
	 
	
	
	
	 Click the
	 ![btn_parametres_window_edit.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_parametres_window_edit.png)
	 button to manage the button display order and edit the button properties.
	 
	
	
	
	
	 Fig. 2 Add a button to the auto-generated page
	 
	
	![chapter_process_designer_auto_page_buttons.png](/docs/sites/en/files/images/BPM_Tools/user_elements_bp/chapter_process_designer_auto_page_buttons.png)
	7. Page Items
	 
	 – click
	 ![btn_button_connections00007.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_button_connections00007.png)
	 and select the type of the item to add to the page (Fig. 3).
	 
	
	
	
	
	
	 Fig. 3
	 
	 Select the type of item to display on the auto-generated page
	 
	
	![chapter_process_designer_elem_auto_page_type.png](/docs/sites/en/files/images/BPM_Tools/user_elements_bp/chapter_process_designer_elem_auto_page_type.png)
	
	
	
	 Fill out the item parameters. The available parameters depend on the item type (Fig. 4).
	 
	
	
		1. Title
		 
		 – enter the page item caption. Required parameter.
		2. Code
		 
		 – enter a unique parameter name that will store the item value.
		3. Text
		 
		 – enter the text to display on the item. Available for the “Notes” item type.
		4. Can be minimized
		 
		 – select the checkbox to allow the user to minimize the item block. Available for the “Item block” item type.
		5. Minimized
		 
		 – select the checkbox to load the item values minimized when the page opens. Available for the “Item block” item type.
		6. Required
		 
		 – select the checkbox to make the field required. Available for the “Text field,” “Selection field,” “Date/time,” “Integer,” and “Decimal” item types.
		7. Multiline
		 
		 – select the checkbox to make the field multiline. Available for the “Text field” item type.
		8. Data source
		 
		 – specify the lookup object. Available for the “Selection field” item type.
		9. View
		 
		 – select how the user can fill out the field: by using a dropdown list or selecting a value from the lookup. Available for the “Selection field” item type.
		10. Date format
		 
		 – select the display format for the “Date/time” item.
		 
		
		
		
		 Use the menu that appears when you click the
		 ![btn_parametres_window_edit00008.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_parametres_window_edit00008.png)
		 button to manage the page item display order, as well as edit and delete items.
		 
		
		
		
		 Fig. 4 Add an item to the auto-generated page
		 
		
		![chapter_process_designer_elem_auto_page_new.png](/docs/sites/en/files/images/BPM_Tools/user_elements_bp/chapter_process_designer_elem_auto_page_new.png)
6. Recommendation to user
 
 – enter the text to display on the page as part of the process. The recommendation text is a single line string, which does not support line breaks regardless of syntax. To display the text in the assignee's language, make sure the “Create business process tasks in the owner's language” (“UsePerformerCultureInUserTask” code) system setting is enabled and the
 
 Translation
 
 section includes the translation. Learn more:
 [Localize UI via the
 
 Translation
 
 section](/docs/8-0/user/customization_tools/custom_localization/translate_the_ui/localize_ui_via_the_%5Btranslation%5D_section) 
 .
 


 Note.
 
 If the assignee is a group whose members use different Creatio languages, the recommendation will use the default culture.
7. User hints
 
 – enter additional information about the task. Click the
 ![btn_com_information.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_com_information.png)
 button on the page to view the hint.
8. Connected object
 
 – specify the object if the action is connected to a particular Creatio object record.
9. Record of connected object
 
 – the record to which the action is connected.
 


 Note.
 
 When the action runs, Creatio will add the record with the connected object specified and the record that is connected to the action to the
 
 Connected items
 
 block of the
 
 Process log
 
 page. Also, the
 
 Move down the process
 
 menu will become available on the edit page of the connected record.
10. Run following elements in the background
 
 – select the checkbox to run the elements connected to the outgoing flows in the background.
11. Create activity
 
 – select the checkbox to create a corresponding activity as part of this process step. If you select the checkbox, the following fields will become available:
	1. Start in
	 
	 – specify the period after which the activity must start, in minutes, hours, days, weeks, or months. The countdown starts after the activity is created. Creatio uses this parameter to populate the
	 
	 Start
	 
	 field of the activity page.
	 
	
	
	 Note.
	 
	 The value of the activity page's
	 
	 Start
	 
	 field is the sum of the current user time and the
	 
	 Start in
	 
	 field value. For example, if you specify “30 minutes” in the
	 
	 Start in
	 
	 field, and the task was created at 12:00 PM, the value of the task's
	 
	 Start
	 
	 field will be “12:30 PM.”
	2. Planned duration
	 
	 – enter the activity duration, in minutes, hours, days, weeks, or months. Creatio uses this parameter to populate the
	 
	 Due
	 
	 field of the activity page.
	 
	
	
	 Note.
	 
	 The value of the activity page's
	 
	 Due
	 
	 field is the sum of the
	 
	 Start
	 
	 and
	 
	 Planned duration
	 
	 field values.
	3. Remind in
	 
	 – specify the period that ends before the activity starts. After this period, the notification for the owner or the role will be created automatically.
	4. Show in calendar
	 
	 – select the checkbox to display the task in the
	 
	 Calendar
	 
	 view of the
	 
	 Activities
	 
	 section.
	5. Connected to
	 
	 – connect the task to other Creatio entities. For example, an account. Creatio will display the task on the
	 
	 Activities
	 
	 detail of the connected record. By default, the element setup area displays account and contact connections. Click the
	 ![btn_button_connections.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_button_connections.png)
	 button to connect the task to other Creatio entities.




