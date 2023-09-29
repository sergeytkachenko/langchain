


 Use the
 
 Sub-process
 
 element (Fig. 1) to run a business process from another process.
 




 Fig. 1
 

 Sub-process
 
 element in a business process diagram
 




[![scr_chapter_process_designer_sub_process.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_sub_process.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_sub_process.png)




 Using the
 
 Sub-process
 
 element to run other processes has the following specifics:
 


* Process parameter values can be passed from the parent process to its sub-process and vice-versa. This means that you can run a sub-process with specific parameter values, and after the sub-process completes – use its results in the parent process.
* The
 
 Sub-process
 
 element will activate its outgoing flows only after the corresponding sub-process is complete.
* If any of the incoming parameters of the
 
 Sub-process
 
 element are mapped to a
 [data collection](https://academy.creatio.com/documents/technic-bpms/7-16/working-collections#HT_chapter_process_principles_working_with_data_collections) 
 , the element will run in the multi-instance mode:
 


	+ The [Sub-process] element will run a separate instance of the sub-process per each instance of the incoming collection.
	+ The [Sub-process] element will return an outbound data collection populated with
	 [outbound and bi-directional parameters](https://academy.creatio.com/documents?product=bpms&ver=7&id=7172) 
	 returned by every sub-process instance.
	+ The [Sub-process] element will complete its execution when all sub-process instances are complete.



 Using sub-processes is recommended to avoid creating process diagrams that are too large and complex to efficiently use or maintain. In addition, large process diagrams are more resource-heavy. The
 
 Sub-process
 
 element also enables re-using business processes that already exist in Creatio. For example, you can use the
 
 Sub-process
 
 element in an opportunity process that includes a “Meeting with customer” stage, which exists as a separate business process in Creatio.
 



 [Sub-process] element operation
---------------------------------



 Based on the type of its incoming parameter values (regular or collection) a sub-process element can run in a “single instance mode,” or “multi-instance mode,” which in turn can be sequential or parallel.
 


### 
 Single instance mode



 The
 
 Sub-process
 
 element runs in the “single instance mode” if none of the sub-process parameters are mapped to a data collection.
 





|  |  |
| --- | --- |
| 
 Execution
  | 
 When the incoming flow is activated, the
 
 Sub-process
 
 element activates the
 [Simple
 
 start event](https://academy.creatio.com/documents/technic-bpms/7-16/simple-start-event#HT_chapter_process_designer_elements_events_simple_start) 
 of the process specified in the
 
 Which process to run?
 
 field.
 

 As a result, the
 actual version
 of the sub-process is launched as a new independent process instance.
 

 If any of the incoming and bi-directional process parameters are populated in the
 
 Process parameters
 
 block of the
 
 Sub-process
 
 element, the sub-process will run with those parameter values.
 

 If you save another version of the sub-process as “actual” after the
 
 Sub-process
 
 element has been launched, the element will continue executing the version that was actual at the time of the
 
 Sub-process
 
 element activation. The new sub-process version will be used on the new activation of the
 
 Sub-process
 
 element. The active instance of the sub-process version that was “actual” when the
 
 Sub-process
 
 element was launched will continue running normally.
 

 The sub-process log page, which displays the sub-process tasks on the
 
 Process elements
 
 detail in the order of their execution, is available as a separate process instance in the
 [Process Log
 
 section](https://academy.creatio.com/documents/technic-bpms/7-16/process-log-section#HT_specs_process_log) 
 and as a clickable process task in the
 
 Process elements
 
 detail of the parent process.
  |
| 
 Completion
  | 
 The
 
 Sub-process
 
 element is considered complete when the corresponding sub-process instance completes its execution.
 

 Upon completion, the
 
 Sub-process
 
 element updates its parameter values from the corresponding parameters of the completed sub-process instance and activates its own outgoing flows.
  |



### 
 Sequential multi-instance mode



 The
 
 Sub-process
 
 element runs in the “sequential multi-instance mode” when at least one of the sub-process elements is mapped to a data collection and the “Sequential” execution method is selected. The sequential execution method is selected by default when a sub-process is mapped to a
 [data collection](https://academy.creatio.com/documents/technic-bpms/7-16/working-collections#HT_chapter_process_principles_working_with_data_collections) 
 .
 





 Note.
 
 Use the
 
 Execution method
 
 parameter to select the sequential or parallel execution method. Selecting the execution method is unavailable when none of the process parameters are mapped to a data collection. More information on the parameters of the
 
 Sub-process
 
 element is available in the “
 
 Sub-process
 
 element parameters” section of this article.
 






|  |  |
| --- | --- |
| 
 Execution
  | 
 When its incoming flow is activated, the
 
 Sub-process
 
 element starts looping through the data collection. For each item of the data collection, the
 
 Sub-process
 
 element runs a new instance of the process specified in the
 
 Which process to run?
 
 field by activating the
 [Simple
 
 start event](https://academy.creatio.com/documents/technic-bpms/7-16/simple-start-event#HT_chapter_process_designer_elements_events_simple_start) 
 of the sub-process.
 

 As a result, the currently
 actual version
 of the sub-process launches as a new independent process instance for each item in the data collection as soon as the previous sub-process instance is complete. Read more in the “
 [Working with collections](https://academy.creatio.com/documents/technic-bpms/7-16/working-collections#XREF_43102_Working_with) 
 ” article.
 

 The incoming and bidirectional
 [sub-process parameters](https://academy.creatio.com/documents?product=bpms&ver=7&id=7172) 
 (specified in the
 
 Process parameters
 
 block of the
 
 Sub-process
 
 element) can be mapped either to process elements from the same data collection or to non-collection elements. Non-collection process parameters will be re-used in all sub-process instances.
 

 If you save another version of the sub-process as “actual” after the
 
 Sub-process
 
 element has been launched, any new sub-process instance will use the newest actual version to date. This means that the first instance of the sub-process and any other instances that ran before updating the actual version of the sub-process will use the previous version. We do not recommend saving another sub-process version as actual until all instances of the sub-process are either complete or canceled.
 

 Note that the sub-process creates a separate instance in the
 [Process Log
 
 section](https://academy.creatio.com/documents/technic-bpms/7-16/process-log-section#HT_specs_process_log) 
 , which displays the sub-process tasks in its
 
 Process elements
 
 detail in the order of their execution. The parent process instance displays the link to the list of sub-process instances as a regular clickable process task in its own
 
 Process elements
 
 detail.
  |
| 
 Completion
  | 
 Upon completion of all sub-process instances, the element creates an entry in the outgoing data collection and populates the entry with parameter values from the corresponding parameters of the completed sub-process instance. After that, the next sub-process instance will be launched.
 

 The
 
 Sub-process
 
 element is considered complete when the last sub-process instance is complete. Upon completion of the last instance, the
 
 Sub-process
 
 element updates the outgoing data collection and activates its own outgoing flows. Read more in the “
 [Working with collections](https://academy.creatio.com/documents/technic-bpms/7-16/working-collections#XREF_43102_Working_with) 
 ” article.
  |



### 
 Parallel multi-instance mode



 The
 
 Sub-process
 
 element runs in the “parallel multi-instance mode” if at least one of the sub-process elements is mapped to a
 [data collection](https://academy.creatio.com/documents/technic-bpms/7-16/working-collections#HT_chapter_process_principles_working_with_data_collections) 
 and the parallel execution method is selected.
 





 Note.
 
 Use the
 
 Execution method
 
 parameter to select the sequential or parallel execution method. Selecting the execution method is unavailable when none of the process parameters are mapped to a data collection. More information on the parameters of the
 
 Sub-process
 
 element is available in the “
 
 Sub-process
 
 element parameters” section of this article.
 






|  |  |
| --- | --- |
| 
 Execution
  | 
 When its incoming flow is activated, the
 
 Sub-process
 
 element starts looping through the data collection. For each item of the data collection, the
 
 Sub-process
 
 element runs a new instance of the process specified in the
 
 Which process to run?
 
 field by activating the
 [Simple
 
 start event](https://academy.creatio.com/documents/technic-bpms/7-16/simple-start-event#HT_chapter_process_designer_elements_events_simple_start) 
 of the sub-process.
 

 As a result, the currently
 actual version
 of the sub-process launches as a new independent process instance for each item in the data collection immediately, barring limitations on the number of active background processes. Read more in the “
 [Working with collections](https://academy.creatio.com/documents/technic-bpms/7-16/working-collections#XREF_43102_Working_with) 
 ” article.
 

 The incoming and bidirectional process parameters specified in the
 
 Process parameters
 
 block of the
 
 Sub-process
 
 element can be mapped either to process elements from the same data collection or to non-collection elements. Non-collection process parameters will be re-used in all sub-process instances.
 

 If you save another version of the sub-process as “actual” after the
 
 Sub-process
 
 element has been launched, any new sub-process instance will use the newest actual version to date. Changing the sub-process actual version immediately after running a parallel multi-instance sub-process will not affect the first instance and any other instances that have already launched. Any instances that run after the change will use the new version. We do not recommend saving another sub-process version as actual until all instances of the sub-process are either running, complete or canceled.
 

 Note that the sub-process creates a separate instance in the
 [Process Log
 
 section](https://academy.creatio.com/documents/technic-bpms/7-16/process-log-section#HT_specs_process_log) 
 , which displays the sub-process tasks in its
 
 Process elements
 
 detail in the order of their execution. The parent process instance displays the link to the list of sub-process instances as a regular clickable process task in its own
 
 Process elements
 
 detail.
  |
| 
 Completion
  | 
 Upon completion of each instance, the
 
 Sub-process
 
 element creates an entry in the outgoing data collection and populates the entry with parameter values from the corresponding parameters of the completed sub-process instance.
 

 Note that the order of data entries in the collection cannot be predicted.
 

 The
 
 Sub-process
 
 element is considered complete when the last remaining sub-process instance is complete. Upon completion of the last instance, the
 
 Sub-process
 
 element updates the outgoing data collection and activates its own outgoing flows. Read more in the “
 [Working with collections](https://academy.creatio.com/documents/technic-bpms/7-16/working-collections#XREF_43102_Working_with) 
 ” article.
  |






 Note.
 
 The actual version of the process used as the sub-process can be found in the
 
 Versions
 
 detail of the
 [Process versions
 
 tab](https://academy.creatio.com/documents/technic-bpms/7-16/process-properties-page#HT_section_process_library_process_versions_tab) 
 when you select this process in the Process Library record list and click
 
 Properties
 
 .
 







 [Sub-process] element parameters
-------------------------------------





|  |  |
| --- | --- |
| 
 Which process to run?
  | 
 Specify a business process to use as the sub-process:
 * you can select an existing Creatio business process to use it as a sub-process from the drop-down list
* you can add a new process via the Process Designer by clicking
 btn_button_connections00035.png
 if the needed process is not available on the list


btn_chapter_designer_user_task_designer_task00036.png
 – opens the process selected as a sub-process in a new Process Designer window.
 

 Note that to be eligible as a sub-process, a business process must start with a
 [Simple
 
 start event](https://academy.creatio.com/documents/technic-bpms/7-16/simple-start-event#HT_chapter_process_designer_elements_events_simple_start) 
 .
  |
| 
 Execution method
  | 
 Only available in the multi-instance mode. To enable the multi-instance mode, map at least one of the process parameters to a data collection. Read more in the “
 [Working with collections](https://academy.creatio.com/documents/technic-bpms/7-16/working-collections#XREF_43102_Working_with) 
 ” article.
 

 Select one of the two execution methods:
 * Sequential
 
 . Sub-process instances run successively; a new sub-process instance runs upon completion of the previous instance. This is the default method.
* Parallel
 
 . Sub-process instances run simultaneously; the
 
 Sub-process
 
 element does not wait for the completion of the already running instances before running a new instance. Sub-process instances may complete in a different order.
 |
| 
 Process parameters
  | 
 When you select an existing Creatio process from the list, the parameters of the selected process are displayed in this block of the
 
 Sub-process
 
 setup area. You can populate the parameter values to run the sub-process with these values. During the execution of the sub-process, these values can be populated or updated, based on the logic of each specific sub-process. You can also map subsequent elements of the parent process to these parameters.
 

 To add/edit/delete the element parameters, modify the process selected in the
 
 Which process to run?
 
 field.
 

 Before making any changes to a business process, which is used as a sub-process, make sure that such changes will not affect other processes. For example, if you edit the data type of a parameter and change it from the “Lookup” value to “Boolean” in a business process, this may lead to errors in any processes that use it as a sub-process.
 

 Please check the
 
 Used as sub-process in processes
 
 detail of the
 [Launch options
 
 tab](https://academy.creatio.com/documents/technic-bpms/7-16/process-properties-page#HT_section_process_library_launch_options_tab) 
 in the Process Library before modifying an existing process. If this process has any sub-processes of its own, they will be displayed in the
 
 Sub-processes
 
 detail of the
 [Sub-processes
 
 tab](https://academy.creatio.com/documents/technic-bpms/7-16/process-properties-page#HT_section_process_library_sub_processes_tab) 
 .
  |





