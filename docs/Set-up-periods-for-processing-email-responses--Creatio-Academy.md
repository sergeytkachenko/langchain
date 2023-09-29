


 By default, Creatio automatically processes email response data once per several minutes. We recommend that you
 **stop parsing email responses** 
 for the time of integration sessions between Creatio and third-party systems to avoid data deadlocks. You can stop parsing every day at a specified time.
 



 The setup procedure is as follows:
 


1. In the
 
 Emails
 
 section, select
 
 Bulk email settings
 
 in the
 
 Actions
 
 menu.
2. On the opened page, select the
 
 Response parsing settings
 
 tab and specify the time when the response parsing should be stopped. Specify the preferred time frame for parsing email responses in the
 
 From
 
 and
 
 To
 
 fields (Fig. 1). Save the changes.
 





 Fig. 1
 

 The
 
 Response parsing settings
 
 tab
 

![section_email_setup_page_responses.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_emails_set_time/section_email_setup_page_responses.png)



 At the figure above, you can see an example of settings enabling the response parsing process stop daily from 1:00 to 4:00 AM. The changes will apply as soon as you save the settings. In this case, the response parsing will resume at 4:01 am.
 



 Response parsing time frames on this tab are displayed in the
 **current user’s time zone** 
 . The parsing process will stop in according to the time zone of the user, specified in the “
 **System operations user** 
 ” (SystemUser) system setting. The Supervisor user is specified in this system setting by default.
 





 Note.
 
 Specify the time zone of a user in the user profile. Read more in the
 [“User profile](https://academy.bpmonline.com/documents?product=base&ver=7&id=1012) 
 article. The list of available time zones is configured in the
 
 Time zones
 
 lookup.
 




 If you leave the
 
 From
 
 and
 
 To
 
 fields unpopulated or populate only one value, the response parsing process will be working continuously.
 




