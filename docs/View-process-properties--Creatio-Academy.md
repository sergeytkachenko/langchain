


 The process properties page contains complete information on the business process structure, starting conditions, execution, and use, as well as links to other processes.
 



 To display the process properties page:
 


1. Click
 ![btn_system_designer.png](/docs/sites/default/files/2020-11/btn_system_designer.png)
 to open the System Designer.
2. Click
 
 Process library
 
 under
 
 Processes
 
 .
3. Select the needed process from the section list and click
 
 Properties
 
 .



 A process properties page will open in a separate window (Fig. 1).
 




 Fig. 1 – Process properties page
 

![src_process_library_proc_characteristics_page.png](/docs/sites/en/files/images/BPM_Tools/view_process_properties/src_process_library_proc_characteristics_page.png)



 View the general process information on the page that opens:
 


* Process name displayed in the
 
 Run process
 
 menu and used in the command line when running processes.
* Name – a unique identifier of the process in Creatio.
* Package name where the process is saved.
* The number of the current business process version.
* A checkbox that identifies process status.
   

 Learn more about activating and disabling business processes in the
 [Activate process](https://academy.creatio.com/documents?ver=7&id=2323) 
 and
 [Disable (deactivate) process](https://academy.creatio.com/documents?ver=7&id=7107) 
 articles respectively.



 The same values are available as process proprieties in the process designer.
 



 Select the
 
 Trace enabled
 
 checkbox in process properties to trace the parameter values during the process execution. Learn more about tracing in the
 [Trace process parameter values](https://academy.creatio.com/documents?ver=7&id=7149) 
 article.
 



 You can also select the
 
 Display in run process button list
 
 checkbox to display the process in the quick launch list (opened by clicking
 ![btn_com_sidebar_start_process.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/section_process_library/btn_com_sidebar_start_process.png)
 on the side panel).
 



 View the process version
--------------------------



 The
 
 Process versions
 
 tab displays information about process versions. The data cannot be edited and are added to the detail automatically, each time a new process version is saved.
 



 The following data are available:
 


* Title – the process version number.
* Date when the process version was saved.
* The package where the process version was saved.
* The process version number.
* Indicates if the process version is the one currently used. All new instances of this business process will be run using the actual version.



 To set a process version as actual, select it in the list and click
 
 Set as actual version
 
 in the
 ![btn_products_change_field.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/section_process_library/btn_products_change_field.png)
 button menu.
 



 Only one of the versions of the same process can be set as actual. Any version can be used as a sub-process.
 





 Note.
 
 Creatio saves the actual version of the process directly to the package. If you
 
 save the package as an archive
 
 and
 
[install the package in a different environment](/docs/7-18/developer/development_tools/delivery/workspaceconsole/overview) 

 , the most actual version of the process will be transferred with the package. Creatio will always determine the final current version of the process based on which package is higher in the hierarchy.
 





 View the ways to start a process
-----------------------------------



 The
 
 Run options
 
 tab contains information about all options for launching the business process, both manual and automatic. All information on this tab is added automatically and is unavailable for editing.
 



 The following data are available:
 


* The
 
 Launch from sections
 
 detail contains a list of sections in which you can run this business process. If a section is in the list of the
 
 Launch from sections
 
 detail, then this business process will be available in the menu of the
 
 Run process
 
 button in the section’s list and record page.
* The
 
 Launch from details
 
 detail contains a list of details in which you can run this business process.
* The
 
 Used as sub-process in processes
 
 detail contains the list of processes where the current process is used as sub-process.
* The
 
 Scheduled launch
 
 detail contains information about
 [start timer events](/docs/node/1682/%26#9;) 
 used in the process. The data is added to the detail automatically and cannot be edited.
* The
 
 Launch by signals
 
 detail contains information about
 [start signal events](/docs/node/1680/%26#9;) 
 used in the process. The records are added to the detail automatically if a
 
 Start signal
 
 element exists on the process diagram.




 View sub-processes
---------------------



 The
 
 Sub-processes
 
 tab contains the list of processes used by the current process as sub-processes. The records are added to the detail automatically if a
 
 Sub-process
 
 element exists on the process diagram.
 



 The following information is available on the
 
 Sub-processes
 
 tab:
 


* Process name – the title of the process used a sub-process. Clicking the title will open the sub-process properties page.
* Date when the used version of the sub-process was created.
* Date when the used version of the sub-process was modified.
* A checkbox that identifies the sub-process status.



 View process logs
-------------------



 The
 
 Process log
 
 tab contains information about all instances of the current process and its current status. The records are added automatically, each time the process is run.
 



 The following information is available on the
 
 Process log
 
 tab:
 


* Title – the process version name.
* The version number used in the process instance.
* Owner – the user on behalf of which the process has been launched.
* Status of the launched process, for example, “Completed” or “Running.”
* Start date and time of the process instance.
* End date and time of the process instance.




