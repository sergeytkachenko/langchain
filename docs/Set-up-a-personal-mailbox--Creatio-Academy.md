


 Each Creatio user can set up an integration with one or more mailboxes and use them to send and receive emails. Creatio uses the emails to enrich contact data and links the emails to existing objects: accounts, contacts, etc.
 



 Set up an email account of a preconfigured provider
-----------------------------------------------------



 You need an email provider integration to add an email account. By default, Creatio is integrated with AOL, Gmail, Yahoo and other email providers. To add an account to Creatio, configure secure access for external apps. Perform the setup in your mailbox. The settings depend on the provider. Learn more in a separate article:
 [Set up a secure mailbox connection](https://academy.creatio.com/documents?id=1843) 
 .
 



 If you use a different provider, set up the synchronization by the
 [IMAP/SMTP](https://academy.creatio.com/documents?id=1415) 
 or
 [Exchange](https://academy.creatio.com/documents?id=1418) 
 protocol. The setup is performed by a system administrator.
 



 To set up an email account of a preconfigured provider:
 


1. Open the
 
 Email
 
 tab on the communication panel →
 ![btn_detail_menu00001.png](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_mailbox_synchronization/btn_detail_menu00001.png)
 →
 
 New email account
 
 . This opens the account authentication window.
2. Enter the email address and click
 
 Next
 
 . Creatio identifies the email provider according to the domain name.
3. If Creatio cannot identify the provider automatically, a window opens. Specify the provider manually in the window (Fig. 1). As a result, the connection parameters of the new email provider will appear in the
 
 Email providers domains
 
 lookup. Creatio will recognize the provider by the domain name when you set up new email accounts.
 




 Fig. 1 Select an email provider for synchronization
 

![scr_chapter_imap_synchronisation_providers_list.png](/docs/sites/en/files/images/Setup_and_Administration/set_up_personal_email/scr_chapter_imap_synchronisation_providers_list.png)
4. Enter the email address and click
 
 Next
 
 . Creatio will request the password to log in to your account.
5. Enter the password for external app access generated by the provider and click
 
 Sign in
 
 (Fig. 2).
 




 Fig. 2 Sign in to an email account
 

![scr_chapter_imap_synchronisation_auth_formt.png](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_mailbox_synchronization/scr_chapter_imap_synchronisation_auth_formt.png)



 As a result, Creatio will add an email account with default parameters. You will receive a notification from which you can proceed to upload emails to Creatio or perform
 [additional account setup](https://academy.creatio.com/documents?id=1918) 
 , for example, add a signature or change the email upload period.
 



 Set up an email account on a corporate domain
-----------------------------------------------



 If you use a corporate email domain, set up integration with the corporate email provider by the
 [IMAP/SMTP](https://academy.creatio.com/documents?id=1415) 
 or
 [Exchange](https://academy.creatio.com/documents?id=1418) 
 protocol and match domain names to the corresponding email providers. The setup is performed by a system administrator.
 





 Note.
 
 Gmail supports authentication without providing the login and password (OAuth connection). Before you set this up, register Creatio in Google Workspace. Learn more in a separate article:
 [Register Creatio application in Google Workspace](https://academy.creatio.com/documents?id=1758) 
 .
 




 To set up an email account on a corporate domain:
 


1. Open the
 
 Email
 
 tab on the communication panel →
 ![btn_detail_menu00002.png](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_mailbox_synchronization/btn_detail_menu00002.png)
 →
 
 New email account
 
 . This opens the account authentication window. This method of adding the account does not depend on the availability of configured accounts.
2. Enter the email address and click
 
 Next
 
 . Creatio identifies the email provider according to the domain name.
3. If Creatio cannot identify the provider automatically, a window opens. Specify the provider manually in the window. As a result, the connection parameters of the new email provider will appear in the
 
 Email providers domains
 
 lookup. Creatio will recognize the provider by the domain name when you set up new email accounts.
 





 Note.
 
 A popular email provider, such as Yahoo or Gmail, can service a mailbox with a corporate domain address. If you do not know which email provider to choose, verify this with your system administrator. To log in to Gmail mailbox without providing the login and password (OAuth connection), register Creatio in Google Workspace first. Learn more in a separate article:
 [Register Creatio application in Google Workspace](https://academy.creatio.com/documents?id=1758) 
 .
4. Enter the mailbox password in the field that appears and click
 
 Sign in
 
 (Fig. 3).
 




 Fig. 3 Sign in to an email account of a corporate provider
 

![scr_chapter_imap_synchronisation_auth_custom.png](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_mailbox_synchronization/scr_chapter_imap_synchronisation_auth_custom.png)



 As a result, Creatio will add an email account with default parameters. You will receive a notification from which you can proceed to upload emails to Creatio or perform
 [additional account setup](https://academy.creatio.com/documents?id=1918) 
 , for example, add a signature or change the email upload period.
 




