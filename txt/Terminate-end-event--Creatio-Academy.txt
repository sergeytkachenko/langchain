


 Use the
 
 Terminate
 
 event (Fig. 1) to terminate a process instance immediately. This event is the last element in the process diagram.
 





 Fig. 1
 
 Terminate
 
 end event
 




![scr_chapter_process_designer_terminate_event.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_terminate_event.png)



 Unless a
 
 Terminate
 
 event is activated in a process instance, it will remain active, until
 [canceled](https://academy.creatio.com/documents?id=7106) 
 in the
 
 Process log
 
 section.
 



 [Terminate] end event operation
---------------------------------





|  |  |
| --- | --- |
| 
 Activation
  | 
 When the
 
 Terminate
 
 end event incoming flow is activated, the whole business process terminates. If there are any process elements that have not been executed before activation of the
 
 Terminate
 
 end event incoming flow, such elements are disregarded.
  |
| 
 Execution
  | 
 The
 
 Terminate
 
 end event is not supposed to have any outgoing flows. Any process parameter values will be recorded as the outgoing parameter values of the completed process instance.
  |






 Attention.
 
 Business processes with several branches that have the
 
 Terminate
 
 end event in them may end as soon as the first branch activates the
 
 Terminate
 
 event. The other branches in this case will not be executed.
 









