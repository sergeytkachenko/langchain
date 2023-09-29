


 When a business process is started, Creatio performs the sequence of steps (process actions). As part of the process, Creatio may prompt you to enter required data, e. g., the results of actions performed outside of Creatio, or to select how a process should continue.
 



 The process can perform the steps in the following ways:
 


* Automatically. For example, when deleting records that meet the set conditions.
* With user input. For example, the process opens a record page for you to fill out. In this case, the process will resume when you complete the required actions: filling out and saving the page.



 If the action that requires your input runs in the background, the process will not perform any logic until you open the corresponding page from the
 
 Business process tasks
 
 tab of the communication panel. In this case, Creatio will perform all system operations of the process in the background without displaying the loading mask.
 



 If such an action does not run in the background, Creatio will open the corresponding page and perform other logic the moment the process starts this action. The page will interrupt any Creatio activities you may be performing at the moment.
 



 If you are responsible for completing a business process step or have the role to which the corresponding task was assigned, Creatio will display the task on the
 
 Business process tasks
 
 tab of your communication panel.
 



 Use hints the process author can add to learn more about each step of the process. Click the
 ![btn_com_information.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_execution/btn_com_information.png)
 button to view the hint.
 



 This article covers different user activities performed as part of a business process.
 



 Complete process activities
-----------------------------



 If the process creates an activity, the next step will be activated only after you complete the activity with a result. You can limit the list of available results to the values available in the process element.
 



 You can assign the activity to another user or role on the activity page.
 



 If you cannot complete the activity immediately after its activation, enter the new date and time in the
 
 Start
 
 and
 
 Due
 
 fields of the activity page and save the record. You can come back to this step later.
 





 Note.
 
 The process activities are available in the
 
 Activities section
 
 , similarly to manually created records.
 




 The process may also create activities when executing other process elements of the “User action” type if the process author toggles on the corresponding setting. Learn more in the corresponding element descriptions:
 [User actions](https://academy.creatio.com/docs/user/bpm_tools/process_elements_reference/user_actions) 
 . The activity completion procedure described above applies to all the elements.
 



 Fill out the record pages
---------------------------



 Creatio may ask you to fill out the page of a new or an existing record as part of a business process. For example, to enter information about a new contact or to specify the status of the existing document (Fig. 1).
 




 Fig. 1 Fill out the record page as part of the process
 

![scr_chapter_processes_execution_page_save.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_execution/scr_chapter_processes_execution_page_save.png)



 The process moves to the next step after you save the record. However, the process author may specify additional completion conditions for a particular action. For example, specific fields are required.
 



 If the process creates a corresponding activity, the process will move to the next step only after you complete the activity with a result. Learn more:
 [Complete process activities](#title-2098-8) 
 .
 



 If you cannot complete a process action immediately after the activation, postpone it. To do this, click the
 
 Perform later
 
 button. Creatio will display additional fields. Enter the new step date and time in them (Fig. 2).
 




 Fig. 2 Postpone the process step
 

![scr_chapter_processes_execution_page_postpone.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_execution/scr_chapter_processes_execution_page_postpone.png)



 Answer a question
-------------------



 The process can display a page with a question (user dialog). Depending on the process configuration, you can select one or several answers (Fig. 3), which will affect the further process flow.
 




 Fig. 3 A question displayed as part of a process
 

![scr_chapter_processes_execution_question.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_execution/scr_chapter_processes_execution_question.png)



 If the process creates an activity when the step is completed, the process will move to the next step only after you complete the activity with a result. Learn more:
 [Complete process activities](#title-2098-8) 
 .
 



 If you cannot answer the question immediately, click the
 
 Perform later
 
 button to postpone it.
 



 Work with custom pages
------------------------



 The process may open a custom page for you to fill out. Custom pages can contain fields and buttons unavailable outside of the business process. For example, a process can display step-by-step forms with custom buttons, comment fields, lookup fields, etc. (Fig. 4).
 




 Fig. 4 A custom page opened as part of the process
 

![scr_chapter_processes_execution_page_custom.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_execution/scr_chapter_processes_execution_page_custom.png)



 The process will move to the next step only after you complete the required actions on the page.
 



 If the process creates a corresponding activity, the process will move to the next step only after you complete the activity with a result. Learn more:
 [Complete process activities](#title-2098-8) 
 .
 



 If you cannot complete the step immediately, click the
 
 Close
 
 button to postpone it.
 





 Note.
 
 The process displays
 [Pre-configured page](/docs/8-0/user/bpm_tools/process_elements_reference/user_actions/pre_configured_page/pre_configured_page_process_element)
 and
 [Auto-generated page](/docs/8-0/user/bpm_tools/process_elements_reference/user_actions/auto_generated_page/auto_generated_page_process_element)
 elements as custom pages.
 





