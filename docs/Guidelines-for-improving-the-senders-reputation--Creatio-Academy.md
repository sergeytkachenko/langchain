


 The sender’s reputation is the rating of the sender with an email provider, such as Gmail. The reputation determines the mailbox folder to which the provider places the incoming message.
 



 Other parameters covered in the
 [Email deliverability: not getting marked as spam](/docs/8-0/user/marketing_tools/email_marketing/email_guidelines/email_deliverability/guidelines_for_increasing_deliverability) 
 article also affect if the provider marks an email as spam, but reputation is the most important factor. Email providers rate senders based on these:
 


* sender blacklists
* frequent spam complaints
* invalid contacts or spam traps in the email audience
* misconfigured DKIM/SPF
* email frequency and intervals
* the tools used for the sending
* email content
* email deletion rate, open rate and click rate
* replies and forwarding.



 The gravity of each factor depends on the email provider and may vary based on the email type.
 



 Reputation assessment
-----------------------



 The sender’s reputation is a fluid parameter. Keeping to the standards of an email provider increases the reputation with that provider and a failure to do that decreases it.
 



 The sender’s reputation comprises the IP address’s reputation and the domain's reputation.
 



 A
 **domain** 
 is part of the email address used to identify the sender.
 



 The
 **IP address** 
 locates the computer or email server that sends the emails.
 



 Changing the domain or IP address is not a valid tactic to restore the reputation since email providers keep the entire mailing history. As such, we recommend that you keep track of your reputation ratings and act to recover them if necessary. Learn more:
 [Reputation control services](/docs/8-0/user/marketing_tools/email_marketing/email_guidelines/web_tools/email_web_tools#title-2159-3) 
 .
 



 Reputation control
--------------------



 To monitor your reputation, configure the authentication of your email: SPF, DKIM, and DMARC. Learn more:
 [Email domain verification](https://academy.creatio.com/docs/user/setup_and_administration/email_domain_verification) 
 .
 



 Many email providers offer native services for reputation monitoring and analytics, also known as postmaster tools. Register with such services to increase the reputation.
 



 We also recommend that you run a blacklist check for your domains and addresses regularly to take immediate action and to unblock them in case of problems. Learn more:
 [Reputation control services](/docs/8-0/user/marketing_tools/email_marketing/email_guidelines/web_tools/email_web_tools#title-2159-3) 
 .
 



 Increase the reputation
-------------------------



 If the check-up revealed a decrease in your reputation, we recommend taking these steps:
 


* **Identify the source of the problem** 
 .
 
 This may include a sudden topic change, a new sender address, added attachments. Check for complaints on and unsubscribes from the email that caused the reputation to deteriorate. If you identified the problem, analyze what caused it to prevent similar issues in the future.
* **Request that the recipient adds the sender’s email to the contact list.** 
**For example, you can** 
 emphasize that this prevents the subscribers from missing out on important news. This guarantees that your email is not marked as spam.
* **Set up Facebook Loop** 
 to receive notifications when your subscribers complain about your emails. Learn more:
 [Feedback Loop (FBL) principles](/docs/8-0/user/marketing_tools/email_marketing/email_analytics/analytics_gathering_shortcut/analytics_gathering#title-1550-3) 
 .
* **Use postmaster tools** 
 to prevent a sudden decrease of the sender reputation and take immediate action to recover it. Learn more:
 [Reputation control services](/docs/8-0/user/marketing_tools/email_marketing/email_guidelines/web_tools/email_web_tools#title-2159-3) 
 .
* **Add an “unsubscribe” button** 
 to enable the uninterested users to unsubscribe rather than make a spam complaint. Learn more:
 [Set up an unsubscribe link in emails](/docs/8-0/user/marketing_tools/email_marketing/additional_setup/set_up_unsubscription/set_up_an_unsubscribe_link_in_emails) 
 .
* **Analyze and improve the content of your emails** 
 . The email must be valuable, well-written, and not contain suspicious links or files. Learn more:
 [Email deliverability: not getting marked as spam](/docs/8-0/user/marketing_tools/email_marketing/email_guidelines/email_deliverability/guidelines_for_increasing_deliverability) 
 .



 After you implement these suggestions, we recommend warming up the audience. Learn more:
 [Set up the email throttling queue](/docs/8-0/user/marketing_tools/email_marketing/additional_setup/throttling/email_throttling_queues) 
 .
 




