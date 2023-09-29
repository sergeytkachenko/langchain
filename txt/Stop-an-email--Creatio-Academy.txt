


 This article is relevant for
 **bulk** 
 and
 **trigger** 
 emails.
 



 You can
 **pause an active email** 
 if Creatio is yet to pass the emails to the sending provider. You will be able to restart the email. Learn more:
 [Pause an email](#title-2045-1) 
 .
 



 You can also
 **stop** 
 an email regardless of its status
 **after** 
 Creatio has already started sending the emails. You will not be able to restart such an email. Learn more:
 [Stop an email](#title-2045-2) 
 .
 



 Pause an email
----------------



 You can pause a bulk or a trigger email soon after the start to edit the template and
 **restart the email** 
 later. The “Delay time before sending bulk email, seconds” (“MandrillMailingDelayInSeconds” code) system setting defines the period when you can pause an email. By default, the delay before Creatio starts sending emails is 10 seconds.
 



 You can pause an email
 **before Creatio starts sending emails** 
 provided that its status is “
 **Waiting before send** 
 .”
 



 Click
 
 Stop sending
 
 and confirm the action in the dialog box to
 **pause an email** 
 (
 
 Fig. 1
 
 ).
 




 Fig. 1 Stopping a bulk email
 

![scr_section_email_how_to_stop_sending_bulk_emails.png](/docs/sites/en/files/images/Marketing_Tools/stop_bulk_email/scr_section_email_how_to_stop_sending_bulk_emails.png)



 Creatio will pause the email and display the corresponding notification in the notification area. The “Email paused manually” event will be recorded in the
 [sending log](/docs/8-0/user/marketing_tools/email_marketing/email_analytics/progress/email_progress#title-1547-11) 
 . The email status will change to “Paused.” Click
 
 Start sending
 
 to restart the email (
 
 Fig. 2
 
 ).
 




 Fig. 2 Restarting an email
 

![scr_section_email_how_to_start_sending_bulk_emails.png](/docs/sites/en/files/images/Marketing_Tools/stop_bulk_email/scr_section_email_how_to_start_sending_bulk_emails.png)



 Stop an email
---------------



 You can stop a bulk or a trigger email after Creatio has already started sending the emails. You
 **cannot restart** 
 such emails.
 



 You can only stop the emails Creatio has not yet passed to the sending provider. The email can have “
 **Queued** 
 ,” “
 **Active** 
 ,” “
 **Sending in progress** 
 ” statuses.
 



 Click
 
 Stop sending
 
 and confirm the action in the dialog box to stop an email after Creatio has already started sending it.
 



 The email status will change to “Stopping.” Creatio will review the recipients and mark all contacts it has not yet passed to the sending provider with the “Stopped (manually)”
 [personal response](/docs/7-18/user/marketing_tools/email_marketing/email_analytics/personal_responses_shortcut/personal_responses) 
 . The email status will change to “Stopped” once all recipients with undelivered emails are marked with this response. The “Email stopped manually” event will be recorded in the
 [sending log](/docs/8-0/user/marketing_tools/email_marketing/email_analytics/progress/email_progress#title-1547-11) 
 . Find out more about the audience that has not received the emails in the
 [email progress](/docs/8-0/user/marketing_tools/email_marketing/email_analytics/progress/email_progress) 
 analytics.
 





 Note.
 
 If the campaign connected to a trigger email remains active, Creatio will keep adding participants to the audience. These participants will be marked with the “Stopped (manually)” personal response. You can still advance such participants through the campaign. For example, add a new conditional flow to send another email.
 





