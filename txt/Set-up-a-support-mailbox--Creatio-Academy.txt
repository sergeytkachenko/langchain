


 Add support mailboxes to Creatio to accelerate communication with your customers:
 


* Creatio will register new cases automatically based on the incoming emails.
* Customers will receive case notifications.
* All case emails will be saved to the case history.



 Add a support mailbox
-----------------------


1. Click the
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_mailbox_settings/btn_system_designer.png)
 button to open the System Designer.
 


 Attention.
 
 Before you begin, set up the mail service provider integration either via the
 [IMAP/SMTP](/docs/8-0/user/setup_and_administration/base_integrations/imap_smtp_email/add_imap_smtp_email_provider) 
 protocol or using the
 [Microsoft Exchange](/docs/7-18/user/setup_and_administration/base_integrations/microsoft_email_contacts_and_calendar/set_up_microsoft_exchange_and_office_365/set_up_the_ms_exchange_and_microsoft_365_services) 
 service.
2. Go to the “System setup” block → “Lookups.”
3. Open the
 
 List of mailboxes for case registration
 
 lookup.
4. Click
 
 New
 
 .
5. **Select the support mailbox** 
 added during the
 [email integration setup](/docs/8-0/user/setup_and_administration/base_integrations/imap_smtp_email/add_imap_smtp_email_provider) 
 in the
 
 Mailbox
 
 field. The field is required.
6. Specify the name of the mailbox you use to receive emails in the
 
 Mailbox alias
 
 field. Fill out the field only if you receive emails in the mailbox that differs from the mailbox you set up originally.
7. Specify the relevant category in the
 
 Case category
 
 field. For example, “incident.” The field is required.
8. Enter the mailbox description in the
 
 Description
 
 field.
9. Select the language Creatio will use for the email if the mailbox language selection rule is triggered in the
 
 Message language
 
 field. Learn more:
 [Set up the language of the support mailbox](#title-2115-2) 
 .
10. Select the
 
 Always use the mailbox language
 
 checkbox to send emails in the specified language regardless of the other rules (Fig. 1).
11. Repeat steps 4–11 if you are using more than one support mailbox.



 Fig. 1 Set up the support mailbox language
 

![service_mailbox.png](/docs/sites/en/files/images/Service_Tools/case_settings/service_mailbox.png)


 As a result, Creatio will process all emails received by the mailboxes in the case registration system.
 



 You can also set up a shared support mailbox for communicating with customers and sending case notifications. Learn more:
 [Configure a shared mailbox](/docs/8-0/user/setup_and_administration/base_integrations/mailbox_setup/set_up_a_shared_mailbox/configure_a_shared_mailbox) 
 .
 



 Set up the language of the support mailbox
--------------------------------------------



 Set up the mailbox language to send localized emails to customers. In Creatio, you can set up the language for:
 


* the case notification mailbox
* the email notification template language
* the notifications sent to customers without the preferred language specified



 Creatio determines the email language based on the following rules:
 


* If you
 **do not select** 
 the
 
 Always use the mailbox language
 
 checkbox during the
 [email setup](#title-2115-1) 
 , Creatio will use the following variables to determine the language, from highest to lowest priority:
	+ The preferred language of the recipient contact.
	+ The email language specified during the mailbox setup.
	+ The value of the “Default language for messages” (“DefaultMessageLanguage” code) system setting.
* If you
 **select** 
 the
 
 Always use the mailbox language
 
 checkbox, Creatio will send emails in the mailbox language regardless of the other rules.




