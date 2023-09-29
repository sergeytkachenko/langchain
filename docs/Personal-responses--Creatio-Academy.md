


 The
 **recipients’ individual responses** 
 are updated as soon as Creatio receives them from the server of the email provider. View responses from each email recipient in the
 
 Response
 
 column of the
 
 Audience
 
 tab (Fig. 1).
 




 Fig. 1 Personal responses
 

![section_email_status_detailed.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_analyze_emails_response/section_email_status_detailed.png)





 Note.
 
 Creatio does not include test email recipients in the email audience. The
 
 Audience
 
 tab does not display responses to test emails.
 




 You can also view recipients’ individual responses to both bulk and trigger emails in the
 
 Contacts
 
 section.
 



 Depending on whether an email was delivered or not, the responses can be grouped as follows:
 


* responses received
 **if an email was delivered**
* responses received
 **if an email was not delivered**



 Creatio can receive responses both from the
 **server of the email provider** 
 (e. g., “Invalid email address” or “Delivery error” responses) and the
 **email recipient** 
 (e. g., “Opened”, “Clicked”).
 



 The tables below list available Creatio responses and their descriptions. Some of the responses below can replace each other, others are final. When Creatio receives a final response, no further change is possible.
 



 Creatio prepares to send the email
------------------------------------





| 
 Response
  | 
 Meaning
  | 
 Reasons for receiving the response
  |
| --- | --- | --- |
| 
**Planned** 
 | 
 Creatio has not processed the email yet.
  | 
 The recipient was added to the audience of an incomplete email manually.
  |
| 
**Ready to send** 
 | 
 Creatio started sending emails and configured the recipient’s email. For example, the template was specified, macro values were added, etc.
  |
| 
**Queued** 
 | 
 Creatio has already forwarded the configured email to the cloud email service, but the service has not sent the email to the recipient yet.
  |




 Creatio did not send the email
--------------------------------





| 
 Response
  | 
 Meaning
  | 
 Reasons for receiving the response
  |
| --- | --- | --- |
| 
**Canceled (email not provided)** 
 | 
 Creatio did not send the email to the recipient. Final response.
  | 
 The email audience contains recipients that do not have an email address specified.
  |
| 
**Canceled (sender’s domain not verified)** 
 | 
 Assigned if your email domain is not verified. Learn more in a separate guide:
 [Email domain verification](https://academy.creatio.com/docs/user/setup_and_administration/email_domain_verification) 
 .
  |
| 
**Canceled (template not found)** 
 | 
 Assigned to recipients whose email was not sent due to a missing email template. This can occur if dynamic content replicas are set up incorrectly and recipient ends up in an email audience without any replica matching the filter conditions of the recipient.
  |
| 
**Canceled (invalid email)** 
 | 
 Assigned to a recipient whose email address has the
 
 Invalid
 
 checkbox selected. Learn more in a separate article:
 [Keep communication options valid](https://academy.creatio.com/documents?id=1309#title-2979-4) 
 .
  |
| 
**Canceled (duplicated email)** 
 | 
 The email audience contains recipients that have the same email address, and the “Prevent to send duplicated emails to recipients with the same address” (“PreventDuplicatesSending” code) system setting is enabled.
  |
| 
**Stopped (manually)** 
 | 
 Creatio did not send the email since the sending was canceled manually.
  |
| 
**Stopped (time to send expired)** 
 | 
 Email expiration date was reached before the Creatio could send the emails.
  |
| 
**Canceled (unsubscribed by email type)** 
 | 
 The recipient is unsubscribed from this email type, which is specified on the
 
 Email subscription
 
 detail of the contact page.
  |
| 
**Canceled (unsubscribed from all emails)** 
 | 
 Recipient unsubscribed from emails. Creatio selects the
 
 Do not use email
 
 checkbox for the contact that received the response.
  |
| 
**Delivery error** 
 | 
 An error occurred while sending the email to the mail server. View the error description in the
 
 Response reasons
 
 and
 
 Reason details
 
 columns of the
 
 Audience
 
 detail.
  |
| 
**Unknown response** 
 | 
 An unidentified error occurred during the sending process.
  |
| 
**Email limit reached** 
 | 
 Creatio rejected the email in accordance with the rules set up in the
 
 Email restriction rules
 
 lookup.
  |




 Provider delivered the email
------------------------------





| 
 Response
  | 
 Meaning
  | 
 Reasons for receiving the response
  |
| --- | --- | --- |
| 
**Delivered** 
 | 
 The provider delivered the email to the recipient successfully but they have not opened it yet.
  | 
 The email was delivered to the server of the recipient’s provider.
  |
| 
**Open** 
 | 
 The provider delivered the email to the recipient successfully and they opened it.
  | 
 The recipient opened the email at least once. View how many times they opened the email on the
 
 Opens
 
 column of the
 
 Audience
 
 tab.
  |
| 
**Open (machine)** 
 | 
 Spam detector bot, not actual recipient, opened the email. For example, the Mail Privacy Protection (MPP) mechanism of the Apple Mail app in iOS 15 and later.
  | 
 The recipient has not opened the email yet, thus Creatio does not include the response in open stats. Currently, only the
 **SendGrid** 
 provider identifies emails opened by bots.
  |
| 
**Clicks** 
 | 
 The provider delivered the email to the recipient successfully and they followed a link in the email.
  | 
 The recipient opened the email and followed any link except the unsubscribe link. The link can be a button, clickable image, contact data link, etc. View the number of clicks in the
 
 Clicks
 
 column of the
 
 Audience
 
 tab.
  |
| 
**Unsubscribed** 
 | 
 The provider delivered the email to the recipient successfully but they unsubscribed from emails. Creatio selects the
 
 Do not use email
 
 checkbox in the recipient’s contact profile automatically. The contact does not receive further emails. Final response.
  | 
 The recipient opened the email and followed the unsubscribe link or unsubscribed directly from the email client without opening the email.
  |
| 
**Spam complaint** 
 | 
 The provider delivered the email to the recipient successfully but they complained about the email and marked it as spam. Creatio selects the
 
 Do not use email
 
 checkbox in the recipient’s contact profile automatically. The contact does not receive further emails. Final response.
  | 
 The recipient marked the email as spam.
  |






 Note.
 
 Creatio displays the responses listed above on the opens/clicks chart and includes them in the click heatmap. Learn more in a separate article:
 [Open and click rates](https://academy.creatio.com/documents?id=1516) 
 .
 




 Provider did not deliver the email
------------------------------------





| 
 Response
  | 
 Meaning
  | 
 Reasons for receiving the response
  |
| --- | --- | --- |
| 
**Soft Bounce** 
 | 
 Creatio sent the email to the server of the provider, but the provider could not deliver the email within the specified period (48 hours for Elastic Email). In most cases, you can resend the email, for example, in another campaign.
 

 If an address receives this response repeatedly, this can indicate that the address is no longer used.
  | 
 The mailbox of the recipient is full.
 

 The mail server of the recipient is in autonomous mode, for example, overloaded, temporarily unavailable or undergoing maintenance.
 

 The IP address of the sender has low reputation.
 

 The SPF record required to verify the domain of the sender is configured incorrectly.
 

 The server of the recipient marked the email content as spam.
 

 View the response reason for each case in the
 
 Response reasons
 
 column on the
 
 Audience
 
 tab or on the contact page.
  |
| 
**Hard Bounce** 
 | 
 The provider did not deliver the email to the recipient. Creatio clears the
 
 Valid
 
 checkbox in the contact profile of the recipient. Final response.
  | 
 Creatio sets this response in case of a constant delivery error, for example:
 

 The email of the contact is incorrect.
 

 The specified email does not exist.
 

 View the response reason for each case in the
 
 Response reasons
 
 column on the
 
 Audience
 
 tab.
  |






 Note.
 
 You can also view the responses above on the general error chart of the
 
 Email totals
 
 tab. Learn more in a separate article:
 [Email delivery rates](https://academy.creatio.com/documents?id=1515) 
 .
 



### 
 Reasons for email delivery failure




 The options below are available in Creatio 8.0.2 Atlas and later.
 




 To analyze the reasons for email delivery failure, use the corresponding dashboard on the Marketing Creatio homepage. To view the reason for the response to a particular email:
 


* Open the email page → the
 
 Audience
 
 tab → the
 
 Response reasons
 
 column.
* Open the contact page → the
 
 History
 
 tab → the
 
 Email - Bulk emails
 
 detail → the
 
 Response reasons
 
 column.





| 
 Response
  | 
 Reason for delivery failure
  | 
 Meaning
  |
| --- | --- | --- |
| 
 Soft Bounce
  | **Will Retry**  | 
 The provider is experiencing temporary email delivery issues. Retries are attempted.
  |
| 
 Hard Bounce
  | **Unknown Recipient**  | 
 The recipient address does not exist.
  |
| **Mailbox Problem**  | 
 The recipient address does not exist.
  |
| **Spam Reject**  | 
 The mail server of the recipient rejected the email due to spam suspicions.
  |
| **Domain Not Found**  | 
 The domain of the recipient does not exist or cannot receive incoming emails.
  |
| **IP Reputation Issue**  | 
 The mail server rejected the email since the reputation of the sender’s IP address is low or the sender’s IP address is blacklisted.
  |
| **Recipient Blocked**  | 
 The provider blocked the address of the recipient.
  |
| **Other**  | 
 The mail server rejected the delivery. Learn more about the error on the email page → the
 
 Audience
 
 tab → the
 
 Reason details
 
 column or on the contact page → the
 
 History
 
 tab → the
 
 Email - Bulk emails
 
 detail → the
 
 Reason details
 
 column.
  |




 Response changes
------------------



 Responses that indicate that the email was not sent or that no delivery / delivery failure confirmation was received are final and cannot be changed.
 



 Responses received for sent emails have different priorities. If Creatio receives a new (non-final) response, the previous responses that have lower priority are replaced with the new response (Fig. 2).
 



 For example, if a recipient opens an email, clicks a link, then marks the email as spam, Creatio displays “Spam complaint” in the
 
 Response
 
 column on the
 
 Audience
 
 detail.
 





 Note.
 
 Specify the number of days within which to record the final response for each contact in the ”Time period (days) to update email statistics” (“MailingStatisticUpdatePeriod” code) system setting. After the specified period, Creatio stops changing the responses on the contact page as well as the
 
 Audience
 
 tab of the email page.
 





 Fig. 2 Email responses
 

![section_email_response_types.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_analyze_emails_response/section_email_response_types.png)




