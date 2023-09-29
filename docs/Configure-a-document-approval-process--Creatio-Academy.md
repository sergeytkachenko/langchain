




 Example.
 
 Create a business process for approving documents in the
 
 Documents
 
 section. Each document is sent for approval manually by launching the process in the section. All employees in the
 
 Financial department
 
 role can approve documents. Additionally, all employees eligible for approving documents receive an email notification once the approval is created. The employee awaiting the approval receives an email once the document is approved. If approved, the document status is changed to “Active”. If it was not approved, the document status is changed to “Draft”, and Creatio automatically creates an activity for the responsible employee to revise the document.
 




 The configuration procedure includes the following general steps:
 


1. Set up the approval case as shown on Fig. 1.
2. Set up running the approval business process for records that require approval in the corresponding section.
 





 Attention.
 
 Before creating and configuring an approval business process, make sure that the
 
 Enable approval in section
 
 checkbox is selected for that section in the section wizard.
 [Read more>>>](/docs/7-18/user/platform_basics/communications/approvals_shortcut/approvals) 







 Fig. 1
 
 A business process for approving documents
 

![chapter_process_creation_designer_document_approvement.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_process_creation_designer_document_approvement.png)


### 
 Configure business processes


1. Open the
 
 Process library
 
 section and add a new process.
2. Enter the name of the process in the
 
 Process
 
 field (e.g., “Document approval”).
3. Open the
 
 Parameters
 
 tab and add a new parameter. This parameter will bind process instances to the documents that needs to be approved (Fig. 2). Once the process is launched from the
 
 Documents
 
 section, the parameter will be populated with the corresponding document. To add a process parameter:
 


	1. Click the
	 
	 Add parameter
	 
	 button, and select “Lookup” in the drop down menu.
	2. In the
	 
	 Title
	 
	 field, enter "Document".
	3. In the
	 
	 Lookup
	 
	 field, select "Document".
	4. Save the changes.
	 
	
	
	
	
	
	 Fig. 2
	 
	
	 Approval business process properties
	 
	
	![chapter_process_creation_designer_set_process_parameter.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_process_creation_designer_set_process_parameter.png)
4. Add the
 
 Read data
 
 element from the
 
 User actions
 
 group to the process diagram. Enter the name of the element in the
 
 Read data
 
 field (e.g., “Read document data”). This element obtains the process parameters necessary to perform the next steps.
5. Set up the element properties (Fig. 3):
	1. In the
	 
	 Which data read mode to use?
	 
	 field, select “Read the first record in the selection”.
	2. In the
	 
	 Which object to read data from?
	 
	 field, select ”Document”. The business process will read the value in the
	 
	 Owner
	 
	 field of this object to send notifications about the approval status to the document owner.
	3. In the
	 
	 How to filter records?
	 
	 area, set the filter “Id = Document”. To do this, click <Add condition>, select the “Id” column, select the
	 
	 Compare with parameter
	 
	 value in the displayed menu, and choose the
	 
	 Document
	 
	 process parameter in the in the appeared window.
	4. The default settings in the
	 
	 How to sort records?
	 
	 area are configured for sorting in ascending order.
	 
	
	
	
	
	
	 Fig. 3
	 
	 The "Read document data" element properties
	 
	
	![chapter_process_creation_designer_read_the_document.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_process_creation_designer_read_the_document.png)
6. Add the
 
 Approval
 
 element from the
 
 User actions
 
 group to the process diagram (e.g., “Approve document”). The element will be activated once the process is launched for a record in the
 
 Documents
 
 section.
7. Set up the element properties (Fig. 4):
	1. In the
	 
	 Approval purpose
	 
	 field, select “Approval required”.
	2. In the
	 
	 Approval object
	 
	 field, select “Document”.
	 
	
	
	
	
	
	 Note.
	 
	 If you cannot find the
	 
	 Document
	 
	 object in the list, the approval procedure might be disabled for the
	 
	 Documents
	 
	 section in the section wizard. More information about the procedure for configuring approvals is available in the
	 [Approvals](/docs/7-18/user/platform_basics/communications/approvals_shortcut/approvals) 
	 article.
	3. In the
	 
	 Record Id
	 
	 field, click
	 ![btn_process_element_settings_lookup00025.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_process_element_settings_lookup00025.png)
	 and select the “Process parameter” option, then choose the “Document” process parameter in the appeared window.
	4. In the
	 
	 Approver
	 
	 field, select “Role”.
	5. In the
	 
	 Role
	 
	 field, select “Lookup value option” and choose the “Financial department” value from the the “Roles (view)” lookup. All employees in the
	 
	 Financial department
	 
	 role will be able to approve documents.
	6. Select the
	 
	 Approval may be delegated
	 
	 checkbox to be able to delegate an approval to a different employee.
	7. In the
	 
	 Send email notification
	 
	 field, configure automatic email notifications for the approvers and the document owner employee.
	 
	
	
		* Select the
		 
		 Notify that approval is required
		 
		 checkbox.
		* In the
		 
		 Email template
		 
		 field, click
		 ![btn_process_element_settings_lookup00026.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_process_element_settings_lookup00026.png)
		 and add an email template for a notification from the
		 
		 Email message template
		 
		 lookup.
		* Select the
		 
		 Notify about the approval result
		 
		 checkbox.
		* In the
		 
		 Recipient
		 
		 field, click the
		 ![btn_parametres_window00027.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_parametres_window00027.png)
		 button and select “Contact” in the menu, and choose the “Process parameter” option. Then, select the “Owner” parameter from the “Read document data” element in the appeared window. The owner of the document will receive an email notification about the approval.
		* In the
		 
		 Email template
		 
		 field, click
		 ![btn_process_element_settings_lookup00028.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_process_element_settings_lookup00028.png)
		 and add an email template for a notification from the
		 
		 Email message template
		 
		 lookup.
		 
		
		
		
		
		
		 Attention.
		 
		 Set up the mailbox for email notifications in the
		 
		 Mailbox for sending email with information on approval
		 
		 system setting. Access the system setting in the Process Designer by clicking the
		 ![btn_com_information00029.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_com_information00029.png)
		 button in the
		 
		 Send email notification
		 
		 area.
		 
		
		
		
		
		
		
		 Note.
		 
		 Create email templates in the content designer, using the
		 
		 Approvals in the Documents section
		 
		 object. The approval objects are created automatically, when you select the
		 
		 Enable approval in section
		 
		 checkbox in the section wizard. For example, if you select the
		 
		 Enable approval in section
		 
		 checkbox in the
		 
		 Documents
		 
		 section wizard, a new object “Approvals in section Document” will be created. If the lookup of the
		 
		 Enable approval in section
		 
		 does not contain the template you need, click
		 ![btn_com_add_tab00030.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_com_add_tab00030.png)
		 in the right part of the field to add a new email template. Learn more about creating an email template in the
		 [Create an email template](/docs/7-18/user/marketing_tools/email_marketing/email_templates/create_a_template/create_an_email_template) 
		 article.
		 
		
		
		
		
		
		
		 Fig. 4
		 
		
		 The
		 
		 Approval
		 
		 element parameters
		 
		
		![chapter_process_creation_designer_visa_settings.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_process_creation_designer_visa_settings.png)
8. Add two
 
 Modify data
 
 elements of the
 
 System actions
 
 group to the process diagram. The “Change document status to Draft” and “Change document status to Active” elements are used to change the document status based on the approval result. Set up the element properties (Fig. 5): The parameters of the two elements are identical, except for the resulting document status.
	1. In the
	 
	 Which object to read data from?
	 
	 , select “Document”. This will be set by default if approvals are enabled in the
	 
	 Documents
	 
	 section. In this case, it is the “Chart” component.
	2. In the
	 
	 How to filter records?
	 
	 area, set the filter “Id = Document”. To do this, click <Add condition>, select the “Id” column, select the
	 
	 Compare with parameter
	 
	 value in the displayed menu, and choose the
	 
	 Document
	 
	 process parameter in the in the appeared window.
	3. In the
	 
	 Which column values to set for modified records?
	 
	 area, select the resulting document status. If approved, the document status changes to “Active”. If not approved, the document status changes to “Draft”. To do this, click <Add field>, and select the “Status” column. In the
	 
	 Status
	 
	 field, click the
	 ![btn_process_element_settings_lookup00031.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_process_element_settings_lookup00031.png)
	 button, select “Lookup value”, and choose the following values: “Active” for the “Change document status to Active” element and “Draft” for the “Change document status to Draft” element.
	 
	
	
	
	
	
	 Fig. 5
	 
	
	 The “Change document status to Active” element parameters
	 
	
	![chapter_process_creation_designer_document_status_actual.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_process_creation_designer_document_status_actual.png)
9. Copy the previously created
 
 Read data
 
 element of the
 
 System actions
 
 group – “Read document data”  – and place it after the
 
 Change document status to Draft
 
 element on the diagram. This element determines the responsible individual for re-working the document.
10. Add the
 
 Perform task
 
 element from the
 
 User actions
 
 group to the process diagram (“Revise the document”). This element will create a task (activity) for the individual to edit the document if it was not approved.
11. Set up the element properties (Fig. 6):
	1. Enter the name of the task in the
	 
	 What should be done?
	 
	 field.
	2. Select the start time of the task in the
	 
	 Start in
	 
	 field, and the approximate duration of the task in the
	 
	 Planned duration
	 
	 field. The value of the
	 
	 Start in
	 
	 field determines a time period at the end of which the task will be scheduled. In the
	 
	 Planned duration
	 
	 field, specify the approximate duration of the task.
	3. Select the
	 
	 Show in calendar
	 
	 checkbox to display the task in the responsible individual’s calendar.
	4. In the
	 
	 Who performs the task?
	 
	 field, click
	 ![btn_process_element_settings_lookup00032.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_process_element_settings_lookup00032.png)
	 and select the “Process parameter” option. Then, select the “Owner” parameter from the “Read document data” element in the appeared window.
	5. In the
	 
	 Connected to
	 
	 field, connect the task to the document. To do this:
	 
	
	
		* Click the
		 ![btn_button_connections00033.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_button_connections00033.png)
		 button and add the “Document” column.
		* Click the
		 ![btn_process_element_settings_lookup00034.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_process_element_settings_lookup00034.png)
		 button and select the “Process parameter” option, and choose the “Document” process parameter in the appeared window.
		 
		
		
		
		
		
		 Fig. 6
		 
		
		 The "Revise the document" element properties
		 
		
		![chapter_process_creation_designer_document_finalization_task.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_process_creation_designer_document_finalization_task.png)
12. After creating the process elements, connect each element with the next one by using the arrows in the upper right corner of the selected element.
	1. Use conditional flows (
	 ![btn_com_mnu_add_flow_default.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_com_mnu_add_flow_default.png)
	 ) to connect the “Approve document” element to the “Change document status to Draft” and “Change document status to Active” elements.
	2. Click the conditional flow connecting the “Approve document” element and the “Change document status to Draft” element and select the “Negative ”approval result.
	3. Click the conditional flow connecting the “Approve document” element and the “Change document status to Active” element and select the “Positive ”approval result.
	4. Use sequence flows (
	 ![btn_com_mnu_add_flow.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_com_mnu_add_flow.png)
	 ) to connect all other elements.
13. Save the business process. Once saved, configure the start of a business process.




 Set up business process launch
---------------------------------



 The process is launched by clicking the
 
 Run process
 
 button on the record page or in the section list. The button is not displayed by default and requires additional setup (Fig. 7).
 



 To configure the button, connect the document approval process to records for which it will be launched. To do this:
 


1. Click the
 
 View
 
 button in the
 
 Contacts
 
 section and select the
 
 Open section wizard
 
 command.
2. Open the
 
 Business process
 
 tab. Click the
 ![btn_com_add_tab00035.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_com_add_tab00035.png)
 button on the
 
 Run business process from section
 
 detail. The window of the business process launch settings will be opened.
3. Select the “Document approval” process in the
 
 Which process to run?
 
 field.
4. To start the process for separate section records, select the “For selected record” radio button.
 



 The
 
 Process parameter where the record is passed
 
 field is populated automatically with the “Document” parameter of the “Document approval” process.
5. Save the changes in the window and the section wizard.
 





 Fig. 7
 

 Add a business process to a section
 

![chapter_process_creation_designer_run_process_for_selected_record_setup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_process_creation_designer_run_process_for_selected_record_setup.png)



 As a result, you will be able to launch the approval process for any record of the
 
 Documents
 
 section (Fig. 8).
 





 Fig. 8
 
 Launch the process from the
 
 Documents
 
 section list
 

![chapter_process_creation_designer_document_approvement_run_process_from_the_list.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_process_creation_designer_document_approvement_run_process_from_the_list.png)








 Set up custom email templates for approval notifications
---------------------------------------------------------------



 Use the
 [Approval](/docs/7-17/user/bpm_tools/process_elements_reference/user_actions/approval/approval_process_element)
 process element to set up custom logic for approving various Creatio records (documents, invoices, orders, etc.) by Creatio users. Both the approver and the user who submits the record for approval will receive email notifications about the approval procedure.
 



 You can set up custom email templates for these notifications. Note that approval notification emails do not require additional
 
 Send email
 
 elements, and are configured in the
 
 Approval
 
 process element.
 





 Example.
 
 During a document approval process (Fig. 42), the approver must receive an email notification, containing document type, number and the name of the user who submitted the document for approval. The user who submitted the document for approval, must receive a notification about the approval result.
 




 The instructions below assume that you have enabled approvals in the
 
 Documents
 
 section, added the
 
 Approval
 
 element on the process diagram (Fig. 9) and set up its properties. Read more about enabling approvals in the
 [Approval
 
 process element](/docs/7-17/user/bpm_tools/process_elements_reference/user_actions/approval/approval_process_element) 
 article. More information about the approval process setup is available in a separate
 [Configure a document approval process](#title-2782-14) 
 guide.
 





 Fig. 9
 
 A business process for approving documents
 

![chapter_process_creation_designer_document_approvement00036.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_process_creation_designer_document_approvement00036.png)



 To set up templates:
 


1. Populate the fields of the
 
 Approval
 
 element setup area. If the
 
 Approval section
 
 field is populated, available email templates for approval notification will be filtered according to the selected section.
 





 Note.
 
 More information about setting up the
 
 Approval
 
 element as part of an approval process is available in the
 [Configure a document approval process](#title-2782-14) 
 guide.
2. Select the
 
 Notify that approval is required
 
 checkbox. As a result, whenever a record is submitted for approval, a notification will be sent to the “approver” user. If “Role” is selected in the
 
 Approver
 
 field, the notification will be sent to all users with the corresponding role.
3. In the
 
 Email template
 
 field, click
 ![btn_com_add_tab00038.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_com_add_tab00038.png)
 (Fig. 10). A new email template window will open on a new tab.
 





 Fig. 10
 

 Opening the email template of an approval notification
 

![chapter_bpmn_approval_email_add_template.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_bpmn_approval_email_add_template.png)
4. In the new template window, populate the
 
 Template name
 
 field. Note that if you populated the
 
 Approval section
 
 field earlier, the
 
 Macro source
 
 field will be already populated with the corresponding approval object (in this case – the “Approvals in section Document” object, (Fig. 11).
 





 Fig. 11
 

 Approval notification template settings
 

![chapter_bpmn_approval_email_template_setup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_bpmn_approval_email_template_setup.png)
5. Click the
 
 Edit
 
 button. The template will open in the content designer.
 





 Note.
 
 Basic instructions on working with the content designer are available in the
 [“Create an email template”](https://academy.creatio.com/documents?product=studio&ver=7&id=1404) 
 article.
6. Enter the email subject.
7. Drag&drop a content block (e.g.,
 
 Text
 
 ) to the template. Replace the text in the
 
 Text
 
 block with your own.
8. Add regular email template macros:
 


	1. Place your cursor in the text block, click
	 ![btn_email_temlate_macro.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_email_temlate_macro.png)
	 and choose
	 
	 Basic macro
	 
	 (Fig. 12). The
	 
	 Macros selection
	 
	 window opens.
	 
	
	
	
	
	
	 Fig. 12
	 
	 Accessing the macros in the content designer
	 
	
	![chapter_bpmn_approval_email_add_macro.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_bpmn_approval_email_add_macro.png)
	
	
	
	
	
	 Note.
	 
	 For users of Creatio version 7.13.2 and below, the command names are different. The command for selecting standard macros is called
	 
	 Select macros
	 
	 , and the
	 
	 Select column
	 
	 command is used to create a custom macro.
	2. In the
	 
	 Macros selection
	 
	 window, choose the needed macro and click
	 
	 Select
	 
	 . The available macros are divided into several groups.
	 
	
	
	
	 You can specify data of the email recipient contact (“Recipient” group), information of the user who runs the approval process (“Current user” group) or the owner of the record being approved (“Owner” group). For example, to add the name of the user who submitted the document for approval, select
	 
	 Current user
	 
	 >
	 
	 Contact name
	 
	 macro (Fig. 13).
	 
	
	
	
	
	
	 Fig. 13
	 
	 Adding a macro to the email text
	 
	
	![chapter_bpmn_approval_email_select_macro.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_bpmn_approval_email_select_macro.png)
	
	
	
	 The corresponding macro will be added to the email text at the insertion point.
9. Add email template macros that are based on the “Macro source” object.
 


	1. Place your cursor in the text block, click
	 ![btn_email_temlate_macro00039.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_email_temlate_macro00039.png)
	 and choose
	 
	 Select column
	 
	 . The
	 
	 Select column
	 
	 window (Fig. 48) opens.
	2. In the
	 
	 Select column
	 
	 window, choose the column of the object (that you specified in the
	 
	 Macro source
	 
	 field) whose values must be added to the notification text. The “approval” object is automatically added once you enable approvals in the section wizard and contains data from the approval itself, e.g., Approval purpose, Approver’s name, etc.
	3. You can add macros for columns of any object, provided it is linked to the “approval” object, e.g., you can add columns of the document being approved. To select a column of a linked object, Click
	 
	 +
	 
	 next to the “approval” object name in the
	 
	 Select column
	 
	 window (Fig. 14). For example, to add the approved document’s type and number, add the
	 
	 Type
	 
	 and
	 
	 Number
	 
	 columns from the linked
	 
	 Document
	 
	 object.
	 
	
	
	
	
	
	 Fig. 14
	 
	
	 Selecting columns of a linked object as macros
	 
	
	![chapter_bpmn_howto_approval_email_object.gif](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_bpmn_howto_approval_email_object.gif)
	
	
	
	 As a result, your template will look like this (Fig. 15):
	 
	
	
	
	
	
	 Fig. 15
	 
	
	 Example of approval notification template
	 
	
	![chapter_bpmn_approval_email_template_result.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_bpmn_approval_email_template_result.png)
10. Save the changes in the content designer and the email template.
11. Select the
 
 Notify about the approval result
 
 checkbox and populate the
 
 Recipient
 
 field. You can specify any Creatio contact, account or an email address. For example, you can send approval result notifications to the user who submitted the record for approval, record owner, etc.
12. Repeat steps 3-10 to create an approval notification email template.
13. Save the process diagram.
 



 As a result, whenever a user submits a record for the approval using this process, email notifications will be sent according to the custom templates.




