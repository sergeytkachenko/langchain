


 The
 
 Approval
 
 case element (
 ![chapter_case_designer_icon_visa.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_icon_visa.png)
 ) is used for creating approvals, as well as for setting up approval-related notifications.
 



 Specify the approval parameters in the element’s setup area (Fig. 1).
 




 Fig. 1 The
 
 Approval
 
 element properties
 

![chapter_case_designer_approving.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_approving.png)



 Set up an object to approve
-----------------------------



 Fill out the following fields:
 


1. Approval purpose
 
 – default purpose is “Approval required.” The approval purpose is displayed on the
 
 Approvals
 
 detail of the record being approved. To display the title in the assignee's language, make sure the “Create business process tasks in the owner's language” (“UsePerformerCultureInUserTask” code) system setting is enabled and the
 
 Translation
 
 section includes the translation. Learn more:
 [Localize UI via the
 
 Translation
 
 section](/docs/7-18/user/customization_tools/custom_localization/translate_the_ui/localize_ui_via_the_%5Btranslation%5D_section) 
 .
 





 Note.
 
 If the assignee is a group whose members use different Creatio languages, the title will use the default culture.
2. Approval section
 
 – the records of this section will be submitted for approval.
 


 Note.
 
 The dropdown list contains sections where approval is enabled. Learn more:
 [Work with approvals](/docs/7-18/user/platform_basics/communications/approvals_shortcut/approvals) 
 .
3. Record Id
 
 – the record approved. This is a required field.



 Set up the approver
---------------------



 Fill out the following fields:
 


1. Approver
 
 – select one of the options and fill out a field that opens:
	* “User” – specify the approver in the
	 
	 Employee
	 
	 field.
	* “Employee’s manager” – specify the employee whose manager will be assigned as the approver in the
	 
	 Employee
	 
	 field. Creatio will submit the approval to the contact specified in the
	 
	 Manager
	 
	 profile on the employee page.
	 
	
	
	
	
	
	 Note.
	 
	 If the employee’s manager cannot be found, the approval will still be created, but the
	 
	 Approver
	 
	 field in it will be empty. In this case, a system administrator user can use the
	 
	 Change approver
	 
	 command in the actions menu of the
	 
	 Approvals
	 
	 detail to assign an approver.
	* “Roles” – specify the role the users with which can approve the record in the
	 
	 Role
	 
	 field.
2. Approval may be delegated
 
 – select the checkbox to allow the approver to forward the approval to another employee.



 Set up the approval notifications
-----------------------------------



 Set up sending of email notifications for the employee who created the approval and the approver in the
 
 Send email notification
 
 area.
 





 Attention.
 
 Set up the mailbox for email notifications in the
 
 Mailbox for sending email with information on approval
 
 system setting. Access the system setting in the Process Designer by clicking the
 ![btn_com_information00012.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/btn_com_information00012.png)
 button in the
 
 Send email notification
 
 area.
 






 Note.
 
 Create email templates in the content designer, for the corresponding object. For example, to set up a notifications for document approvals, create a template using the
 
 Approvals in section Document
 
 object. The approval objects are created automatically when you select the
 
 Enable approval in section
 
 checkbox in the section wizard. If the lookup of the
 
 Enable approval in section
 
 does not contain the template you need, click
 ![btn_com_add_tab.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/btn_com_add_tab.png)
 in the right part of the field to add a new email template. Learn more:
 [Create an email template](/docs/7-18/user/marketing_tools/email_marketing/email_templates/create_a_template/create_an_email_template) 
 .
 



1. Select the
 
 Notify that approval is required
 
 checkbox to notify the approver. As a result, the approver user will be notified whenever a record is submitted for approval. If you select “Role” in the
 
 Approver
 
 field, all members of the corresponding role will receive a notification.
2. Email template
 
 – select a notification email template from the
 
 Email templates
 
 lookup.
3. Select the
 
 Notify about the approval result
 
 checkbox to notify the employee about the result of the approval.
4. Recipient
 
 – specify who will receive the email notification: an email address, a contact, or an account. You can enter the value in the
 
 Recipient
 
 field directly or map it using the parameter value menu. For example, map the recipient to the
 
 Owner
 
 field of the record submitted for approval.
5. Email template
 
 – select a notification email template from the
 
 Email templates
 
 lookup.
6. Ignore errors on sending
 
 – select the checkbox to continue the case regardless of notification sending errors. Otherwise the case will end with an error should a sending error occur.
7. When is the step performed?
 
 – indicates whether to activate element at the start of the stage or after a case step. By default, the step is performed at the start of the stage. Select “After the previous step is complete” if the
 
 Approval
 
 element must start after the previous step in the case stage. Specify the step in the
 
 Perform after step
 
 field.
 





 Note.
 
 Users can advance to the final “unsuccessful” stage from any stage without completing the required steps.
8. Step type
 
 – specify if the step is required. Select “Required step” if the task must be completed to transition to the next stage. If the approval is not required to perform to transition to the next stage, select “Optional step.”
9. Change stage after element is completed
 
 – click
 
 Add condition
 
 and set up transitions based on the approval results.
10. Select one of the available approval results in the
 
 If result
 
 column and specify the next stage in the
 
 Set stage to
 
 the column.



 What happens when the [Approval] element is activated
-------------------------------------------------------


* A new approval record is created. All approval information, such as the approver, approval result, comments, etc. is displayed on the
 
 Approvals
 
 tab of the record that was submitted for approval. Learn more about the
 
 Approvals
 
 tab:
 [Work with approvals](/docs/7-18/user/platform_basics/communications/approvals_shortcut/approvals) 
 .
* The first email notification is sent to the approver user or role when the approval record is created.
* After the approver approves or denies the approval, another email notification is sent to the employee specified in the
 
 Recipient
 
 field under the
 
 Notify about the approval result
 
 checkbox.




