


 View the email data in the
 
 Sending progress
 
 tab on the email page, available out-of-the-box (Fig. 1). Use this data to adjust the email sending process and improve the delivery rate. The following email data is available:
 


* Email
 [delivery chart](#title-2036-1) 
 that displays the current status of individual emails.
* Email sending
 [progress analytics](#title-2036-2) 
 that displays recipient quantity and percentage metrics by status.
* The email start and finish
 [date and time](#title-2036-3) 
 .
* [Sending log](#title-2036-4) 
 that displays successful events and sending errors.



 Summary data for emails started in the last 72 hours is available in the
 [sending progress dashboard](#title-2036-7) 
 .
 




 Fig. 1 Email sending progress
 

![email_progress_page.png](/docs/sites/en/files/images/Marketing_Tools/email_progress/email_progress_page.png)



 Email delivery progress chart
-------------------------------



 The
 **chart** 
 (Fig. 2) on the email page visualizes real-time information about the email sending and delivery progress. Hover over the chart to view the more information by email status.
 




 Fig. 2 Email progress chart
 

![email_progress_bar.png](/docs/sites/en/files/images/Marketing_Tools/email_progress/email_progress_bar.png)


* **Preparing to send** 
 – the number of emails Creatio has not yet sent. For instance, Creatio sets the status to “Preparing to send” when going through the
 [throttling](/docs/7-18/user/marketing_tools/email_marketing/additional_setup/throttling/email_throttling_queues) 
 segmentation. This status corresponds to the “Planned” response.
* **Queued** 
 – the number of segmented and ready-to-send emails for which Creatio has not yet received the mail provider's response. This status corresponds to the “Queued” response.
* **Delivered** 
 – the number of emails delivered to recipients. This is the number of recipients with the “Accepted by the server” mail service provider response.
* **Bounce** 
 – the number of emails with “Hard Bounce” and “Soft Bounce” responses.
* **Delivery error** 
 – the number of emails with “Sending error (to provider)” and “Rejected” responses.
* **Stopped** 
 – the number of unprocessed emails. This is the number of recipients with “Stopped (manually)” and “Stopped (time to send expired)” responses.
* **Canceled** 
 – the number of unsent emails. This is the sum of recipients with the “Canceled (Duplicate email),” “Canceled (Unsubscribed from all emails),” “Canceled (Unreachable email), “Canceled (Incorrect email),” and “Canceled (email not provided)” responses.



 Read more:
 [Personal responses](/docs/7-18/user/marketing_tools/email_marketing/email_analytics/personal_responses_shortcut/personal_responses) 
 .
 



 Email sending progress analytics
----------------------------------



 Creatio displays email progress analytics in “Metric” type dashboards on the
 
 Sending progress
 
 tab (Fig. 1):
 


* Recipients
 
 – the number of email recipients.
* Preparing to send
 
 – the number and percentage of emails Creatio is yet to send. This metric corresponds to the “Planned” response in the
 
 Audience
 
 tab and should display 0 for completed emails.
* Queued
 
 – the number of segmented emails the cloud service provider is ready to send or has already sent but for which it has not yet received the mail provider's response. This metric corresponds to the “Sent to the provider” response in the
 
 Audience
 
 tab and should display 0 for completed emails.
* Sent
 
 – how many recipients returned the provider's first response. This metric corresponds to the “Delivered,” “Hard Bounce,” “Soft Bounce,” and other similar responses in the
 
 Audience
 
 tab.
* Stopped
 
 – the number of recipients Creatio did not process, either due to
 [manual](/docs/7-18/user/marketing_tools/email_marketing/bulk_email/stop_an_email_shortcut/stop_an_email) 
 stop of the email or due to the email reaching the expiration date.
* Canceled
 
 – the number of unsent emails. This metric corresponds to the “Canceled (Duplicate email),” “Canceled (Unsubscribed from all emails),” “Canceled (Unreachable email), “Canceled (Incorrect email),” and “Canceled (email not provided)” responses in the
 
 Audience
 
 tab.



 Read more:
 [Personal responses](/docs/7-18/user/marketing_tools/email_marketing/email_analytics/personal_responses_shortcut/personal_responses) 
 .
 



 Email start/finish date
-------------------------



 You can view the following information in the
 
 Sending duration
 
 field group:
 


* Started on
 
 – the email start date.
* Finished on
 
 – the email completion date.
* Duration
 
 – how much time it took to send the email to all recipients.



 Sending log
-------------



 Monitor the email sending progress in the
 
 Sending log
 
 detail on the
 
 Sending progress
 
 tab.
 



 Alternatively, view data about all bulk emails in the mailing log. Open the mailing log from the
 **System designer** 
 or by clicking
 
 Email
 
 →
 
 Actions
 
 →
 
 Mailing log
 
 .
 



 Should any errors occur during the sending process, the log will help you to find out the reasons and fix the original issue.
 



 The log displays data as a record list. The
 
 Type
 
 column specifies the log record type: “
 [Info](#title-2036-5) 
 ” for successful events or “
 [Error](#title-2036-7) 
 ” for unsuccessful events.
 


### 
 Successful events in the sending log



 The table below lists events that indicate successful email sending progress.
 





| 
 Event
  | 
 Description
  | 
 Comment
  |
| --- | --- | --- |
| 
 Start sending email
  | 
 The email is scheduled on {MM/DD/YYY HH:MM:SS time zone}.
  | 
 Creatio will record this event for bulk emails only if you select “at the specified time” in the
 
 Send time
 
 field and click Schedule sending.
  |
| 
 Sending email was started.
  | 
 Creatio records this event after the email starts regardless of the start option.
  |
| 
 Check integration with cloud email service
  | 
 Connection with cloud email service is active.
  | 
 Creatio records this event before the email starts. It means Creatio integration with the cloud email service has been set up correctly.
  |
| 
 Preparing a batch of recipients for sending to the cloud email service (batch can contain up to 20000 recipients)
  | 
 Batch #{0} of {1} recipients contains: {2} - will send to cloud email service, {3} - will not send, incorrect email, {4} - will not send, email does not exist, {5} - will not send, email is not actual, {6} - will not send, recipient unsubscribed.
  | 
 Creatio sends emails in batches of 20000 messages, one after another, until it covers the entire email audience.
 

 The event description elaborates on how many emails Creatio did not send and specifies reasons.
  |
| 
 Sending batch of emails to the cloud email service
  | 
 Batch #{0} of emails was successfully sent.
  | 
 The event means Creatio sent an email batch successfully.
  |
| 
 Email paused manually
  | 
 Email was paused by user.
  | 
 Creatio records this event if a user pauses the email with the “Waiting before send” status. Read more:
 [Pause an email](/docs/7-18/user/marketing_tools/email_marketing/bulk_email/stop_an_email_shortcut/stop_an_email#title-2045-1) 
 .
  |
| 
 Email stopped manually
  | 
 Email was stopped by user.
  | 
 Creatio records this event if a user stops the email manually. Read more:
 [Stop an email](/docs/7-18/user/marketing_tools/email_marketing/bulk_email/stop_an_email_shortcut/stop_an_email#title-2045-2) 
 .
  |
| 
 Email expiration date reached
  | 
 Email was stopped and switched the status to "Expired" due to expiration date is reached.
  | 
 Creatio records this event if the email stops after reaching the expiration date. Read more:
 [Set up the email expiration date](/docs/7-17/user/marketing_tools/email_marketing/additional_setup/email_expiration_date_shortcut/email_expiration_date) 
 .
  |
| 
 Emails was successfully sent
  | 
 Sending complete.
  | 
 If Creatio finds no new recipients, it will record this event. There will be no more attempts to send out this email. Creatio will change the email status to “Completed.”
  |






 Note.
 
 Creatio records the event that activates a trigger email to the campaign log. Read more:
 [Monitor campaigns](/docs/7-17/user/marketing_tools/marketing_campaings/monitor_campaigns_shortcut/monitor_campaigns) 
 .
 



### 
 Error events in the sending log



 The
 
 Error description
 
 column in the sending log contains the full description of each sending error.
 



 Should an error occur, contact Creatio support and describe the error in as many details as possible.
 



 The table below lists errors Creatio records to the email sending log.
 





| 
 Event
  | 
 Description
  | 
 Comment
  |
| --- | --- | --- |
| 
 Audience actualization from the campaign
  | 
 Error while updating the email audience from the campaign.
  | 
 Creatio records this event if unable to add a campaign audience to the email.
  |
| 
 Adding audience to email
  | 
 Recipients group processing failed.
  | 
 Creatio records this event if unable to add recipients to the email audience.
  |
| 
 Sending messages to cloud services
  | 
 Error while sending messages to cloud services.
 

 Email sending error.
 

 Error while setting a communication limit.
 

 Error while saving the template.
  | 
 Creatio records this event if the cloud email service is not available.
  |
| 
 Sending a batch of emails
  | 
 Error while handling initial responses of an email.
 

 Error while sending a batch of {Number} emails.
 

 Email sending error.
  | 
 This event means Creatio cannot send an email batch.
  |
| 
 Message validation
  | 
 Error while validating the message.
  | 
 Creatio records this event if the sender's email was not verified during the email setup.
  |




 Email sending progress summary dashboard
------------------------------------------



 View data about the progress of emails started in the last
 **72 hours** 
 in the
 
 Sending progress
 
 tab of the
 
 Email
 
 section's
 
 Dashboards
 
 view (Fig. 3).
 




 Fig. 3 Sending progress dashboard
 

![dashboard_email_progress.png](/docs/sites/en/files/images/Marketing_Tools/email_progress/dashboard_email_progress.png)



 The real-time
 
 Sending progress
 
 dashboard displays the numbers of prepared and processed recipients, as well as that of sent emails.
 



 The table below describes the columns of the
 
 Sending progress
 
 dashboard.
 





| 
 Column
  | 
 Description
  |
| --- | --- |
| 
 Recipients
  | 
 The sum of email recipients
  |
| 
 Prepared recipients count
  | 
 The number of recipients Creatio segmented. Creatio is ready to send emails to those recipients.
  |
| 
 Processed recipients count
  | 
 The number of emails Creatio has already passed to the cloud service or was unable to send. For instance, the email was a duplicate or an unforeseen error occurred.
  |
| 
 Status
  | 
 The current email status. For example, “Planned” or “Sending.”
  |
| 
 Received initial response count
  | 
 The number of recipients whose email provider sent the initial response.
  |
| 
 Errors count
  | 
 The number of errors occurred after the cloud service passed emails to providers.
  |





