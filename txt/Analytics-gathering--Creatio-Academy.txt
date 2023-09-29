






 How Creatio calculates the number of opened emails
--------------------------------------------------------



 To get information about email opens, use the
 **“pixel” tracking method** 
 . A one-pixel image is automatically added to each message sent as part of a marketing email campaign. After the recipient opens the email, the image is downloaded from the server. The number of downloads corresponds to the number of opens.
 



 In some cases, the recipient's browser or email software can block image downloads. If the
 
 Opens
 
 column of the
 
 Audience
 
 detail shows “0”, but there are recorded clicks, it means that image downloading is blocked by the recipient’s software and accurate data about the opens was not received. Such cases are analyzed by the system and calculated within the
 
**Open rate, %** 

 and
 **No. of opens** 
 metrics of the delivery statistics diagram. Read more about test emails in the “
 
[Analyze delivery rates](/docs/7-18/user/marketing_tools/email_marketing/email_analytics/delivery_rates/email_delivery_rates#HT_section_email_analytics_tab_in_page) 

 ” article.
 



 MS Outlook only considers an email opened if it’s been viewed in a separate window. Previewing a message in MS Outlook is not considered as an “Open”, because in this case the images are not loaded. Test email opens do not count.
 





 How Creatio monitors the “Marked as spam” responses
-------------------------------------------------------



 Spam complaints must be monitored to prevent possible blocking of your emails by spam filters in the future.
 



 Creatio will add “
 **Marked as spam** 
 ” response if an email is sent to the spam folder. An email can be sent to spam not only by the recipient but also as a result of being blocked by the email provider’s spam filter or because of detecting viruses in the email.
 



 This type of response is processed through the
 **Feedback Loop** 
**(FBL))** 
 mechanism.
 


### 
 Feedback Loop (FBL) basics



 The FBL ensures that
 **the sender is notified if a complaint was received** 
 about their emails from the recipient. As soon as an email is flagged as spam, the email provider reports a complaint to the sender. Usually, the report contains the recipient’s email, the original message and the reason for flagging the email as spam. These reports trigger “Spam” response in Creatio. The
 
 Audience
 
 tab of the email page contains information about spam complaints.
 


### 
 Email providers that support FBL



 The following recipient providers can send “Spam” responses (the list is not complete):
 


* Hotmail;
* Microsoft (Hotmail, Outlook, Live, MSN);
* Comcast;
* Yahoo Mail;
* AOL Mail, etc.



 Gmail does not support FBL technology but uses an alternative mechanism for unsubscribing Gmail users from emails. It is a special List-Unsubscribe caption, which allows displaying the “Unsubscribe” button next to the “Report spam” button. In this case, the user is more likely to click the “Unsubscribe” button than report spam. All recipients who click the unsubscribe button or link will get the “Unsubscribed” response.
 




