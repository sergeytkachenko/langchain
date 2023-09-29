


 If you need to stop a process, you can cancel it.
 



 To
 **cancel a process instance** 
 :
 


1. Click
 ![btn_system_designer.png](/docs/sites/default/files/2020-11/btn_system_designer.png)
 to open the System Designer.
2. Under
 
 Processes
 
 , click
 
 Process log
 
 .
3. In the list of the process log, select a process instance that is in progress, and click the
 
 Cancel process
 
 button (Fig. 1).
 




 Fig. 1 – Cancel running processes
 

![Cancel running process](/docs/sites/en/files/2020-12/scr_chapter_processes_monitoring_cancel_process.png)



 This will terminate the process forcibly. The state of the selected process instance changes to “Canceled.”
 




 Select the needed record in the process log list and run the
 

 Cancel execution
 
 action (Fig. 2) to cancel a business process instance.
 




 Fig. 2 –
 
 Cancel Execution
 
 action on the process list toolbar
 

![Process log actions](/docs/sites/en/files/2020-12/section_process_log_actions.png)



 Use the
 
 Select multiple records
 
 command in the
 
 Actions
 
 menu
 **to cancel more than one record** 
 . Select processes to cancel and perform the
 
 Cancel Execution
 
 action in the
 
 Actions
 
 menu (Fig. 3).
 




 Fig. 3 – Canceling multiple business processes
 

![Cancel multiple](/docs/sites/en/files/2020-12/scr_chapter_process_execution_cancel_multiple_processes.gif)





 Note.
 
 The
 
 Cancel Execution
 
 action is available to the users who have access to the “Cancel running processes” (“CanCancelProcess”) system operation to access.
 




 Multiple process instances are canceled one by one. Upon running the
 
 Cancel Execution
 
 command, Creatio changes the status of all selected process instances to “Canceling.” As soon as a process instance is actually canceled, its status will change to “Canceled.”
 




