


 Business processes in Creatio can be run multiple times. Each time a process is run, a separate process instance is created. This instance can be linked to different existing records in the system and records created during a process flow.
 



 To monitor the processes that affect different system records, a list of linked business processes can be saved for those records.
 



 All records that a process is connected to are displayed on the
 
 Linked objects
 
 block of the
 
 Process log
 
 page.
 



 The
 
 Link process to object
 
 item (Fig. 1) is used to connect a process to a certain record in the system.
 




 Fig. 1 Using the
 
 Connect process to object
 
 process element
 

![scr_process_designer_usertask_connect_to_object.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_usertask_connect_to_object.png)



 Specify the parameters of linking a process to an object using the
 
 Connect process to object
 
 element setup area (Fig. 2):
 




 Fig. 2
 
 Connect process to object
 
 process element properties
 

[![chapter_process_designer_user_task_connect.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/chapter_process_designer_user_task_connect.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/chapter_process_designer_user_task_connect.png)


1. Connected object
 
 – This field contains the name of the object with which the process should be connected. You can fill in this field using the
 parameter value window
 .
2. In the
 
 Record of connected object
 
 field, you can specify the record with which the process should be connected. You can fill in this field using the
 parameter value window
 . You can select a specific record or define it based on information from other process elements.




