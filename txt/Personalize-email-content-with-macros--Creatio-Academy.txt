


 You can use
 **macros** 
 to add sender's and recipient's personal details (name, job title, etc.) when setting up email templates. When sending an email, the macros will be replaced with the corresponding values of the contact page fields (recipient's or sender's).
 



 You can add macros to the email's header and preheader, sender's name and sender's email as well as the email's subject and body. It is also possible to personalize the email images with macros.
 



 You can use:
 


* **[Basic macros](#title-1568-1)**
 . They let you add data from the recipient's or the sender's contact profile to the template. For example, you can add their full name, job title, etc.
* **[Custom macros](/docs/7-16/user/marketing_tools/email_marketing/email_templates/html_code/add_custom_html_code_to_an_email_template#title-1542-1)**
 . They let you add data from the records connected to the recipient's or the sender's contact profile. For instance, you can add an account name from the relevant contact page.
* **[Linked entity macros](#title-1568-7)**
 . They let you add data from the linked object's records to the template. For example, you can add the relevant content (a link to the recorded webinar, an event location, etc.) by adding a linked entity macro based on the “Event participants” linked object.



 Macro formatting guidelines
-----------------------------



 Macro formatting in Creatio might differ from external email builders. Emails that contain incorrectly formatted macros will not be sent. To ensure your macros are formatted correctly, follow these guidelines:
 


* Enclose macros only in square brackets. For example, [#value#].
* Divide tables and fields in macro paths only using periods. For example, [#Table.Table.Field#].
* Define the path to the required field only via linked Creatio entities.
* Use only Creatio object codes as table or column IDs.







 Add a basic macro
-----------------------





 Case.
 
 Add a salutation for the recipient to the email text.
 



1. Open the email template in the Content Designer.
2. Click the template text in the area where you would like to place the macro.
3. Click
 ![text_toolbar_text_macros.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_macroses/text_toolbar_text_macros.png)
 →
 
 Basic macro
 
 in the toolbar above the text.
4. Select the “Salutation” macro in the “Recipient” group and click
 
 Select
 
 .
5. Save the template
6. This will add
 
 #Recipient.Title#
 
 macro to the relevant area of the email. When sending the email, the macro will be replaced with the value of the
 
 Recipient’s name
 
 field on the recipient's contact page (
 [Fig. 1](#XREF_96180_232)
 ).
 





 Fig. 1
 

 Adding macros to the email subject
 

![img_section_email_macro_subject.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_macroses/img_section_email_macro_subject.gif)


#### 
 Common email template macros





| 
 Macro
  | 
 Definition
  |
| --- | --- |
| 
**Unsubscribe macros** 
 |
| 

 #Unsubscribe.URL#
 
 | 
 Adds the unsubscribe function as a direct link (e.g., “http://www.mysite.com/act/unsubscribe”) to the unsubscribe page.
  |
| 
**Recipient information macros** 
 |
| 

 #Recipient.Contact name#
 
 | 
 The recipient's first and last name
  |
| 

 #Recipient.Title#
 
 | 
 The recipient's honorifics, for example, “Mr” or “Mrs”.
  |
| 

 #Recipient.Salutation#
 
 | 
 The usual way to greet the recipient, taken from the contact's
 
 Recipient's name
 
 field. For instance, “Wilson”.
  |
| 
**Email owner information macros** 
 |
| 

 #Owner.Contact name#
 
 | 
 Last name, first name and honorific (if available) of the employee responsible for the email.
  |
| 

 #Owner.Salutation#
 
 | 
 The usual way to greet the employee, taken from the contact's
 
 Recipient's name
 
 field. For example, “Wilson”.
  |
| 

 #Owner.Business phone#
 
 | 
 The communication options of the employee responsible the email.
  |
| 

 #Owner.Mobile phone#
 
 |
| 

 #Owner.Skype#
 
 |
| 

 #Owner.Email#
 
 |
| 

 #Owner.Job name#
 
 | 
 The general job title of the employee responsible for the email, for example “customer manager”.
  |
| 

 #Owner.Job title#
 
 | 
 The full job title of the employee responsible for the email, for example “VIP customer manager”.
  |
| 

 #Owner.Department#
 
 | 
 The company division where the employee responsible for the email works.
  |
| 

 #Owner.Account#
 
 | 
 Your company's name.
  |
| 

 #Owner.Account address#
 
 | 
 Your company's address.
  |
| 

 #Owner.Account primary phone#
 
 | 
 Your company's primary phone number.
  |
| 

 #Owner.Account web address#
 
 | 
 Your company's website.
  |
| 
**Contact owner information macros** 
 |
| 

 #Contact.Owner.Name#
 
 | 
 The name of the manager of an email participant — the user specified in the
 
 Owner
 
 field of the recipient's contact. This macro is available only in the
 
 Sender's name
 
 field of the template header. It lets you send emails on behalf of the employee responsible for each email participant
  |
| 

 #Contact.Owner.Email#
 
 | 
 The email of the manager of an email participant — the user specified in the
 
 Owner
 
 field of the recipient's contact. This macro is available only in the
 
 Sender's email
 
 field of the template header. It lets you send emails from the email address of the employee responsible for each email participant.
  |




 Add a linked entity macro
---------------------------





 Case.
 

 Send emails on behalf of the lead's owner.
 



1. Open the email template in the Content Designer.
2. Click
 ![btn_macro.png](/docs/sites/en/files/images/Marketing_Tools/email_template_macro/btn_macro.png)
 in the
 
 Sender’s name
 
 field. This will open the column selection window.
3. Click
 
 +
 
 to the left of
 
 Email participant
 
 field and select
 
 Linked entity
 
 in the newly-opened dropdown.
 





 Note.
 
 You need to specify the linked entity used for email macros in the
 
 Audience source
 
 field at the top of the email page. You can read more about forming the bulk email audience in the
 [Add bulk email audience](/docs/7-16/user/marketing_tools/email_marketing/bulk_email/create_an_email/add_a_bulk_email#title-1551-5) 
 article.
4. Click
 
 +
 
 to the left of
 
 Linked entity
 
 field and select a connected object in the newly-opened dropdown, for instance,
 
 Owner
 
 .
5. Specify the connected object's column, for example,
 
 First name
 
 .
6. Click
 
 Select
 
 (
 [Fig. 2](#XREF_96180_232)
 ).
7. Save the template
 




 Fig. 2
 
 Creating a connected object macro
 

![email_linked_entity_macro.png](/docs/sites/en/files/images/Marketing_Tools/email_template_macro/email_linked_entity_macro.png)



 This will add the
 
 #LinkedEntity.Owner.GivenName#
 
 macro to the
 
 Sender's name
 
 field. When sending an email, the macro will be replaced with with the value of the
 
 First name
 
 field of the connected record (the owner).
 





 Note.
 
 You can read more about using linked entity macros when sending test emails in the
 [Send a test email](/docs/7-16/user/marketing_tools/email_marketing/additional_setup/test_emails/send_a_test_email) 
 article.
 





