


 The
 
 Process file
 
 process element lets you automate file operations in business processes (Fig. 1).
 




 Fig. 1 The
 
 Process file
 
 process element
 

![process_file_element_1.png](/docs/sites/en/files/images/BPM_Tools/process_file/process_file_element_1.png)
![process_file_element_1.png](/docs/sites/en/files/images/BPM_Tools/use_process_parameters/process_file_element_1.png)



 The
 
 Process file
 
 element lets you:
 


* Read and copy files from the
 
 Attachments
 
 details of Creatio records.
* Get files from process parameters.
* Generate Word and Fast Report reports.



 There are several ways to take advantage of the read or generated files:
 


* Use them during the business process runtime. For example, send the files as email attachments.
* Save them to the
 
 Attachments
 
 detail of other records (Fig. 2).




 Fig. 2 Setting up the
 
 Process file
 
 element
 

![process_file_new_report_generate.gif](/docs/sites/en/files/images/BPM_Tools/process_file/process_file_new_report_generate.gif)



 Process files in a business process
-------------------------------------


### 
 Example setup for object files





 Case.
 
 Copy 10 most recent files on the
 
 Attachments
 
 detail from one contact to a different contact's detail.
 




 Set up the
 
 Process file
 
 element the following way (Fig. 3).
 


1. What is the source of the file?
 
 – select “Attachments and notes of the object” to let the element read the files on the
 
 Attachments
 
 detail.
2. Which object to receive file from?
 
 – select a Creatio object that contains the relevant files. In this case the relevant object is “Contact attachment”.
3. How to filter records?
 
 – set the necessary filters and specify the number of records to read. In this case, select the attachments of James Smith and specify 10 records. This way, the element will use the first 10 records that correspond to the sorting order (see below). Read more about working with filters in the
 [Filters](/docs/8-0/user/platform_basics/business_data/filters_shortcut/filters) 
 article.
4. How to sort records?
 
 – specify the sorting order. For example, changing the sorting order helps if there is a large number of documents in the
 
 Attachments
 
 detail yet only the most recent documents are relevant. In this case, sort the records by creation date in descending order.
5. What to do with file?
 
 – select one of the following options:
	1. “
	 **Use in process** 
	 ” if you need to use the file records in the process itself without saving the files to any Creatio object or if you need to to pass the files to a different business process as a parameter.
	2. “
	 **Save to “Attachments and notes” of the object** 
	 ” if you need to save the files to the
	 
	 Attachments
	 
	 detail of a particular object. You can also use the file collection in the process itself or pass these files to another business process as a parameter.
	   
	
	 In this case, select “Save to “Attachments and notes” of the object”.
	 
	
	
	 Note.
	 
	 If you select “Save to “Attachments and notes” of the object” in the
	 
	 Process file
	 
	 element, Creatio will save the Ids of the copied file records. If necessary, you can connect the other process elements to these record Ids.
6. What object to save file to?
 
 displays if you select “Save to “Attachments and notes” of the object” in the previous step. Specify the
 
 Attachments
 
 detail of the Creatio object that will contain the copied files. In this case you need to copy the files from a Creatio contact to a different contact's detail, therefore select “Contact attachment”.
   

 A new field connected to the selected object will appear. Specify the record that will store the saved files in this field. In this case, the
 
 Attachments
 
 detail is connected to the “Contact” object. Use
 [parameters](/docs/7-17/user/bpm_tools/business_process_setup/parameters/process_parameters) 
 or values to fill out this field. For example, click “Lookup value”, specify the relevant contact from the list, and click
 
 Select
 
 .




 Fig. 3 Setting up the
 
 Process file
 
 element for file processing
 

![process_file_word.png](/docs/sites/en/files/images/BPM_Tools/process_file/process_file_word.png)



 That way the element will copy the first 10 files selected based on the sorting order from the
 
 Attachments
 
 detail of the contact (e.g., James Smith) and save the files to the
 
 Attachments
 
 detail of another contact (e.g., Valerie E. Murphy) during a business process.
 


### 
 Example setup for process parameter files





 Example.
 
 Get the file from a process parameter and add it to the current contact’s
 
 Attachments
 
 detail.
 




 To do this, set up the
 
 Process file
 
 element as displayed on Fig. 4.
 


1. What is the source of the file?
 
 – select “Process parameter” to enable the element to read process parameters of the “File” type.
2. Files
 
 – specify the process parameter that contains the relevant file. You can specify a single file or a collection. Click the
 ![btn_process_element_settings_lookup00002.png](https://academy.creatio.com/docs/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_creation_parameters/btn_process_element_settings_lookup00002.png)
 button next to the field and select:
	* “
	 **Process parameter** 
	 ” to select the parameter whose value you want to pass.
	* “
	 **Formula** 
	 ” to set up file generation conditions based on the process parameters.
3. What object to save file to?
 
 – specify the
 
 Attachments
 
 detail of a Creatio object to store the copied files. Since this example requires copying the file to the current contact’s detail, select the “Contact attachment” value.
 



 Depending on the specified object, a new field may appear. Use this field to specify the record to store the saved files. For this example, the
 
 Attachments
 
 detail is connected to the “Contact” object. Use
 [parameters](/docs/7-17/user/bpm_tools/business_process_setup/parameters/process_parameters) 
 or values to fill out this field. For example, select “Current user contact.”




 Fig. 4 Setting up the
 
 Process file
 
 element to process a file from the parameter
 

![process_file_from_parameter.png](/docs/sites/en/files/images/BPM_Tools/process_file/process_file_from_parameter.png)


 As a result, Creatio will save the file retrieved from the process parameter to the current user’s
 
 Attachments
 
 detail.
 




 Generate reports in a business process
----------------------------------------



 This functionality is available for Creatio version 7.17.2 and up.
 





 Case.
 
 Generate an order report and save it to the
 
 Attachments
 
 detail of a partnership.
 






 Note.
 
 The
 
 Partnerships
 
 section is available in Sales Creatio Enterprise and CRM Creatio.
 




 Set up the
 
 Process file
 
 element the following way (Fig. 5).
 


1. What is the source of the file?
 
 – select “Generated report” to let the element generate a report during the process itself.
2. What report to generate?
 
 – select an available report from the dropdown. In this case, select “Order”.
   

 You can generate Word or Fast Report reports. Fast Report lets you generate a report for each record. Activate this option by checking the
 
 Generate separate report for each record
 
 box. By default,
 **Fast Report** 
 generates a single report with all the data of the filtered records.
   

**Word** 
 always generates individual reports for each record. Learn more about generating reports in the
 [Print-ready reports](https://academy.creatio.com/docs/user/no_code_customization/print_ready_reports) 
 section.
3. Section
 
 – displays the section used as a report source. This is a non-editable field.
4. How to filter records?
 
 – set the necessary filters. In this case, filter orders issued in specific currencies: Euro or US Dollar. Read more about working with filters in the
 [Filters](/docs/8-0/user/platform_basics/business_data/filters_shortcut/filters) 
 article.
5. File name
 
 – set a custom report file name pattern. Use
 [parameters](/docs/7-17/user/bpm_tools/business_process_setup/parameters/process_parameters) 
 or values to fill out this field. For example, click “Column from this selection” → “Number” to set the file name pattern based on the order number.
6. File name
 
 – set a custom report file name pattern. The file name will consist of the report’s name and the value specified in this parameter. For example, select
 
 Column from this selection
 
 →
 
 Number
 
 to make the name of the generated file look like this: “Order. ORD-30.”
7. What to do with file?
 
 – select one of the following options:
	1. “
	 **Use in process** 
	 ” if you need to use the file records in the process itself without saving the files to any Creatio object or if you need to to pass the files to a different business process as a parameter.
	2. “
	 **Save to “Attachments and notes” of the object** 
	 ” if you need to save the files to the
	 
	 Attachments
	 
	 detail of a particular object. You can also use the file collection in the process itself or pass these files to another business process as a parameter.
	   
	
	 In this case, select “Save to “Attachments and notes” of the object”.
	 
	
	
	 Note.
	 
	 If you select “Save to “Attachments and notes” of the object” in the
	 
	 Process file
	 
	 element, Creatio will save the Ids of the copied file records. If necessary, you can connect the other process elements to these record Ids.
	3. What object to save file to?
	 
	 displays if you select “Save to “Attachments and notes” of the object” in the previous step. Specify the
	 
	 Attachments
	 
	 detail of the Creatio object that will contain the copied files. In this case you need to save the generated report to the partnership record, therefore select “Partnership attachment”.
	   
	
	 A new field connected to the selected object will appear. Specify the record that will store the saved files in this field. In this case, the
	 
	 Attachments
	 
	 detail is connected to the “Partnership” object. Use
	 [parameters](/docs/7-17/user/bpm_tools/business_process_setup/parameters/process_parameters) 
	 or values to fill out this field. For example, click “Lookup value”, specify the relevant partnership from the list, and click
	 
	 Select
	 
	 .




 Fig. 5 Setting up the
 
 Process file
 
 element for report generation
 

![process_file_report.png](/docs/sites/en/files/images/BPM_Tools/process_file/process_file_report.png)



 That way the element will generate a set of reports for all the filtered records of the
 
 Orders
 
 section during a business process. Creatio will save the reports to the
 
 Attachments
 
 detail of the partnership (for instance, ClearSoft Systems).
 




