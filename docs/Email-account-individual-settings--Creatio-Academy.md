



 Email accounts are added with default parameters. For each added email account, you can configure:
 


* email downloading parameters;
* email sending parameters;
* email signatures.





 Note.
 
 If you have configured the synchronization with the MX Exchange mailbox, the
 
 Meetings and tasks
 
 and
 
 Contacts
 
 tabs will be displayed at the email account settings page. Here you can configure parameters of synchronization of MS Exchange calendar and contacts.
 [Read more >>>](https://academy.creatio.com/docs/user/setup_and_administration/base_integrations/microsoft_email_contacts_and_calendar) 





 You can go to the mailbox settings directly from the mailbox registration notification or by selecting the account in the
 
 Edit email accounts
 
 menu of the
 ![btn_com_roles_actions_menu.png](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_mailbox_synchronization/btn_com_roles_actions_menu.png)
 button.
 




 Fig. 1 Edit page of the email account settings
 

![](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_mailbox_synchronization/scr_chapter_imap_synchronisation_edit_settings_page.png)



 Receive emails in Creatio
---------------------------


1. To receive emails from the mailbox, toggle on the
 
 Download mail for period
 
 switch and specify the time interval (for example, day, week, month) for which emails will be downloaded to the system at the first synchronization.
 



 You can change how often Creatio will synchronize the mailbox in the “Mailbox synchronization interval” (“MailboxSyncInterval” code)
 [system setting](https://academy.creatio.com/docs/documents?ver=7&id=269) 
 .
2. Select the
 
 Automatically download new emails
 
 checkbox to download incoming emails automatically.
3. Select the
 
 Download all emails from mailbox
 
 option to download all messages from the mailbox or the
 
 Download emails from customized folders
 
 option to download messages from specific folders only.
4. To download emails from specific folders only, select the
 
 Download emails from customized folders option
 
 , click the
 
 +
 
 button to display the folders of the specified account and select folders from which you need to receive emails (
 [Fig. 2](#XREF_67143_3)
 ).
 

 Fig. 2
 
 Specifying synchronization folders
 

![](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_mailbox_synchronization/chapter_imap_synchronization_yahoo_folders_select.png)
5. Save the changes.





 Note.
 
 If you only select a parent folder for downloading emails, the messages from the nested folders will not be downloaded to Creatio. Select the nested folders to download emails from them.
 





 Send emails from Creatio
---------------------------



 To reply to emails directly from Creatio, set up email sending parameters. To do this:
 


1. Toggle on the
 
 Send emails using this mailbox
 
 switch to use the mailbox for sending the emails. If the switch is disabled, the mailbox will not be available for selection on the email edit page, as well as in the corresponding business process and case elements.
2. Select the
 
 Set “email address” as default sender address
 
 checkbox to use the mailbox by default. The mailbox address will be specified by default in the
 
 From
 
 field for new emails.
3. Save the changes.




 Configure an email signature
-------------------------------



 To add a signature to outgoing emails, select the
 
 Add signatures to outbound emails
 
 checkbox and add the signature text in the input area below (
 [Fig. 3](#XREF_90883_398)
 ). Save the changes.
 




 Fig. 3
 
 Adding signatures to outgoing emails
 

![](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_mailbox_synchronization/email_signature_paste_very_slow.gif)





 Note.
 
 You can copy a signature from your mail client and paste it to the text area. In some browsers, only one image can be copied to the signature template at a time from the clipboard. If your signature contains several images, the remaining images must be added one by one.
 





