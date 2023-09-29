


 You can send emails during process execution. Depending on the setup, you can do it in the following ways:
 


* Send emails manually
 . The user will see a new email page that has pre-populated fields upon reaching this step of the process.
* Send emails
 automatically.



 Use the
 [Send email
 
 element](https://academy.creatio.com/documents?id=7127) 
 to send emails both manually and automatically in your business processes.
 





 Note.
 
 Be sure to set up
 [email server integration](https://academy.creatio.com/docs/user/setup_and_administration/base_integrations) 
 to enable sending emails.
 




 Send emails manually
----------------------



 Use manual email sending if you need to make changes (additions) to the email body or add attachments to it. Let's take a look at
 **sending emails manually** 
 as part of a meeting process workflow (Fig. 1).
 




 Fig. 1 Meeting process
 

![scr_process_creation_designer_process_email_with_data.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/scr_process_creation_designer_process_email_with_data.png)





 Example.
 
 The customer must receive meeting minutes after the meeting. The process must open a new email page automatically where the user must enter minutes or attach them manually before sending the email.
 



1. Drag the
 
 Send email
 
 element of the
 
 User actions
 
 group to the business process diagram. Specify the parameter values on the
 
 Send email
 
 element setup area (Fig. 2):
 

 Fig. 2
 
 Send email
 
 element setup area
 

![scr_process_creation_designer_send_email_manual.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/scr_process_creation_designer_send_email_manual.png)


	1. Select
	 
	 Lookup value
	 
	 in the
	 
	 From
	 
	 field to send the email from a corporate mailbox. Select the corporate mailbox account in the window that opens. If you leave the
	 
	 From
	 
	 field empty, the user who runs the process has to specify the sender email address in the
	 
	 From
	 
	 field on the edit page of the email.
	2. Specify the recipient's email address in the
	 
	 To
	 
	 field. Select
	 
	 Contact
	 
	 →
	 
	 Process parameter
	 
	 in the parameter value menu. Specify the recipient's email address in the
	 
	 To
	 
	 field. Select
	 
	 Process parameter
	 
	 in the
	 
	 Contact
	 
	 menu. Select the
	 
	 Conduct meeting
	 
	 element and its parameter –
	 
	 Account
	 
	 (Fig. 3).
	 
	
	 Fig. 3 Select the recipient’s email address
	 
	
	![chapter_process_creation_designer_choose_email_address.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_creation_designer_choose_email_address.png)
	3. If you need to send the meeting minutes to several contacts, click the
	 ![btn_button_connections.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_emails/btn_button_connections.png)
	 button and add the
	 
	 Cc
	 
	 and
	 
	 Bcc
	 
	 fields. Specify the necessary recipients in the fields.
	4. Select “Custom message” in the
	 
	 What is the message?
	 
	 field.
2. Enter the email content.
 


	1. Click the
	 ![create_or_edit_mail.text.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_emails/create_or_edit_mail.text.png)
	 button in the email body area.
	2. Create your email in the Content Designer.
	3. Save the changes.
	4. Enter “Meeting minutes” in the
	 
	 Subject
	 
	 field.
	5. Select “Send email manually” in the
	 
	 How is the message sent?
	 
	 field.
	6. Select “Current user contact” in the
	 
	 Who is the sender?
	 
	 field to open the email edit page for the person responsible for the task.
	7. Select the
	 
	 Show page automatically
	 
	 checkbox so the page appears for the responsible individual once they reach this part of the process. If the checkbox is cleared, the email is saved as a draft and not sent.
	8. Specify the account from the “Conduct meeting" activity in the
	 
	 Account
	 
	 field. Click the field and select
	 
	 Process parameter
	 
	 in the parameter value menu. Select the
	 
	 Conduct meeting
	 
	 element and its
	 
	 Account
	 
	 parameter. The sent email will be displayed on the
	 
	 History
	 
	 tab of the customer's account record.
	 
	
	
	
	 As a result, a new email page will open where you can enter needed changes and add the meeting minutes (Fig. 4).
	 
	
	
	
	
	
	 Note.
	 
	 If you enabled automatic email signatures, a signature will be added to the email body.
	 
	
	
	
	
	
	 Fig. 4 Edit an email
	 
	
	![scr_process_creation_designer_send_protocol.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/scr_process_creation_designer_send_protocol.png)



 Send emails automatically
---------------------------



 While configuring a process that contains the
 
 Send Email
 
 element, you can choose to send emails automatically whenever a record is added, modified or deleted in Creatio. For example, each time a new contact is created, Creatio can send a “welcome email” to that contact (Fig. 5).
 




 Fig. 5 “Welcome email” business process diagram
 

![chapter_process_designer_email_element_paramaters_in_email_body_process00002.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_email_element_paramaters_in_email_body_process00002.png)



 Use
 [Signal
 
 start event](https://academy.creatio.com/documents?id=7027) 
 to run business processes automatically, upon changes in Creatio records. Use the
 [Send email](https://academy.creatio.com/documents?id=7127)
 element to send an email as part of a business process. If the email text must contain data from specific Creatio records, such as the data of the added contact, use the
 [Read data](https://academy.creatio.com/documents?id=7023)
 element to retrieve that data in the process.
 



 To send emails on cue:
 


1. Add the start event to the process diagram:
 


	1. Use the
	 [Start timer
	 
	 event](https://academy.creatio.com/documents?id=7133) 
	 to trigger the email sending either once at a specified time, or regularly with a specified frequency.
	2. Use the
	 [Signal
	 
	 start event](https://academy.creatio.com/documents?id=7027) 
	 to trigger the sending process on certain changes in Creatio, such as adding a contact (Fig. 6).
	 
	
	
	
	
	 Fig. 6 Start event properties
	 
	
	![chapter_process_designer_signal_event_parameters.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_signal_event_parameters.png)
	
	
	
	 In this case, the
	 
	 Signal
	 
	 start event is used to trigger the process once a contact is added to Creatio.
2. Add the
 
 Send Email
 
 element to the process diagram and fill out its fields (Fig. 7).
 




 Fig. 7 Set up the
 
 Send Email
 
 element properties
 

![chapter_process_designer_send_email_parameters.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_send_email_parameters.png)



 In this case, you can map the
 
 To
 
 field to the
 
 Id of created record
 
 parameter of the
 
 Signal
 
 start event, and send emails to the newly created contacts. To do this, hold the pointer over the
 
 To
 
 field and click
 ![btn_process_element_settings_lookup.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_emails/btn_process_element_settings_lookup.png)
 , then select
 
 Contact
 
 →
 
 Process parameter
 
 . In the menu that appears, select
 
 Process parameter
 
 . In the window that appears, select the “Unique identifier of record” parameter of the
 
 Signal
 
 start event (Fig. 8).
 




 Fig. 8 Map the
 
 To
 
 field to the ID of a contact record that triggered the
 
 Signal
 
 start event
 

![chapter_process_designer_send_selecting_id_of_signal.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_send_selecting_id_of_signal.png)
3. Select one of the following options depending on the desired outcome:
 


	1. If you choose to send a message that
	 **uses** 
	[process parameters](https://academy.creatio.com/documents?id=7054) 
	 or
	 [macros](https://academy.creatio.com/documents?id=1502) 
	 , add the element that can get these values from the Creatio database.
	2. If you choose to send an email that
	 **does not** 
	 use macros or other process parameters, simply connect the
	 
	 Signal
	 
	 element to the
	 
	 Send Email
	 
	 element.
	 
	
	
	
	 For example, if you need the name and email address of the newly added contact, place the
	 
	 Read Data
	 
	 element (Fig. 9) on the diagram and
	 [read the data of the contact](https://academy.creatio.com/documents?id=7023) 
	 who triggered the process. The data will be recorded into the element’s outgoing parameters, which you can then use as macros in the email body.
	 
	
	
	
	
	 Fig. 9 Set up the
	 
	 Read Data
	 
	 element properties
	 
	
	![chapter_process_designer_read_data_parameters.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_read_data_parameters.png)
4. Save the process diagram.
 



 As a result, the email will be sent upon certain changes / user actions in Creatio. In this case, all newly added contacts will receive a welcome email.
5. Use process parameters in the email body
------------------------------------------



 While setting up the
 [Send Email
 
 element](https://academy.creatio.com/documents?id=7127) 
 , you can use process parameters to personalize custom emails. This lets you include specific information in the email body, such as the first name or the phone number of a contact created as part of the process workflow (Fig. 10).
 




 Fig. 10 First name and phone number parameters used in the email body
 

![chapter_process_designer_email_element_paramaters_in_email_body_template_macros.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_email_element_paramaters_in_email_body_template_macros.png)



 Parameters are displayed in the email body as macros, i. e., codes that gets replaced with information specific to each recipient. For example, the
 
 #Read Data.First item of resulting collection.Full name#
 
 macro (Fig. 10) represents the
 
 Full name
 
[parameter](https://academy.creatio.com/documents?id=7054) 
 of the
 
 Read contact data
 
 element (Fig. 11). In the actual email this macro will be replaced with the first name of the contact created as part of the process workflow. Learn more about macros:
 [Personalize email content with macros](https://academy.creatio.com/documents?id=1502) 
 .
 





 Note.
 
 In the
 
 Send Email
 
 element, process parameters can only be used if “Custom message” is selected in the
 
 What is the message?
 
 field, i. e., you cannot use them in email templates created outside of the
 
 Send Email
 
 element.
 




 Any process parameter of the text, date/time, integer, and boolean types can be used to form macros in a custom message. This lets you use virtually any process parameter in the email body. For example, you can create a welcome email (Fig. 11) for all new contacts added to Creatio, and get their full name and business phone as macros in the email body.
 




 Fig. 11 Business process diagram
 

![chapter_process_designer_email_element_paramaters_in_email_body_process.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_email_element_paramaters_in_email_body_process.png)



 To add process parameters to a custom message:
6. Add the elements whose parameters you are going to need to the process diagram. To get the field values of existing records, use the
 [Read Data
 
 element](https://academy.creatio.com/documents?id=7023) 
 .
 



 To get the name and the business phone of the created contact, use the
 
 Signal
 
 start event together with the
 
 Read Data
 
 element.
7. Add the
 
 Send email
 
 element and fill out its
 
 From
 
 and
 
 To
 
 parameters.
8. Select “Custom message” in the
 
 What is the message?
 
 field of the
 
 Send Email
 
 element.
9. Hold the pointer over the area under the
 
 Subject
 
 field and click
 ![create_or_edit_mail.text00001.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_emails/create_or_edit_mail.text00001.png)
 to open the
 [Content Designer](https://academy.creatio.com/documents?id=1267) 
 .
10. Add the necessary blocks to the custom message. For example, add a “Text” block.
11. Click anywhere in the working area of the Content Designer, and click the
 ![icn_content_designer_parameter.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_emails/icn_content_designer_parameter.png)
 button on the toolbar. (Fig. 12):
 




 Fig. 12 Opening the parameter selection window in the Content Designer
 

![Email elements parameters in email body](/docs/sites/en/files/2020-11/chapter_process_designer_email_element_paramaters_in_email_body_content_designer.GIF)
12. Select the necessary parameter in the selection window. In this case, add the “First name” and the “Business phone” (Fig. 13) parameters of the
 
 Read Data
 
 element to add their values to the email template body. The parameter will be placed at insertion point.
 




 Fig. 13 Select a parameter to use as an email text macro
 

![chapter_process_designer_email_element_paramaters_in_email_body_template_selecting_param.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_email_element_paramaters_in_email_body_template_selecting_param.png)
13. Save the changes in the Content Designer.
14. Fill out other fields in the
 
 Send Email
 
 element and save the process.
 



 As a result, the process will send emails whose text will contain values of the corresponding parameters. In this case, contact first name and the business phone will be dynamically received from all created contacts in Creatio.



 Use email templates in business processes
-------------------------------------------



 Creatio lets you send emails based on the templates from the
 
 Email templates
 
 lookup as part of a business process flow. In Creatio, email templates are created using the
 [Content Designer](https://academy.creatio.com/documents?id=1267) 
 . When designing a business process, you can select templates in the
 [Send Email
 
 element](https://academy.creatio.com/documents?id=7127) 
 . For example, you can send a “Welcome on board” email template to all new employees at your company (Fig. 14).
 




 Fig. 14 “Welcome on board” process
 

![chapter_process_designer_email_element_template_process.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_email_element_template_process.png)





 Note.
 
 Objects and their connected objects are used to populate macros in email templates. If you are looking to use available
 [process parameters](https://academy.creatio.com/documents?id=7054) 
 in the email body, use a custom message option in the
 
 What is the message?
 
 field. Learn more:
 [Send email
 
 process element](https://academy.creatio.com/documents?id=7127) 
 .
 




 To send a template-based email as part of a business process:
 


1. Add the
 
 Send Email
 
 element to the process diagram and fill out its fields (Fig. 15).
 




 Fig. 15 Set up the
 
 Send Email
 
 element properties
 

![chapter_process_designer_email_template_send_email_element_properties.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_email_template_send_email_element_properties.png)
2. Fill out the
 
 To
 
 field. In this case, you can map the
 
 To
 
 field to a parameter that stores the ID of the added employee record, which you can retrieve from the
 
 Signal
 
 start event (Fig. 16).
 




 Fig. 16 Properties of the
 
 Signal
 
 start event
 

![chapter_process_designer_email_template_signal_start_event_properties.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_email_template_signal_start_event_properties.png)



 To do this, hold the pointer over the
 
 To
 
 field and click
 ![btn_process_element_settings_lookup00003.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_emails/btn_process_element_settings_lookup00003.png)
 , then select
 
 Contact
 
 →
 
 Process parameter
 
 . In the menu that appears, select
 
 Process parameter
 
 . In the window that appears, select the “Unique identifier of record” parameter of the
 
 Signal
 
 start event (Fig. 17).
 




 Fig. 17 Select the ID of the employee record
 

![chapter_process_designer_email_template_selecting_Id.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_email_template_selecting_Id.png)
3. Select “Template message” in the
 
 What is the message?
 
 field.
4. Select a pre-configured template in
 
 Template message
 
 field. In this case, select a “Welcome on board” template.
5. Specify the record whose field values will be used as macros in the selected template in the
 
 Record for macros
 
 field. The type of record depends on the object specified in the
 
 Macro source
 
 field on the email template edit page (Fig. 18).
 




 Fig. 18
 
 Macro source
 
 field on the email template edit page
 

![inset_000004.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/inset_000004.png)



 In this case, since the template uses the “Employee” object, specify the ID of the employee record similarly to the
 
 To
 
 field.
6. Save the process diagram.
 



 As a result, an email template will be sent as part of a business process. In this case, a “Welcome on board” email will be sent to all new employees after they are added in Creatio.



 Specify recipients or senders in the
 
 Send email
 
 element
---------------------------------------------------------------



 In the
 [Send Email
 
 element](https://academy.creatio.com/documents?id=7127) 
 , the values of the
 
 From
 
 and
 
 To
 
 fields are specified similarly to any other element or
 [process parameter](https://academy.creatio.com/documents?id=7054) 
 . You can select any available value or process parameter by clicking
 ![btn_process_element_settings_lookup00005.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_emails/btn_process_element_settings_lookup00005.png)
 in these fields. However, there are certain specifics when it comes to selecting senders and recipients or using process parameters as values of these fields.
 


### 
 Select the email sender



 The value of the
 
 From
 
 field is a mailbox. You can select any of the mailboxes synchronized with your Creatio application, i. e., any mailbox registered in Creatio with login and password data. For example, you can set up a separate mailbox that sends notifications as part of a business process, then select it in the
 
 From
 
 field (Fig. 19).
 




 Fig. 19 Selecting a mailbox
 

![chapter_process_designer_selecting_system_setting_values.gif](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_selecting_system_setting_values.gif)





 Note.
 
[Email integration](https://academy.creatio.com/docs/user/setup_and_administration/base_integrations) 
 is required to work with emails in Creatio. Make sure that all users who start the process have access to the mailbox specified in the
 
 From
 
 field. Learn more:
 [Share records](http://academy.creatio.com/documents/?id=1014) 
 .
 




 Additionally, you can map any process parameter whose value is selected from the
 
 Mailbox synchronization settings
 
 lookup to the
 
 From
 
 field. Learn more:
 [Use process parameters](https://academy.creatio.com/documents?id=7154) 
 .
 


### 
 Select email recipients



 You can specify the email recipients in the
 
 To
 
 field using the following methods:
 


* **Enter the email manually** 
 . For example, “johnbest@gmail.com.” Note that you cannot specify several addresses in one field this way. To add another recipient, click + and enter the new address in the new field.
* **Map another parameter** 
 of the lookup type that uses
 
 Account
 
 or
 
 Contact
 
 lookup. To do this, click
 ![btn_process_element_settings_lookup00006.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_emails/btn_process_element_settings_lookup00006.png)
 in the
 
 To
 
 field and select
 
 Contact
 
 /
 
 Account
 
 →
 
 Process parameter
 
 . For example, you can select a “Contact” parameter from a preceding
 
 Activity
 
 process element (Fig. 20). The email of this contact will be pulled from its
 
 Communication options
 
 detail.
 




 Fig. 20 Selecting a contact from the
 
 Activity
 
 process element
 

![chapter_process_designer_selecting_contact_as_parameter.gif](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_selecting_contact_as_parameter.gif)
* **Select a specific account or contact** 
 . To do this, click
 ![btn_process_element_settings_lookup00007.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_emails/btn_process_element_settings_lookup00007.png)
 in the
 
 To
 
 field and select
 
 Contact
 
 /
 
 Account
 
 → “Lookup value,” then select the needed account or contact from the list.
* **Map a text parameter that contains an email address** 
 . For example, you can select a manually created “Email” text parameter from the
 [Auto-generated page
 
 process element](https://academy.creatio.com/documents?id=7007) 
 (Fig. 21). In this case, the parameter is filled out by a user once the auto-generated page opens, and can be used in the
 
 To
 
 field as a recipient’s email address.
 




 Fig. 21 Selecting an email from the
 
 Auto-generated page
 
 process element
 

![chapter_process_designer_selecting_text_parameter.gif](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_selecting_text_parameter.gif)
* **Select system settings whose values are email addresses (text), accounts, or contacts** 
 . For example, “1st-line support.”
* **Select an account or contact email address of the user who runs the process** 
 . To do this, click
 ![btn_process_element_settings_lookup00008.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_emails/btn_process_element_settings_lookup00008.png)
 in the
 
 To
 
 field and select
 
 Contact
 
 /
 
 Account
 
 →“Current user account” / “Current user contact.”



 Depending on the selected option, the
 
 Send Email
 
 element will use the mailbox specified in the
 
 From
 
 field to send an email to the recipient(s) specified in the
 
 To
 
 field.
 



 Auto-link emails to existing Creatio records
----------------------------------------------



 In Creatio, each email or draft created on execution of the
 [Send Email
 
 element](https://academy.creatio.com/documents?id=7127) 
 can be linked to other Creatio objects, meaning that an email can be linked to an account, contact, document, etc.
 





 Note.
 
 You can only link emails created manually in the
 
 Send Email
 
 element to other Creatio objects. However, the element can also create a corresponding activity upon execution. Learn more:
 [Send email
 
 process element](https://academy.creatio.com/documents?id=7127) 
 .
 




 By default, the emails are linked to account or contact specified in the
 
 To
 
 field of the
 
 Send email
 
 element. If you specify a contact record whose
 
 Account
 
 field is populated, the email will be linked to the corresponding account as well.
 



 For example, during a process of meeting with the customer (Fig. 22) a “Meeting minutes” email must be sent after the meeting. In addition to the customer contact and account, which will be linked by default, you can also link the email to the opportunity related to the meeting.
 




 Fig. 22 “Meeting minutes” business process
 

![chapter_process_designer_process_diagram_meeting.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_process_diagram_meeting.png)



 To link an email to other Creatio records:
 


1. Select the
 
 Send Email
 
 element on the diagram.
2. Click
 ![btn_com_add_tab.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_emails/btn_com_add_tab.png)
 in the
 
 Email connections
 
 area and select one or more types of records to link to the sent email (Fig. 23). For example, to link the email to opportunity, select the
 
 Opportunity
 
 field.
 




 Fig. 23 Select the record type
 

![chapter_process_designer_selecting_opportunity_record.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_selecting_opportunity_record.png)




 Note.
 
 The
 
 Account
 
 and
 
 Contact
 
 record fields are added by default.
3. Fill out one or more fields in the
 
 Email connections
 
 block. You can link the email to a specific record or map the field to another parameter of the corresponding type. To do this:
 


	1. Click
	 ![btn_process_element_settings_lookup00009.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_emails/btn_process_element_settings_lookup00009.png)
	 in the
	 
	 Email connections
	 
	 field next to the connected record type field and select
	 
	 Process parameters
	 
	 from the list.
	2. Select the needed parameter in the window that opens. For example, to connect the “Meeting minutes” email to the opportunity that was specified in the meeting activity, select that activity in the
	 
	 Process element
	 
	 column, and its
	 
	 Opportunity
	 
	 parameter (Fig. 24).
	 
	
	
	
	
	 Fig. 24 Select the opportunity parameter of a process element
	 
	
	![chapter_process_designer_selecting_opportunity_lookup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_selecting_opportunity_lookup.png)



 As a result, whenever an email is sent according to this process, the corresponding fields in the
 
 Connected to
 
 field block of the email page will be populated automatically. Additionally, email links will be displayed on the
 
 Email
 
 tab of the communication panel (Fig. 25).
 




 Fig. 25 Email connected to an opportunity
 

![chapter_process_designer_selecting_communication_panel.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_emails/chapter_process_designer_selecting_communication_panel.png)




