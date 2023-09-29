


 If you have several recipients with the same email address in your database, you can merge duplicates and avoid sending emails to the same email address. Use the
 **Prevent to send duplicated emails to recipients with the same address** 
 system setting for this purpose. If the system setting is enabled and the email audience has several contacts with the same email address, Creatio will send a single email to one of these contacts, selected at random. The email response of the rest of the contacts with the same email address will be “Canceled (Duplicate email).”
 



 The setup procedure is as follows:
 


1. Open the system designer by clicking the
 
![system_designer.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_emails_avoid_duplicates/system_designer.png)

 button.
2. Click “
 **System settings** 
 ” in the “System setup” block.
3. Open the “
 **Prevent to send duplicated emails to recipients with the same address** 
 ” (“PreventDuplicatesSending” code) system setting and select the
 
 Default value
 
 checkbox on the opened page.
4. Click
 
 Save
 
 .



 As a result, Creatio will search for duplicate email addresses before sending
 **bulk emails** 
 . If Creatio detects the same email address for several contacts, the email will be sent to only one of them.
 



 Creatio removes duplicate email addresses from
 **trigger emails** 
 only in the same campaign launch. If an email address that has already received a trigger email is included in another campaign launch, for example, after a re-entry, Creatio sends another trigger email to the email address.
 




