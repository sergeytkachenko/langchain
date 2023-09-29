


 Send emails as part of a business process using the
 
 Send Email
 
 element (Fig. 1). The element can send emails automatically or open a new email page for the process user to send the email manually. It uses all common email integration features available in Creatio, such as macros, templates, and linking emails to section records.
 




 Fig. 1 The
 
 Send email
 
 element on the process diagram
 


![chapter_process_designer_email_element_on_diagram.png](/docs/sites/en/files/images/BPM_Tools/send_email/chapter_process_designer_email_element_on_diagram.png)






 Note.
 
[Email integration](https://academy.creatio.com/docs/user/setup_and_administration/base_integrations) 
 is required to work with emails in Creatio.
 




 The
 
 Send email
 
 element is a means of automating email communication without a programming background. For example, the element lets you:
 


* Move on to the next step in the business process while Creatio is sending emails to multiple recipients on your behalf automatically.
* Send important system messages, notifications, and updates automatically.
* Personalize emails with information available in other process parameters using macros.
* Assign email-related activities to other employees in your company automatically.



 To display the element title and user hint in the assignee's language, make sure the “Create business process tasks in the owner's language” (“UsePerformerCultureInUserTask” code) system setting is enabled and the
 
 Translation
 
 section includes the translation. Learn more:
 [Localize UI via the
 
 Translation
 
 section](/docs/8-0/user/customization_tools/custom_localization/translate_the_ui/localize_ui_via_the_%5Btranslation%5D_section) 
 .
 





 Note.
 
 If the assignee is a group whose members use different Creatio languages, the title and hint will use the default culture.
 




 Set up the main element properties
------------------------------------



 Creatio displays the following
 
 Send Email
 
 element properties regardless of how the email is sent (automatically or manually) and how the message text is generated (template message or custom message):
 





|  |  |
| --- | --- |
| 
**From** 
 | 
 An email account integrated with Creatio and used for sending emails. Fill out this parameter with the values from the
 
 Mailbox synchronization settings
 
 lookup. There are several ways to retrieve the parameter values:
 * Specify the email account directly by selecting it from the
 
 Mailbox synchronization settings
 
 lookup.
* Specify a system setting that uses the
 
 Mailbox synchronization settings
 
 lookup values. For example, “Mailbox for sending email with information on approval” (“VisaMailboxSettings” code).
* Map any other process parameter that uses the
 
 Mailbox synchronization settings
 
 lookup values. Learn more:
 [Process parameters](/docs/8-0/user/bpm_tools/business_process_setup/parameters/process_parameters) 
 .


 If the element sends the email automatically, the
 
 From
 
 parameter is required. If the process user sends the email, the parameter is optional. The user may select an email account from the list on the email edit page.
  |
| 
**To** 
 | 
 The recipient's email addresses. Click the
 
btn_button_preconfigured_new.png

 button to add carbon copy (Cc) and/or hidden copy (Bcc) recipients.
 

 You can populate the To/Cc/Bcc fields in several ways:
 * Enter the emails manually (e. g., john\_best\_business@yahoo.com). Click the
 
btn_button_preconfigured_new.png

 button and specify other addresses to add multiple recipients manually.
* Select accounts/contacts from a lookup.
* Select system settings, whose values are email addresses. For example, “1st-line support.”
* Select the account or contact email of the user who runs the process (“Current user account,” “Current user contact”).
* Retrieve the email from another process parameter. You can map any parameter of the “text” type. Note that the value of the mapped parameter must still be a valid email address, otherwise the element will not execute properly. Learn more:
 [Process parameters](/docs/8-0/user/bpm_tools/business_process_setup/parameters/process_parameters) 
 .


 If you select either a contact or an account, Creatio will pull the email from the
 
 Communication options
 
 detail. If there are multiple emails specified for an account/contact, Creatio will use the most recent email added to the detail.
  |
| 
**What is the message?** 
 | 
 Select “Custom message” to create a unique email for the business process in the
 [Content Designer](/docs/8-0/user/marketing_tools/email_marketing/email_templates/create_a_template/create_an_email_template) 
 .
 

 Select “Template message” to use one of the templates from the
 
 Email templates
 
 lookup.
  |
| 
**How is the message sent?** 
 | 
 If you select “Send email manually,” the email edit page will open (or the email activity will be created) for the process user once the
 
 Send Email
 
 element is activated on the process diagram.
 

 If you select “Send email automatically,” Creatio will send the email automatically from the mailbox specified in the
 
 From
 
 field once the
 
 Send Email
 
 element is activated on the process diagram.
  |
| 
**Subject** 
 | 
 Enter the email subject. You can populate the field in several ways:
 * Enter the subject manually.
* Map a process parameter of the “text” type. Learn more:
 [Process parameters](/docs/8-0/user/bpm_tools/business_process_setup/parameters/process_parameters) 
 .
* Select a system setting of the “text” type.
* Use a formula to create a personalized subject, e. g., “Hi, John Best!,” where the name “John Best” is received from the previous process element. Learn more:
 [Process formulas](/docs/8-0/user/bpm_tools/business_process_setup/formulas/process_formulas) 
 .


 The subject text is also displayed on the
 
 Business process tasks
 
 tab of the communication panel. If you select a template, Creatio will populate the
 
 Subject
 
 field with the subject specified in the template.
  |




 Set up a custom message
-------------------------



 If you select “
 **Custom message** 
 ” in the
 
 What is the message?
 
 field, the following properties will become available:
 





|  |  |
| --- | --- |
| 
**Email body** 
 | 
 The area below the
 
 Subject
 
 field displays an email body preview. Hover over this area and click
 
create_or_edit_mail_text.png

 to open the
 [Content Designer](/docs/8-0/user/marketing_tools/email_marketing/email_templates/create_a_template/create_an_email_template) 
 to create a custom message.
  |




 Template message properties
-----------------------------



 If you select “
 **Template message** 
 ” in the
 
 What is the message?
 
 field, the following properties will become available:
 





|  |  |
| --- | --- |
| 
**Template message** 
 | 
 Select a template from the
 
 Email templates
 
 lookup. Click the
 
btn_chapter_designer_user_task_designer_task.png

 button to open the selected template in the
 [Content Designer](/docs/8-0/user/marketing_tools/email_marketing/email_templates/create_a_template/create_an_email_template) 
 . You can send localized emails using multilingual templates. If you specify contacts with different languages or contacts without the preferred language in the
 
 To
 
 field, Creatio will send the template in the default language to all recipients. Learn more:
 [Work with message templates](/docs/7-17/user/platform_basics/communications/message_templates/work_with_message_templates#title-2050-10) 
 .
  |
| 
**Record for macros** 
 | 
 The record to use as a source for email template macros. For example, if the template contains macros like
 
 #Contact.Name#
 
 and
 
 #Contact.Mobile phone#
 
 , the actual name and phone number in the email will correspond to the contact specified in the
 
 Record for macros
 
 field. Learn more:
 [Process parameters](/docs/8-0/user/bpm_tools/business_process_setup/parameters/process_parameters) 
 .
 

 This field is linked to the
 
 Macro source
 
 field in the selected email template record. For example, if you specify “Contact” in the
 
 Macro source
 
 field, the value in the
 
 Record for macros
 
 field will be a specific contact record.
 

 You can retrieve a macro source record in several ways:
 * Map a process parameter. The parameter must have a “Lookup” type, and the lookup itself must correspond to the object selected in the
 
 Macro source
 
 field in the email template.
* Select a record from a lookup.
* Select a system setting of a “Lookup” type, whose lookup corresponds to the one selected in the
 
 Macro source
 
 field in the email template. For example, “Test email recipient.” Select “Current user contact” to generate macros based on the data of the user who runs the process.
 |






 Note.
 
 Use the
 
 Formula
 
 process element or the “Formula” option of the parameter value menu to generate dynamic text for email subject and body. Learn more:
 [Process formulas](/docs/8-0/user/bpm_tools/business_process_setup/formulas/process_formulas) 
 . Switch the
 
 Send email
 
 element setup area to the “advanced mode” to populate the email body using a formula.
 




 Send the email automatically
------------------------------



 If you select “
 **Send email automatically** 
 ” in the
 
 How is the message sent?
 
 field, the following properties will become available:
 





|  |  |
| --- | --- |
| 
**Importance** 
 | 
 Creatio populates the
 
 Priority
 
 field of the corresponding email activity with the value of this property.
  |
| 
**Ignore errors on sending** 
 | 
 If this checkbox is selected, the process will progress further even if sending errors occur. If the checkbox is not selected, and errors occur, the
 
 Send email
 
 element will end with an error and will not activate its outgoing flows. You can view any process-related errors in the
 
 Process log
 
 section.
  |
| 
**Run following elements in the background** 
 | 
 If the checkbox is selected, the process will run the element in the background without displaying the loading mask.
  |
| **Create an activity**  | 
 If the checkbox is selected, the process will create a corresponding activity when executing this process step. Selecting the checkbox will make the
 
 Email connections
 
 field group available.
  |
| **Email connections**  | 
 Connect the task to other Creatio entities. For example, an account. Creatio will display the task on the
 
 Activities
 
 detail of the connected record. By default, the element setup area displays account and contact connections. Click the
 btn_button_connections.png
 button to connect the task to other Creatio entities.
  |




 Set up the manual sending
---------------------------



 If you select “Send email manually” in the
 
 How is the message sent?
 
 field, the following properties will become available:
 





|  |  |
| --- | --- |
| 
**Who performs the task?** 
 | 
 Select one of the options and fill out the field that opens:
 * “User” – specify the user who will see the email edit page in the
 
 Contact
 
 field.
* “Employee’s manager” – specify the user whose manager will see the email edit page in the
 
 Contact
 
 field.
* “Role” – specify the role the users with which will see the email edit page in the
 
 Role
 
 field.


 You can specify a dynamic parameter value or select a constant in the parameter value box.
 

 Once the process reaches the
 
 Send Email
 
 element, the email edit page will open for the user or role if the
 
 Show page automatically
 
 checkbox is selected. If not, the email task will be displayed on the user or role's communication panel.
  |
| 
**User hints** 
 | 
 A text hint for the user who performs this process task. The user can view the hint by clicking the
 
btn_com_information.png

 button on the email page.
  |
| 
**Show page automatically** 
 | 
 If this checkbox is selected, the email edit page will open for the user selected in the
 
 Who is the sender?
 
 property once the process reaches the
 
 Send Email
 
 element.
 

 Note that if the
 
 Run following elements in the background
 
 checkbox is selected for a preceding element, the edit page will not open once the process reaches the
 
 Send email element
 
 , even if the
 
 Show page automatically
 
 checkbox is selected.
  |
| 
**Run following elements in the background** 
 | 
 If this checkbox is selected, all process elements connected to the outgoing flows will run in the background without displaying the loading mask or opening the corresponding pages.
  |
| 
**Email connections** 
 | 
 Use this property to connect the email to other Creatio records. Creatio will display the connected records in the
 
 Connected to
 
 block of the email page and in the form of links on the
 
 Email
 
 tab of the communication panel. Click the
 
btn_button_preconfigured_new.png

 button to add different record types.
  |





 Note.
 
 If you choose to send emails manually, all due email tasks (drafts) will be displayed on your communication panel.
 





 Set up the email attachments
------------------------------



 Add and set up the
 [Process file](/docs/8-0/user/bpm_tools/process_elements_reference/system_actions/process_file/process_file_element)
 element before setting up attachments in the
 
 Send email
 
 element. The
 
 Process file
 
 element will allow you to map a file collection to the
 
 Send email
 
 element.
 





|  |  |
| --- | --- |
| 
**Add attachments** 
 | 
 Click
 
btn_button_preconfigured_new.png

 in the
 
 Add attachments
 
 block of the
 
 Send email
 
 element setup area to attach files to the email.
 

 In the field that appears, click
 
btn_process_element_settings_lookup.png

 → “Process parameter.” In the parameter window, map the element to the needed file collection. Click
 
 Select
 
 .
 

 As a result, Creatio will send the file collection as an email attachment during the
 
 Send email
 
 element execution.
  |




 Retrieve the outgoing element parameters
------------------------------------------





|  |  |
| --- | --- |
| 

btn_iD.png


 Task Id
  | 
 The Id of the email sending activity created during the element execution. Type: “Id.” In Creatio, all manually created emails and drafts are considered activities and have a unique identifier in the database. Learn more:
 [Work with data in a business process](/docs/8-0/user/bpm_tools/process_element_use_cases/data/how_to_work_with_data) 
 .
  |
| 

btn_text.png


 Recommendation
  | 
 Retrieve the value of this parameter from the
 
 Hint for user
 
 field, available only for manual emails. Type: “Text.”
  |
| 

btn_boolean.png


 Ignore email errors
  | 
 Retrieve the value of this parameter from the
 
 Ignore errors on sending
 
 setting, available only for automatic emails. Type: “Boolean.”
  |




 Element activation
--------------------



 If the email
 **is sent manually** 
 :
 


* Creatio will open a new email window for the process user if the
 
 Show page automatically
 
 checkbox is selected, and the element does not run in the background. The draft will use all properties specified in the
 
 Send Email
 
 element. For example, the email template, the mailbox, etc.
* Creatio will display the email task on the communication panel for the process user if the
 
 Show page automatically
 
 checkbox is cleared in the element properties.



 If the email is
 **sent automatically** 
 , Creatio will generate a message based on the
 
 Send Email
 
 element properties. For example, the email template, the mailbox, etc. The email will be sent automatically from the address specified in the
 
 From
 
 field on the email page.
 



 Element completion
--------------------



 The completion of the
 
 Send email
 
 element depends on how the message is sent.
 



 If the email is
 **sent manually** 
 , the element will be deemed complete as soon as the user sends the email.
 



 If the email is
 **sent automatically** 
 , the element does not require any user actions and will be deemed complete as soon as the email is sent.
 



 If any errors occur while sending, the element completion will be determined by the
 
 Ignore errors on sending
 
 checkbox:
 


* If the
 
 Ignore errors on sending
 
 checkbox is selected, the element is deemed complete as soon as the first sending attempt is made, regardless of its result. For example, if the email server returns a sending error, the element will still be completed successfully and activate its outgoing flows.
* If the
 
 Ignore errors on sending
 
 checkbox is cleared, the element will be deemed complete only if the email is sent successfully. If any errors occur while sending, the process will not progress to the next step. You can view any process-related errors in the
 
 Process log
 
 section.



 Upon completion, the element will update the values of its parameters according to changes the user made on the email page and activate its outgoing flows.
 




