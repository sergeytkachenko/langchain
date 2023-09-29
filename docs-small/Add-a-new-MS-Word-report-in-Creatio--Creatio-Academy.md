


 After you
 [install the MS Word plug-in](/docs/8-0/user/customization_tools/print_ready_reports/install_the_plugin/install_creatio_plug-in_for_ms_word) 
 , you can start setting up the report.
 



 To add a new report:
 


1. Add a new report record in Creatio.
 [Read more >>>](#title-280-1)
2. Navigate to the record's page and set up the fields and tables to display in the report.
 [Read more >>>](#title-280-2) 






 Example.
 
 Set up a “Meeting minutes” report in the
 
 Activities
 
 section.



 Add a new MS Word report record in Creatio
--------------------------------------------





 Note.
 
 If you plan to migrate the package to a different environment,
 [create a new package](/docs/7-17/developer/development_tools/packages/packages#case-1198) 
 and set it as current.
 



1. Click
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/btn_system_designer.png)
 to open the System Designer.
2. Navigate to the “System setup” block and click “
 **Report setup** 
 .”
 



 This will open the
 
 Report setup
 
 section.
3. Click
 
 New report
 
 →
 **MS Word** 
 (Fig. 1).
 




 Fig. 1 MS Word report setup
 

![chapter_print_forms_setup_add_report.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/chapter_print_forms_setup_add_report.png)
4. Enter the new report name, e. g. “Meeting minutes.”
5. Select a section where the report should be available. For example, specify the
 
 Activities
 
 section for the “Meeting minutes” report.
6. Select the
 
 Show in the section list view
 
 and/or
 
 Show in the section record page
 
 checkboxes, depending on where the report should be available (Fig. 2).
 




 Fig. 2 Add the “Meeting minutes” report
 

![chapter_print_forms_setup_add_report_name_and_place.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/chapter_print_forms_setup_add_report_name_and_place.png)



 Proceed to configure the report data fields and tables.
 



 Set up the content of a MS Word report
----------------------------------------



 You can add simple data, such as a contact name or activity date, as well as table data. In the table data, you can display records that are directly connected to the primary report object, as well as records of objects with the reverse connection.
 


### 
 Set up the report fields


1. Open a MS Word report in the
 
 Report setup
 
 section. For example, open the “Meeting minutes” report created earlier.
2. Click
 ![btn_com_add_tab.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/btn_com_add_tab.png)
 on the report page in the
 
 Set up report data
 
 block.
3. This will open a column selection window. Select all columns that hold the data required for the report (Fig. 3). For example, select the
 
 Subject
 
 column to display the activity name in the report. Add the
 
 Start
 
 and
 
 Due
 
 columns to display the activity time frame, etc.
 




 Fig. 3 The report page field setup
 

![chapter_print_forms_setup_report_fields.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/7.17/chapter_print_forms_setup_report_fields.png)



 As a result, the added columns will become available when setting up the report layout in the Creatio MS Word plug-in.
 



 If necessary, add Boolean fields, such as the
 
 Do not use phone
 
 contact checkbox or
 
 Confirmed
 
 activity checkbox, to your report. Use special macros to set up displaying of the Boolean fields in the report. Learn more:
 [Basic macros in the MS Word reports](/docs/8-0/developer/application_components/reports/ms_word/overview) 
 .
 


### 
 Set up the report tables



 In the tables, you can display a number of records connected to the primary report object. The displayed records can belong to objects that are connected to the report object directly, as well as to objects with the reverse connection.
 


#### 
 Set up a table by the connected object's data





 Example.
 
 The primary object of the “Meeting minutes” report is an activity. The report must display a table with the list of activity participants (records of the “Activity participant” object connected to the corresponding activity).
 



1. Open a MS Word report in the
 
 Report setup
 
 section. For example, open the “Meeting minutes” report created earlier.
2. Click
 ![btn_com_add_tab00001.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/btn_com_add_tab00001.png)
 on the report page in the
 
 Set up report tables
 
 block.
3. Fill out the fields on the report table page (Fig. 4):
 


	1. In the
	 
	 Table object
	 
	 field, select an object whose data will be used to create a table. For example, select the “Activity participant” object to add a table containing the list of the meeting participants.
	2. In the
	 
	 Table name
	 
	 field, specify the table title that will display when setting up the report layout in the Creatio MS Word plug-in.
	3. In the
	 
	 Column of report table object
	 
	 field, specify the column that will link the records in the table object to the primary object of the report. For example, the "Activity" column.
	4. In the
	 
	 Column of the primary report object
	 
	 field, specify the column that Creatio will use to filter the table records. In most cases, the column of the report table object is “Id.”
	5. Select the
	 
	 Hide the table if it contains no data
	 
	 checkbox to avoid displaying empty tables in the report.
	 
	
	
	
	
	 Fig. 4 The general settings of the “Activity participants” table
	 
	
	![chapter_print_forms_setup_table_fields.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/chapter_print_forms_setup_table_fields.png)
4. On the
 
 Table parameters
 
 tab, set up the list of report table columns. Click
 ![btn_com_add_tab00002.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/btn_com_add_tab00002.png)
 and select the columns to add to the list. For example, to create a list of activity participants with their names and roles, add the
 
 Participant
 
 and
 
 Role
 
 columns.
5. Set the sorting order of the table records. Click
 ![chapter_print_forms_setup_table_sorting.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/chapter_print_forms_setup_table_sorting.png)
 next to a column and select “Ascending” or “Descending” in the menu to sort the table records based on the values in that column. For example, set the “Ascending” sorting order for the “Participant” column to sort the list of participants alphabetically by name (Fig. 5).
 




 Fig. 5 The report table record sorting settings
 

![chapter_print_forms_setup_table.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/7.17/chapter_print_forms_setup_table.png)



 Make sure that your MS Word template includes all the report table columns involved in the sorting rules to apply the sorting rules when printing the report. Learn more about adding table data to the template using the plug-in:
 [Set up the report in the MS Word plug-in and upload it in Creatio](/docs/8-0/user/customization_tools/print_ready_reports/set_up_a_report/set_up_the_report_in_the_ms_word_plug-in_and_upload_it_in_creatio) 
 .
 



 You can also sort the table records by several columns. The sorting is performed by the column with a higher position in the group of settings of the table columns.
6. If necessary, go to the
 
 Table filters
 
 tab and set up an additional filter whose conditions will define which records should appear in the report table. For example, use the following filter to display only those participants who are the company's employees: “Participant.Type = Employee; Customer” (Fig. 6).
 




 Fig. 6 Report table record filters
 

![chapter_print_forms_setup_table_filter.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/chapter_print_forms_setup_table_filter.png)
7. Click
 
 Apply
 
 to save the report table settings.
8. Save the settings on the report page.



 As a result, the added table columns will become available when setting up the report layout in the Creatio MS Word plug-in.
 


#### 
 Set up table by data of object with reverse connection





 Example.
 
 The primary object of the “Meeting minutes” report is an activity. Besides the table with the list of activity participants, the report must display a list of participants of the opportunity connected to the current meeting.
 



1. Open an MS Word report record in the
 
 Report setup
 
 section. For example, open the “Meeting minutes” report created earlier.
2. Click
 ![btn_com_add_tab00003.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/btn_com_add_tab00003.png)
 in the report page under
 
 Set up report tables
 
 .
3. Fill out the fields on the report table page (Fig. 7):
 


	1. In the
	 
	 Table object
	 
	 field, select an object whose data will be used to create a table. For example, to add a table with the opportunity participants, select “Opportunity participant.”
	2. In the
	 
	 Table name
	 
	 field, specify the table title that will display when setting up the report layout in the Creatio MS Word plug-in.
	3. In the
	 
	 Column of report table object
	 
	 field, specify the column that will link the records in the table to the primary object of the report – the activity. In our example, it is the “Opportunity” column of the “Opportunity participant” objects.
	4. In the
	 
	 Column of the primary report object
	 
	 field, specify the column of the primary report object that connects the object with the table. In our example, it is the “Opportunity” column of the “Activity” object.
	5. Select the
	 
	 Hide the table if it contains no data
	 
	 checkbox to avoid displaying empty tables in the report.
	 
	
	
	
	
	 Fig. 7 The general settings of the “Opportunity participants” table
	 
	
	![chapter_print_forms_setup_table_fields_2.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/chapter_print_forms_setup_table_fields_2.png)
4. On the
 
 Table parameters
 
 tab, set up the list of report table columns. Click
 ![btn_com_add_tab00004.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/btn_com_add_tab00004.png)
 and select the column to add it to the list. For example, select the
 
 Contact
 
 ,
 
 Role
 
 , and
 
 Account
 
 columns to display the addresses of the meeting participants.
5. Set the sorting order of the table records. Click
 ![chapter_print_forms_setup_table_sorting00005.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/chapter_print_forms_setup_table_sorting00005.png)
 next to a column and select “Ascending” or “Descending” in the menu to sort the table records based on the values in that column.
6. If necessary, go to the
 
 Table filters
 
 tab and set up an additional filter whose conditions will define which records should appear in the report table. For example, use the following filter to display the participants who are the company's customers: “Account.Type = Customer.”
7. Click
 
 Apply
 
 to save the report table settings. Save the settings on the report page.



 As a result, the added table columns will become available when setting up the report layout in the Creatio MS Word plug-in.
 



 After you create a report in Creatio, you can
 [set up the report](/docs/8-0/user/customization_tools/print_ready_reports/set_up_a_report/set_up_the_report_in_the_ms_word_plug-in_and_upload_it_in_creatio) 
 in the MS Word plug-in.
 



 Copy the MS Word report
-------------------------



 Copy the report to set up similar reports faster.
 



 The report copy keeps the original report template and the following settings:
 


* columns
* macros
* tables
* filters.



 Click
 
 Copy
 
 in the
 
 Report setup
 
 section to copy a report.
 



 Click
 ![btn_copy_table.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/7.17/btn_copy_table.png)
 next to the table's name to copy a table to the same report.
 



 Transfer the package with the report to another development environment (optional)
------------------------------------------------------------------------------------


1. Click
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/licensing/BPMonlineHelp/licensing_creatio/btn_system_designer.png)
 to open the System Designer.
2. Click “
 **Advanced settings** 
 ” in the “Admin area” block.
3. Click
 
 Add
 
 →
 
 Data
 
 in the section list's toolbar (Fig. 8).
 

 Fig. 8 The
 
 Add
 
 menu in the
 
 Configuration
 
 section
 

![scr_add_data.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/7.17/scr_add_data.png)
4. [Bind the data](/docs/7-17/developer/development_tools/packages/packages#case-1199) 
 to the following elements (Fig. 9):
	* SysModuleReport\_
	 
	 ReportName – the report. Use the report Id from the
	 
	 dbo.SysModuleReport
	 
	 database table to bind it. For example, it is “SysModuleReport\_
	 
	 MeetingMinutes” for the “Meeting minutes” report.
	* SysModuleReportTable\_
	 
	 ReportName – the table part of the report. Use the report Id from the
	 
	 dbo.SysModuleReportTable
	 
	 database table to bind it. For example, it is “SysModuleReportTable\_
	 
	 MeetingMinutes” for the “Meeting minutes” report.

 Fig. 9 The bound report data in the
 
 Configuration
 
 section list
 

![scr_bound_data.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_create_report/7.17/scr_bound_data.png)



 Proceed to
 [transfer the package](/docs/8-0/developer/development_tools/delivery/creatio_ide/overview#case-1223) 
 with the report to another environment.
 




