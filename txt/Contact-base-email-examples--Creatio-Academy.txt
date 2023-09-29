


 Working with the subscriber base sometimes requires the following scenarios that strengthen the sender’s reputation and increase deliverability.
 



 This article covers the following examples of subscriber base management:
 


* [Send emails to new subscribers (cold leads)](#title-3593-1) 
 .
* [Send a subscription request to a new audience](#title-3593-2) 
 .
* [Send emails to recipients who did not receive emails for a long time](#title-3593-3) 
 .
* [Send emails to recipients who did not open the emails for a long time](#title-3593-4) 
 .
* [Send emails after the sender’s domain or IP address changed](#title-3593-5) 
 .



 Send emails to new subscribers (cold leads)
---------------------------------------------



 Warm-up is an email audience management method intended to prepare the subscribers for active communication that leads to product sales.
 



 Before warming up a cold audience, make sure that the following conditions are met:
 


* The email addresses are valid.
* The contact base is collected using legal means and the recipients have consented to receive emails.
* You configured DKIM, SPF, and DMARC for the sender’s domain.
* The monitoring of the sender’s reputation delivers good results.
* The sender’s domain and IP address are not blacklisted.



 Keeping to these recommendations can prevent your email from being sent to spam.
 



 The general procedure for managing a base of new contacts is as follows:
 


1. **Segment your audience** 
 . Filter out the contacts with whom you are yet to communicate. Besides isolating cold leads, make sure a single contact is a part of a single segment. Each segment uses an individual warm-up strategy. Therefore Creatio may send a contact several emails per each of their segments. Redundant emails can impact the sender’s reputation negatively, provoke distrust in the recipient, and cause the email to end up marked as spam.
2. **Create separate queues for each recipient segment** 
 . We recommend naming each queue in agreement with the name of the relevant contact segment. Learn more:
 [Set up a throttling queue](/docs/7-18/user/marketing_tools/email_marketing/additional_setup/throttling/email_throttling_queues#title-2016-5) 
 .
3. **Prepare emails** 
 for each cold audience segment. Use the
 [“Warm up cold audience” mode](/docs/7-18/user/marketing_tools/email_marketing/additional_setup/throttling/email_throttling_queues#title-2016-11) 
 to set up email throttling. Select queues configured on the previous step in the
 
 Throttling queue
 
 field. When working with a cold audience, we recommend setting up marketing campaigns that contain 3-4 emails for each segment. Always select the “Warm up cold audience” mode and the queue that matches the corresponding segment for each email in the campaign.
4. **Set up a campaign to automate nurturing** 
 . For each segment, merge the emails created on the previous step into a single campaign. You can create several campaign diagrams or merge all segments into a single campaign, provided their number is moderate. Learn more:
 [Create a campaign](/docs/7-18/user/marketing_tools/marketing_campaings/create_a_campaign/add_campaign) 
 .
5. **Analyze campaign results** 
 :
	1. Active recipients (such as those who click the links) are considered interested. You can keep managing them based on the strategy for warmed-up leads.
	2. Do not send more than three activation emails to inactive recipients as part of the campaign. Delay the next warm-up for such contacts for at least half a year.
	3. Creatio will automatically clear the contact base of recipients that have irrelevant addresses (“Hard Bounce” responses).





 Note.
 
 We recommend against sending emails to recipients who unsubscribed. To ensure that Creatio cancels emails addressed to the unsubscribed users, enable the “Unsubscribe user from all bulk emails” system setting (“UnsubscribeFromAllMailings” code).
 




 Send a subscription request to a new audience
-----------------------------------------------



 For a bulk email to be legitimate and not incite a negative reaction, the user must consent to receive emails. In that case, send a manual email instead of using bulk email services.
 



 Use Creatio to set up an email template, specify the throttling parameters, and send regular bulk emails disguised as manual emails.
 



 The general procedure for working with subscription requests is as follows:
 


1. **Verify the sender’s domain** 
 . Learn more:
 [Email domain verification](https://academy.creatio.com/docs/user/setup_and_administration/email_domain_verification) 
 .
2. **Choose a title** 
 for the future email. Learn more:
 [Email deliverability: not getting marked as spam](https://academy.creatio.com/documents?id=2389) 
 .
3. **Prepare an email template** 
 that has a suggestion to subscribe. Cover what you will be sending, how often, on whose behalf, and from what mailbox in the copy. Tell more about your company and provide a link to your website.
4. Set up email throttling. Learn more:
 [Set up the email throttling queue](/docs/7-18/user/marketing_tools/email_marketing/additional_setup/throttling/email_throttling_queues) 
 .
5. **Start sending emails** 
 . Keep track of the deliverability rates and analyze the recipients’ responses. Do not send more than three emails per week between the first email and the subscription. If a user clicks a link in the email but does not subscribe, wait for some time and send them one more email that contains offers in which they took interest. After they subscribe, send them a thank-you email.



 Do not add the contact to your recipient base until they consent to receive newsletters in their response email. We recommend that you keep their confirmation.
 



 Send emails to recipients who did not receive emails for a long time
----------------------------------------------------------------------



 You can resume contact with your subscribers even after a prolonged hiatus.
   

 The general procedure for renewing an old contact base is as follows:
 


1. **Validate the contacts** 
 . Delete email addresses that have non-existent domains or clearly invalid addresses. You can validate small contact bases manually. For larger bases, use Creatio deduplication tools or third-party validation services. Learn more:
 [Deduplication](https://academy.creatio.com/docs/user/platform_basics/business_data/duplicates/find_and_merge_duplicates) 
 .
2. **Draw up several email templates** 
 that offer to resubscribe to the newsletter. Use personalization opportunities, call the recipient by name, tell more about the newsletter and its value, offer a good bargain, and add an unsubscribe link. Learn more:
 [Email deliverability: not getting marked as spam](https://academy.creatio.com/documents?id=2389) 
 .
3. **Do A/B-testing** 
 for a minor recipient segment of 400-500 email addresses. Send the emails gradually. Learn more:
 [Split tests](/docs/7-18/user/marketing_tools/email_marketing/ab_testing/testing/run_ab_tests) 
 .
4. **Make a set of emails (campaign) out of 3-4 reactivation emails** 
 . Analyze the results and clear the base of email addresses whose responses are “Hard Bounce,” “Unsubscribed,” etc. If a contact does not open a single email of the set, delete them as well. Learn more:
 [Create a campaign](/docs/7-18/user/marketing_tools/marketing_campaings/create_a_campaign/add_campaign) 
 .
5. **Segment your base after sending several emails** 
 . You can set up an individual set of emails for each contact group. If you have a default base and want to join it with an older base, do that in segments as well.



 Send emails to recipients who did not open the emails for a long time
-----------------------------------------------------------------------



 Usually, the less time passes since the subscription, the more active the recipients. The subscriber activity expectedly decreases as time goes by. To update the subscribers’ contacts, thus saving funds and clearing the base of irrelevant addresses, we recommend a reactivation.
 



 The general reactivation procedure is as follows:
 


1. **Remove all irrelevant email addresses.** 
 Irrelevant contacts decrease the sender's reputation and email deliverability. As part of contact base renewal, we recommend the following:
	1. Remove contacts who did not open their emails for a long time (more than six months).
	2. Remove contacts who unsubscribed, made a spam complaint or specified an invalid address.
	3. Segment your subscriber base depending on the length of the inactivity period and response to emails. You can set up a unique set of emails for each contact group.
2. **Work out and set up a reactivation campaign** 
 . Its main goal is prompting users to click the links in the emails and thus confirm they are still interested in the emails. If they do not react after several emails, delete the contact from the base.
3. **Send reactivation emails** 
 that have engaging copy.



 Send emails after the sender’s IP address or domain changed
-------------------------------------------------------------



 Should one of the factors affecting the sender’s reputation change (such as the domain, IP, or contact base), audience warm-up is required. Such changes raise suspicions with email providers, and they can mark the emails as spam.
 



 Do not warm up a new IP address, a new domain, or a new contact base simultaneously. If you plan to warm up the sender’s domain, make sure that the IP address is not blacklisted and the recipients are loyal and active.
 



 If you plan to warm up the sender’s IP address, use postmaster tools to make sure that the domain has a good reputation and your recipient base is loyal and warmed up.
 





 Note.
 
 In Creatio, the sender’s IP address may change if the dedicated IP address is enabled.
 




 Before the warm-up, make sure that the following conditions are met:
 


* The email addresses are valid.
* The contact base is collected using legal means and the recipients have consented to receive emails.
* You configured DKIM, SPF, and DMARC for the sender’s domain.
* You configured postmaster tools for the sender’s domain.



 The general warm-up procedure for a new IP address or domain is as follows:
 


1. **Draw up an email** 
 that meets the following criteria:
	* The framing of the message is neutral. The content is interesting and valuable.
	* The message provides an easy-to-notice unsubscribe link. Learn more:
	 [Set up an unsubscribe link in emails](/docs/7-18/user/marketing_tools/email_marketing/additional_setup/set_up_unsubscription/set_up_an_unsubscribe_link_in_emails) 
	 .
	* The email is up to 100Kb in size, and it is not too long. Email providers such as Gmail can truncate overly long emails, purging the unsubscribe link. Learn more:
	 [Email deliverability: not getting marked as spam](https://academy.creatio.com/documents?id=2389) 
	 .
	* The email is responsive, which makes it render properly on various devices. Learn more:
	 [Responsive design of emails](https://academy.creatio.com/documents?id=1772) 
	 .
	* The email subject and body do not contain spammy words (“Giveaway,” “Free,” etc.) or, too many capital letters. The email body does not comprise images only. Learn more:
	 [Email deliverability: not getting marked as spam](https://academy.creatio.com/documents?id=2389) 
	 .
2. **Keep the address base updated** 
 to ensure it contains only interested contacts.
	* Delete invalid and inactive addresses, as well as spam traps. This will improve the email open rate. To do this, use validation services. Learn more:
	 [Email web tools](https://academy.creatio.com/documents?id=2387) 
	 .
	* Segment your audience based on activity. Divide the customer base into groups who did not open your emails in one, two, three, and more months. This approach will increase both deliverability and CTR.
	 
	
	
	 Note.
	 
	 If you warm up a sender’s domain, segment the part of the base allotted to that domain. If you change the sender’s domain for the recipient base, you will have to re-do the warm-up.
3. **Draw up a warm-up schedule** 
 . Send a small number of emails to the most active subscribers at first and gradually increase the number of recipients by adding relatively inactive subscribers.



 For example:
 





|  |  |
| --- | --- |
| 
 Week 1-2
  | 
 Send emails only to subscribers who were active in the last 30 days.
  |
| 
 Week 3-4
  | 
 Add recipients who did not open your emails in 30-60 days and remove those who did not open them in 60-90 days.
  |




 We recommend sending emails in small portions at first. That way, you can slow down and update your strategy if the contact activity is below the expected results or the recipients make spam complaints.
 


### 
 Example warm-up for a base of loyal contacts



 Warm up a base of loyal contacts who were active in the last 30 days. The base contains 250,000 addresses. Based on the recommendations above, the distribution schedule can look like this:
 





| 
 Day
  | 
 Number of emails
  | 
 Delay between emails, s\*
  |
| 
 1
  | 
 600
  | 
 35
  |
| 
 2
  | 
 1200
  | 
 30
  |
| 
 3
  | 
 2400
  | 
 20
  |
| 
 4
  | 
 3000
  | 
 20
  |
| 
 5
  | 
 4500
  | 
 15
  |
| 
 6
  | 
 6000
  | 
 0
  |
| 
 7
  | 
 9000
  | 
 0
  |
| 
 8
  | 
 18000
  | 
 0
  |
| 
 9
  | 
 30000
  | 
 0
  |
| 
 10
  | 
 45000
  | 
 0
  |
| 
 11
  | 
 60000
  | 
 0
  |
| 
 12
  | 
 90000
  | 
 0
  |
| 
 13
  | 
 150000
  | 
 0
  |
| 
 14
  | 
 300000
  | 
 0
  |




 Learn more:
 [Set up the email throttling queue](/docs/7-18/user/marketing_tools/email_marketing/additional_setup/throttling/email_throttling_queues) 
 .
 




