


 Use the
 
 Sub-process
 
![chapter_case_designer_icon_subprocess.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_icon_subprocess.png)
 case designer element to add a BPMN process as a stage step. The parameters of the
 
 Sub-process
 
 Case Designer element are identical to those of the corresponding Process Designer element. The sub-process starts automatically when you transition to the stage that has this step.
 



 Set up the [Sub-process] element
----------------------------------



 Specify the process to run as a sub-process in the
 
 Which process to run?
 
 field of the element setup area (Fig. 1).
 




 Fig. 1 The
 
 Sub-process
 
 element setup area
 

![chapter_process_designer_sub_process.png](/docs/sites/en/files/images/BPM_Tools/dcm_elements/chapter_process_designer_sub_process.png)



 Click the
 ![btn_chapter_designer_user_task_designer_task.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/btn_chapter_designer_user_task_designer_task.png)
 button to open the process in the BPMN Process Designer.
 



 Fill out the following fields:
 


1. Which process to run?
 
 – specify an existing process to use as a sub-process or create a new process in the Process Designer. After you add the process, the
 
 Process parameters
 
 field group will become available.
2. Process parameters
 
 – specify the parameters of the process.
 



 The field group displays all parameters of the selected sub-process. You can also use parameters to connect the process to the main column of the current record. Read more:
 [Process parameters](/docs/7-18/user/bpm_tools/business_process_setup/parameters/process_parameters) 
 .
3. When is the step performed?
 
 – indicates whether to activate the element at the start of the stage or after a case step. Select “At the start of the stage” to run the sub-process at the start of the case stage. Select “After the previous step is complete” if the sub-process must run after the previous step in the case stage. Specify the step in the
 
 Perform after step
 
 field.
4. Step type
 
 – specify if the step is required. Select “Required step” if the sub-process must be completed to transition to the next stage. Select “Optional step” if the user can advance to the next case stage without completing this sub-process.
 


 Note.
 
 Users can advance to the final “unsuccessful” stage from any stage without completing the required steps.
5. Which process to run?
 
 – select an existing process to use as a sub-process.
6. Change stage after element is completed
 
 – configure stage transitions depending on sub-process results. Click the
 ![btn_button_connections00002.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/btn_button_connections00002.png)
 button to add fields for configuring the conditions of case transition. Click the
 ![chapter_case_designer_icon_parameter_menu.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_icon_parameter_menu.png)
 button in the
 
 If result
 
 field to build the formula with conditions to move to another stage and specify the transition stage in the
 
 Set stage to
 
 field. For example, to advance a case to a different stage only if the contract in the approval sub-process was approved, set up the following formula:
 
 #Getting the contract approved.Result#
 
 ==
 
 #Lookup.Approval status.Positive#
 
 .




