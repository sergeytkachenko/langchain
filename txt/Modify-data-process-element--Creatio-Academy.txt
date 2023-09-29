


 The
 
 Modify data
 
 process element (Fig. 1) is used to change field values of specific existing records.
 




 Fig. 1
 
 The
 
 Modify data
 
 process element
 




![scr_process_designer_modify_data00019.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_modify_data00019.png)




 The element can modify any number of records in one batch, but the changes in all of these records will be the same. For example, you can use the
 
 Modify data
 
 element to change the status of all activities to “Canceled”. To set different values for different records, use several
 
 Modify data
 
 elements.
 



 The records to modify are selected using the standard filter. For example, you can modify all activities whose due date was yesterday. You can modify one or several fields of the selected records.
 



 The changes are made on the background without opening the record edit pages. Use the
 
 Modify data
 
 element for any changes that do not require user interference or editing records in objects that do not have proper UI (e.g. a record page) for the user to edit them manually.
 



 The element can modify any record, regardless of the permissions of the user who runs the process.
 



 Use examples
--------------



 Information on how to use each of the modes is available below:
 


* [Modify multiple records that match a condition](/docs/7-16/user/bpm_tools/process_element_use_cases/data/how_to_work_with_data#XREF_65730_Modify_data)
* [Modify specific records](/docs/7-16/user/bpm_tools/process_element_use_cases/data/how_to_work_with_data#XREF_78838_Modifying_specific)




