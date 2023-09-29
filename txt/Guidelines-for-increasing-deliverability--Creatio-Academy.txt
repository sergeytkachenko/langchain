


 This article covers factors that affect the email deliverability rates and steps which can prevent an email from getting marked as spam.
 



**Deliverability** 
 rate is the ratio of delivered emails to the total number of sent emails. An email is considered delivered whether it ends up in the inbox folder or the spam folder. That means if an email is marked as spam, it still is considered delivered. However, such an outcome does not convert well since the recipient is unlikely to read the message.
 



 The reasons an email may be marked as spam are as follows:
 


* The user marked the email as spam manually.
* The email was marked as spam due to individual subscription settings.
* The email provider (for example, Gmail) declined the email.
* The mail server declined the email.
* Factors that affect deliverability can be roughly split into internal and external.



 Internal factors
------------------



**Internal factors** 
 concern the email content and the template’s compliance with standards.
   

 The internal factors include:
 


* email headers
* email copy
* email footer.


### 
 Email headers



 Email headers include:
 


* the sender's name
* the sender’s email address
* the email subject
* the preheader.



 When filling out the email headers, keep to the following recommendations:
 


* **The “From” field** 
 must contain the real name of the sender. This is important for brand awareness and loyalty. You can use the following examples for reference: “Company name” (“Alpha Business”), “Sender’s name and company name” (“Alexander Wilson, Alpha Business”), “Sender’s name” (“Alexander Wilson”), “Company name and category” (“Alpha Business News”).
* **The “Sender’s email” field** 
 must correspond to the sender's name. If the email is sent on behalf of a specific employee, the sender’s email must be theirs. For example, put down “Alpha Business” as the sender and send emails from the info@alphabusiness.com mailbox for a newsletter. For personalized emails (e. g., transactional and trigger emails), an employee can be the sender: “Alexander Wilson, Alpha Business,” the “a.wilson@alphabusiness.com” mailbox.
* Fill out
 **the “Subject” field** 
 of the email based on its actual content. It is best to avoid spammy words, such as “Free,” “Giveaway,” “Right now!” etc. For the same reason, we do not advise overusing uppercase letters and exclamation marks. We recommend adding the recipient’s name to the subject. This adds a personalized touch to the email and makes it stand out among the other messages. This is also good for increasing your reputation with email providers. In Creatio, you can use macros to achieve that. Learn more:
 [Personalize content using macros](/docs/7-18/user/marketing_tools/email_marketing/email_templates/macros/personalize_email_content_with_macros) 
 .
* **The “Preheader” field** 
 covers the email’s subject further. Use it to draw attention to your email, inform the subscribers about the highlights, and persuade them to open the email.


### 
 Email content



 The email’s content is the most important factor for the end-user. Low-quality or irrelevant content may cause the user to mark the email as spam. Email providers also scrutinize the content.
 



 Use the following guidelines to increase the deliverability rates:
 


* Check the spelling in your email manually or by using dedicated web services. Learn more:
 [Email web tools](https://academy.creatio.com/documents?id=2387) 
 .
* Avoid spammy words. You can find a list of spammy words on SimplyCast’s
 [website](https://www.simplycast.com/blog/100-top-email-spam-trigger-words-and-phrases-to-avoid) 
 .
* Add alt text to the included images. This helps the recipient to understand the email if the images are disabled. Do not send emails that only include images and no copy. The recipient will not be able to read them in the situation mentioned above.
* Do not attach files or link suspicious domains. If a domain is blacklisted with an email provider, the provider will mark an email linking that domain as spam. To share a file, upload it to a trusted filesharing service and provide a link to the file.
* Create a browser version of your email. The users will be able to read it even if the email service has problems rendering it. Some email services, such as Outlook, support this solution.
* Do not shorten your links. That makes predicting the link destination hard for email providers. They can mark your email as spam because of that.
* Personalize the email content. Creatio offers a set of tools for that: macros, trigger emails, and more. Learn more:
 [Email personalization](https://academy.creatio.com/documents?id=2388) 
 .


### 
 Footer



 Most email services have guidelines for the footer content.
 



 Normally, the following information is required in the footer:
 


* The company’s legal address and contact data.
* The reason for sending the email. For example: “You received this email because you are subscribed to Creatio’s newsletter.”
* The ability to unsubscribe. Learn more:
 [Set up an unsubscribe link in emails](/docs/7-18/user/marketing_tools/email_marketing/additional_setup/set_up_unsubscription/set_up_an_unsubscribe_link_in_emails) 
 .



 External factors
------------------



**External factors** 
 that can affect the deliverability rates include:
 


* the sender’s reputation
* the subscriber base management
* the mail regularity.


### 
 The sender’s reputation



 The sender’s reputation is one of the vital factors affecting the email deliverability rates. To avoid reputation damage, use the following approach:
 


* For initial emails or emails sent after a prolonged hiatus, use an audience warm-up schedule, which imitates manual sending. Learn more:
 [Set up the email throttling queue](/docs/7-18/user/marketing_tools/email_marketing/additional_setup/throttling/email_throttling_queues) 
 .
* We recommend the same course of action if you add a large number of new subscribers to an existing base. Such an audience is considered cold. Learn more:
 [Set up the email throttling queue](/docs/7-18/user/marketing_tools/email_marketing/additional_setup/throttling/email_throttling_queues) 
 .
* Verify your domain before sending the email. Learn more:
 [Email domain verification](https://academy.creatio.com/docs/user/setup_and_administration/email_domain_verification) 
 .


### 
 The subscriber base management



 To increase the deliverability rates, keep the subscriber base updated and relevant. Learn more:
 [Working with the subscriber base](https://academy.creatio.com/docs/user/marketing_tools/email_marketing/contact_base_collection_guidelines) 
 .
 



 We recommend establishing regular contact base cleanup and update procedures.
 


* Verify the email addresses at least twice a year.
* Remove inactive subscribers from your contact base.
* Set up Double opt-in (a two-factor subscription consent). The user must provide their email address and consent to receive emails when registering with the website. Then, send them an email that has a confirmation link. This helps to capture a relevant and existing address, and, consequently, ensure the validity of the entire base.
* Segment the base using various criteria. For example, account for your subscribers’ preferences or their responses to the previous emails.
* Make content for your emails based on the subscribers’ preferences.
* Personalize the emails. This helps to build a trusting relationship with your subscribers, establish an emotional connection between them and your brand, and keep the audience engaged as a result. Learn more:
 [Email personalization](https://academy.creatio.com/documents?id=2388) 
 .


### 
 The email regularity



 Sending emails regularly improves the subscribers’ loyalty and increases the conversion rates. Email providers track and evaluate this parameter as well. A prolonged hiatus between emails may look suspicious and affect the deliverability negatively. At the same time, too frequent emails also have a negative effect. The optimal email frequency varies on a case-by-case basis, but it is 2-4 emails monthly on average. Send emails regularly to prevent the emails from getting marked as spam.
 




