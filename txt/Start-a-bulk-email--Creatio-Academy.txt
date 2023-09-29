


 We recommend
 **sending test emails** 
 before you start your email. This enables checking of macro values and contents display in the email. Learn more about test emails:
 [Send a test email](/docs/8-0/user/marketing_tools/email_marketing/additional_setup/test_emails/send_a_test_email) 
 .
 



 Run synchronization manually
------------------------------



 If the “
 **run manually** 
 ” value is selected in the
 
 Send time
 
 field, you can start an email manually at any time.
 



 Open the needed email and click
 **Start sending** 
 . Confirm the action in the new window.
 





 Attention.
 
 Email domain verification is required to start sending the email.
 




 Creatio will start sending emails in a few seconds after you click the
 
 Start sending
 
 button. During this time, you can stop the email, if necessary. You can specify the delay time in the “Delay time before sending bulk email, seconds” (“MandrillMailingDelayInSeconds” code) system setting. The delay is 10 seconds by default.
 



 Learn more about how to stop an email:
 [Stop an email](/docs/8-0/user/marketing_tools/email_marketing/bulk_email/stop_an_email_shortcut/stop_an_email) 
 .
 



 Schedule an email sending
---------------------------



 If the “
 **at the specified time** 
 ” value is selected in the
 
 Send time
 
 field, the email will start automatically at the specified time.
 



 Open a bulk email record and click the
 **Schedule sending** 
 button. Confirm the action in the new window.
 



 As a result, the email will be scheduled and the emails will be sent at the specified time automatically. If the due time has already passed when you click the
 
 Schedule sending
 
 button, Creatio will offer you to start sending the email immediately.
 





 Note.
 
 If you cannot start an email or the
 
 Email totals
 
 tab values do not update, the reason might be in the “System operations user” (“SystemUser” code) system setting: the user value might have been changed or updated. Learn more:
 [Change the “system” user (Supervisor)](/docs/8-0/user/setup_and_administration/user_and_access_management/user_management/supervisor_user/change_the_system_user_supervisor) 
 .
 




 Bulk email check-up
---------------------



 To make the email analysis more convenient and minimize the number of delivery errors, Creatio verifies the email audiences before starting the email. To ensure a comprehensive email response analysis,
 **all contacts** 
 can be added as email recipients, including contacts who have already unsubscribed from emails or contacts with invalid or incorrect email addresses.
 



 Use email responses on the
 
 Audience
 
 tab of the
 
 Email
 
 section page to analyze delivery errors. The responses are populated automatically after the email starts. Learn more about how to manage individual responses:
 [Personal responses](/docs/7-18/user/marketing_tools/email_marketing/email_analytics/personal_responses_shortcut/personal_responses) 
 .
 



 Contact data can be modified from the moment you add it to the audience until the email start. For example, during this period the customer may unsubscribe from your email or the customer's email box may become unavailable. To take into account such changes, an additional check is performed upon email sending.
 


* **Subscription to your emails.** 
 The
 **Do not use email** 
 checkbox must be cleared on the contact page. Creatio will not send any emails to the contacts who have the
 
 Do not use email
 
 checkbox selected on their page. In this case, the “Canceled (unsubscribed from all emails)” response will be set in the
 
 Response
 
 column on the
 
 Audience
 
 tab.
* **Email address relevance.** 
 The
 **Valid** 
 checkbox must be selected for the email address of each contact. The address is flagged as invalid automatically, upon receiving any “Hard Bounce” response. Creatio will not send any emails to the contacts, whose email address does not have the
 
 Valid
 
 checkbox selected. These contacts will have the “Canceled (invalid email)” response.
* **Email address availability** 
 . The system checks whether the
 **Email** 
 field is populated on the contact page. Creatio will not send any emails to the contacts who have no email address in their profile. In this case, the “Canceled (email not provided)” response will be set in the
 
 Response
 
 column on the
 
 Audience
 
 tab.
* **Email address availability** 
 . An email will be considered “incorrect” if it does not correspond to the email address format. Creatio will not send any emails to the contacts who have incorrect email address in their profile. In this case, the “Canceled (incorrect email)” response will be set in the
 
 Response
 
 column on the
 
 Audience
 
 tab.
* **Marketing communication limit** 
 for each recipient. You can limit the number of emails sent to contact during a set time, for example, no more than 5 emails per week. Creatio checks for this limit are based on the rules in the
 
 Email restriction rules
 
 lookup. For example, if a rule is set to send not more than two emails per day while two emails have already been sent to the contact today, then the third email will not be sent. These contacts will have the “Email limit reached” response selected in the
 
 Response
 
 field of the
 
 Audience
 
 tab. Learn more:
 [Configure restriction of the number of emails for sending](/docs/8-0/user/marketing_tools/email_marketing/additional_setup/limit_the_number_of_emails/configure_restriction_of_the_number_of_emails_for_sending) 
 .



 When you add the email audience, Creatio checks the subscription to the selected email type. You can check the subscription status on the contact page: use the
 
 Email subscription
 
 detail on the
 
 Communication channels
 
 tab. Contacts without a subscription to the selected email type are not added to the email audience.
 




