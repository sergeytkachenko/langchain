


 Send test emails to preview the email content in an email client and check how the message will look like for your recipients. The marketing email metrics and analytics ignore test emails.
 





 Attention.
 
[Verify](https://academy.creatio.com/docs/user/setup_and_administration/email_domain_verification) 
 your email domain before sending a test email. Besides that, specify a valid sender's address in the email.
 




 You can send  test email from the relevant email page or the Content Designer by clicking the
 
 Test email
 
 button (Fig. 1). We recommend against using words like “Test”, “Hello”, “Checking” as the email subject when sending test emails. The recipient server might perform a series of checks that could mark such emails as spam. We recommend preparing the test email content of the same quality as the content intended for the end recipients.
 





 Fig. 1
 

 Sending test emails from the email page
 

![section_email_test_email.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_emails_test/section_email_test_email.gif)


1. Open the email in the section list. Click the
 
 Test email
 
 button on the
 
 Template
 
 tab (Fig. 1).
2. Enter the recipient email addresses  in the
 
 Test email(s) will be sent to email addresses
 
 field, enter email addresses where the test email will be sent. field. Use commas “,” or semicolons ”;” as separators.
3. In the
 
 Recipient's contact for testing macros
 
 field, specify the contact whose data will be used in the test email.
   

 You can generate the test email's macros based on a contact connected to one of several objects. Specify the object in the
 
 Audience source
 
 field at the top of the email page. The name of the
 
 Recipient's contact for testing macros
 
 field changes depending on the object you selected. For example, if you select the “Lead” value in the
 
 Audience source
 
 field, the field name will change to
 
 Recipient's lead for testing macros
 
 . You can select any contact that is connected to the object.
   

 By default, if you select the “Contact” object in the
 
 Audience source
 
 field, the campaign will use the contact specified in the “Test email recipient” (“TestSendingBulkEmailContact” code) system setting.
 


 Note.
 
 Creatio stores the values you entered in the previous steps. Should you need to send the test email again, Creatio will populate these fields automatically. You will be able to either use those values once more or update them.
4. Click
 
 Send
 
 .



 As a result, the test email will be sent to the specified addresses. You can send test emails from the Content Designer in a similar way.
 



 If you send test emails with
 **dynamic content** 
 , the “Send test email” window will display a
 
 Test email template settings
 
 field (Fig. 2). Choose between sending the current email template version or all template versions in this field.
 





 Fig. 2
 

 Sending a test email with dynamic content
 

![section_email_test_email_dynamic_content.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_emails_test/section_email_test_email_dynamic_content.gif)





 Note.
 
 Learn more about how to create emails with dynamic content in the
 [Configure dynamic content for marketing emails](/docs/7-16/user/marketing_tools/email_marketing/email_templates/dynamic_content/configure_dynamic_content_for_emails#HT_section_email_dynamic_content_setup) 
 article.
 





