


 The
 
 Message
 
 start event (Fig. 1) is used to activate
 [event sub-processes](https://academy.creatio.com/documents?id=7042) 
 within a parent business process. Such event sub-processes are run through the
 [Throw message
 
 intermediate event](https://academy.creatio.com/documents?id=7034) 
 in the corresponding parent business process.
 




 Fig. 1
 

 Message
 
 start event (activating a sub-process)
 




![process_designer_event_subprocess_element_example.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/process_designer_event_subprocess_element_example.png)




 For example, your sales process can include an event sub-process during which the list of ordered products is modified. The customer can modify the list of ordered products at any time, any number of times. Each case of modifying the order must be followed with a
 
 Throw message
 
 event, which would activate the
 
 Message
 
 start event of the order modification event sub-process.
 



 [Message] start event operation
---------------------------------





|  |  |
| --- | --- |
| 
 Activation
  | 
 The element is triggered by a
 [Throw message
 
 event](https://academy.creatio.com/documents?id=7034) 
 on the same business process diagram.
  |
| 
 Execution
  | 
 When activated, the
 
 Message
 
 start event initiates the event sub-process. The
 
 Message
 
 start event activates its outgoing flows and enables execution of the other actions in the event sub-process. Same
 
 Message
 
 start event can be triggered multiple times within a process instance.
  |




 [Message] start event parameters
----------------------------------





|  |  |
| --- | --- |
| 
 Which message event should start the process?
  | 
 Enter the name of the message event that will activate this element. Make sure that the message name matches the one specified in the
 
 Which message to generate?
 
 field of the
 
 Throw message
 
 element (Fig. 2 and Fig. 3) on the same process diagram.
  |
| 
 Run following elements in the background
  | 
 Select this checkbox, if you want any “User action” elements activated with the outgoing flows of the current element to run “in the background”. When process elements are executed in the background, their loading mask is not displayed, no windows pop up for the user, etc. The user will be able to interact with the elements via the
 
 Business process tasks
 
 tab of the communication panel.
  |





 Fig. 2
 
 Specifying the name of a message that activates the
 
 Message
 
 start event
 




![scr_chapter_process_designer_message_start_event_name.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_message_start_event_name.png)





 Fig. 3
 
 Example of a
 
 Throw message
 
 element that generates the message event
 




![scr_chapter_process_designer_throw_message_event_name.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_throw_message_event_name.png)





