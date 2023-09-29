


 You can use business processes to grant or deny
 [access permissions](http://academy.creatio.com/documents/?product=administration&ver=7&id=1014) 
 to a Creatio record. Any
 event
 can trigger the process automatically on specific conditions.
 





 Example.
 
 Set up a business process to strip all Creatio users of their permissions to edit or delete a contact whenever its type is changed to “Employee”. Only members of the “HR. Managers group” organizational role can view, edit or delete the contact.
 




 Business process diagram (Fig. 1) elements:
 


1. [The
 
 Signal
 
 start event](/docs/8-0/user/bpm_tools/process_elements_reference/events/signal/signal_start_event) 
 triggers the process when a contact’s type is changed to “Employee” and records the Id of the contact record.
2. [The
 
 Change access rights
 
 element](/docs/8-0/user/bpm_tools/process_elements_reference/system_actions/change_access_rights/change_permissions_process_element) 
 sets permissions to update or ddelete Creatio records. This element can obtain the contact’s id from the
 
 Signal
 
 element.
 





 Fig. 1
 

 The “Change access permissions to modify new employee record” business process
 

![chapter_process_creation_designer_access_rights_process.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_process_creation_designer_access_rights_process.png)







 To do this:
 


1. On the process diagram, add the
 [Signal
 
 start event](/docs/8-0/user/bpm_tools/process_elements_reference/events/signal/signal_start_event) 
 and specify its parameter values (Fig. 2).
	1. In the
	 
	 Object
	 
	 field, select “Contact”.
	2. In the
	 
	 Which event should trigger the signal?
	 
	 field, select “Record modified”.
	3. In the
	 
	 Changes expected
	 
	 field, select “In any of the selected fields”, and add the “Type” column.
	4. In the
	 
	 The modified record must meet filter conditions
	 
	 field, select “Type = Employee”.
	 
	
	
	
	
	
	 Fig. 2
	 
	 The
	 
	 Signal
	 
	 start event parameters
	 
	
	![chapter_process_creation_designer_employee_type.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_process_creation_designer_employee_type.png)
2. Add the
 [Change access rights
 
 process element](/docs/8-0/user/bpm_tools/process_elements_reference/system_actions/change_access_rights/change_permissions_process_element) 
 on the process diagram and set up its parameters (Fig. 4).
3. In the
 
 Which object to apply access rights to?
 
 field, select “Contact”.
4. In the
 
 Apply access rights to all records that match conditions
 
 field, set up a filter (Fig. 3) by the Id column (“Id=Contact type updated.Unique identifier of record”):
 





 Note.
 
 You can learn more about passing the unique record identifier (Id) between process elements in the
 [Process parameters](/docs/7-17/user/bpm_tools/business_process_setup/parameters/process_parameters#XREF_95466) 
 article.
 



	1. Click
	 
	 + Add condition
	 
	 to add a new filter condition.
	2. In the pop-up window, select “Id” from the drop-down list.
	3. Click <?> and select
	 
	 Compare with parameter
	 
	 .
	4. In the pop-up window, under
	 
	 Process elements
	 
	 , select the start signal event (on the left).
	5. Select the “Unique identifier of record” parameter on the right.
	 
	
	
	
	
	
	 Fig. 3
	 
	 Setting up a filter by the Id column
	 
	
	![chapter_process_creation_designer_access_rights_element_id_filter.GIF](/docs/sites/en/files/images/BPM_Tools/remove_record_permissions/chapter_process_creation_designer_access_rights_element_id_filter.GIF)
5. Click
 ![btn_com_add_tab00021.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_com_add_tab00021.png)
 in the
 
 Which access rights to remove?
 
 field and select “For all users and roles”. Clear the checkbox under
 ![icn_chapter_process_designer_read_access.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/icn_chapter_process_designer_read_access.png)
 to remove permissions to edit or delete the record.
6. Click
 ![btn_com_add_tab00022.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_com_add_tab00022.png)
 in the
 
 Which access rights to add?
 
 field and select “For a user role”.
 


	1. In the “Role” field that appears, click
	 ![btn_process_element_settings_lookup00023.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_process_element_settings_lookup00023.png)
	 and choose “Lookup value”.
	2. Select the “HR, Managers group” organizational role in the opened window.
	 
	
	
	
	
	
	 Fig. 4
	 
	 The
	 
	 Change access rights
	 
	 process element parameters
	 
	
	![chapter_process_creation_designer_access_rights_element_paramters.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/chapter_process_creation_designer_access_rights_element_paramters.png)
7. After creating the process elements, connect them on the diagram and save the process.
   

 As a result, each time a contact’s type is changed to “Employee”, all Creatio users are stripped of their permissions to edit or delete the contact, and only members of the “HR. Managers group” organizational role obtain full access to the record and can view, modify or delete it.”





 Note.
 
 Please make sure that access to operations with the object (in this case, “Contact”) is enabled in the
 
 Object permissions
 
 section in the System Designer. Learn how to set up object operation permissions in the
 [Object operation permissions](https://academy.creatio.com/documents?product=BPMS&ver=7&id=250) 
 article.
 





