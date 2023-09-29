


 <!--/\*--><![CDATA[/\* ><!--\*/

<!--/\*--><![CDATA[/\* ><!--\*/
div.table > table > tbody > tr > td:first-child{ min-width:74pt; text-align: center; vertical-align: middle; } .field--name-body ul ol { list-style-type: lower-alpha; } .field--name-body ul ol>li::before{ content:none; }

/\*--><!]]]]><![CDATA[>\*/

/\*--><!]]>\*/
 


 Create a new activity as part of the process using the
 
 Perform task
 
 process element.
 



 Specify the task parameters in the element setup area (Fig. 1).
 




 Fig. 1 The
 
 Perform task
 
 element setup area
 

![chapter_process_designer_make_a_task_7.18.png](/docs/sites/en/files/images/BPM_Tools/user_elements_bp/chapter_process_designer_make_a_task_7.18.png)



 Fill out the fields using the parameter value menu:
 


1. Enter the element caption at the top of the element setup area. Creatio will display the caption on the process diagram.
2. What should be done?
 
 – enter the task title. Specify the goal of the task in this field. To display the task title in the assignee's language, make sure the “Create business process tasks in the owner's language” (“UsePerformerCultureInUserTask” code) system setting is enabled and the
 
 Translation
 
 section includes the translation. Learn more:
 [Localize UI via the
 
 Translation
 
 section](/docs/7-18/user/customization_tools/custom_localization/translate_the_ui/localize_ui_via_the_%5Btranslation%5D_section) 
 .
 





 Note.
 
 If the task is assigned to a group whose members use different Creatio languages, the task will use the default culture.
3. Who performs the task?
 
 – select one of the options and fill out the field that opens:
	* “User” – specify the user responsible for the task in the
	 
	 Contact
	 
	 field.
	* “Employee's manager” – specify the user whose manager is responsible for the task in the
	 
	 Contact
	 
	 field.
	* “Role” – specify the role the users with which can perform the task the
	 
	 Role
	 
	 field.
	 
	
	
	
	 You can specify a dynamic parameter value or select a constant value in the parameter value box.
4. Show page automatically
 
 – select the checkbox to display the task page automatically as soon as the process initiates the action.
5. Run following elements in the background
 
 – select the checkbox to run the elements connected to the outgoing flows in the background.
6. Hint for user
 
 – enter additional information about the task. Click the
 ![btn_com_information.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_com_information.png)
 button on the activity page to view the hint.
7. Task category
 
 – select the task category. For example, “To do” or “Meeting”. This is a required field.
8. Start in
 
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
9. Planned duration
 
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
10. Remind in
 
 – specify the period that ends before the activity starts. After this period, Creatio will add a notification for the owner or the role automatically.
11. Show in calendar
 
 – select the checkbox to display the task in the
 
 Calendar
 
 view of the
 
 Activities
 
 section.
12. Connected to
 
 – connect the task to other Creatio entities. For example, an account. Creatio will display the task on the
 
 Activities
 
 detail of the connected record. By default, the element setup area displays account and contact connections. Click the
 ![btn_button_connections.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_button_connections.png)
 button to connect the task to other Creatio entities.



 If you specify a parameter, Creatio will populate the corresponding field on the activity page when creating a process task. If you do not specify a parameter, the corresponding field on the activity page will remain empty. You will be able to fill it out manually.
 




