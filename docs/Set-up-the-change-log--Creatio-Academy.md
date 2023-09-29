


 The
 **change log** 
 records changes to business data. You can use it for things like tracking product price or account balance changes.
 



 The
 **audit log** 
 records system events, system settings, and system data. Learn more in a separate article:
 [Set up the audit log](https://academy.creatio.com/documents?id=1260) 
 .
 



 The change log is disabled by default. Follow the steps in this article to enable this feature.
 



 To set up logging, you can use either the
 
 Change log
 
 section or any other Creatio section, lookup or detail.
 





 Example.
 
 Set up logging of changes in contacts’ phone numbers and emails.
 




 Emails, mobile and work phones are available in the contact profile, so logging must be enabled in the
 
 Contacts
 
 section on the column level.
 





 Note.
 
 If you use a load balancer to ensure fault tolerance of your Creatio application, perform the setup on one Creatio instance, then transfer settings to other instances. The setup process applies to Marketplace apps, custom packages, and other settings that require compilation. Learn more in a separate article:
 [Compile an app on a web farm](https://academy.creatio.com/documents?id=2410) 
 .
 




 Method 1. Set up logging in the [Change log] section
------------------------------------------------------





 Note.
 
 We recommend setting up logging only for columns whose values you need to track. With large databases, logging a significant number of objects and columns might reduce Creatio’s performance.
 



1. Open the system designer. For example, click the
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/set_up_change_log/btn_system_designer.png)
 button.
2. Click “Change log” in the “Users and administration” block.
 





 Note.
 
 You must have permission to the “Access to "Change log" section” (the “CanManageChangeLog” code) system operation to manage the
 
 Change Log
 
 section. Learn more in a separate article:
 [System operation permissions](https://academy.creatio.com/documents?id=258) 
 .
3. Find the needed section object, detail, or lookup in the object list. For example, set the “Sections” filter (Fig. 1).
 




 Fig. 1 The object filter in the change log
 

![scr_section_change_log_choosing_object.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/set_up_change_log/scr_section_change_log_choosing_object.png)
4. Select the section from the list or find it using the search bar (Fig. 2). Click the title of the needed object. For example, the “Contact” object. This will open a new page.
 




 Fig. 2 The search bar in the change log
 

![scr_section_change_log_wnd_find_object.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/set_up_change_log/scr_section_change_log_wnd_find_object.png)
5. Enable logging on the page that opens via the corresponding switch.
 





 Note.
 
 If you save the changes on this step, Creatio will log the record create, update, and delete operations.
6. Set up the list of columns for logging when a record is changed. For example, use the
 
 Email
 
 ,
 
 Mobile phone
 
 , and
 
 Business phone
 
 columns (Fig. 3).
 



 Click
 
 Add
 
 to add a new column. Hover over the column title and click
 ![btn_delete.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/set_up_change_log/btn_delete.png)
 to delete an added column.
 




 Fig. 3 The column logging setup
 

![scr_section_change_log_choosing_column.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/set_up_change_log/scr_section_change_log_choosing_column.png)
7. Click
 
 Apply
 
 to save the changes.
 



 After you apply the settings, Creatio will start monitoring the changes and recording them to the change log.



 Method 2. Set up logging in a section, lookup or detail
---------------------------------------------------------


1. Open the needed section, lookup, or detail. For example, the
 
 Contacts
 
 section.
2. Click
 
 Actions
 
 →
 
 Change log setup
 
 (Fig. 4).
 




 Fig. 4 Set up the change log in the Contacts section
 

![scr_section_change_log_wnd_set_section.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/set_up_change_log/scr_section_change_log_wnd_set_section.png)





 Note.
 
 If you cannot see
 
 Change log setup
 
 in the action list, make sure you have permission to the “Access to "Change log" section” (the “CanManageChangeLog” code) system operation. Learn more in a separate article:
 [System operation permissions](https://academy.creatio.com/documents?id=258) 
 .
 




 As a result, the change log setup page of the
 
 Contacts
 
 section will open. Follow
 **steps 5 through 7** 
 from the
 **Method 1** 
 to complete the setup.
 




