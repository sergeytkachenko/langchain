


 Why won’t the mobile app sync in online mode (Error "Item% 24 batch not found)?
---------------------------------------------------------------------------------



 Online sync errors are often associated with the “on-site” deployment of Creatio. Certain combinations of the IIS, .NET Framework, and ASP.NET services screen special characters ($ character) in website URLs. The mobile app cannot connect to the Creatio website because of that.
 



 To omit the “$” character while generating request URLs, introduce a different type of query generation by setting up configuration files on the Creatio server. To do this:
 


1. Open the
 
 Creatio root directory path
 
 \Web.config file with any text editor, e.g. Notepad. Find the <appSettings> part and add the following line:
 






```

<add key="aspnet:UseLegacyRequestUrlGeneration" value="true" />
```





 Save the changes.
2. Make the same adjustments to the
 
 Creatio root directory path
 
 \Terrasoft.WebApp\Web.config configuration file.
3. Restart the web site in IIS and clear the Redis server cache.




 How to resolve the synchronization conflict in the offline mode?
-------------------------------------------------------------------



 If the conflict occurred because of access permission during the synchronization with the desktop application, you can resolve it by canceling the modifications you made in the mobile application.
 





 Case.
 
 The administrator has restricted the access rights to edit the account type for all employees (
 [Fig. 1](#XREF_85418_84)
 ). The mobile user changes the account type in the offline mode. During the synchronization process, the user gets a notification about conflict (
 [Fig. 2](#XREF_18480_85)
 ).
 






 Note.
 
 Managing user access permission to the system objects is covered in the "
 [Users and access management](https://academy.creatio.com/docs/user/setup_and_administration/user_and_access_management) 
 " guide.
 




 To resolve the conflict:
 


1. Tap the
 
 Review issues
 
 button.
2. Select a record that invoked a conflict of insufficient permissions in the synchronization log.
3. Tap the
 
 Revert changes
 
 button (
 [Fig. 1](#XREF_43545_86)
 ).
 





 Fig. 1
 

 The
 
 Revert changes
 
 action in the synchronization log
 


![scr_chapter_mobile_faq_colflict_record.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_faq/scr_chapter_mobile_faq_colflict_record.png)



 As a result, all changes made in the account’s record will be reverted and the record will be removed from the synchronization log. The local record will be updated with the latest data from the desktop application.
 



 You can send a request for access permission to an administrator. More details about actions with records in the log are described in a separate article.
 
[Read more >>>](/docs/8-0/user/platform_basics/mobile_app/setup/mobile_application_setup#HT_chapter_mobile_preparation_sync_log) 





 How to clear the mobile app cache?
------------------------------------



 You can clear the mobile app cache in one of the following options:
 


* Enter the
 
 Settings
 
 section of the mobile application and tap the
 
 Clear cache
 
 button (
 
[Fig.](#XREF_50926_86) 
 2
 
 ).





 Fig. 2
 

 Clearing mobile application cache
 


![chapter_mobile_faq_clear_cache.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_faq/chapter_mobile_faq_clear_cache.png)



* Log out of the application and log in to another Creatio site, for example, to a trial version. In this case, the app cache will be cleaned automatically.
* Perform the cache cleanup of the mobile device.





 Attention.
 
 After cleaning the mobile application cache, all data modifications that were made offline and not synchronized with the main application will be deleted.
 




 How can I set up push notifications for mobile application users?
-------------------------------------------------------------------



 Mobile application users will now receive push notifications and reminders with valuable updates, such as meeting reminders or feed notifications. The configuration of push notifications is performed in the "
 [BPMN process examples](https://academy.creatio.com/docs/user/bpm_tools/bpm_process_examples) 
 " guide.
 




