


 The
 
 Simple
 
 start event (Fig. 1) is used when a process is initiated by a user directly, as opposed to being started by a
 [signal](https://academy.creatio.com/documents?id=7027) 
 or
 [timer](https://academy.creatio.com/documents?id=7133) 
 . The element initiates two types of processes:
 


* Processes that are run manually, by a Creatio user. Different methods of running business processes manually in Creatio are covered in a
 [separate article](https://academy.creatio.com/documents?id=7098) 
 .
* Processes that are used as
 [sub-processes](https://academy.creatio.com/documents?id=7041) 
 .





 Note.
 
 Start events initiate a new process instance and enable execution of all other elements on the process diagram. No process element (e.g., intermediate signals or timers) can be triggered before the start element is executed.
 






 Fig. 1 A business process initiated with a
 
 Simple
 
 start event
 




![scr_chapter_process_designer_simple_start_event.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_simple_start_event.png)



 For example, you can use the
 
 Simple
 
 start event in a “Corporate sale” business process, if it is usually initiated manually as a result of an executive decision.
 



 [Simple] start event operation
--------------------------------





|  |  |
| --- | --- |
| 
 Activation
  | 
 The element is triggered whenever a user runs the business process, e.g., by clicking the
 
 Run
 
 button in the
 
 Process library
 
 section or running a process from the
 [Command line](https://academy.bpmonline.com/documents/technic-sdk/7-13/command-line) 
 . Alternatively, the element can be triggered by the parent process, if the current process is run as a sub-process.
  |
| 
 Execution
  | 
 When triggered, the event activates its outgoing flows, which enables the execution of the other actions in the business process flow.
  |




 [Simple] start event parameters
---------------------------------





|  |  |
| --- | --- |
| 
 Run following elements in the background
  | 
 Select this checkbox, if you want any “User action” elements activated with the outgoing flows of the current element to run “in the background”. When process elements are executed in the background, their loading mask is not displayed, no windows pop up for the user, etc. The user will be able to interact with the elements via the
 
 Business process tasks
 
 tab of the communication panel.
  |





