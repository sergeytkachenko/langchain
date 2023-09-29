


 Open a new or existing record page as part of the process using the
 
 Open edit page
 
 process element. For example, open an account page to view or edit the account information.
 



 Specify the edit page parameters in the element setup area (Fig. 1).
 




 Fig. 1 The
 
 Open edit page
 
 element setup area
 

![chapter_process_designer_edit_page_7.18.png](/docs/sites/en/files/images/BPM_Tools/user_elements_bp/chapter_process_designer_edit_page_7.18.png)



 Fill out the fields using the parameter value menu:
 


1. Enter the element caption at the top of the element setup area. Creatio will display the caption on the process diagram.
2. Which page to open?
 
 – select the edit page to open. This is a required field.
3. Who performs the task?
 
 – select one of the options and fill out the field that opens:
	* “User” – specify the user who will see the edit page in the
	 
	 Contact
	 
	 field.
	* “Employee's manager” – specify the user whose manager will see the edit page in the
	 
	 Contact
	 
	 field.
	* “Role” – specify the role users with which will see the edit page in the
	 
	 Role
	 
	 field.
	 
	
	
	
	 You can specify a dynamic parameter value or select a constant in the parameter value box.
4. Show page automatically
 
 – select the checkbox to display the page automatically as soon as the process initiates the action.
5. Editing mode
 
 – select one of the options: This is a required field.
	* Add new record
	 
	 – select this option to open the edit page of a new record. If you select this option, the
	 
	 Which default values to set in the fields of new records?
	 
	 field will become available. Click the
	 
	 Add field
	 
	 button to select the fields Creatio will populate automatically (Fig. 2).
	 
	
	
	
	
	 Fig. 2 Select the fields Creatio will populate as part of the process
	 
	
	![chapter_process_designer_edit_page_choose_fields.png](/docs/sites/en/files/images/BPM_Tools/user_elements_bp/chapter_process_designer_edit_page_choose_fields.png)
	* Edit existing records
	 
	 – select this option to open the edit page of an existing record. If you select this option, the
	 
	 Record ID
	 
	 field will become available.
6. Recommendations for filling in the page
 
 – enter the recommendations to display on the edit page. The recommendation text is a single line string, therefore it does not support line breaks regardless of syntax. This is a required field. To display the text in the assignee's language, make sure the “Create business process tasks in the owner's language” (“UsePerformerCultureInUserTask” code) system setting is enabled and the
 
 Translation
 
 section includes the translation. Learn more:
 [Localize UI via the
 
 Translation
 
 section](/docs/8-0/user/customization_tools/custom_localization/translate_the_ui/localize_ui_via_the_%5Btranslation%5D_section) 
 .
 





 Note.
 
 If the assignee is a group whose members use different Creatio languages, the recommendation will use the default culture.
7. Hint for user
 
 – enter additional information about the task. Click the
 ![btn_com_information.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_com_information.png)
 button on the record page to view the hint.
8. Create a list of results by column
 
 – select the checkbox to branch the process depending on the value of a record column. If you select the checkbox, the
 
 Column
 
 field will become available. The value of the column in this field will determine the element execution result. For example, after you fill out the opportunity page, the process may schedule a presentation or create a new contract, depending on the selected opportunity stage. In this case, create a list of results by the
 
 Stage
 
 column.
9. When is the element considered complete?
 
 – select the conditions for completing the element.
	* Immediately after saving the records
	 
	 – the action will be considered complete once the user saves the record page.
	* If the record matches conditions
	 
	 – specify the filtering conditions. Set a filter by the columns of the current object or one of its connected objects. You can specify the filter value in several ways:
	 
	
	
	
	
		1. Compare with parameter
		 
		 – specify the filter value using the parameter value box. Select a process or element parameter.
		2. Compare with value
		 
		 – specify the filter value using the specific column value.


 Note.
 
 If you have several
 
 Open edit page
 
 elements by the same object in parallel process flows, we recommend adding unique completion conditions to each element.
 



 If the completion condition of several elements is “Immediately after saving the record” or there is no condition specified, all the elements with the same condition will be considered complete when one of the elements completes.
10. Run following elements in the background
 
 – select the checkbox to run the elements connected to the outgoing flows in the background.
11. Create activity
 
 – select the checkbox to create a corresponding activity as part of this process step. If you select the checkbox, the following fields will become available:
	1. Start in
	 
	 – specify the period after which the activity must start, in minutes, hours, days, weeks, or months. The countdown starts as soon as the activity is created. Creatio uses this parameter to populate the
	 
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




