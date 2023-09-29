


 Use the mailbox synchronization setup page to set up the synchronization of Creatio activities with Microsoft Exchange or Microsoft 365 tasks and meetings (Fig. 1). You can open the page in several ways:
 


* Click
 ![btn_com_roles_actions_menu.png](/guides/sites/en/files/documentation/user/en/base_integrations/BPMonlineHelp/synchronize_calendar_MSExchange_Microsoft/btn_com_roles_actions_menu.png)
 →
 
 Edit email accounts
 
 in the communication panel.
* Select
 
 Actions
 
 →
 
 Synchronize activities
 
 →
 
 Set up...
 
 in the
 
 Activities
 
 section.



 The command contains the name of the account, for example,
 
 Set up john.best@mycompany.com
 
 .
 




 Fig. 1 Set up the synchronization of Creatio activities with Microsoft Exchange calendar
 

![scr_chapter_exchange_synchronisation_calendar_synch.png](/guides/sites/en/files/documentation/user/en/base_integrations/BPMonlineHelp/synchronize_calendar_MSExchange_Microsoft/scr_chapter_exchange_synchronisation_calendar_synch.png)



 Creatio uses only the main Exchange calendar (default calendar) for synchronization. The records of additional calendars are not imported. Learn more about setting up the default calendar in
 [Microsoft documentation](https://support.microsoft.com/en-us/office/set-default-calendar-7c546486-0c7c-4870-964a-0d6eb4de83e0) 
 .
 



 Set up the import of activities into Creatio
----------------------------------------------



 To set up the import of Microsoft Exchange or Microsoft 365
 **meetings** 
 into Creatio:
 


1. Go to the
 
 Meetings and tasks
 
 tab and enable the
 
 Import meetings
 
 toggle.
2. Select
 
 Import all appointments and meetings
 
 to import all records from Microsoft Exchange or Microsoft 365 calendars.
 



 If you only want to import records from the selected calendars, select
 
 Import appointments and meetings from specific MS Exchange calendars
 
 . Expand the index of calendars and select the calendars to import.
3. Select the
 
 Import tasks
 
 checkbox and if necessary, select folders whose tasks to import.
4. Click
 
 Save
 
 on the mailbox synchronization setup page.
 



 As a result, Creatio will add the calendar tasks. In this case, only the tasks owned by the current Creatio user will be imported. Set up the import of
 **tasks** 
 similar to the import of meetings.



 Set up the export of activities from Creatio
----------------------------------------------



 To set up the export of Creatio activities to Microsoft Exchange or Microsoft 365:
 


1. Go to the
 
 Meetings and tasks
 
 tab and enable the
 
 Export activities
 
 toggle.
2. Select
 
 Export all tasks and meetings
 
 to export all activities to which you have access.
 



 If you only want to export activities from specific folders, select
 
 Export tasks and meetings from specific folders
 
 . The index of folders corresponds to the folders configured in the
 
 Activities
 
 section.
3. Click
 
 Save
 
 on the mailbox synchronization setup page.
 



 As a result, when exporting tasks that have the
 
 Display in calendar
 
 checkbox selected, Mircosoft Exchange or Microsoft 365 will create activities of the “Appointment” type. When exporting tasks that have the
 
 Display in calendar
 
 checkbox cleared, Microsoft Exchange or Microsoft 365 will create activities of the “Task” type.



 Synchronize activities with Microsoft Exchange and Microsoft 365
------------------------------------------------------------------



 Creatio can synchronize activities with the Exchange server automatically. To enable automatic synchronization, open the mailbox synchronization setup page, enable the
 
 Synchronize activities automatically
 
 toggle, and select the date in the
 
 Import activities starting from
 
 field. To perform the synchronization immediately, open the
 
 Activities
 
 section, click
 
 Actions
 
 →
 
 Synchronize activities
 
 →
 
 Synchronize now
 
 .
 




