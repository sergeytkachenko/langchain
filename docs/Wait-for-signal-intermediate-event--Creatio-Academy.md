


 The
 
 Wait for signal
 
 intermediate event (Fig. 1) is used for resuming a business process by events that occur in other processes or whenever a specific record is modified or deleted in Creatio.
 





 Fig. 1
 
 Wait for signal
 
 intermediate event
 




![scr_process_designer_catch_signal_event.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_catch_signal_event.png)



 For example, a business process can wait until the user starts working on an activity (its status is changed to “In progress”) before proceeding to the next step.
 



 [Wait for signal] intermediate event operation
------------------------------------------------





|  |  |
| --- | --- |
| 
 Activation
  | 
 After the element incoming flow is activated, the
 
 Wait for signal
 
 intermediate event waits for the corresponding signal. Depending on the element mode, the
 
 Wait for signal
 
 element will wait for one of the following events:
 * A corresponding signal is generated by the
 [Throw signal
 
 intermediate event](https://academy.creatio.com/documents?id=7034) 
 in any other business process.
* A corresponding Creatio record is modified or deleted.
 |
| 
 Execution
  | 
 When the expected signal is generated by a
 
 Throw signal
 
 event, or the monitored record is modified or deleted, the
 
 Wait for signal
 
 element activates its outgoing flows and enables the execution of the other actions in the business process.
  |




 [Wait for signal] intermediate event parameters
-------------------------------------------------





|  |  |
| --- | --- |
| 
 Which type of signal is received?
  | 
 Choose which signal activates the event:
 * Select “Custom signal” if the event is activated by a
 [Throw signal
 
 intermediate event](https://academy.creatio.com/documents?id=7034) 
 in any business process (the current business process or any other).
* Select “Record signal” if the event is activated whenever an object record is modified or deleted in Creatio.


 The selected option determines what following parameters will appear in the element setup area.
  |
| 
 Run following elements in the background
  | 
 Select this checkbox, if you want any “User action” elements activated with the outgoing flows of the current element to run “in the background”. When process elements are executed in the background, their loading mask is not displayed, no windows pop up for the user, etc. The user will be able to interact with the elements via the
 
 Business process tasks
 
 tab of the communication panel.
  |




 Custom signal mode parameters
-------------------------------



 In the “Custom signal” mode, the
 
 Wait for signal
 
 event is triggered by a
 [Throw signal
 
 intermediate event](https://academy.creatio.com/documents?id=7034) 
 from another process(es).
 





|  |  |
| --- | --- |
| 
 Signal
  | 
 Enter a signal value. Make sure that the field is populated with the custom-generated signal name matching the name of the signal specified in the
 
 Which signal is generated?
 
 field of the
 
 Throw signal
 
 element (Fig. 2 and Fig. 3) in the corresponding process. Such signal name can be generated by user at random.
  |






 Fig. 2
 
 Specifying the name of a signal that activates the
 
 Wait for signal
 
 intermediate event in the “Custom signal’ mode
 




![scr_chapter_process_designer_wait_signal_example00032.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_wait_signal_example00032.png)




 Fig. 3
 
 Example of a
 
 Throw signal
 
 element that generates the corresponding signal
 




![scr_chapter_process_designer_throw_signal_example100033.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_throw_signal_example100033.png)


 Record signal mode parameters
-------------------------------



 In the “Record signal” mode, the
 
 Wait for signal
 
 element is triggered when an object record is modified or deleted in Creatio.
 





|  |  |
| --- | --- |
| 
 Record Id
  | 
 Specify the record that triggers the
 
 Wait for signal
 
 element. Learn more about how to work with parameter values in a separate
 article.
 For example, if the process waits for a signal from an activity record, specify the unique identifier of an activity.
  |
| 
 Object
  | 
 Select the object whose record generates the signal. For example, to catch a signal from an activity record, select the “Activity” object. Note that if you specify the
 
 Record Id
 
 field value via a corresponding lookup, the
 
 Object
 
 field value will be populated automatically with the name of the corresponding object.
  |
| 
 Which event should trigger the signal?
  | 
 Choose whether the element should activate when the record is modified or deleted:
 * Select “Record modified” if editing the specified object record activates the signal.
* Select “Record deleted” if deleting the specified object record activates the signal.
 |
| 
 Changes expected
  | 
 The field becomes available when the “Record modified” is selected in the
 
 Which event should trigger the signal
 
 field.
 * Select “In any field” to run business process automatically, upon changes in any field of the selected object record.
* Select “In any of the selected fields” to run business process automatically, upon changes in specific fields only. Click
 
 +Add column
 
 and select the needed fields. For example, if the signal can be activated only if an activity status is modified, add the
 
 Status
 
 column. If a change occurs in a column that has not been added, the process will not start.
 |
| 
 The record must meet the filter conditions
  | 
 If the record does not meet the filter conditions, the element will not be activated. For example, the signal should only be activated if the status of an activity is set to “Completed”. If the filter is not set, the signal will be activated on any modification of record (for “Record modified” mode) or on deletion of any record (for “Record deleted” mode).
  |




 [Wait for signal] intermediate event outgoing parameters
----------------------------------------------------------



 The
 
 Wait for signal
 
 intermediate event outgoing parameters include:
 





|  |  |
| --- | --- |
| 
 RecordId
  | 
 The parameter contains the identifier of the modified/deleted record that triggered the signal. Note that the data of a deleted record can only be read if the process is not run in the background mode.
 

 This parameter is similar to the
 
 Unique identifier of record
 
 parameter of the
 [Signal
 
 start event.](https://academy.creatio.com/documents?id=7027) 
 |







