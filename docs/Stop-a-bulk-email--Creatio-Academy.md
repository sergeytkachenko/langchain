


 Stop an email before the sending starts
-----------------------------------------



 You can stop a bulk email
 **before any email messages are actually sent** 
 . Creatio does not start sending emails immediately, so if you manage to stop a bulk email within a certain period (10 seconds by default) no actual emails will be sent. You can modify the delay time using the “Delay time before sending email, seconds” (“MandrillMailingDelayInSeconds” code) system setting.
 



 To stop an email after it has started, click the
 
 Stop sending
 
 button and confirm the action in the pop-up window that appears (Fig. 1).
 





 Fig. 1
 
 Stopping a bulk email
 

![scr_section_email_how_to_stop_sending_bulk_emails.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_stop_bulk_email/scr_section_email_how_to_stop_sending_bulk_emails.png)



 The email will be stopped and a notification will appear in the notification area. The email will change to “Paused”. You can start the email later by clicking the
 
 Start sending
 
 button on the email page (Fig. 2).
 





 Fig. 2
 
 Resending a bulk email
 

![scr_section_email_how_to_start_sending_bulk_emails.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_stop_bulk_email/scr_section_email_how_to_start_sending_bulk_emails.png)



 Stop an email after the sending has started
---------------------------------------------



 The ability to stop emails
 **after sending has started** 
 depends on the number of email recipients. Bulk email sending is performed in batches. By default, the number of emails in a batch cannot exceed more than 20,000 emails. If you have less than 20,000 recipients, after the delay time all emails will be sent immediately in one batch. If you have a large number of recipients in your bulk email, then the next batch will be terminated when the bulk email is aborted. It is not possible to stop any batches that have already been sent.
 



 To stop an email after it has started, click the
 
 Stop sending
 
 button. The email status will be changed to “Stopping”, but sending of the current batch will continue. After sending all emails in the current batch, the email status will change to “Paused”. A notification will appear in the notification area.
 



 You can start the bulk email later by clicking the
 
 Start sending
 
 button on the bulk email page. In this case, emails will be sent to those recipients to whom the emails from the current bulk email were not sent.
 




