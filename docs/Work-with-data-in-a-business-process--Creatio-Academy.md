







 Read data from the record that triggered the process
-----------------------------------------------------------



 If a business process is run by a
 
 Signal
 
 start event, it will store the Id of the corresponding record in its outgoing parameter (Fig. 1).
 





 Fig. 1
 

 Getting the Id of the record that triggered the signal
 

![scr_chapter_bpms_data_start_signal_parameter_id.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_start_signal_parameter_id.png)



 For example, if a process is set to run every time an activity is added, you will be able to access the id of the added activity.
 



 To use the data (i.e., a field value) of the record further down the process, you need to obtain its field values using the
 
 Read data
 
 element. For example if the process was triggered by adding a new activity, you will know which activity is that, but will not be able to access that activity data, such as subject or assignee, unless you “read” them.
 



 To fetch the data from the record that triggered the process, add the
 
 Read data
 
 element on the diagram (Fig. 2) and set up its properties (Fig. 3):
 





 Fig. 2
 

 Reading the data of the record that triggered the business process
 

![scr_chapter_bpms_data_signal_process.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_signal_process.png)





 Fig. 3
 

 Specifying the record in the
 
 Read data
 
 element
 

![scr_chapter_bpms_data_read_signal_data.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_signal_data.png)


1. In the
 
 Which data read mode to use?
 
 field, select “Read the first record in the selection”.
2. In the
 
 Which object to read data from?
 
 field, select the object whose record triggered the process start signal event. For example, if the start signal event is set up so that the process starts whenever a new activity is added, select the “Activity” object.
3. Set up the following filter by the Id column and the value of the
 
 Unique identifier of record
 
 parameter of the start signal event:
 


	1. Click
	 
	 add
	 
	 and select the
	 
	 Id
	 
	 column.
	2. Click <?> and select
	 
	 Compare with parameter
	 
	 option in the menu.
	3. In the window that appears, select the “Unique identifier of record” parameter of the
	 
	 Signal
	 
	 start event (Fig. 4).
	 
	
	
	
	
	
	 Fig. 4
	 
	 Getting the Id of the record that triggered the signal
	 
	
	![scr_chapter_bpms_data_start_signal_parameter_id00001.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_start_signal_parameter_id00001.png)
4. There is no need to set up record sorting in the
 
 How to sort records?
 
 block, since only one record will match a filter by Id.
5. Specify the columns whose values must be fetched:
 


	1. Select “Read data from all columns” to read values of all columns of the record.
	2. Select “Read data from selected columns only” (Fig. 5), then click
	 
	 + Add column
	 
	 and select the columns whose values you are going to use later, down the process.
	 
	
	
	
	
	
	 Fig. 5
	 
	
	 Reading data from specific columns
	 
	
	![scr_chapter_bpms_data_read_select_colums.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_select_colums.png)





 Note.
 
 We recommend limiting the number of columns to read data from, as reading too many columns will affect process performance.
 




 As a result, the added
 
 Read data
 
 element will obtain the values of the specified columns for the record whose Id matches the Id of the record that triggered the process. The column data will be passed to the outgoing parameters of the
 
 Read data
 
 element.
 








 Read data from a record that matches certain criteria
------------------------------------------------------------



 If the Id of the needed record is unavailable, you can filter and sort records, then read the data from the first record in the resulting list. For example, you can read data of the latest completed “Call” activity.
 



 To read data of a specific record, populate the fields of the
 
 Read data
 
 element the following way (Fig. 6):
 





 Fig. 6
 

 Example of
 
 Read data
 
 element settings for reading the first record in selection
 

![scr_chapter_bpms_data_read_call.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_call.png)


1. In the
 
 Which data read mode to use?
 
 field, select “Read the first record in the selection”.
2. In the
 
 Which object to read data from?
 
 field, select the object that contains the needed record. For example, to read activity data, select the “Activity” object.
3. Set up the filter. To specify static filter values, select the
 
 Compare with value
 
 option. For example, to select completed calls, you need to filter the activities by the
 
 Type
 
 and
 
 Status
 
 columns, as shown on Fig. 6.
4. Set up record sorting: select a column to sort records by and select the sorting mode (“Ascending“ or “Descending“), so that the needed record is the first in the list of filtered records. For example, to obtain latest activity, sort records by the
 
 Due
 
 column in descending order (i.e., later “larger” dates are on top).
5. Specify the columns whose values must be fetched:
 


	1. Select “Read data from all columns” to read values of all columns of the record.
	2. Select “Read data from selected columns only” (Fig. 7), then click
	 
	 + Add column
	 
	 and select the columns whose values you are going to use later, down the process.
	 
	
	
	
	
	
	 Fig. 7
	 
	 Reading data from specific columns
	 
	
	![scr_chapter_bpms_data_read_select_colums00002.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_select_colums00002.png)





 Note.
 
 We recommend limiting the number of columns to read data from, as reading too many columns will affect process performance.
 




 As a result, the added
 
 Read data
 
 element will get a list of records that match the filter, sort them in the specified order and obtain the values of the needed columns for the first record in the list. The column data will be passed to the outgoing parameters of the
 
 Read data
 
 element.
 








 Read the data of the record being processed
--------------------------------------------------



 Some business processes are designed to run by a chosen record in a specific section. For example, you can run a “Meeting with customer” process for a specific customer account. These processes are available in the
 
 Run process
 
 menu in the list and on the record page of the corresponding section (Fig. 8).
 





 Fig. 8
 
 An example of the customized
 
 Run process
 
 menu in the
 
 Accounts
 
 section
 

![scr_chapter_bpms_data_running_process_by_record.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_running_process_by_record.png)



 To set up such a process, add a separate process parameter (Fig. 9) where Creatio will automatically pass the record Id (e.g., the account for which the process is run).
 





 Fig. 9
 

 Example of a process parameter that stores a section record
 

![scr_chapter_bpms_data_process_parameter_account.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_process_parameter_account.png)



 Later down the process flow, you can always obtain the record Id from that process parameter.
 



 To read a record that has its Id stored in a process parameter, add a
 
 Read data
 
 element on the process diagram and populate its setup area (Fig. 10):
 





 Fig. 10
 

 Mapping a
 
 Read data
 
 element to a process parameter
 

![scr_chapter_bpms_data_read_process_parameter.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_process_parameter.png)


1. In the
 
 Which data read mode to use?
 
 field, select “Read the first record in the selection”.
2. In the
 
 Which object to read data from?
 
 field, select the object, which contains the records of the needed type. For example, if the process is run by an account record, select the “Account” object.
3. Set up the following filter by the Id column and the parameter that stores the record by which the process was run:
 


	1. Click
	 
	 Add
	 
	 and select the
	 
	 Id
	 
	 column.
	2. Click <?> and select
	 
	 Compare with parameter
	 
	 option in the menu.
	3. In the opened
	 
	 Select parameter
	 
	 window, click
	 
	 Process parameters
	 
	 and select the parameter that contains the needed record (Fig. 11).
	 
	
	
	
	
	
	 Fig. 11
	 
	 Getting the Id of the record by which the process was run
	 
	
	![scr_chapter_bpms_data_process_parameter_id.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_process_parameter_id.png)
4. There is no need to set up record sorting in the
 
 How to sort records?
 
 block, since only one record will match a filter by Id.
5. Specify the columns whose values must be fetched:
 


	1. Select “Read data from all columns” to read values of all columns of the record.
	2. Select “Read data from selected columns only”, then click
	 
	 + Add column
	 
	 and select the columns whose values you are going to use later, down the process.








 Read the data of a record from another object
----------------------------------------------------



 When a
 
 Read data
 
 element reads a lookup column (e.g., a
 
 Primary contact
 
 field of an account), it obtains the Id of the corresponding lookup record. To obtain the actual values of the record, selected in the lookup column, it must be read separately.
 



 To read the data from a linked record, you will need to use 2
 
 Read data
 
 elements (Fig. 12).
 





 Fig. 12
 
 Reading account data and then the account’s primary contact data
 

![scr_chapter_bpms_data_read_linked_record.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_linked_record.png)


* First
 
 Read data
 
 element reads the data of the parent record, namely the lookup column that references the linked record.
* Second
 
 Read data
 
 element obtains the Id of the linked record from the first element an then reads the linked record itself.



 Make sure that the corresponding lookup column is added to the list of read columns in the first
 
 Read data
 
 element (Fig. 13).
 





 Fig. 13
 
 Reading the value of the lookup column that references the needed linked record
 

![scr_chapter_bpms_data_read_linked_record_field.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_linked_record_field.png)



 Set up the second
 
 Read data
 
 element:
 


1. In the
 
 Which data read mode to use?
 
 field, select “Read the first record in the selection”.
2. In the
 
 Which object to read data from?
 
 field, select the object that contains the needed record. For example, to read contact data, select the “Contact” object.
3. Set up the filter by Id:
 


	1. Add the
	 
	 Id
	 
	 column to the filter and select
	 
	 Compare with parameter
	 
	 .
	2. In the
	 
	 Select parameter
	 
	 window, select the
	 
	 Read data
	 
	 element that obtained information about the record with the lookup column. For example, if you need to read data of the account’s contact, select the
	 
	 Read data
	 
	 element that obtained information from the account record.
	3. In the right area of the
	 
	 Select parameter
	 
	 window, select the first
	 
	 Read data
	 
	 element, and then the lookup parameter, where the needed record from the linked object is selected (Fig. 14). For example, if you need to read data of the account’s contact, select the
	 
	 Primary contact
	 
	 column.
	 
	
	
	
	
	
	 Fig. 14
	 
	
	 Selecting the Id of the linked record
	 
	
	![scr_chapter_bpms_data_read_linked_record_id.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_linked_record_id.png)
4. Specify the columns of the connected record whose values must be fetched, or select “All columns“ to fetch all data.
 





 Note.
 
 We recommend limiting the number of columns to read data from, as reading too many columns will affect process performance.




 Calculate sum, minimum, maximum and average of several records
-----------------------------------------------------------------



 Use the “Calculate function“ mode of the
 
 Read data
 
 element for calculating various functions using the data from the records that match a filter. You can calculate the sum of values in a specific column for a number of records, as well as determine minimum, maximum or average value of a specific column. For example, you can calculate the total duration of activities of a specific employee for today.
 



 To calculate a function, add the
 
 Read data
 
 element on the diagram and set up its properties (Fig. 15):
 





 Fig. 15
 
 The
 
 Read data
 
 element setup area “Calculate function“ mode
 

![scr_chapter_bpms_data_read_calculate_function_setup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_calculate_function_setup.png)


1. In the
 
 Which data read mode to use?
 
 field, select “Calculate function“.
2. In the
 
 Which object to read data from?
 
 field, select the object (section, detail or lookup). For example, to calculate the duration of activities, select the “Activity“ object.
3. In the
 
 Function
 
 field, select the function to use for calculation. For example, to calculate the total duration of activities, select “Sum”.
4. In the
 
 By column
 
 field, select the column by which the value must be calculated. For example, to calculate the total duration of activities, select the “Duration (minutes)” column. Only the columns that are compatible with the selected function will be available for selection.
5. In the
 
 How to filter records?
 
 block, specify filter conditions for record selection. The function will be calculated only for the columns that match the filter. For example, to calculate the functions only for the current user’s activities that are due today, set up the filter as shown on Fig. 15.
 



 As a result, when the process is run, Creatio will access the data of the specified object, get a list of records that match the filter, and calculate the specified function by the values of the specified column. The resulting value will be passed in the outgoing parameter of the
 
 Read data
 
 element.




 Calculate the number of records that match a condition
---------------------------------------------------------



 Use the “Calculate the number of records“ mode of the
 
 Read data
 
 element for determining the number of records that match specific filer conditions. This is usually used for determining whether specific records exist (i.e., the number of records is not “0”), or whether the number of records reaches specific threshold. For example, you can calculate the number of calls an employee has scheduled for today.
 



 To calculate the number of records, add the
 
 Read data
 
 element on the diagram and set up its properties. Below is an example of calculating the number of records (Fig. 16).
 





 Fig. 16
 

 The
 
 Read data
 
 element setup area in the ”Calculate the number of records” mode
 

![scr_chapter_bpms_data_read_number.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_number.png)


1. In the
 
 Which data read mode to use?
 
 field, select “Calculate the number of records”.
2. In the
 
 Which object to read data from?
 
 field, select the object (section, detail or lookup) whose records to calculate. For example, to calculate the number of activities, select the “Activity“ object.
3. In the
 
 How to filter records?
 
 block, specify filter conditions for record selection. The
 
 Read data
 
 element will calculate only the number of records that match the filter. For example, to calculate the number of the current user’s activities that are due today, set up the filter as shown on Fig. 16.
 



 As a result, when the process is run, Creatio will access the data of the specified object, get a list of records that match the filter, and calculate the number of records in the list. The resulting value will be passed in the outgoing parameter of the
 
 Read data
 
 element.








 Read data from multiple records (collection)
---------------------------------------------------



 In the “Read collection of records” mode, the
 
 Read data
 
 element can obtain field values from several records. For example, you can read the names of all contacts of a specific account (Fig. 17).
 



 To read a collection of records, add the
 
 Read data
 
 element on the diagram and set up its properties:
 





 Fig. 17
 
 Example of
 
 Read data
 
 element settings for reading a collection of records
 

![scr_chapter_bpms_data_read_collection.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_collection.png)


1. In the
 
 Which data read mode to use?
 
 field, select “Read collection of records”.
2. In the
 
 Which object to read data from?
 
 field, select the object that contains the needed record. For example, to read contact data, select the “Contact” object.
3. Set up the filter. For example, to read all contacts of a specific account, set up a filter by the
 
 Account
 
 column and use the
 
 Compare with value
 
 option to select a specific account, or use the
 
 Compare with parameter
 
 option to map the filter value to the value of a process or a process element parameter.
4. Specify the limit the number of records in the resulting collection by populating the
 
 Read first ... records
 
 field. If you need to select all records that match the filter, specify the number larger than maximum possible records.
 





 Note.
 
 Reading more than 5000 records may cause performance issues.
5. If necessary, set up sorting in the
 
 How to sort records?
 
 block. Note that the process will read data from the first records in the list according to sorting rules.
6. Specify the columns whose values must be fetched:
 


	1. Select “Read data from all columns” to read values of all columns of the record.
	2. Select “Read data from selected columns only” (Fig. 18), then click
	 
	 + Add column
	 
	 and select the columns whose values you are going to use later, down the process.
	 
	
	
	
	
	
	 Fig. 18
	 
	 Reading data from specific columns
	 
	
	![scr_chapter_bpms_data_read_signal_data_columns.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_signal_data_columns.png)





 Note.
 
 We recommend limiting the number of columns to read data from, as reading too many columns will affect process performance.
 




 As a result, the
 
 Read data
 
 element will obtain the data of the specified columns for all records that match the filter and fit within the
 
 Read first ... records
 
 limit and pass their values to an outgoing parameter of the “collection” type.
 





 Fig. 19
 
 An example of outgoing
 
 Collection of records
 
 parameter of the collection type
 

![scr_chapter_bpms_data_read_array_params.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_read_array_params.png)





 Note.
 
 The complete list of element parameters is available on the
 
 Parameters
 
 tab in the
 
 Advanced
 
 mode.
 [Read more >>>](/docs/7-16/user/bpm_tools/business_process_setup/overview/process_designer#HT_chapter_process_designer_element_setup_area) 










 Add one record
---------------------



 You can add a new record to an object using the
 
 Add data
 
 element in the “Add one record” mode. For example, you can add current user as a participant of an activity that triggered the process.
 



 To add a single record, populate the fields of the
 
 Add data
 
 element in the following way (Fig. 20):
 





 Fig. 20
 
 The
 
 Add data
 
 element setup page in the
 
 Add one record
 
 mode
 

![scr_chapter_bpms_data_add_one.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_add_one.png)


1. Select an object to which the record will be added. For example, to add a record on the
 
 Participants
 
 detail of an activity page, you need to select the
 
 Activity participant
 
 object.
2. In the
 
 What is the data adding mode?
 
 field, select “Add one record”.
3. In the
 
 Which column values to set?
 
 field, add the columns that must be populated for the new record:
 


	1. Click
	 
	 + Add field
	 
	 and choose an object column from the list. A new field will be added in the
	 
	 Which column values to set?
	 
	 block. For example, when adding activity participants, you need to specify the activity and the participating contact.
	2. Click the
	 ![btn_process_element_settings_lookup.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_data/btn_process_element_settings_lookup.png)
	 icon in the field and populate it using standard functions of the Process Designer. For example, when adding an activity participant, add an
	 
	 Activity
	 
	 column and map it to a parameter that contains the Id of the needed activity, then add a
	 
	 Participant
	 
	 column and populate it with the needed contact (to specify the contact of the user who runs the process, click
	 ![btn_process_element_settings_lookup00003.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_data/btn_process_element_settings_lookup00003.png)
	 and select
	 
	 Current user contact
	 
	 ).
	 
	
	
	
	 As a result a new record will be added to the specified object. The record columns will be populated according to the settings in the
	 
	 Which column values to set?
	 
	 block. The other columns of the new record will be populated with default values or remain empty.








 Add multiple records
---------------------------



 You can add multiple records to an object using the
 
 Add data
 
 element in the “Add selection” mode. For example, you can add activity participants based on the contacts who live in Boston. In this case, “Activity participant” will be the target object and “Contact” – reference object.
 



 The added records will be based on a “selection”, which is a list of filtered records from another object. For example, you can add records to the
 
 Participants
 
 detail based on the selection from the “Contact” object (i.e., a list of filtered contacts). A filter by the
 
 City
 
 field will select all contacts who live in Boston, and an activity participant will be added based on each contact that matches filter.
 



 The column values from the selection can be passed to the added records. For example, the records in the “Activity participant” object must be linked to the corresponding contacts. When adding activity participants, you can populate the contact fields of the new records with the values from the corresponding contacts in the selection.
 



 To add a single record, populate the fields of the
 
 Add data
 
 element the following way (Fig. 21):
 





 Fig. 21
 
 The
 
 Add data
 
 element setup page in
 
 Add multiple records
 
 mode
 

![scr_chapter_bpms_data_add_selection.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_add_selection.png)


1. Select an object to which the records will be added. For example, to add records on the
 
 Participants
 
 detail of an activity page, you need to select the
 
 Activity participant
 
 object.
2. In the
 
 What is the data addition mode?
 
 field, select “Add selection”.
3. In the
 
 Selection from an object
 
 field, select the object whose data will be used in the new records. For example, we need to add activity participants based on the contacts who live in Boston. Hence, a selection from the “Contact” object is required.
4. Specify filter for the selection. If the filter is not applied, then Creatio will assume that the selection contains all records from the object specified in the
 
 Selection from an object
 
 field. For example, to get a list of contacts who live in Boston, apply a filter by the
 
 City
 
 column as shown on Fig. 21.
5. In the
 
 Which column values to set?
 
 field, add the columns that must be populated for the new records:
 


	1. Click
	 
	 + Add field
	 
	 and choose an object column from the list. A new field will be added in the
	 
	 Which column values to set?
	 
	 block. For example, when adding activity participants, you need to specify the activity and the participating contact.
	2. Click the
	 ![btn_process_element_settings_lookup00004.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_data/btn_process_element_settings_lookup00004.png)
	 icon in the field and populate it using standard functions of the Process Designer. For example, when adding an activity participant, add an
	 
	 Activity
	 
	 column and map it to a parameter that contains the Id of the needed activity, then add a
	 
	 Participant
	 
	 column and populate it with the contact Id from the selection (Fig. 22).
	 
	
	
	
	
	
	 Fig. 22
	 
	
	 Mapping the value of the new record to a column from the selection
	 
	
	![scr_chapter_bpms_data_add_selection_set_contactid.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_add_selection_set_contactid.png)



 As a result, for each record from the selection, a new record will be added to the specified object. The record columns will be populated according to the settings in the
 
 Which column values to set?
 
 block. The other columns of the new record will be populated with default values or remain empty. For example, for each contact who lives in Boston, a new activity participant will be added. For each added record, the
 
 Activity
 
 field will be populated with the needed activity, and the
 
 Participant
 
 field (which is a lookup field based on the “Contact” object) will be populated with the corresponding contact from the selection.
 








 Modify multiple records that match a condition
-----------------------------------------------------



 You can modify several existing records using the
 
 Modify data
 
 element. For example, you can change the status of all overdue activities to “Canceled”.
 



 To modify records, populate the fields of the
 
 Modify data
 
 element the following way (Fig. 23):
 





 Fig. 23
 

 Modifying all records that match a filter
 

![scr_chapter_bpms_data_modify.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_modify.png)


1. In the
 
 Which object data to modify?
 
 field, select the object whose records must be modified. For example, to change the status of activities, select the “Activity” object.
2. In the
 
 Modify all records that match condition
 
 block, set up a filter. All records that match the filter will be modified. For example, to modify all overdue activities, set up a filter by the
 
 Due
 
 column as shown on (Fig. 23).
3. In the
 
 Which column values to set for modified records?
 
 block, set up a list of columns whose values must be modified:
4. Click
 
 + Add field
 
 and select a field from the list. A new field will appear.
 


	1. Click
	 
	 + Add field
	 
	 and choose an object column from the list. A new field will be added in the
	 
	 Which column values to set for modified records?
	 
	 block. For example, to change the status of an activity, you need to modify the value in the
	 
	 Status
	 
	 field.
	2. Click the
	 ![btn_process_element_settings_lookup00005.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_data/btn_process_element_settings_lookup00005.png)
	 icon in the field and populate it using standard functions of the Process Designer. For example, to set the value in a lookup field to another specific value, select
	 
	 Lookup value
	 
	 in the menu an choose the needed value from the list (Fig. 22).
	 
	
	
	
	 As a result, the
	 
	 Modify data
	 
	 element will set the specified values to the corresponding fields for all records that match the filter. For example, it will change the value of the
	 
	 Status
	 
	 field to “Canceled” for all activities that were due yesterday or earlier.




 Modify specific record
-------------------------



 To modify a specific record, you need to obtain its Id from a process or process element parameter. If the Id of the needed record is available in the process, you can set up a filter by the
 
 Id
 
 column in the
 
 Modify data
 
 element. For example, you can use the
 
 Modify data
 
 element to complete an activity created earlier in the process flow.
 



 To modify records, populate the fields of the
 
 Modify data
 
 element the following way (Fig. 24):
 





 Fig. 24
 

 Modifying a specific record
 

![scr_chapter_bpms_data_modify_by_Id.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_modify_by_Id.png)


1. In the
 
 Which object data to modify?
 
 field, select the object whose records must be modified. For example, to change the status of activities, select the “Activity” object.
2. In the
 
 Modify all records that match condition
 
 block, set up a filter by the
 
 Id
 
 column. If the corresponding Id is available in a process, you can obtain it from the corresponding process or element parameter:
 


	1. In the
	 
	 Modify all records that match condition
	 
	 block, click
	 
	 +Add condition
	 
	 and select the
	 
	 Id
	 
	 column.
	2. Click <?> and select “Compare with parameter”. Select a process or element parameter that contains the needed Id (Fig. 25). For example, if you need to modify an activity created earlier in the process flow, select the corresponding
	 
	 Perform task
	 
	 element and its
	 
	 Task Id
	 
	 parameter.
	 
	
	
	
	
	
	 Fig. 25
	 
	 Setting up a filter to modify a specific record
	 
	
	![scr_chapter_bpms_data_modify_filter_id.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_modify_filter_id.png)
3. In the
 
 Which column values to set for modified records?
 
 block, set up a list of columns whose values must be modified:
 


	1. Click
	 
	 + Add field
	 
	 and choose an object column from the list. A new field will be added in the
	 
	 Which column values to set for modified records?
	 
	 block. For example, to change the status of an activity, you need to modify the value in the
	 
	 Status
	 
	 field.
	2. Click the
	 ![btn_process_element_settings_lookup00006.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_data/btn_process_element_settings_lookup00006.png)
	 icon in the field and populate it using standard functions of the Process Designer. For example, to set the value in a lookup field to another specific value, select
	 
	 Lookup value
	 
	 in the menu an choose the needed value from the list ().
	 
	
	
	
	 As a result, the
	 
	 Modify data
	 
	 element will set the specified values to the corresponding fields for all records that match the filter. For example, it will change the value of the
	 
	 Status
	 
	 field to “Canceled” for all activities that were due yesterday or earlier.








 Delete all records that match a condition
------------------------------------------------



 You can delete all records that match specific filter conditions. For example, you can delete all canceled future activities.
 



 To delete records that match a filter, populate the fields of the
 
 Delete data
 
 element the following way (Fig. 26):
 





 Fig. 26
 

 The
 
 Delete data
 
 element setup area
 

![scr_chapter_bpms_data_delete_filter.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_delete_filter.png)


1. In the
 
 Which object to delete data?
 
 field, select an object whose records must be deleted. For example, to delete activities, select the “Activity” object.
2. In the
 
 Delete all records that match condition
 
 area, specify filtering conditions for selecting a list of records to delete. For example, to delete future canceled activities, set up a filter by the
 
 Start
 
 and
 
 Status
 
 columns as shown on Fig. 25.
 



 As a result, the
 
 Delete data
 
 element will delete all records that match the filter. For example, it will delete all activities with the “Canceled” status and whose due date is tomorrow.








 Delete a specific record
-------------------------------



 To delete a specific record, you need to get its Id, provided the Id is available in the process. For example, you can delete a specific contact.
 



 To delete records that match a filter, populate the fields of the
 
 Delete data
 
 element the following way (Fig. 27):
 





 Fig. 27
 

 The
 
 Delete data
 
 element setup area
 

![scr_chapter_bpms_data_delete_id.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_data_delete_id.png)


1. In the
 
 Which object to delete data?
 
 field, select an object whose records must be deleted. For example, to delete activities, select the “Activity” object.
2. In the
 
 Delete all records that match condition
 
 area, set up a filter by the
 
 Id
 
 column. If the corresponding Id is available in a process, you can obtain the Id from the corresponding process or element parameter:
 


	1. In the
	 
	 Delete all records that match condition
	 
	 block, click
	 
	 +Add condition
	 
	 and select the
	 
	 Id
	 
	 column.
	2. Click <?> and select “Compare with parameter”. Select a process or element parameter that contains the needed Id (Fig. 28). For example, if you need to delete an activity created earlier in the process flow, select the corresponding
	 
	 Perform task
	 
	 element and its parameter
	 
	 Task Id
	 
	 .
	 
	
	
	
	
	
	 Fig. 28
	 
	
	 Selecting filter conditions
	 
	
	![scr_chapter_bpms_delete_data_parameter_id.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_data/scr_chapter_bpms_delete_data_parameter_id.png)



 As a result, the
 
 Delete data
 
 element will delete the record whose Id matches the Id in the filter. For example, it will delete the activity that was created earlier in the process flow.
 




