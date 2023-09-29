


 Add process elements to the working area to build a new business process.
 



 The process elements are covered in separate articles.
 



 Learn more about improving the performance of your business processes in an online course:
 [How to start modeling your process? Creatio best practices and tools](https://academy.creatio.com/online-courses/how-start-modeling-your-process-creatio-best-practices-and-tools) 
 .
 



 Add an element to a process diagram
-------------------------------------



 You can add elements to a business process in several ways:
 


* Drag an element
 **from the process element toolbar** 
 on the left to the working area of the Process Designer (Fig. 1).
 




 Fig. 1 Dragging an element from the element toolbar
 

![drag_and_drop_from_drop-down_menu.gif](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/drag_and_drop_from_drop-down_menu.gif)
* Select an element
 **from the context menu of another element on the diagram** 
 and drag the element to the working area. This adds the element and connects it to the previously selected element with a sequence flow (Fig. 2). Click
 ![icon_tools_setup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/icon_tools_setup.png)
 and select the element type if needed.
 




 Fig. 2 Adding an element from the context menu of another element
 

![add_element_and_change_type.gif](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/add_element_and_change_type.gif)
* Select an element
 **from the suggestion dialog** 
 and drag the element to the working area (Fig. 3). The AI suggestion mechanism generates recommendations for each user based on their previous decisions, as well as best practices for business process setup in Creatio. Recommendations are generated after you set up an existing element. The suggestion menu displays 5 most suitable options for the next element sorted by probability. The mechanism also predicts a block of settings for certain elements. You can change the element settings if needed. To reopen the index of suggested elements, click the
 ![btn_ai_recomendations.png](/docs/sites/en/files/images/BPM_Tools/working_in_process_designer/btn_ai_recomendations.png)
 button in the context menu of the business process element.
 



 The suggestion mechanism speeds up the diagram setup for experienced users and improves the learning curve for new users. Creatio trains the data prediction model constantly to tailor predictions to specifics of your company’s processes.
 





 Note.
 
 Suggestions for next process steps are available since Creatio 8.0.1.
 





 Fig. 3 Adding an element to the diagram from suggestions
 

![gif_add_element_via_ai_recomendations.gif](/docs/sites/en/files/images/BPM_Tools/working_in_process_designer/gif_add_element_via_ai_recomendations.gif)



 As you move the element on the diagram, alignment lines appear (Fig. 4).
 




 Fig. 4 Alignment lines
 

![alignment.gif](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/alignment.gif)



 If you place a process element on a sequence flow that connects two other elements, the flow splits into two flows to encompass the new element (Fig. 5).
 




 Fig. 5 Placing a process element on a sequence flow
 

![scr_connection_splitting.gif](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/scr_connection_splitting.gif)



 Connect elements
------------------



 You can connect Creatio process elements with
 [conditional flows](https://academy.creatio.com/documents?id=7045) 
 ,
 [sequence flows](https://academy.creatio.com/documents?id=7043) 
 , and
 [default flows](https://academy.creatio.com/documents?id=7046) 
 . When you add a process element from the context menu of a different element, Creatio connects the elements with a
 [sequence flow](https://academy.creatio.com/documents?id=7043) 
 automatically.
 



 Also, you can connect elements by adding a sequence flow from the context menu of an element (Fig. 6).
 




 Fig. 6 Adding an outgoing flow from the context menu of an element
 

![dragging_connection.gif](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/dragging_connection.gif)



 The
 [sequence flow](https://academy.creatio.com/documents?id=7043) 
 is the default connection item. To connect elements with a
 [default flow](https://academy.creatio.com/documents?id=7046) 
 or
 [conditional flow](https://academy.creatio.com/documents?id=7045) 
 , change the sequence flow type by clicking
 ![icon_tools_setup00001.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/icon_tools_setup00001.png)
 in the element context menu (Fig. 7).
 




 Fig. 7 Changing the flow type
 

![changing_flow_type.gif](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/changing_flow_type.gif)



 Change the element type
-------------------------



 The element toolbar and element context menu display several basic process elements.
 




 Fig. 8 Adding elements and changing their types
 

![add_element_and_change_type00002.gif](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/add_element_and_change_type00002.gif)


* You can change a
 ![process_designer_system_action_palette.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/process_designer_system_action_palette.png)
 system action group to
 ![process_designer_task_palette.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/process_designer_task_palette.png)
 user action group and vice versa.
* You can change
 ![process_designer_start_event_palette.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/process_designer_start_event_palette.png)
 start,
 ![process_designer_intermediate_event_palette.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/process_designer_intermediate_event_palette.png)
 intermediate, or
 ![process_designer_end_event_palette.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/process_designer_end_event_palette.png)
 end events to any other event type.
* You can change a
 ![process_designer_gateway_palette.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/process_designer_gateway_palette.png)
 gateway to any other gateway type.
* You can change a
 ![process_designer_context_icon_tools_arrow.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/process_designer_context_icon_tools_arrow.png)
 sequence flow to a
 ![process_designer_context_icon_tools_conditional_arrow.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/process_designer_context_icon_tools_conditional_arrow.png)
 conditional flow or
 ![process_designer_context_icon_tools_default_arrow.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/process_designer_context_icon_tools_default_arrow.png)
 default flow.



 Select multiple elements on the process diagram
-------------------------------------------------



 You can select multiple elements on the diagram, for example, to move them.
 



 To select multiple elements, click on individual elements while holding Ctrl (Fig. 9).
 




 Fig. 9 Select multiple elements on the process diagram
 

![chapter_process_creation_designer_choose_few_elem.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/chapter_process_creation_designer_choose_few_elem.png)



 Creatio highlights the selected elements with a dotted frame around them. You can move or delete the selected elements (Fig. 10).
 




 Fig. 10 Move selected elements
 

![chapter_process_creation_designer_change_place_elem.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/chapter_process_creation_designer_change_place_elem.png)





 Note.
 
 To select the entire business process diagram, hold Shift, left-click the working area of the Process Designer, and select the business process while holding the left mouse button.
 




 Set up branching processes
----------------------------



 Business processes can branch into several parallel or alternative flows.
 





 Example.
 
 Create a process that branches depending on call results. If the customer is interested, schedule the meeting. If the customer is not interested, end the process. The task can also be completed with the “Call later” result, in which case the call element must be run again.
 




 Use the following elements to branch the process:
 


* [Conditional flows](https://academy.creatio.com/documents?id=7045) 
 that activate if their conditions are met.
* [Gateways](https://academy.creatio.com/documents?id=7036) 
 that activate one ore more outgoing flows depending on the gateway type: “exclusive OR,” “inclusive OR,” “parallel AND.”
* [User dialog](https://academy.creatio.com/documents?id=7010)
 and
 [Auto-generated page](https://academy.creatio.com/documents?id=7007)
 process elements whose results depend on the items (answers, buttons) selected on the dialog page or auto-generated page. You can use the selected items as conditions for outgoing conditional flows.
* [Perform task](https://academy.creatio.com/documents?id=7009)
 ,
 [Open edit page](https://academy.creatio.com/documents?id=7012)
 process elements whose results depend on the values of a field. You can use the value of the field that determines the element result as a condition for outgoing conditional flows.



 The
 
 Exclusive gateway (OR)
 
 gateway is the best element for task result processing since the task can only have one result. Alternatively, you can add outgoing conditional flows directly to the
 
 Call customer
 
 process element without using the gateway.
 



 To branch the process based on the
 
 Perform task
 
 element results (Fig. 11):
 




 Fig. 11 Meeting process
 

![scr_process_creation_designer_linear_process.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/scr_process_creation_designer_linear_process.png)





 Note.
 
 Use the
 [[Exclusive gateway (OR)](https://academy.creatio.com/documents?id=7036) 
 gateway when only one of the alternative process branches can be executed.
 



 If both process branches must be executed simultaneously, use the
 [Parallel gateway (AND)](https://academy.creatio.com/documents?id=7038)
 gateway. This gateway supports
 [sequence flows](https://academy.creatio.com/documents?id=7044) 
 only.
 



1. Place the
 
 Exclusive gateway (OR)
 
 gateway on the process diagram after the
 
 Call customer
 
 element (Fig. 12).
 

 Fig. 12 Add a gateway to a process
 

![scr_process_creation_designer_operator_on_process.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/scr_process_creation_designer_operator_on_process.png)
2. Connect the gateway and the ”Conduct meeting” element with a conditional flow.
3. Select the
 
 Completed
 
 checkbox in the element setup area of the conditional flow (Fig. 13).
 

 Fig. 13 Select a condition for a conditional flow
 

![scr_process_creation_designer_conditional_interesting.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/scr_process_creation_designer_conditional_interesting.png)
4. Add conditional flows for other results similarly. Add a return flow to the meeting element and select
 
 Call later
 
 . Add another outgoing conditional flow to the process end event and select
 
 Not interested
 
 (Fig. 14).
 




 Fig. 14 Branch a process using a gateway
 

![scr_process_creation_ready_process_with_conditionals.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/scr_process_creation_ready_process_with_conditionals.png)
5. Save the process.



 As a result, three results will be available on the “Call customer” activity page:
 
 Completed
 
 ,
 
 Not interested
 
 , and
 
 Rescheduled
 
 (Fig. 15).
 




 Fig. 15 Select the task result for process branching
 

![scr_process_creation_designer_different_results.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_basics/scr_process_creation_designer_different_results.png)



 Clicking
 
 Completed
 
 will open the “Conduct meeting” page. Clicking
 
 Rescheduled
 
 will create another call task. Clicking
 
 Not interested
 
 will end the process.
 





 Note.
 
 To change the condition for the conditional flow, click the flow and select the new condition in the window that opens.
 




 If the process depends on the activity results, you can complete the activity only with the results provided by the process.
 



 If a process branch must be executed when you select any other result, add a
 default flow
 that triggers if the activity result is not specified in the conditional flows.
 



 Process version control
-------------------------



 Process version control in Creatio ensures that business process revisions and updates do not disrupt any active process instances. Also, the version control enables seamless updates to business processes and easy switching between the existing process versions.
 



 You can modify a process and save it as the current or new version regardless of the existence of active process instances. To do this, modify the process, click
 
 Save
 
 , and select “Save new version” or “Save current version.”
 



 The
 **new version** 
 replaces the earlier process versions in every place that uses the process schema, for example, sub-processes. However, the active instances of the process continue to work according to the version in which they were launched.
 



 Whenever a process is saved, Creatio checks:
 


* whether the process package is editable
* whether the process was exported



 If the process package is non-editable, Cratio asks if you want to save the new business process version. After you confirm this, Creatio saves the new version to the package specified in the
 
 Current package
 
 system setting.
 



 If the business process schema was exported, Creatio asks if you want to create a new schema version. If you choose not to, Creatio saves the process to the existing schema.
 



 To view the business process version, select the process, click
 
 Properties
 
 , and go to the
 
 Process versions
 
 tab.
 



 If you do not need to create several process versions, save the changes to the
 **current process version** 
 . If the process has active instances, they might be stopped when you save the changes.
 





 Note.
 
 Creatio saves the latest process version directly to the package. If you save the package as an archive and
 [transfer the package to a different environment](https://academy.creatio.com/documents?id=15207) 
 , the latest process version is transferred with the package. Creatio determines the final current process version based on which package is higher in the hierarchy.
 





