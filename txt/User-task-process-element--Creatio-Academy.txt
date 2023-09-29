


 The
 
 User task
 
 process elements represent generic activities that are performed within a process. The function of the
 
 User task
 
 element and its parameters depend on the type of user task selected in the element setup area (Fig. 1).
 




 Fig. 1 The
 
 User task
 
 element setup area
 

![chapter_process_designer_user_task.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/chapter_process_designer_user_task.png)




 User task
 
 – shows the type of user task. After this field is populated, the user task parameters will be added on the
 
 Parameters
 
 tab of the setup area (Fig. 2).
 




 Fig. 2 List of user task parameters
 

![chapter_process_designer_user_task_parameters.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/chapter_process_designer_user_task_parameters.png)



 You can fill out these fields using the
 parameter value window
 .
 





 Note.
 
 You can select a specific record or define it based on information from other process elements.
 




 Use the
 ![btn_chapter_designer_user_task_designer_task00021.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/btn_chapter_designer_user_task_designer_task00021.png)
 button to open the User Task Designer for editing the parameters.
 



 User tasks support
 [collection parameters](/docs/7-18/user/bpm_tools/business_process_setup/collections/process_collections) 
 that contain complex values, each representing several entries. For example, several contacts with the name, address, and phone number for each contact. To set up a collection parameter in the user task, open the task in the User Task Designer, add the “Serializable list of composite values” parameter with the needed sub-parameters, and code the business logic.
 



 The
 
 Elements
 
 menu includes basic activities (“Perform task” and “Write email”) that you can use when creating business processes.
 



 In addition to basic process activities, the list also contains system user tasks used to implement the basic logic of sections, for example, initializing details in the section. As a rule, system user tasks are used in the base page and object processes and can be inherited by other pages and objects.
 




