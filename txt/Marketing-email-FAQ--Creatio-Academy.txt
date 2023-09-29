


 What is the difference between domain verification and email confirmation?
----------------------------------------------------------------------------



**Domain verification** 
 is done to display the correct sender name in the “From” field of emails and avoid unsanctioned emails on your behalf. After completing the domain verification, you enable the email service that your audiences use to sign your emails with your domain name. For example, if you are using ElasticEmail and have not performed domain verification, your recipients will see the following in the “From” field of all emails:
 



 “mailer@ee.mailbpm.com on behalf of; Manager Name <youremail@gmail.com>.”
 



 This means that the message was sent from your email provider’s server on your behalf.
 



 After the domain verification, the “From” string will contain only your email. Verification is performed on the DNS-server of your domain using the Sender Policy Framework (
 [SPF](https://en.wikipedia.org/wiki/Sender_Policy_Framework) 
 ) and DomainKeys Identified Mail (
 [DKIM](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) 
 ) methods. Learn more about verifying domains in a separate article:
 [Domain verification for the Elastic Email provider](https://academy.creatio.com/documents?id=1714) 
 .
 



**Sender email address confirmation** 
 is confirming that your email address belongs to you. After performing this procedure, you can send emails on your behalf. If your emails are sent via Elastic Email, you do not need to confirm the sender’s email.
 



 Why does an email recipient get access error after clicking a link in an email?
---------------------------------------------------------------------------------



 Certain countries might limit access to certain email services. In this case, the recipients will not be able to open the link from the email. We recommend adding a full URL text of your links to the email body as well as a recommendation to copy the link in the recipient’s browser.
 



 What are the reasons for marketing email licensing errors?
------------------------------------------------------------



 The licensing error can occur in the following cases:
 


* The number of active contacts exceeds the number of available licenses.
 



 When you try to send a bulk email, Creatio checks the available
 **marketing campaign** 
 and
 **active contact** 
 licenses. Any contact added to a bulk email audience at least once consumes an active contact license. If the number of active contacts (including those in the audience of your email) exceeds the total number of available licenses, the email cannot be sent. Learn more in a separate article:
 [Marketing Creatio licensing](https://academy.creatio.com/documents?id=1932) 
 . Creatio regularly notifies the users when the number of available active contact licenses becomes lower than 10% of the total number of paid licenses. Please check the “Notifications” tab of the Communication panel regularly. The minimum number of paid licenses required by Creatio (in percentage) is specified in the “Active contacts - warning threshold (%)” (“ActiveContactsWarningThreshold” code) system setting.
* A user tries to save a section record but does not have a license for this specific functionality.
 



 To be able to save an
 **Email** 
 or
 **Campaign** 
 section record, the user must have a
 **marketing campaign** 
 license. Learn more in a separate article:
 [Marketing Creatio licensing](https://academy.creatio.com/documents?id=1932) 
 .



 Are contacts that have the “Soft Bounce” and “Hard Bounce” email responses still considered active?
-----------------------------------------------------------------------------------------------------



 Yes. Any contact for whom at least one communication attempt via emails, campaigns or events has been made within a year is considered an active marketing contact and requires a “marketing active contacts” license, even if the contact has “Soft Bounce” and “Hard Bounce” email responses.
 



 Are contacts to whom an email was sent via SMTP still considered “Active”?
----------------------------------------------------------------------------



 No. The contacts to whom an email was sent via the SMTP simple mail transfer protocol, for example, via a business process
 **are not considered active** 
 .
 



 To be considered active, a contact must be a recipient of the email, a member of the campaign or event. Learn more about the active contacts in a separate article:
 [Marketing Creatio licensing](https://academy.creatio.com/documents?id=1932) 
 .
 



 Can I add a link that opens the email in the browser to the template?
-----------------------------------------------------------------------



 Only Elastic Email can open emails in the browser. To use this functionality, add the {view} macro to the link in the following format:
 






```

<a href="{view}">Anchor text</a>

```





 How can I view the contacts that followed a link?
---------------------------------------------------



 To do this, set the following filter in the
 
 Contacts
 
 section (Fig 1):
 




 Fig. 1 Filter contacts by link
 

![scr_link_filter.png](/docs/sites/en/files/images/Marketing_Tools/marketing_email_faq/scr_link_filter.png)



 Viewing a link that a contact followed requires custom coding.
 




