


 The
 
 Wait for timer
 
 intermediate event (Fig. 1) is used to pause the process for a certain period of time. The process will resume in the background mode.
 




 Fig. 1
 
 Wait for timer
 
 intermediate event
 




![scr_chapter_process_designer_wait_timer.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_wait_timer.png)




 For example, a process can create a task for the user to check for invoice payment five days after the invoice had been issued.
 



 [Wait for timer] event operation
----------------------------------





|  |  |
| --- | --- |
| 
 Activation
  | 
 After the element incoming flow is activated, it starts the countdown.
  |
| 
 Execution
  | 
 When the specified period of time expires, the
 
 Wait for timer
 
 element activates its outgoing flows.
  |




 [Wait for timer] event parameters
-----------------------------------





|  |  |
| --- | --- |
| 
 Start in (sec.)
  | 
 Specify the process pause duration in seconds (e.g., specify “3600” for 1 hour). This field is populated using the
 parameter value window
 .
  |





