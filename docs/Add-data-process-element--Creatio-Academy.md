


 Use the
 
 Add data
 
 element (Fig. 1) to automatically create new records in a specific object.
 




 Fig. 1
 
 The
 
 Add data
 
 process element
 




![scr_process_designer_add_data00018.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_add_data00018.png)




 The records are added in the background, without opening any pages. This is useful for adding records automatically, without the user interference, or adding records to objects that do not have proper UI (e.g. a record page) for the user to populate them.
 



 The
 
 Add data
 
 element will add records in any object, regardless of the access permissions of the user who runs the process.
 



 The element has two modes (Fig. 2).
 




 Fig. 2
 
 Selecting a mode for an
 
 Add data
 
 element
 




![scr_chapter_bpms_data_add_modes.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_bpms_data_add_modes.png)




 Add one record
----------------



 The element adds a new record in the specified object (section, detail or lookup) with the specified field values. For example, you can add the current user as a participant of an activity that triggered the process. The element will return only the Id of the added record. To retrieve the remaining data from the added record, use the
 
 Read data
 
 element after the
 
 Add data
 
 element.
 



 Add selection
---------------



 The element adds multiple records to the target object (section, detail or lookup) based on a filtered list of records (a “selection”) from a reference object. The number and contents of the added records will depend on the records from the selection, namely:
 


* For each record of the selection, a new record will be created in the target object.
* You can populate fields of the new records with values from the corresponding records in the selection. To do this, select the
 
 Column from this selection
 
 option when specifying column values of the records to add (Fig. 3).




 Fig. 3
 
 Mapping column values of the new records to the columns from the selection
 




![scr_chapter_bpms_data_add_selection_values.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_bpms_data_add_selection_values.png)




 Use cases
-----------



 Information on how to use each mode is available below:
 


* [Add a single record](/docs/7-16/user/bpm_tools/process_element_use_cases/data/how_to_work_with_data#XREF_92339_How_to_add_a)
* [Add multiple records](/docs/7-16/user/bpm_tools/process_element_use_cases/data/how_to_work_with_data#XREF_10881_How_to_add)




