


 Creatio will not add a mailbox
--------------------------------



 To connect a mailbox, create a
 **third-party app password** 
 and use it when you register a mailbox.
 



 Learn more about setting up the third-party app password in your email provider documentation:
 


* [AOL](https://help.aol.com/articles/Create-and-manage-app-password)
* [Gmail](https://support.google.com/accounts/answer/185833?hl=en)
* [Yahoo](https://help.yahoo.com/kb/generate-manage-third-party-passwords-sln15241.html)
* [Zoho](https://help.zoho.com/portal/en/kb/bigin/channels/email/articles/generate-an-app-specific-password#To_generate_app_specific_password_for_Zoho_Mail)
* [Microsoft Exchange](https://support.microsoft.com/en-us/account-billing/create-app-passwords-from-the-security-info-preview-page-d8bc744a-ce3f-4d4d-89c9-eb38ab9d4137)





 Attention.
 
 Before you add a
 **Microsoft Exchange mailbox** 
 , add or set up your email provider. Learn more about setting up the email provider in a separate article:
 [Set up the Microsoft Exchange and Microsoft 365 services](https://academy.creatio.com/documents?id=1418&anchor=title-192-1) 
 .
 




 “Need Admin Approval” error occurs when you connect an Office365 mailbox
--------------------------------------------------------------------------



 After you set up OAuth for Office365, “
 
 Need admin approval
 
 ” error can occur when you add a mailbox. The following combination of settings causes the error:
 


* Admin approval is required before you can use the app.
* Requests to connect the app are not sent to the admin.



 If the error occurs, the
 **user** 
 must contact the system administrator.
 



 To let the user add the Office365 mailbox, the
 **system administrator** 
 must take the following steps:
 


1. Allow user consent for low impact apps.
 




 Fig. 1 Allow consent
 

![scr_chapter_low_impact.png](/docs/sites/en/files/images/Setup_and_Administration/set_up_personal_email/scr_chapter_low_impact.png)
2. Add
 
 EWS.AccessAsUser.All
 
 to the index of low impact permissions.
 




 Fig. 2 Add EWS.AccessAsUser.All
 

![scr_chapter_ews_access.png](/docs/sites/en/files/images/Setup_and_Administration/set_up_personal_email/scr_chapter_ews_access.png)



 The sender’s name is different from Creatio username
------------------------------------------------------



 To ensure the email displays the sender’s name correctly, change the name directly in the settings of the mail server that manages emails.
 



 Is it possible to set up two OAuth providers simultaneously?
--------------------------------------------------------------



 At this time, it is not possible to configure more than one OAuth provider for a single Creatio instance.
 




