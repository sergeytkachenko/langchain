


 Email integration features in Creatio let you track the history of your cooperation with customers. The emails that you receive will be bound to other Creatio objects automatically. You can create and manage emails and run business processes by email directly in Creatio.
 





 Note.
 
 To receive and send emails in Creatio, you need to set up the email provider connection parameters, add an email account, and set up mailbox synchronization. Read more in the
 [Base integrations](https://academy.creatio.com/docs/user/setup_and_administration/base_integrations) 
 guide.
 




 Open the
 **email area** 
 by clicking the
 ![btn_com_email_tab.png](/docs/sites/default/files/images/2020-11/btn_com_email_tab.png)
 button on the communication panel. The button counter displays the number of unread email messages.
 



 At the top of the
 
 Email
 
 tab on the communication panel, you can see filters and buttons for managing emails (Fig. 1). You can:
 


* [create](#title-749-1) 
 a new email message
* [add](https://academy.creatio.com/docs/user/setup_and_administration/base_integrations) 
 a new account and set up your mailbox
* [upload](#title-749-3) 
 emails to Creatio
* filter your emails, for example, display only the outbound or unprocessed email messages




 Fig. 1 Filters and buttons for email management
 

![chapter_emails_manage_emails_pane.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/chapter_emails_manage_emails_pane.png)



 Email messages are displayed as a list. You can see the sender's data, time of sending, email subject, and the initial text in every email. At the bottom of each email, you can see the icons of all bound objects (Fig. 2).
 




 Fig. 2 The bound email records on the communication panel
 

![chapter_emails_linked_objects_view.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/chapter_emails_linked_objects_view.png)



 Send an email
---------------


1. Click the
 ![btn_com_email_tab00001.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_com_email_tab00001.png)
 button in the communication panel.
2. Click the
 ![btn_com_add_email.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_com_add_email.png)
 button to create an email.
3. Fill out the required fields on the email page:
 


	1. Select the mailbox to send the email in the
	 
	 From
	 
	 field. If you configured an email signature, it will be added to the text area.
	2. Specify the recipient's email.
	3. Click the
	 
	 Cc
	 
	 and
	 
	 Bcc
	 
	 buttons to display the
	 
	 Carbon copy
	 
	 and
	 
	 Blind carbon copy
	 
	 fields (optional).
	4. Specify the message subject.
	5. Enter the email body.
	6. Paste the image from the clipboard or drag the image to the email text to add an image to the email body (Fig. 3).
	 
	
	
	
	
	 Fig. 3 Dragging the image to the email
	 
	
	![add_picture_to_email.gif](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/add_picture_to_email.gif)
4. Click the
 
 General information
 
 tab.
 


	1. Fill out the standard activity fields (such as
	 
	 Show in calendar
	 
	 ,
	 
	 Start
	 
	 ,
	 
	 Due
	 
	 , etc.) if the email must be displayed as a calendar activity.
	2. Fill out the corresponding fields in the
	 
	 Connected to
	 
	 field group if the email is bound to other Creatio objects, such as accounts and documents.
5. Click the
 
 Attachments
 
 tab of the email page to add an attachment.
 


	1. Click the
	 
	 Add file
	 
	 button. This opens a box.
	2. Select the file to attach in the box that opens.
	 
	
	
	
	
	
	 Note.
	 
	 By default, the maximum size of an attachment is 10 MB. You can change this value in the “Attachment max size” (“MaxFileSize” code) system setting.
6. Click
 
 Send
 
 .
 



 As a result, the email will be sent from the mailbox specified in the
 
 From
 
 field to the addresses specified in the
 
 To
 
 ,
 
 Cc
 
 , and
 
 Bcc
 
 fields. The email sending status will be changed to “Completed.”



 Send a template-based email
-----------------------------



 You can use email templates when sending emails using the
 ![btn_com_workflow_card_email.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_com_workflow_card_email.png)
 action panel button. The
 [action panel](https://academy.creatio.com/documents?id=1765&anchor=title-2141-5) 
 is available in several system sections, such as
 
 Contacts
 
 ,
 
 Accounts
 
 ,
 
 Leads
 
 , etc.
 



 To create an email based on a template:
 


1. Click the
 ![btn_com_workflow_card_email00002.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_com_workflow_card_email00002.png)
 button on the action panel of a record page.
2. Fill out the needed fields (
 
 From
 
 ,
 
 To
 
 ,
 
 Subject
 
 , etc.) in the email message area.
3. Click the
 
 /...
 
 button to open the template lookup instead of entering message text (Fig. 4).
 




 Fig. 4 Select an email template
 

![scr_emails_go_to_templates.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/scr_emails_go_to_templates.png)
4. Select the needed template.
 



 The template list displays the records from the
 
 Email templates
 
 lookup. If you are creating an email from a contact page, the list displays only those templates that have the “Contact” specified as a source of macros, as well as any templates that have no source specified at all. The same applies to accounts, leads, etc.
 



 As a result, the text of the selected template will be added to the email. Macros, such as the recipient's name and the sender’s name will be highlighted in the text.
5. Edit the template text if needed and click the
 
 Send
 
 button.
 





 Note.
 
 Email templates are available only when sending emails from the action panel. Email templates are not available when creating a message through the communication panel, or from the
 
 Communication options
 
 detail on pages of certain Creatio sections.
 




 You can add and modify templates in the
 
 Email templates
 
 lookup. The
 [Content Designer](https://academy.creatio.com/documents?id=1974) 
 is used for creating and editing email templates.



 Receive emails
----------------


1. Click the
 ![btn_com_email_tab00003.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_com_email_tab00003.png)
 button in the communication panel.
2. Select
 
 Synchronize email
 
 in the
 ![btn_com_roles_actions_menu.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_com_roles_actions_menu.png)
 menu (Fig. 5).
 




 Fig. 5 Synchronize email
 

![scr_emails_act_synchronize_mail.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/scr_emails_act_synchronize_mail.png)



 As a result, emails will be downloaded from the synchronized email server folders. Email attachments will be automatically added to the
 
 Files
 
 detail of the
 
 Attachments
 
 tab.
 





 Note.
 
 You can set up periodic synchronization of the email account using the
 [synchronization setup](https://academy.creatio.com/docs/user/setup_and_administration/base_integrations) 
 page.
 




 Each time an email is downloaded, Creatio automatically performs initial email processing:
 


1. The
 
 From
 
 field value is associated with the communication options of contacts and accounts registered in the system. If the match is found, the
 
 Account
 
 and
 
 Contact
 
 fields on the email page will be populated automatically.
2. If no match is found, the system analyzes the values in the
 
 To
 
 ,
 
 Cc
 
 , and
 
 Bcc
 
 fields. Then, if the match is found, the
 
 Account
 
 and
 
 Contact
 
 fields on the email page will be populated automatically.
 





 Note.
 
 When matching the
 
 To
 
 ,
 
 Cc
 
 , and
 
 Bcc
 
 fields with contact communication options, any contacts connected to Creatio user records will be ignored.
3. Creatio also verifies the
 **rules for binding emails to other Creatio objects** 
 .
 [Read more >>>](#title-749-9)



 As a result, the user who loaded the email will be specified as the record's author and owner.
 



 Process emails
----------------



 An email is considered
 **processed** 
 if either the
 
 Account
 
 or
 
 Contact
 
 is specified and at least one of the connection fields, for example,
 
 Opportunity
 
 or
 
 Contract
 
 , is filled out.
 





 Note.
 
 Emails in which the
 
 Contact
 
 ,
 
 Account
 
 , and
 
 Case
 
 fields were automatically populated are not processed.
 




 When uploaded, the emails are processed
 **automatically** 
 according to the
 [email binding rules](#title-749-9) 
 .
 





 Note.
 
 An email is considered processed if the
 
 Needs processing
 
 checkbox on the email page is cleared. The checkbox is selected/cleared automatically.
 




 The emails that were not processed automatically require
 **manual** 
 processing.
 


1. Display the unprocessed emails by selecting the
 
 Not processed
 
 filter (Fig. 6).
 




 Fig. 6 Filter emails
 

![scr_emails_act_uncultivated_email.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/scr_emails_act_uncultivated_email.png)
2. Select the email to process (Fig. 7).
 




 Fig. 7 Select an unprocessed email
 

![chapter_emails_connect_existing_2.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/chapter_emails_connect_existing_2.png)
3. Bind an email to Creatio records. Learn more about the manual binding of emails to Creatio records in the
 [Link emails to existing records](#title-749-8) 
 article
4. Click the
 
 Mark as processed
 
 button. If the email that you processed is part of an email thread, Creatio will offer to process all emails in the thread.
 



 As a result, this email or email thread will no longer be displayed in the list of unprocessed emails and the
 
 Needs processing
 
 checkbox on its page will be cleared. To view the list of processed emails, select the
 
 Processed
 
 filter in the filter area.



 Run a business process by an incoming email
---------------------------------------------



 You can set up the list of business processes involved in email management. For example, if a customer expresses interest in your products in his email, a new lead has to be created, if the email contains a request or a question, the system has to register a case.
 





 Note.
 
 Detailed descriptions of the business process automation are available in the Creatio business process documentation.
 




 To run a business process by email:
 


1. Click the
 ![btn_com_email_tab00004.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_com_email_tab00004.png)
 button on the communication panel.
2. Select the email to run the business process by.
3. Select the process to run by the current email from the
 ![btn_email_menu.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_email_menu.png)
 menu (Fig. 8).
 




 Fig. 8 Run a process by email
 

![scr_emails_act_start_process.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/scr_emails_act_start_process.png)



 As a result, the business process will be run by the selected email.
 





 Note.
 
 To display the business process in the
 ![btn_email_menu00005.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_email_menu00005.png)
 menu of the email, add the “Email Process” tag, as well as a parameter with the “RecordId” code and the
 
 Unique identifier
 
 data type in the business process parameters (see business process documentation for more information).
 



 You can change the tag using the “Email processes tag” (“EmailProcessTag” code) system setting.
 




 Add records based on emails
-----------------------------



 You can create a new record in any Creatio section based on an email message from the communication panel. For instance, you can add a new contact based on an email from an unknown sender. His email address and name will be automatically filled in on his edit page with the data from the linked email message. If you add another record (i. e., an opportunity, invoice, or an order), Creatio will automatically populate its corresponding fields on the contact page with the corresponding data from the email message. For instance, when you create a new opportunity, the
 
 Customer
 
 field on the opportunity page will contain the name of the account or contact.
 



 To create a new contact record based on an incoming email:
 


1. Click the
 ![btn_com_email_tab00006.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_com_email_tab00006.png)
 button in the communication panel.
2. Select an email message.
3. Click the
 ![btn_com_add_tab.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_com_add_tab.png)
 button in the top right corner of the email message and select the
 
 Add new
 
 command (Fig. 9).
 




 Fig. 9 Add a new record based on an email message in the communication panel
 

![chapter_emails_create_new.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/chapter_emails_create_new.png)
4. Select an object (the type of Creatio record to create) from the menu, for example, “Contact” (Fig. 10).
 




 Fig. 10 Select the type of Creatio record to add
 

![chapter_emails_new_object_choice.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/chapter_emails_new_object_choice.png)
5. A new contact edit page will be created, its
 
 Name
 
 and
 
 Email
 
 will be populated with the email message data. You can modify the entered data manually before saving the changes (Fig. 11).
 




 Fig. 11 The page of the contact created from the email message
 

![chapter_emails_new_contact_page.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/chapter_emails_new_contact_page.png)



 As a result, a new record based on the email message data will appear in the
 
 Contacts
 
 section.
 



 Link emails to existing records
---------------------------------



 You can bind email messages to other records manually:
 


* By using a special email field where you can specify a Creatio record to bind (Fig. 12).




 Fig. 12 Bind an email message to another record using email message fields
 

![chapter_emails_connect_existing_200007.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/chapter_emails_connect_existing_200007.png)


* By clicking the
 ![btn_com_add_tab00008.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_com_add_tab00008.png)
 button in the top right corner of the email message (Fig. 13).




 Fig. 13 Bind an email message to another record using the
 ![btn_com_add_tab00009.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_com_add_tab00009.png)
 button
 

![chapter_emails_connect_existing.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/chapter_emails_connect_existing.png)


* By using the
 
 General information
 
 tab of the email message page. To open the email message page, click its subject.



 As a result, the bound email message will be displayed in the
 
 History
 
 tab of the activity page.
 



 Auto-link emails to existing records
--------------------------------------



 To bind an incoming or outgoing email to other Creatio objects, set up the binding rules in the
 
 Rules for connecting emails to system sections
 
 lookup. For example, if the email subject contains an invoice number, the email will be automatically bound to the corresponding Creatio invoice.
 



 To set up the binding rules:
 


1. Open the System Designer by clicking the
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/btn_system_designer.png)
 button in the top right corner of the application window.
2. Click the “Lookups” link in the “System setup” block.
3. Open the
 
 Rules for connecting emails to system sections
 
 lookup.
4. Click the
 
 Add rule
 
 button or open an existing rule for editing on the lookup page.
5. Fill out the required fields (Fig. 14) on the displayed page:
 




 Fig. 14 Set up the binding rules
 

![scr_emails_lcp_rule.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_emails/scr_emails_lcp_rule.png)
6. Specify the rule name, for example, “Email subject with invoice number.”
7. Enter a regular expression that would match the subject text in the
 
 Rule
 
 field, such as the invoice number prefix.
 



 For example, if the following invoice auto numbering format is set up as follows: Inv-1, Inv-2, Inv-3, ..., Inv-n, the regular expression is Inv-
 
 0-9
 
 +. As a result, when the following email is received - “Additional information for Inv-53,” Creatio will automatically verify whether the specified invoice exists. If the invoice is found, the
 
 Invoice
 
 field on the email page will be populated with the corresponding value.
 





 Note.
 
 To assure the right connection between emails and other system objects, configure different auto numbering patterns for different system objects. For example, the auto numbering pattern is “Inv-{0}” for invoices, “Ord-{0}” for orders, “Cont-{0}” for contacts, etc. The
 [record auto numbering](https://academy.creatio.com/documents?id=269) 
 in Creatio is set up via the system settings.
 



	1. Fill out the
	 
	 Object for connection
	 
	 field group. To automatically bind emails to Creatio objects, select “Activity” in the
	 
	 Object
	 
	 field. In the
	 
	 Column
	 
	 field, specify the field to bind by. The system performs the match search using the email subject. It is located in the
	 
	 Subject
	 
	 column.
	2. Fill out the
	 
	 Connected object
	 
	 fields group. In the
	 
	 Object
	 
	 field, select the system object that the rule is set up for, for example, “Invoice.” In the
	 
	 Column
	 
	 field, select the column to perform the match search. In this case, the column is
	 
	 Number
	 
	 .
8. Save the rule.
9. Add the rules for other sections similarly.
 



 As a result, when uploading messages to Creatio and sending emails from the system, the message subjects will be checked according to the configured rules. If the match is found, the connection fields will be automatically populated. In addition, such messages will be automatically considered processed.



 Working with emails FAQ
-------------------------


### 
 Why do I receive an email notification that the login/password is incorrect after mailbox registration?



 Email server security settings sometimes block access to mailboxes from third-party applications. If you entered the information correctly during the email account registration, but still received a notification about an incorrect user name or password, do the following:
 


1. Enable IMAP access in the mailbox settings. Usually, email forwarding and POP/IMAP protocol management settings are in a separate group.
2. Enable access to your email account from third-party applications in the email account security settings.
3. In most cases, the email server sends the users an email about an attempt to connect to the mailbox. Confirm the connection authenticity by following a special link from the email.
4. Repeat the mailbox registration procedure.


### 
 How do I set up a custom email provider?





 Note.
 
 Set up the
 [Exchange Listener](https://academy.creatio.com/documents?id=2074) 
 synchronization service before setting up an email provider.
 




 To set up email provider integration, you need to open ports 25 and 587 on the Creatio application server. On the email provider selection page, click the
 
 Add provider
 
 button, select the provider type and fill out the send/receive settings. Learn more about the detailed procedures for email provider setup in separate articles:
 [Add IMAP/SMTP email provider](https://academy.creatio.com/documents?id=1415) 
 .
 [MS Exchange / Microsoft 365 email, contacts, and calendar](https://academy.creatio.com/docs/user/setup_and_administration/base_integrations/microsoft_email_contacts_and_calendar) 
 .
 


### 
 Why no emails can be received in Creatio after a successful mailbox synchronization setup?



 This can occur if one of the following is the case:
 


1. The “Activity” object includes a custom field required on the application level.
 



 To ensure Craetio receives emails properly, modify the field attributes. Make it required on the page level, but not required in the object.
2. The emails received from an IMAP mail server have been downloaded to Creatio and then deleted, or they have been downloaded to any other email client earlier.
 



 To upload the email to Creatio, change the name of the lookup based on the “EmailSynchronizedKey” object to an arbitrary name.


### 
 How to set up a shared mailbox?



 Shared email accounts are used for email communication between the support team and users.
 [Shared mailbox](https://academy.creatio.com/documents?id=1867) 
 setup is similar to individual mailbox setup in general, but has a number of additional steps.
 


### 
 Why the outgoing emails are not imported to Creatio?



 You can set up the import of all emails from your mailbox to Creatio. Alternatively, you can import emails from specific mailbox folders only. Check your email account folder settings for email import.
 



 If your mailbox security settings restrict access to certain mailbox folders for third-party applications, these folders will be unavailable for importing into Creatio. To permit access to these folders for third-party applications, modify your mailbox security settings.
 



 Also, in some cases, outgoing emails might not import from MS Outlook, because not all email servers support saving emails sent from third-party applications.
 


### 
 Why do I receive the “Error sending email, please contact system administrator” message when trying to send emails?



 This error might be the result of the following:
 


* sending emails is restricted on the provider level
* no connection to SMTP server
* one of the following ports is closed on the SMTP server: 25, 465, 587



 Contact your system administrator to determine the exact cause of the error and correct it.
 


### 
 I cannot see the
 
 Email
 
 detail in the
 
 Contacts
 
 section. Why?



 The
 
 Email
 
 detail is not displayed for contacts who have “Employee” specified in the
 
 Type
 
 field and “Our company” specified in the account profile. Use Creatio development tools to modify this logic.
 




