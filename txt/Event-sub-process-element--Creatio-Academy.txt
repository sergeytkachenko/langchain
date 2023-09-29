


 Use the
 
 Event sub-process
 
 element (Fig. 1) when you need to perform a sequence of tasks whenever a specific event occurs. Event sub-processes can be performed several times during business process execution and can be used for implementing cyclic or repeated activities.
 




 Fig. 1
 

 Event sub-process
 
 element with a
 
 Message
 
 start event and a process task placed inside it
 





![chapter_process_designer_event_subprocess_element.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/chapter_process_designer_event_subprocess_element.png)



 For example, during a sale process, a customer can modify the list of ordered products at any stage of the negotiations, any number of times. In this case, your sales process can include an event sub-process for updating the list of ordered products.
 



 In Creatio, an event sub-process is not a typical process element. Please take the following into account when creating event sub-processes:
 


* Unlike regular business process elements, the event sub-process is displayed as a separate diagram area. It is not supposed to connect with the rest of the diagram via flows.
* Any regular elements placed on the event sub-process (e.g., activities, gateways, events and sequence flows) are considered elements of that sub-process and will be executed only if the event sub-process is triggered.
* In Creatio, the event sub-process must always start with a
 [Message
 
 start event.](#HT_chapter_process_designer_elements_events_message_start) 
 The diagram of the event sub-process will be executed once for each execution of the corresponding
 [Throw message
 
 event](#HT_chapter_process_designer_elements_events_intermediate_throwing_message) 
 in a process instance.
* The
 [Terminate
 
 end event](#HT_chapter_process_designer_elements_events_terminate) 
 in an event sub-process flow will terminate the entire process. Normally, event sub-processes do not have the
 
 Terminate
 
 event, unless the function of the event sub-process includes terminating the entire process (e.g., the event sub-process handles the cancellation of a sale, etc.).



 [Event sub-process] operation
-------------------------------





|  |  |
| --- | --- |
| 
 Activation
  | 
 The
 
 Event sub-process
 
 element executes each time the
 [Message
 
 start event](#HT_chapter_process_designer_elements_events_message_start) 
 is triggered by the corresponding
 [Throw message
 
 event](#HT_chapter_process_designer_elements_events_intermediate_throwing_message) 
 (Fig. 2). Same event sub-process can be activated several times in a single process instance.
  |
| 
 Execution
  | 
 When the corresponding message is thrown by the process
 
 Throw message
 
 event, the
 
 Message
 
 start event activates its outgoing flow and enables the execution of the other actions in the event sub-process flow.
 

 The event sub-process actions are executed as regular elements of the current business process and do not interrupt its execution.
 

 Pending user actions of both the event sub-process and the regular process can be performed in any order by the users.
 

 Unlike regular
 [Sub-processes](#HT_chapter_process_designer_elements_sub_process) 
 , event sub-processes do not create a separate process instance in the
 
 Process Log
 
 section. The event sub-process tasks are displayed in the
 
 Process elements
 
 detail of the process log as regular business process tasks, in the order of their execution.
  |





 Fig. 2
 
 Execution diagram of a business process using the
 
 Event sub-process
 
 element, which was triggered twice during the instance shown
 





![scr_chapter_process_designer_event_sub_process_execution_diagram.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_event_sub_process_execution_diagram.png)




