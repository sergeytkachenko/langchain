


 Configure automatic identification of category for cases registered from incoming emails to accelerate the processing of new cases created from emails. You are able to assign categories for cases received from different shared email accounts.
 



 The setup procedure is as follows:
 


1. Make sure that support service mailboxes are configured. Read more in the “
 
[Set up support mailboxes](/docs/7-17/user/service_tools/service_cases/case_settings/shared_email_account/set_up_a_shared_email_account#HT_specs_service_requests_support_mailbox_setup) 

 ” article.
2. Enable automatic categorization by editing the “Enable the relationship between support mailboxes and the categories of processed cases”
 
 system setting
 
 .
3. In the
 
 List of mailboxes for case registration
 
 lookup configure connection between support service mailboxes and case categories. To do this:
 


	1. Select a mailbox to set connection with case categories and click
	 
	![btn_edit.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_automatically_categorizing_cases/btn_edit.png)
	
	 .
	2. On the opened edit page, specify the value in the
	 
	 Case category
	 
	 field. This value will be assigned to all cases registered from this mailbox. For example, “Service request”.
	3. If you already have configured case registration from incoming emails for several mailboxes, repeat steps a and b for each mailbox.



 Set up case registration from emails from mailbox alias
---------------------------------------------------------



 Creatio can automatically register cases based on the emails that were forwarded to the Creatio mailbox from a different email. Note that Creatio will not add new cases for emails that were copied from one mailbox to another on the email server. To do this:
 


1. Click
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_forwarded_emails_settings/btn_system_designer.png)
 to open the
 **System Designer** 
 .
2. Open the
 **Lookups** 
 section.
3. Open the
 **List of mailboxes for case registration** 
 .
4. Click
 **New** 
 .
5. Populate the
 **parameters** 
 of the new record:
 


	1. **Mailbox** 
	 – the mailbox that was synchronized with Creatio.
	2. **Mailbox alias** 
	 – the mailbox alias from which the emails are forwarded to the Creatio mailbox.
	3. **Case category** 
	 – the default category for all cases received from this mailbox. This lets you set up different categories for cases that arrive at a regular mailbox and those forwarded from mailbox aliases.
6. **Add a lookup record for each mailbox alias** 
 used for receiving support emails.



 If Creatio does not register cases from emails sent to mailbox aliases, check if the mail client sets the tag “Auto-Submitted: auto-generated” for the forwarded messages. Cancel tagging the emails with this tag if your email client permits it. If the “Auto-Submitted” tag is required, make sure that you set its value to “No.” If you cannot manage tags on the email client side,
 **disable protection from auto-generated emails** 
 in Creatio. To do so:
 


1. Click
 ![btn_system_designer00001.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_forwarded_emails_settings/btn_system_designer00001.png)
 to open the
 **System Designer** 
 .
2. Open the
 **Lookups** 
 section.
3. Open the
 **Email header properties management** 
 lookup.
4. Click “
 **Auto-Submitted** 
 ” and clear the checkbox in the
 **Active** 
 column.
 



 Please note that disabling protection from auto-generated emails will decrease the strength of Creatio’s spam protection.




