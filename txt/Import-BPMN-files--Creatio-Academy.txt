


 There are several ways you can import a \*.BPMN file to the Creatio Process Designer:
 


* Drag&drop the file on the diagram working area (Fig. 1).
* Click
 
 Actions
 
 >
 
 Import from \*.bpmn
 
 .



 Upload file to the process designer
-------------------------------------



 You can import a process diagram from a .BPMN file created in
 [Studio Creatio, free edition](https://academy.creatio.com/documents/studio-free/user-guide/studio-creatio-free-edition) 
 , or any other valid BPMN 2.0 diagram editor. Imported diagrams require additional setup before they can be used as full-fledged automate business processes. For more information on exporting business processes from Studio Creatio, free edition, please see the
 [Import / Export process diagrams in Studio Free](/docs/8-0/user/bpm_tools/collaborative_business_processes_design_in_studio_creatio/import_and_export/import_/_export) 
 article.
 





 Fig. 1
 

 Importing a \*.BPMN file
 

[![chapter_process_principles_import_process_drag_n_drop.gif](/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_principles/chapter_process_principles_import_process_drag_n_drop.gif)](/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_principles/chapter_process_principles_import_process_drag_n_drop.gif)



 As a result, the diagram from the imported file will replace the current process diagram. The elements of the imported BPMN diagram will be converted to the Creatio Process Designer elements. Before running an executable business process, you will need to set its parameters. You may also need to add several elements to the process.
 



 The imported process will preserve a link to its description in Studio Creatio, free edition, which lets you get back to documenting the business process as you set up its execution in Creatio. The link is located in the
 **Link to process in Studio Free** 
 field of the process setup area.
 




 Element conversion specifics
-------------------------------



 Creatio Process Designer uses BPMN notation for implementing custom business logic on the Creatio platform. Although most elements are easily converted to their Creatio counterparts, some of the BPMN 2.0 elements do not affect the platform operation and cannot be converted to executable elements in the Process Designer. An imported process in Creatio can have three types of elements:
 


* **Executable elements** 
 . These elements affect process flow and business logic. These include sequence flows, most events, and gateways, as well as several types of process actions. For instance, BPMN “task” elements coverts to the
 
 Perform task
 
 element.
 [Read more >>>](#HT_chapter_process_creation_designer_converting_elements_supported)
* **Non-executable elements** 
 . These elements remain part of the imported diagram, but do not affect the process flow or business logic. Non-executable elements are marked with a question mark (
 ![process_designer_element_non-supported.png](/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_principles/process_designer_element_non-supported.png)
 ) on a Creatio process diagram.
 [Read more >>>](#HT_chapter_process_creation_designer_converting_elements_unsupported)
* **Ignored elements** 
 . Elements, such as “pool” or “data object” would be redundant in an executable Creatio business process and therefore are not imported.
 [Read more >>>](#HT_chapter_process_creation_designer_converting_elements_ignored)


### 


 Executable elements



 The list of executable elements is available in the table:
 





| 
**BPMN 2.0 element** 
 | 
**Executable Process Designer element** 
 |
| --- | --- |
| 
process_designer_element_small_icon_perform_task.png
 Task
  | 
scr_process_designer_task.png
[Perform task](/docs/7-17/user/bpm_tools/process_elements_reference/user_actions/perform_task/task_process_element) 
 |
| 
process_designer_element_small_icon_send_email.png
 Send Task
  | 
scr_process_designer_new_send_email.png
[Send email](/docs/7-17/user/bpm_tools/process_elements_reference/user_actions/send_email/send_email_process_element) 
 |
| 
process_designer_element_small_icon_user_task.png
 User task
  | 
scr_process_designer_user_task.png
[User task](/docs/node/1678/%26#9;) 
 |
| 
process_designer_element_small_icon_service.png
 Service task
  | 
scr_process_designer_call_web_service.png
[Call web service](/docs/node/1673/%26#9;) 
 |
| 
process_designer_element_small_icon_script_task.png
 Script task
  | 
scr_process_designer_script_task.png
[Script task](/docs/node/1676/%26#9;) 
 |
| 
process_designer_element_small_icon_non-auto-task.png
 Manual task
  | 
scr_process_designer_task00013.png
[Perform task](/docs/7-17/user/bpm_tools/process_elements_reference/user_actions/perform_task/task_process_element	) 
 |
| 
process_designer_element_small_icon_event_sub-process.png
 Sub-process (collapsed)
  | 
scr_process_designer_subprocess.png
[Sub-process (Call activity)](/docs/node/1703/%26#9;) 
 |
| 
process_designer_element_small_icon_sub-process-(call_activity).png
 Call activity
  | 
scr_process_designer_subprocess00014.png
[Sub-process (Call activity)](/docs/node/1703/%26#9;) 
 |
| 
process_designer_element_small_icon_event_sub-process00015.png
 Event sub-process
  | 
scr_process_designer_event_subprocess.png
[Event sub-process](/docs/node/1704/%26#9;) 
 |
| 
process_designer_event_icon_start_simple.png
 Start event
  | 
scr_process_designer_start_simple.png
[Simple](/docs/node/1679/%26#9;) 
 |
| 
process_designer_event_icon_start_message.png
 Message start event
  | 
scr_process_designer_start_message.png
[Message](/docs/8-0/user/bpm_tools/process_elements_reference/events/message/message_start_event_process_element) 
 |
| 
process_designer_event_icon_start_timer.png
 Timer start event
  | 
scr_process_designer_start_timer.png
[Start timer](/docs/node/1682/%26#9;) 
 |
| 
process_designer_event_icon_start_signal.png
 Signal start event
  | 
scr_process_designer_start_signal.png
[Signal](/docs/node/1680/%26#9;) 
 |
| 
process_designer_event_icon_intermediate_throwing_message.png
 Intermediate throw message
  | 
scr_process_designer_intermediate_generating_message.png
[Throw message](/docs/node/1684/%26#9;) 
 |
| 
process_designer_event_icon_intermediate_throwing_signal.png
 Intermediate throw signal
  | 
scr_process_designer_intermediate_generating_signal.png
[Throw signal](/docs/node/1683/%26#9;) 
 |
| 
process_designer_event_icon_intermediate_catching_message.png
 Intermediate catch message
  | 
scr_process_designer_intermediate_generating_message00016.png
[Wait for message](/docs/node/1686/%26#9;) 
 |
| 
process_designer_event_icon_intermediate_catching_signal.png
 Intermediate catch signal
  | 
scr_process_designer_intermediate_processing_signal.png
[Wait for signal](/docs/node/1685/%26#9;) 
 |
| 
process_designer_event_icon_intermediate_catching_timer.png
 Timer intermediate event
  | 
scr_process_designer_timer.png
[Wait for timer](/docs/node/1688/%26#9;) 
 |
| 
process_designer_event_icon_start_simple00017.png
 End event
  | 
scr_process_designer_end_terminate.png
[Terminate](/docs/node/1689/%26#9;) 
 |
| 
process_designer_event_icon_final_stop.png
 Terminate end event
  | 
scr_process_designer_end_terminate00018.png
[Terminate](/docs/node/1689/%26#9;) 
 |
| 
process_designer_gateway_exclusive.png
 Exclusive gateway (OR)
  | 
scr_process_designer_exclusive_gateway.png
[Exclusive gateway (OR)](/docs/node/1699/%26#9;) 
 |
| 
process_designer_gateway_inclusive.png
 Inclusive gateway (OR)
  | 
scr_process_designer_inclusive_gateway.png
[Inclusive gateway (OR)](/docs/node/1700/%26#9;) 
 |
| 
process_designer_gateway_event_based.png
 Event-Based Gateway
  | 
scr_process_designer_event-based_gateway.png
[Exclusive event-Based Gateway](/docs/node/1702/%26#9;) 
 |
| 
process_designer_gateway_parallel.png
 Parallel gateway (AND)
  | 
scr_process_designer_parallel_gateway.png
[Parallel gateway (AND)](/docs/node/1701/%26#9;) 
 |
| 
process_designer_context_icon_tools_arrow00019.png
 Sequence flow
  | 
scr_process_designer_sequence_flow.png
[Sequence flow](/docs/node/1705/%26#9;) 
 |
| 
process_designer_context_icon_tools_conditional_arrow00020.png
 Conditional sequence flow
  | 
scr_process_designer_conditional_flow.png
[Conditional flow](/docs/node/1705/%26#9;) 
 |
| 
process_designer_context_icon_tools_default_arrow00021.png
 Default sequence flow
  | 
scr_process_designer_default_flow.png
[Default flow](/docs/node/1705/%26#9;) 
 |
| 
process_designer_expanded_process.png


 Expanded sub-process
  | 
scr_process_designer_subprocess00022.png


[Sub-process (Call activity)](/docs/node/1703/%26#9;) 
 |








 Creatio populates the parameters of imported executable elements with default values. Some required parameters may not have a default value. Please make sure you go through all the required parameters and populate them before running an imported process for the first time.
 


### 


 Non-executable elements



 Imported non-executable elements display as the same types of BPMN 2.0 elements in an executable process diagram, and are marked with a question mark.
 



 The list of
 **non-executable elements** 
 is available in the table:
 





| 
**BPMN 2.0 element** 
 | 
**Non-executable Process Designer element** 
 |
| --- | --- |
| 
process_designer_event_icon_intermediate_escalation.png
 Throw - Escalation Intermediate Event
  | 
process_designer_element_non-supported00023.png
 Non-executable element
  |
| 
process_designer_element_small_icon_rule.png
 Business rule task
  | 
process_designer_element_non-supported_2.png
 Non-executable element
  |
| 
process_designer_gateway_complex.png
 Complex gateway
  | 
process_designer_element_non-supported_3.png
 Non-executable element
  |








 Imported business processes ignore any non-executable elements. If an incoming flow of a non-executable element activates, all its outgoing flows activate immediately. Boundary events are imported as non-executable elements.
 



 After importing a business process, go through the non-executable element and either remove it or replace it with an executable process designer element that does the same business logic. For example, a “Receive task” element can be replaced with the
 **Perform task** 
 element.
 



 Non-executable end events behave exactly like the
 **Terminate** 
 end event.
 


### 


 Ignored elements



 Creatio does not import the following BPMN 2.0 elements:
 


* ![process_designer_pool.png](/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_principles/process_designer_pool.png)
 Pools
* ![process_designer_object.png](/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_principles/process_designer_object.png)
 Data objects
* ![process_designer_storage.png](/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_principles/process_designer_storage.png)
 Data storages
* ![process_designer_text.png](/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_principles/process_designer_text.png)
 Annotations
* ![process_designer_association.png](/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_principles/process_designer_association.png)
 Associations
* ![process_designer_group.png](/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_principles/process_designer_group.png)
 Groups. This type of element is not supported by Studio Creatio, free edition.
* ![process_designer_message_flow.png](/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_principles/process_designer_message_flow.png)
 Message flows. This type of element is not supported by Studio Creatio, free edition.



 These elements will not be available in the imported diagram. Any executable and non-executable elements located in pools of the imported BPMN 2.0 diagram will be converted to the corresponding Creatio elements in the resulting process.
 








