


 This chapter covers a step-by-step procedure of setting up a typical approval case: a leave request in the
 
 Documents
 
 section.
 


1. Each record with the “Approval” type is submitted for approval automatically, right after a new record is saved.
2. First, an HR employee must approve the request.
3. Once approved by the HR, the request is submitted for approval by the corresponding department manager.
4. Approvers will receive email notifications that a new record awaits their approval. The employees who submit requests for approval will receive email notifications about approval results.
5. If the approval has been denied by HR, the case transitions to the
 
 Preparation
 
 stage, at which the employee must revise the request. If the approval has been denied by the department manager, the case transitions to the
 
 Canceled
 
 stage.
6. If the request is approved by the department manager, the case transitions to the
 
 Completed
 
 stage.
7. The
 
 Completed
 
 and
 
 Canceled
 
 stages are final.
   

 Set up the approval case as shown in
 [Fig. 1](#XREF_51444_226)
 .
 




 Attention. Please note that the example below refers to a custom case. Not all fields and values used are available in the base Creatio configuration. You can set up additional section fields in the
 [Section wizard](https://academy.creatio.com/documents?product=studio&ver=7&id=1245) 
 .
   

 Before creating and configuring an approval business process, make sure that the
 
 Enable approval in section
 
 checkbox is selected for that section in the section wizard.
 [Read more>>>](/docs/node/765/%26#9;) 






Fig. 1
 – Case for leave request approval
 

![Case for leave request approval](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_case_diagram.png)



 Set up the leave request approval case
 


1. Click Click
 
 View
 
 →
 
 Set up section cases
 
 in the
 
 Documents
 
 section. The Case Designer will open (
 [Fig. 2](#XREF_71630_246)
 ).
2. In the case list, select “Status” in the
 
 Which column to build the stages by?
 
 field. As a result, the case stages will be defined by the document status.
3. Select “Type” in the
 
 Which column determines which case to use with a record?
 
 field. As a result, the case will apply only to documents of a specific type (i.e., “Request”).
 





 Fig. 2
 

 Case list of the
 
 Documents
 
 section
 

![Case list in the Documents section](/docs/sites/en/files/2020-12/scr_chapter_case_designer_documents_section_cases_list.png)
4. Click the
 
 New case
 
 button to open the Case Designer. Here you will need to set up:
	* Case parameters.
	* Case sequence.
	* Activities on each case stage.



 Set up case parameters.
-------------------------



 The case parameters are set up in the case setup area (
 [Fig. 3](#XREF_58497_246)
 ).
 


1. Click
 ![btn_system_designer.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_system_designer.png)
 to open case properties.
2. Specify the case title (i.e., “Request processing”).
3. Optionally, populate the
 
 Description
 
 field with additional information for anyone who may edit this case.
4. In the
 
 Use this case with records where:
 
 area, click
 ![btn_case_designer_case_properties_initial_case_condition_choice.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_case_designer_case_properties_initial_case_condition_choice.png)
 and select “Request.” As a result, the case will apply to all documents of the “Request” type.
 




 Attention. Please note that the example below refers to a custom case. Not all fields and values used are available in the base Creatio configuration. You can add document types to the
 
 Document types
 
 lookup. Learn more about working with lookups in the “
 [Manage lookup values](/docs/node/285/%26#9;) 
 ” article.
5. The
 
 Section
 
 ,
 
 Stage column
 
 ,
 
 Code
 
 ,
 
 Package
 
 ,
 
 Active,
 
 and
 
 Actual version
 
 fields will be populated automatically.
 





 Fig. 3
 

 Case setup area
 

![Case setup area](/docs/sites/en/files/2020-12/chapter_case_designer_application_case_properties.png)



 Set up case stages
--------------------



 Use the stages panel to set up the case workflow. The leave request approval case will have 5 stages that correspond to the values in the
 
 Status
 
 field in the
 
 Documents
 
 section. Use the
 ![btn_case_designer_add_case.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_case_designer_add_case.png)
 button to add case stages:
 
 Draft
 
 ,
 
 Approval
 
 ,
 
 Completed
 
 ,
 
 Canceled
 
 , and
 
 Archive
 
 . Set up stage properties and steps to complete at each stage. We will use the first stage as an example.
 


1. Click the first stage to open its setup area (
 [Fig. 4](#XREF_25065_248)
 ).
2. Enter the name of the stage.
3. Select the corresponding document stage in the
 
 Stage value in the lookup
 
![btn_case_designer_choose_from_lookup.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_case_designer_choose_from_lookup.png)
 field.  You can add document stages directly from the Case Designer by typing in the new stage name. Make sure to save the case each time you add a new lookup value this way.
4. All other case stages will be automatically added to the
 
 Possible next stages
 
 area. Remove all stages from the list, except for the
 
 Approval
 
 and
 
 Canceled
 
 stages.
5. All other case stages will be automatically added to the
 
 Possible previous stages
 
 area. Remove all stages, except for
 
 Approval
 
 from the list. If the approval is denied, the case will transition back to the
 
 Draft
 
 stage.
6. In the
 
 Automatic transition to the next case stage
 
 field, select “If required steps are completed.”
7. In the
 
 Additional settings
 
 area, select a color for this stage.
8. Leave the
 
 Group with another stage
 
 checkbox cleared. Grouped stages will display as one for the case user. Clicking a grouped stage will open a menu with all stages in the group. Note that this checkbox must be selected for the
 
 Canceled
 
 stage, which must be grouped with the
 
 Completed
 
 stage.
 





 Fig. 4
 

 The
 
 Draft
 
 stage parameters
 

![Draft stage parameters](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_preparation_stage_properties.png)



 Set up other stage properties in a similar way: “Approval” (
 [Fig. 5](#XREF_41209_249)
 ), “Completed” (
 [Fig. 6](#XREF_73316_250)
 ), “Canceled” (
 [Fig. 7](#XREF_22038_251)
 ), and “Archive” (
 
[Fig. 8](#XREF_85206_252) 

 ).
 





 Fig. 5
 

 The
 
 Approval
 
 stage parameters
 

![Approval stage parameters](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_approving_stage_properties.png)





 Fig. 6
 

 The
 
 Completed
 
 stage parameters
 

![Completed stage parameters](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_completed_stage_properties.png)





 Note.
 
 The
 
 Completed
 
 and
 
 Canceled
 
 stages are mutually exclusive and are therefore grouped. The grouping is configured in the properties of the
 
 Canceled
 
 stage. In the setup area of the
 
 Completed
 
 stage, a
 ![btn_com_information.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_com_information.png)
 icon is displayed next to the
 
 Group with another stage
 
 checkbox. If you hover the cursor over the icon, a tooltip will appear, indicating that the stage is already grouped.
 






 Fig. 7
 
 The
 
 Canceled
 
 stage parameters
 

![Canceled stage parameters](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_rejected_stage_properties.png)





 Fig. 8
 

 The
 
 Archive
 
 stage parameters
 

![Archive stage parameters](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_archived_stage_properties.png)



 Set up case stage steps
-------------------------



 Set up the steps of the
 
 Draft
 
 stage. To do this:
 


1. Click
 ![btn_case_designer_add_step_menu.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_case_designer_add_step_menu.png)
 below the
 
 Draft
 
 stage in the Case Designer working area. Select the
 
 Open edit page
 

 element. As a result, the document page will open on the
 
 Draft
 
 stage.
2. Enter the name of the new case element and press Enter. Click the added element to view its setup area.
3. In the
 
 Which page to open?
 
![btn_case_designer_choose_from_lookup00001.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_case_designer_choose_from_lookup00001.png)
 field, select “Document.“
4. In the
 
 Editing mode
 
 field, select “Edit existing record.“
 
 Record Id
 
 field will display below.
5. In the
 
 Record Id
 
 field, click
 ![chapter_case_designer_icon_parameter_menu.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_case_designer_icon_parameter_menu.png)
 and select “Main record column.” Choose the
 
 Id
 
 column. As a result, the case will open the document record for which the case instance is run.
6. In the
 
 Who fills in the page?
 
 field, the current user contact is specified by default. Click
 ![chapter_case_designer_icon_parameter_menu00002.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_case_designer_icon_parameter_menu00002.png)
 to change this value, if needed.
7. In the
 
 Recommendation for filling in the page
 
 field, list the actions that the user must perform on the opened document page, such as “Specify type of leave and exact dates.” This text will be displayed on the new document page.
8. In the
 
 Hint for user
 
 field, enter additional information for the user. For example, you can use this field to specify the maximum number of available vacation days or add a reminder to adjust the vacation with the head of the department before filling in the request.
9. When is the element considered complete?
 

 – you can optionally select “If the record matches conditions” to consider the case element complete when the record matches required conditions (certain fields are filled, etc.).
10. Otherwise, leave “Immediately after saving the record” in the
 
 When is the element considered complete?
 
 field (
 [Fig. 9](#XREF_95013_254)
 ). To do this:
 


	1. Click the
	 
	 Add condition
	 
	 button and select the
	 
	 Vocation type
	 
	 column as required.
	2. Select the
	 
	 Number of vacation days
	 
	 column as required.
	 
	
	
	
	
	
	 Fig. 9
	 
	
	 Setting up filter conditions
	 
	
	![Set up filter conditions](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_preparation_stage_actions_2.png)
11. The “At the start of the stage” value will be displayed by default in the
 
 When is the step performed?
 
 field. After the case transition to the
 
 Draft
 
 stage, the task for filling the application will be created. The task will be displayed on the application page which is processed by the case.
12. In the
 
 Step type
 
 field, specify the step as required.
 



 As a result, the settings for the case element will look like this (
 
[Fig. 10](#XREF_95178_253) 

 ):
 





 Fig. 10
 

 Properties of the “Fill application” element
 

!["Fill out" properties](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_preparation_stage_actions.png)



 Set up the sequence of stages
-------------------------------



 Set up the steps of the
 
 Approval
 
 stage.
 


1. Add a new
 

 Approval
 
 case element on the Case Designer working area. Enter the name of the new case element (i.e., “HR approval”) and press Enter. Populate the case element parameters.
2. In the
 
 When is the step performed?
 
 field the “At the start of the stage” value will be displayed by default.
3. In the
 
 Step type
 

 field, specify the step as required.
4. The “Approval required” value will automatically display In the
 
 Approval purpose
 
 field. If needed, modify the value in the
 
 Approval purpose
 
 field.
5. The value in the
 
 Approval section
 

 field should be “Documents” (the section, for which the case is being set up). This will be set by default if approvals are enabled in the
 
 Documents
 
 section.
 




**Note.** 
 If you cannot find the
 
 Document
 
 object in the list, the approval procedure might be disabled for the
 
 Documents
 
 section in the Section wizard. More information about approvals is available in the “
 [Set up approvals in a section](/docs/node/765/%26#9;) 
 ” article.
6. The
 
 Record Id
 
 field will be set to the record for which the case is run.
7. In the
 
 Approver
 
 field, select “Role.”
8. In the
 
 Role
 
 field, select the “Lookup value” option and choose the value that corresponds to the HR department from the “Roles (view)” lookup. All employees in the selected role will be able to process this approval.
9. In the
 
 Send email notification
 
 area, configure automatic email notifications for the approvers and the document owner.
 


	1. Select the
	 
	 Notify that approval is required
	 
	 checkbox.
	2. In the
	 
	 Email template
	 
	 field, click
	 ![btn_process_element_settings_lookup.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_process_element_settings_lookup.png)
	 and select an email template from the
	 
	 Email message template
	 
	 lookup.
	3. Select the
	 
	 Notify about the approval result
	 
	 checkbox.
	4. In the
	 
	 Recipient
	 
	 field, click the
	 ![btn_parametres_window.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_parametres_window.png)
	 button and select the “Main record column” option. In the opened
	 
	 Select column
	 
	 window, click
	 
	 +
	 
	 and select the
	 
	 Owner
	 
	 column. In the appeared
	 
	 Column
	 
	 field, select the
	 
	 Email
	 
	 column of the document owner’s contact record and click
	 
	 Select
	 
	 . The value in the
	 
	 Recipient
	 
	 field should now be “
	 
	 #Main record.Owner.Email#
	 
	 .”
	5. In the
	 
	 Email template
	 
	 field, click
	 ![btn_process_element_settings_lookup00003.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_process_element_settings_lookup00003.png)
	 and select an email template from the
	 
	 Email message template
	 
	 lookup.
	 
	
	
	
	
	
	 Attention.
	 
	 Set up the mailbox for email notifications in the
	 
	 Mailbox for sending email with information on approval
	 
	 system setting. Access the system setting in the Process Designer by clicking the
	 ![btn_com_information00004.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_com_information00004.png)
	 button in the
	 
	 Send email notification
	 
	 area.
	 
	
	
	
	
	
	
	 Note.
	 
	 Create email templates in the content designer, using the
	 
	 Approvals in the Documents section
	 
	 object. The approval objects are created automatically when you select the
	 
	 Enable approval in section
	 
	 checkbox in the section wizard. For example, if you select the
	 
	 Enable approval in section
	 
	 checkbox in the
	 
	 Documents
	 
	 section wizard, a new object “Approvals in section Document” will be created. If the lookup of the
	 
	 Enable approval in section
	 
	 does not contain the template you need, click
	 ![btn_com_add_tab.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_com_add_tab.png)
	 in the right part of the field to add a new email template. Learn more about creating an email template in the “
	 [Create an email template](https://academy.creatio.com/documents?product=administration&ver=7&id=1404)
	 ” article.
10. Select the
 
 Ignore errors on sending
 
 checkbox.
11. In the
 
 Change stage after element is completed
 
 area, set the following condition:
 
 If result
 
 – “Negative”;
 
 Set stage to
 
 – “Draft.”
 





 Note.
 
 There is no need to set stage transition for a positive approval result in this case, as the case will need to proceed to the next step within the same stage.
 




 As a result, the settings for the case element will look like this (
 [Fig. 11](#XREF_97479_254_HR)
 ):
 





 Fig. 11
 

 – “HR approval” case element setup area
 

!["HR approval" setup area](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_approving_stage_actions_1.png)
12. Add another
 
 Approval
 

 element to the
 
 Approval
 
 stage. Enter the name of the new case element (i.e., “Manager’s approval”) and press Enter. The properties of this case element will be the same as the ones of the “HR approval” element, except for the values in the
 
 When is the step performed?
 
 ,
 
 Approver
 
 and
 
 Change stage after element is completed
 
 properties.
	1. In the
	 
	 When is the step performed?
	 
	
	 field, select “After the previous step is complete.”
	2. In the
	 
	 Perform after step
	 
	 field, select “HR approval” (if the “HR approval” is the only preceding element, it will be selected by default).
	3. In the
	 
	 Approver
	 
	 field, select “Employee's manager.”
	4. In the
	 
	 Employee
	 
	 field, click
	 ![chapter_case_designer_icon_parameter_menu00005.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_case_designer_icon_parameter_menu00005.png)
	 and select “Main record column.” In the opened window, select the needed column of the Creatio object, specified in the
	 
	 Macro source
	 
	 field. As a result, whoever is specified as the manager of the employee submitting a leave request, will have to approve it.
	 
	
	
	
	
	 Attention. Please note that not all mentioned objects, fields, and values may be available by default in your Creatio configuration. You can set up additional section fields in the
	 [Section wizard](https://academy.creatio.com/documents?product=studio&ver=7&id=1245) 
	 .
	5. In the
	 
	 Change stage after element is completed
	 
	 area, set up the following stage transitions:
	 
	
	
		1. If result
		 
		 – “Positive”;
		 
		 Set stage to
		 
		 – “Completed.” As a result, if the request is denied by the employee’s manager, the case transitions to the
		 
		 Canceled
		 
		 stage.
		2. Click
		 ![btn_button_connections.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_button_connections.png)
		 and add another condition:
		 
		 If result
		 
		 – “Positive”;
		 
		 Set stage to
		 
		 – “Completed.” As a result, if the request is approved by the employee’s manager, the case transitions to the
		 
		 Completed
		 
		 stage.
		   
		
		 The remaining properties of the “Manager’s approval” case element match those of the “HR approval” element. As a result, the settings for the case element will look like this (
		 [Fig. 12](#XREF_56634_255) 
		 ):






 Fig. 12
 

 – “Manager’s approval” case element setup area
 



!["Manager's approval" setup area](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_approving_stage_actions_2.png)


 At the
 
 Completed
 
 case stage, set up a timer before the document status is changed to “Archive.”
 


1. Add a new
 
 Subprocess
 

 case element on the Case Designer working area on the
 
 Completed
 
 stage. Enter the name as “Term of the application relevance” (
 [Fig. 13](#XREF_34170_256) 
 ).
2. In the
 
 Which process to run?
 
 field, click and select the application activation business process. If the business process is disabled in the list, click the
 ![btn_button_connections00007.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_button_connections00007.png)
 button to add it.
 



 A Diagram of the business process of transfer application to the archive is provided in
 [Fig. 14](#XREF_86435_256)
 .
 



 The
 
 Simple start event
 
 and
 
 Wait for timer
 
 process elements – the process will start after 15 seconds after transitioning the case to the
 
 Completed
 
 stage.
 



 The
 
 Modify data
 
 element will change the status of the completed to “Archive.”
 




Fig. 13
 – Business process diagram
 

![Business process diagram](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_subprocess_stage_bp_scheme.png)



 To transfer the application by which the case is running, you should set up the transfer of the main record parameter from the case to the process. In our case, the main record is a document and the parameter which getting is to be configured is the document ID. Perform configuration in the Process Designer if the pass of the parameter is not set up. To do this:
 


	1. Open the designer of the process of transfer the application to the archive by clicking the
	 ![btn_chapter_designer_user_task_designer_task.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_end/btn_chapter_designer_user_task_designer_task.png)
	 button at the
	 
	 Which process to run
	 
	 field.
	2. Double click on the designer workspace to display the edit page of the process parameters.
	3. Click the
	 
	 Add parameter
	 
	 button on the
	 
	 Parameters
	 
	 tab.
	4. Select the “Lookup” in the list of the parameter types and specify the “Document” value in the
	 
	 Lookup
	 
	 field.
	5. Save the changes.
3. Return to the Case Designer to the configuration of the “The term of the application relevance” element properties. After you specify the process in the
 
 Which process to run
 
 field the parameter described above will be displayed in the
 
 Process parameters
 
 area.
4. The “At the start of the stage” value will be displayed by default in the
 
 When is the step performed?
 
 field.
5. The “Optional step” will be displayed in the
 
 Step type
 

 field. You can make it required, if necessary.
 





 Fig. 14
 

 – “The term of the application relevance” element properties
 

!["Term of application relevance" setup area](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_subprocess_stage_actions.png)
6. Save all changes made in the Case Designer.



 Configuration results
-----------------------



 As a result, all documents of the “Request” type will be processed according to the “Leave of absence approval” case (
 [Fig. 15](#XREF_95791_260)
 ). As soon as an employee who created a request clicks the
 
 Approval
 
 stage, the document is submitted for approval to HR. If HR denies the approval, the document status is set back to “Draft.” If HR approves the document, it is submitted for the employee's manager's approval. If the manager denies the approval, the document status is set to “Canceled.” If the manager approves the request, the document status is set to “Completed.”
 





 Fig. 15
 

 – Case for leave request approval
 

![Case for leave request approval](/docs/sites/en/files/2020-12/chapter_case_designer_application_approving_case_illustration.png)




