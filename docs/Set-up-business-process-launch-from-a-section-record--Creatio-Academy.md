


 In Creatio, you can run a business process for a specific section record, e.g., a customer onboarding process can be run for a specific account, contact details verification process can be run for a specific contact, etc. Such a process, must be linked to the corresponding record via a process parameter of the “Id” type.
 



 Each record in Creatio has a unique identifier (Id), i.e. a code that uniquely identifies each record in the database. The Id of the needed record can be passed to a process parameter automatically, which in turn will enable you to work with that record as part of the process flow.
 





 Note.
 
 More information on identifying records by Id is available in the
 [Working with data](/docs/8-0/user/bpm_tools/process_element_use_cases/data/how_to_work_with_data) 
 article.
 




 For example, you can create a simple call scheduling business process (“Call a client”) and run it for individual records in the
 
 Contacts
 
 section (Fig. 1). The following three steps are required to create a business process:
 


1. [Create a unique Id parameter](#title-2784-3) 
 .
2. [Map the parameter to process elements](#title-2784-4) 
 .
3. [Add the business process to a section](#title-2784-5) 
 .
 



 When you select a record in the section and run the process, the process parameter value will be populated with the unique identifier of the selected record.
 



 Any element that needs to work with that record can obtain its Id from the process parameter afterwards.
 





 Fig. 1
 
 Simple task scheduling process
 

![chapter_process_parameters_business_process_scheduling_call.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_parameters/chapter_process_parameters_business_process_scheduling_call.png)




 1. Create a unique Id parameter
----------------------------------



 To create a process parameter that will store the unique Id of a record:
 


1. Open the sub-process in the Process Designer.
2. In the process setup area, go to the
 
 Parameters
 
 tab.
3. Click
 
 Add parameter
 
 and select
 
 Other
 
 >
 
 Unique identifier
 
 (Fig. 2). This parameter will store the Id of the record for each instance of this business process.
 





 Fig. 2
 
 How to add parameters to a process
 

![chapter_process_parameters_business_process_add_Id_parameter.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_parameters/chapter_process_parameters_business_process_add_Id_parameter.png)
4. You can change the
 
 Title
 
 field to make the parameter more recognizable. The
 
 Code
 
 field will be populated automatically (Fig. 3).
 





 Fig. 3
 

 Parameter properties area
 

![chapter_process_parameters_parameter_properties_area.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_parameters/chapter_process_parameters_parameter_properties_area.png)
5. Click
 
 Save
 
 in the parameter properties area.
6. Save the process diagram.




 2. Map the parameter to process elements
-------------------------------------------



 The new process parameter can now be used to connect the necessary process elements to the section record for which the process was started. For example, you can connect the
 
 Perform task
 
 element to the contact record for which the process was run, and automatically populate the
 
 Contact
 
 field in the created task.
 



 To specify the element parameters:
 


1. Select the element on the diagram and make the changes in the element setup area to map an element parameters (Fig. 4):
 


 Fig. 4
 


 Perform task
 
 process element parameters
 

![chapter_process_parameters_business_process_perform_task_action_properties.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_parameters/chapter_process_parameters_business_process_perform_task_action_properties.png)
2. Click the
 ![btn_process_element_settings_lookup00001.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_parameters/btn_process_element_settings_lookup00001.png)
 button next to the field of the parameter, which must be mapped to a process parameter and select
 
 Process parameter
 
 from the menu (Fig. 5). For example, if the process is run for a contact record, click the
 
 Contact
 
 field.
 





 Fig. 5
 

 Opening the parameter selection window
 

![chapter_process_parameters_parameter_selection.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_parameters/chapter_process_parameters_parameter_selection.png)
3. In the window that appears, click
 
 Process elements
 
 .
4. In the list of the process parameters, select the one that stores the needed value (Fig.  6). For example, you can map the
 
 Contact
 
 parameter of a
 
 Perform task
 
 element to the process parameter that stores the Id of the contact record. As a result, when the process is executed, the
 
 Contact
 
 field of the created task will be populated with the contact whose Id was stored in the process parameter.
 





 Fig. 6
 

 Parameter selection window
 

![chapter_process_parameters_business_process_select_parameter.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_parameters/chapter_process_parameters_business_process_select_parameter.png)
5. Save the process diagram.
 



 As a result, whenever the process is run, the value of the element parameter will be populated automatically from the corresponding process parameter. For example, the contact in the
 
 Connected to
 
 block in the task will be populated from the
 
 Contact
 
 parameter of the process.






 3. Add the business process to a section
---------------------------------------------



 You can add business processes to any section using the section wizard. For example, you can add the “Call a client” process to the
 
 Contacts
 
 section to be run for specific contacts.
 



 To do this:
 


1. Open the needed section and access the section wizard from the
 
 View
 
 menu.
2. Open the
 
 Business processes
 
 tab, and click the
 ![btn_basis_filters_add_condition.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_parameters/btn_basis_filters_add_condition.png)
 button next to the
 
 Run business process from section
 
 field (Fig. 7).
 





 Fig. 7
 
 Adding the business process to a section
 

![chapter_process_parameters_parameter_add_process_to_section.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_parameters/chapter_process_parameters_parameter_add_process_to_section.png)
3. In the window that appears, populate the following fields (Fig. 8):
 





 Fig. 8
 

 Business process launch settings
 

![chapter_process_parameters_business_process_launch_settings.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_parameters/chapter_process_parameters_business_process_launch_settings.png)


	1. Which process to run?
	 
	 – select the process to run for section records. For example, you can select the “Call a client” process.
	2. Select the “For selected record” option to run the process for individual records in the section.
	3. In the
	 
	 Process parameter where the record is passed
	 
	 field, specify the process parameter, that will store the record Id. This must be a parameter of the “Id” type, such as the “Record Id parameter created earlier.
4. Save the changes.



 As a result, a new “Run process” button will appear in the section list (Fig. 9) and on record pages of the section. Clicking this button will enable you to run processes for records of this section.
 





 Fig. 9
 

 “Run a process” button
 

![chapter_process_parameters_business_process_in_record.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_parameters/chapter_process_parameters_business_process_in_record.png)



 For example, running the “Call a client” process created in the previous step will automatically create a task in your calendar and connect it to the contact record for which the process was run.
 




