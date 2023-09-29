


 Regular process monitoring allows you to analyze employee productivity and to track “bottlenecks” in diagrams for optimization.
 



 All history of business processes is kept in the
 
 Process log
 
 section. The section is designed for managing the business processes that have been initiated (process instances).
 



 A business process can be started several times by different users at different times. A new “process instance” is created on each launch of the process. Each instance of the process corresponds to a record in the
 
 Process log
 
 section. Records appear in the section automatically, each time a business process starts. Information about each instance displays as a separate log record. The process log records cannot be edited.
 





 Note.
 
 To access the
 
 Process log
 
 , a user requires permission for the following system operation: “Access to "Process log" section” (“CanManageProcessLogSection” code). Learn more about using system operations: in a separate article:
 [System operation permissions](https://academy.creatio.com/documents?id=258) 
 .
 




 View process history
----------------------



 Once a business process is initiated, information about the process instance is saved in the
 
 Process log
 
 section. The log record page contains the name of the employee who initiated the process, the status of the process instance (“Running” or “Completed”), and a list of the activated process steps.
 



 To view process history:
 


1. Click
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_monitoring/btn_system_designer.png)
 to open the System Designer.
2. Click
 
 Process log
 
 under
 
 Processes
 
 .
3. Select a business process and click
 
 Open
 
 (Fig. 1).
 




 Fig. 1 Select a process
 

![Select a process](/docs/sites/en/files/2020-12/scr_chapter_process_monitoring_open_process_history.png)



 As a result, Creatio will open the process log page that contains the process execution history (Fig. 2).
 




 Fig. 2 Process execution history
 

![View log](/docs/sites/en/files/2020-12/scr_chapter_processes_monitoring_view_log.png)



 If this is a sub-process, you can run the
 
 Parent process
 
 action to open the parent process page quickly (Fig. 3).
 




 Fig. 3 Opening the parent process page
 

![subprocess_to_parent_process.gif](/docs/sites/en/files/images/BPM_Tools/view_process_properties/subprocess_to_parent_process.gif)



 Archive the process log records
---------------------------------



 To speed up the process log, Creatio automatically deletes or archives completed and canceled processes that remain in the
 
 Process log
 
 section list for more than a set period. The default period is 30 days. You can manage the archival status in the “Archive data on deletion from log” (“ArchiveProcessLogOnDeletion” code)
 [system setting](https://academy.creatio.com/documents?id=1259) 
 .
 





 Note.
 
 By default, Creatio instances originally deployed as version 8.0.2 and earlier archive the old records, while Creatio instances originally deployed as version 8.0.3 and later delete the records.
 




 You can change the period for the process records to be displayed in the
 
 Process log
 
 section before they are automatically deleted or archived. To do this, use one of the following system settings:
 


* “Process log archiving period (days)” (“ProcessLogArchivingPeriod” code) for Creatio version 8.0.2 and earlier
* “Log data expiration period (days)” (“ProcessLogExpirationPeriod” code) system setting for Creatio version 8.0.3 and later



 The data of the archived process instances remain available in the archive, including record history and connections to other system objects.
 



 To view the data, select the “Archived” checkbox in the filter area of the
 
 Process log
 
 section.
 



 To avoid increasing the amount of data in the database tables and overloading the system, Creatio automatically deletes the records archived for longer than the period specified in the “Archive data expiration period (days)” (“ProcessLogArchiveDataExpirationTerm” code) system setting.
 



 You can manage the archive operations using the
 
 Settings
 
 action (Fig. 4).
 




 Fig. 4
 
 Settings
 
 option in the
 
 Process log
 
 section
 

![Log archiving](/docs/sites/en/files/2020-12/section_process_log_archiving.png)



 The
 
 Settings
 
 action opens the list of system settings that manage the process log maintenance (the settings located in the
 
 Process log
 
 folder of the
 
 System settings
 
 section). These system settings let you manage:
 


* How long the process instances in the “Error” state stay active in the process log.
* How often to archive the log records for completed and canceled processes.
* How long to store the archived records.



 Learn more in a separate article:
 [Manage system settings](https://academy.creatio.com/documents?id=269) 
 .
 




