


 The mobile application is used to work with Creatio on mobile devices and is a supporting tool to the primary Creatio application. You can use the configured mobile application for meetings, exhibitions, presentations, etc.
 





 Note.
 
 The mobile application is only available for users of the primary
 

 Creatio
 

 application and cannot be used by the portal users.
 




 To use a mobile application, you should perform some
 
[preliminary settings](/docs/8-0/user/platform_basics/mobile_app/setup/mobile_application_setup#title-773-9) 

 .
 



 You can configure the list of mobile application sections using the
 
mobile application wizard

 . To reduce the synchronization time between the mobile and primary applications, we recommend setting up only the sections that you will use.
 





 Attention.
 
 To ensure the correct operation of the mobile application, make sure the mobile application version is no lower than that of the Creatio primary application.
 




 After you
 
[install the mobile application and log in for the first time](#title-773-2) 

 , the application will be synchronized with your Creatio desktop application. Depending on the mobile app
 
[operation mode (online or offline)](#title-773-3) 

 , further synchronization steps may differ.
 



 You can set up automatic synchronization, switch workplaces, and view information about the last synchronization on the
 
[mobile application settings page](#title-773-9) 

 .
 








 System requirements for mobile devices
---------------------------------------------



 To install and use the Creatio mobile application, the user's phone/tablet must meet the system requirements below:
 





| 
 Characteristics
  | 
 iOS
  | 
 Android
  |
| --- | --- | --- |
| 
 Supported version (minimal)
  | 
 11.0
  | 
 7.0
  |
| 
 Recommended version
  | 
 Latest version available
  | 
 9.0
  |
| 
 Supported devices (minimal)
  | 
 iPhone 6s
  | 
 Nexus 7
  |
| 
 Recommended devices
  | * iPhone 8 or higher;
* iPad 3 or higher,
 | 
 Google Pixel or higher.
  |









 Install the app
----------------------



 Creatio mobile application is available on:
 


* The
 
[App Store](https://itunes.apple.com/us/app/creatio-mobile-7/id708432450?mt=8) 

 for iOS users.
* The
 
[Google Play Store](https://play.google.com/store/apps/details?id=com.creatio.mobileapp) 

 for Android users.



 The mobile application will be synchronized with Creatio upon the first login.
 





 Attention.
 
 A certificate signed by a certification authority is required to sync with Creatio on-site. Mobile application security policies do not support connections to sites that use self-signed certificates.
 




 Enter the address of the Creatio server, specify the workplace and tap the
 
 Continue
 
 button (Fig. 1) to log in to the mobile application. If SSO is configured, you will see a login and password form on the identity provider page. If SSO is not configured, enter your login and password and tap the
 
 Login
 
 button.
 





 Fig. 1
 

 Logging in Creatio mobile app
 

![scr_group_mobile_app_demo.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_preparation/scr_group_mobile_app_demo.png)





 Note.
 
 Connection protocols (HTTP://, HTTPS://) are determined by the application automatically. You can specify the connection protocol manually if the application is unable to determine the protocol.
 




 After this, the mobile application will start the synchronization process with the primary Creatio application. After the synchronization is complete, the mobile appl becomes operational.
 



 Tap the
 
 Demo login
 
 button to connect to the demo version. After this, the mobile application will be synchronized with the demo database.
 





 Note.
 
 Login and password are not required to access the demo version. The application opens automatically after the synchronization.
 






 Note.
 
 The
 
 Demo login
 
 button is displayed if you have not synchronized your app with a Creatio database yet. If you did, then to access the demo database you will need to
 
[clear the application cache](#title-773-9) 

 .
 









 Mobile application settings
----------------------------------



 Use the mobile application settings page to:
 


* Specify the connection parameters with the primary Creatio server
* Select a workplace and synchronize the mobile application
* Log out of the application
* Clear application cache (Fig. 2)



 To open the settings page, tap the
 
 Settings
 
 button in the main menu of the app.
 





 Fig. 2
 
 Mobile application settings page
 

![scr_group_mobile_app_settings.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_preparation/scr_group_mobile_app_settings.png)





 Note.
 
 To connect to a different Creatio server, enter the address in the
 
 Creatio server address
 
 field, and specify your username and password for that server. Then tap the
 
 Synchronization
 
 button.
 



### 


 Select a workplace



 To switch workplaces while working in the mobile application, tap the
 
 Workplace
 
 field, and select one of the available
 
workplaces

 . The mobile application will need to be synchronized again after switching to a different workplace (Fig. 3).
 





 Fig. 3
 
 Synchronizing the mobile application after switching to a new workplace
 

![scr_group_mobile_app_information_synchronization.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_preparation/scr_group_mobile_app_information_synchronization.png)





 Note.
 
 The workplaces of the mobile application are set up in the Mobile Application Wizard, which is available in the primary application.
 



### 



 Clear cache and synchronize



 During the synchronization with the primary Creatio application, the database structure and other information are downloaded by the mobile application.
 



 If the database structure changes (it does when you add new sections and details to the mobile application), the structure is updated in the mobile application. For proper synchronization of the modified structure, delete the outdated database structure and data that are stored in the cache of the mobile application. To do so, tap the
 
 Clear
 
 cache button (Fig. 4).
 





 Fig. 4
 
 Clearing mobile application cache
 

![scr_group_mobile_clear.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_preparation/scr_group_mobile_clear.png)





 Note.
 
 Clearing the cache will discard all changes in the mobile application that were not synchronized with the primary application. It is recommended to run the synchronization before clearing the cache.
 




 Message operation modes
-------------------------



 There are two modes available for the mobile application in Creatio: “online” and “offline”. You can select the mode in the “Mobile application operation mode” (MobileApplicationMode) system setting in the desktop application.
 





 Note.
 
 Regardless of the working mode, mobile devices only display data that the users have permission to access.
 



### 


 Online mode



 If you select the online operation mode, manual synchronization is not required. Synchronization with the Creatio server is performed automatically, in real-time, i.e., if you add a task using the mobile application, the task will be immediately displayed in the main application and vice versa. The
 
![scr_group_mobile_app_online_mode_0.png](/docs/sites/default/files/images/2020-12/scr_group_mobile_app_online_mode_0.png)

 icon is displayed in the top right corner of the app to indicate a stable Internet connection in the online operation mode.
 


### 
 Hybrid mode



**Hybrid mode** 
 is a type of online mode. It lets the users access the data seemingly in real-time, even without having a stable Internet connection. The hybrid mode
 **turns on automatically** 
 whenever the Internet connection disappears. Hybrid mode enables:
 


* Working with recent records in all sections. “Recent records” are the last 10 records that the user interacted with.
* Creating new records.
* Work with the schedule.



 The
 
![scr_group_mobile_app_hybrid_mode_0.png](/docs/sites/default/files/images/2020-12/scr_group_mobile_app_hybrid_mode_0.png)

 icon is displayed in the top right corner of the app to indicate no Internet connection in the hybrid operation mode.
 



 After the connection is restored, the app resumes real-time automatic synchronization with the primary application.
 





 Note.
 
 Note that hybrid mode is not available when using the “
 
[Field sales for Creatio](https://marketplace.creatio.com/app/field-sales-creatio) 

 ” and “
 
[Pharma Creatio](https://marketplace.creatio.com/app/pharma-creatio) 

 ” Marketplace applications.
 






 Attention.
 
 If the same record (for example, the duration of the activity) has been changed in both the desktop and the mobile application, the conditions for saving these changes after synchronization will depend on the order in which the changes were made. Creatio will save the latest changes.
 



### 


 Offline mode



 In the
 **offline** 
 mode, the mobile app user should synchronize periodically with the primary Creatio application. Synchronization with the primary application is performed via the DataService web service.
 



 Changes made to the mobile application are saved on the Creatio server only after synchronizing with the primary application. If there were any conflicts during synchronization, they will display in the synchronization log.
 



 To synchronize manually in the “offline” mode:
 


1. Tap the
 ![btn_group_mobile_menu.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_preparation/btn_group_mobile_menu.png)
 button and select
 
 Settings
 
 .
2. Tap
 
 Synchronization
 
 (Fig. 5) on the page that opens.
 





 Fig. 5
 
 Running synchronization in the mobile application
 

![scr_group_mobile_app_synchronozation.png](/guides/sites/en/files/documentation/user/en/mobile_app/BPMonlineHelp/chapter_mobile_preparation/scr_group_mobile_app_synchronozation.png)



 As a result, the data from the primary application will be displayed in the mobile application and the primary application will display the records that were created using the mobile application.
 





 Attention.
 
 If the same record (for example, the duration of the activity) has been changed in both the desktop and the mobile application, the conditions for saving these changes after synchronization will depend on the order in which the changes were made. Creatio will save the latest changes.
 




 For example, whenever an opportunity advances to the next stage, a business process creates new activity. When this happens, synchronization with the primary application is performed. The business logic of creating an activity is handled on the primary application, then the created activity is displayed in the mobile application.
 



 A user working in the “online” mode will not notice this because the application will be working directly with the server. The new activity will appear in the mobile application immediately after the corresponding business process completes, with no need for manual synchronization. Users who work in the “offline” mode will need to run synchronization for the activity to be displayed.
 


### 



 Synchronization log



 The synchronization log is available only in offline mode. The log displays the date of the last synchronization and any conflicts that occurred when records were last synchronized with the desktop application.
 



 The
 
 Log
 
 tab includes a list of all conflicts found during the previous synchronization. Conflict details are specified for each record individually.
 



 The
 
 Pending changes
 
 tab includes all data that were not yet exported to the desktop application during the last synchronization attempt.
 



 Depending on the conflict, clicking the record in the log will display the following actions:
 


* Revert changes
 
 - undo all changes and delete the record from the synchronization log. If triggered, the local copy of this record will be overwritten with the server (desktop application) copy. For example, your system administrator took away your rights to edit an account’s type. A conflict occurs once you edit the
 
 Type
 
 field and attempt to synchronize with the desktop application. To resolve this conflict, you can undo the changes and re-synchronize. Learn more about how to deal with synchronization conflicts that occur due to lack of permissions in the “
 
[Mobile application FAQ](/docs/8-0/user/platform_basics/mobile_app/faq/mobile_application_faq#title-771-2) 

 ” article.
* Go to record
 
 - opens the record edit page. For example, a field that could previously be left blank is now required. Creating a new account without populating this field will result in a conflict during the next synchronization attempt. To resolve this conflict, open the record edit page, populate the required field, and re-synchronize.
* Request access
 
 - opens your preferred mobile mail client and creates a template of a request to provide the permissions necessary to complete the synchronization.





 Note.
 
 To send requests to system administrators, please make sure that their correct email address is specified in the “Email for sending permission requests” system setting.
 





