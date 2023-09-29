


 Use the
 
 Perform task
 
![chapter_case_designer_icon_task.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_icon_task.png)
 case element to create an activity for the user to complete as part of the case.
 



 Set up the [Perform task] element
-----------------------------------



 Specify the task parameters in the element setup area (Fig. 1).
 




 Fig. 1 The
 
 Perform task
 
 element setup area
 

![chapter_case_designer_task_properties_7.18.png](/docs/sites/en/files/images/BPM_Tools/dcm_elements/chapter_case_designer_task_properties_7.18.png)



 Most element parameters, such as
 
 Task category
 
 ,
 
 Priority
 
 , correspond to activity page fields. If you specify a parameter, Creatio will populate the corresponding field on the activity page when creating a case task. If you do not specify a parameter, the corresponding field on the activity page will remain empty. You will be able to fill it out manually.
 



 The element caption is displayed at the top of the setup area. This makes the element easy to find on the case diagram.
 



 Fill out the following fields:
 


1. What should be done?
 
 – enter the task title. The subject briefly summarizes the task for the user to perform. This is a required field. To display the task title in the assignee's language, make sure the “Create business process tasks in the owner's language” (“UsePerformerCultureInUserTask” code) system setting is enabled and the
 
 Translation
 
 section includes the translation. Learn more:
 [Localize UI via the
 
 Translation
 
 section](/docs/7-18/user/customization_tools/custom_localization/translate_the_ui/localize_ui_via_the_%5Btranslation%5D_section) 
 .
 





 Note.
 
 If the task is assigned to a group whose members use different Creatio languages, the task will use the default culture.
2. Who performs the task?
 
 – select one of the options and fill out the field that opens:
	* “User” – specify the user responsible for the task in the
	 
	 Contact
	 
	 field.
	* “Employee's manager” – specify the user whose manager is responsible for the task in the
	 
	 Contact
	 
	 field.
	* “Role” – specify the role associated with the users who can perform the task in the
	 
	 Role
	 
	 field.
	 
	
	
	
	 You can specify a dynamic parameter value or select a constant value in the parameter value box.
3. Show page automatically
 
 – select the checkbox to display the task page automatically as soon as the case initiates the task.
4. Run following elements in the background
 
 – select the checkbox to run the subsequent elements in the background.
5. Hint for user
 
 – enter additional information about the task. Click the
 ![btn_com_information00012.png](/docs/sites/en/files/images/BPM_Tools/dcm_elements/btn_com_information00012.png)
 button on the activity page to view the hint.
6. Task category
 
 – select the task category. For example, “To do” or “Meeting.” This is a required field.
7. Start in
 
 – specify the period after which the activity must start, in minutes, hours, days, weeks, and months. The countdown starts after the case activity is created. Creatio uses this parameter to populate the
 
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
8. Planned duration
 
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
9. Remind in
 
 – the period that ends before the activity starts. After this period, the notification for the owner or the role will be created automatically.
10. Show in calendar
 
 – select the checkbox to display the task in the
 
 Calendar
 
 view of the
 
 Activities
 
 section.
11. Connected to
 
 – connect the task to other Creatio entities and the main record column. For example, an account and the account's primary contact. Creatio will display the task on the
 
 Activities
 
 detail of the connected record. By default, the element setup area displays connections to the case section record. For example, the task of the
 
 Lead
 
 section case will be connected to the corresponding lead. Click the
 ![btn_button_connections.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/btn_button_connections.png)
 button to connect the task to other Creatio entities.
12. When is the step performed?
 
 – indicates whether to activate the element at the start of the stage or after a case step. Select “At the start of the stage” to create activity at the start of the case stage. Select “After the previous step is complete” if the activity must be created after the previous step in the case stage. Specify the step in the
 
 Perform after step
 
 field.
13. Step type
 
 – specify if the task is required. Select “Required step” if the task must be completed to transition to the next stage. Select “Optional step” if the user can advance to the next case stage without completing this task.
 


 Note.
 
 Users can advance to the final “unsuccessful” stage from any stage without completing the required steps.
14. Change stage after element is completed
 
 – configure stage transitions depending on activity results. Click the
 ![btn_button_connections00001.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/btn_button_connections00001.png)
 button to add fields for configuring the conditions of case transition. Select the completion result of the
 
 Perform task
 
 element after which the case must be transferred to a different stage in the
 
 If result
 
 field. Specify the destination stage in the
 
 Set stage to
 
 field.




