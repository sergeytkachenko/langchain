


 Trigger emails are sent automatically, upon a specific event. For instance, whenever a new participant enters a campaign, Creatio sends a trigger email to that participant. The sending method of a trigger email is determined by the campaign in which the trigger email is included. There are three sending methods:
 


* **Daily** 
 at a specified time with the option to specify a delay up to several days. Trigger email will be sent to the contacts who moved to the corresponding step in the campaign. For example, you can send educational content on your software product in three days after the trial version order.
* **After a defined time** 
 – sent after some time after an event. For example, you can send a trigger email 15 minutes after a customer leaves your website without placing an order but did add products to the cart. Such emails are sent throughout the day.
* **Event-based** 
 – sent after a certain event. For example, this can be a welcome letter after filling out the landing form.



 We recommend
 **sending test emails** 
 before you start your email. This enables checking of macro values and contents display in the email. Learn more about test emails:
 [Send a test email](/docs/7-18/user/marketing_tools/email_marketing/additional_setup/test_emails/send_a_test_email) 
 .
 





 Attention.
 
 Email domain verification is required to start sending the email.
 




 You can stop trigger emails manually. Learn more:
 [Stop an email](/docs/7-18/user/marketing_tools/email_marketing/bulk_email/stop_an_email_shortcut/stop_an_email) 
 .
 



 Set up a trigger email
------------------------


1. **Create a new campaign** 
 in the
 
 Campaigns
 
 section.
2. **Include the trigger email in the campaign** 
 and set the sending conditions. For example, emails can be sent after an event is finished or daily at a specified time. Add other items in the campaign if needed.
3. **Start the campaign** 
 that is connected to the trigger email. The trigger email will be sent automatically after the campaign has launched. The audience for the trigger email can be formed automatically.
4. **Analyze the totals** 
 of the trigger email and email conversion for this recipient.



 Trigger email check-up
------------------------



 An email recipient validity check is also performed during the sending of a trigger email. For example, while assigning the audience, a customer may unsubscribe from your email or a customer's email inbox may become unavailable. To take into account such changes, a check is performed upon sending emails.
 


* **Subscription to your bulk emails.** 
 The
 
 Do not use email
 
 checkbox must be cleared on the contact page. Contacts who have the
 
 Do not use email
 
 checkbox selected will not receive further marketing emails.
* **Email address relevance.** 
 The
 
 Current
 
 checkbox must be selected for the email addresses used for contacts in the email. The address is considered to be invalid if a “Soft Bounce” or “Hard Bounce” response is received. The email will be sent to those contacts who have neither a “Soft Bounce” response nor a “Hard Bounce” response. These contacts will have the “Canceled (invalid email)” response.
* **Email address availability** 
 . The system checks whether the
 
 Email
 
 field is filled in on the contact page. Creatio will not send any emails to the contacts who have no email address in their profile. In this case, the “Canceled (email not provided)” response will be set in the
 
 Response
 
 column on the
 
 Audience
 
 tab.
* **Email address correctness** 
 . An email will be considered “incorrect” if it does not correspond to the email address format (for example, does not contain the “@” character). Creatio will not send any emails to the contacts who have incorrect email address in their profile. In this case, the “Canceled (incorrect email)” response will be set in the
 
 Response
 
 column on the
 
 Audience
 
 tab.




