


 The
 
 Throw signal
 
 intermediate event (Fig. 1) is used to broadcast signals that can be caught by corresponding process elements in any business process. It works in the same manner as the
 [Throw message
 
 intermediate event](https://academy.creatio.com/documents?id=7033) 
 , but unlike the latter, the signal of the
 
 Throw signal
 
 intermediate event is sent to all active processes in Creatio.
 





 Fig. 1
 
 Throw signal
 
 intermediate event
 




![scr_process_designer_throw_signal_event.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_throw_signal_event.png)



 For example, after finishing processing an order as part of one process, you can notify all other processes that a new order has been processed.
 



 This signal will advance another process to the shipment document preparation stage (Fig. 2)
 





 Fig. 2 Activating the
 
 Wait for signal
 
 intermediate event
 




![scr_process_designer_catch_signal_event1.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_catch_signal_event1.png)



 At the same time, the same
 
 Throw signal
 
 event will initiate a “post-order survey” process
 





 Fig. 3 Activating the
 
 Signal
 
 start event
 




![scr_process_designer_catch_signal_start_event.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_catch_signal_start_event.png)



 [Throw signal] intermediate event operation
---------------------------------------------





|  |  |
| --- | --- |
| 
 Activation
  | 
 When the element incoming flow is activated, the
 
 Throw signal
 
 event broadcasts its signal and activates its outgoing flows. As a result:
 * All
 [Wait for signal](https://academy.creatio.com/documents?id=7031)
 elements in the “Custom signal” mode that await the generated signal and whose incoming flows have been activated - will activate their outgoing flows.
* All business processes whose starting element is
 [Signal](https://academy.creatio.com/documents?id=7027)
 start event in the “Custom signal” mode, which awaits the generated signal - will start.
 |
| 
 Execution
  | 
 After broadcasting the signal, the
 
 Throw signal
 
 element activates its outgoing flows.
  |




 [Throw signal] intermediate event parameters
----------------------------------------------





|  |  |
| --- | --- |
| 
 Which signal is generated?
  | 
 Enter the name of the signal event that will be broadcast. Make sure that the signal name (Fig. 4) matches the name(s) of the signal(s) specified in the
 
 Signal
 
 field of the
 
 Wait for signal
 
 (Fig. 5) and the
 
 Signal
 
 start event (Fig. 6).
  |






 Fig. 3 Specifying the name of a signal that activates the
 
 Wait for signal
 
 intermediate event(s) or the
 
 Signal
 
 start event in the corresponding business processes
 




![scr_chapter_process_designer_throw_signal_example1.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_throw_signal_example1.png)





 Fig. 4 Example of the
 
 Wait for signal
 
 intermediate event that catches the corresponding signal
 




![scr_chapter_process_designer_wait_signal_example.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_wait_signal_example.png)





 Fig. 5 Example of the
 
 Signal
 
 start event that is triggered by the corresponding
 
 Throw signal
 
 event
 




![scr_chapter_process_designer_start_signal_example.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_start_signal_example.png)




