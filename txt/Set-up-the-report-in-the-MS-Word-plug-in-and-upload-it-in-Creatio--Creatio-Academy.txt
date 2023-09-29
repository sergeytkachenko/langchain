


 After you
 
[install the MS Word plug-in](/docs/8-0/user/customization_tools/print_ready_reports/install_the_plugin/install_creatio_plug-in_for_ms_word#HT_cases_print_forms_setup_word_plugin_install) 

 and
 
[create a report](/docs/8-0/user/customization_tools/print_ready_reports/create_a_report/add_a_new_ms_word_report_in_creatio#HT_cases_print_forms_setup_word_add) 

 in Creatio, you can start setting up the report layout. You can customize the layout by editing the standard MS Word template.
 



 MS Word report template setup includes the following general steps:
 


1. Download and edit the template in the Creatio MS Word plug-in.
 
[Read more >>>](#HT_cases_print_forms_setup_word_template_setup)
2. Modify the ready template in the Creatio MS Word plug-in if needed.
 
[Read more >>>](#HT_cases_print_forms_setup_word_template_edit)
3. Upload the updated template file to Creatio.
 
[Read more >>>](#HT_cases_print_forms_setup_word_template_upload) 





 You can also use macros to set up reports. For more information about custom macros and adding them to the MS Word reports, please see the “
 [MS Word reports](/docs/8-0/developer/application_components/reports/ms_word/overview#title-1372-1) 
 ” article.







 Download and edit the template in the Creatio MS Word plug-in
-------------------------------------------------------------------


1. Open an empty MS Word document on your computer.
2. Click
 
 Connect
 
 on the Creatio plug-in toolbar.
3. Log in to the system with your Creatio credentials (
 [Fig. 1](#XREF_71983_11_11_MS_Word)
 ).
 





 Fig. 1
 

 Connecting the plug-in and authorization.
 

![scr_cases_print_forms_setup_word_connect.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_edit_and_upload/scr_cases_print_forms_setup_word_connect.png)
4. Select the needed report from the list by clicking
 
 Select report
 
 .
 



 As a result, a list of columns for the selected report will be displayed in the right part of the MS Word window.


### 
 Add fields to the template



 In the template, the report fields are represented as the MS Word fields. When the report is generated, the field will contain data from the corresponding Creatio record. The list of available fields is displayed in the
 
 Word report data
 
 window (
 [Fig. 1](#XREF_79096_11_11)
 ).
 


#### 
 Add all fields to the template



 To add all the fields
 
[configured in the report designer](/docs/8-0/user/customization_tools/print_ready_reports/create_a_report/add_a_new_ms_word_report_in_creatio#HT_cases_print_forms_setup_word_add_fields) 

 to a template, drag a group of fields to the template page (
 [Fig. 1](#XREF_79096_11_11)
 ).
 





 Fig. 1
 

 Adding a field group to a template
 

![scr_cases_print_forms_setup_word_template_add_all.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_edit_and_upload/scr_cases_print_forms_setup_word_template_add_all.png)



 As a result, all fields and names of the corresponding Creatio columns will be added to the template (
 [Fig. 2](#XREF_25821_11_12)
 ).
 





 Fig. 2
 

 A report template with a field group
 

![scr_cases_print_forms_setup_word_template_view_all.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_edit_and_upload/scr_cases_print_forms_setup_word_template_view_all.png)



 You can use standard MS Word tools to customize the added fields.
 


#### 
 Add separate fields to the template


1. To add data to the template, drag the corresponding field on the page (
 [Fig. 1](#XREF_56713_11_13)
 ).
 





 Fig. 1
 

 Adding a field to the report template
 

![scr_cases_print_forms_setup_word_template_add_one_field.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_edit_and_upload/scr_cases_print_forms_setup_word_template_add_one_field.png)
2. As a result, a field will be added on the page. When the report is generated, the field will contain data from the corresponding system record in Creatio.
3. Add all other necessary fields as well as the text in the report (
 [Fig. 2](#XREF_61460_11_14)
 ).
 





 Fig. 2
 

 A report with the added fields and static text
 

![scr_cases_print_forms_setup_word_template_view_added.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_edit_and_upload/scr_cases_print_forms_setup_word_template_view_added.png)
4. Save the report template.


### 
 Add table data to a template



 Add all table columns to the template
 



 To add all the table columns
 
[configured in the report designer](/docs/8-0/user/customization_tools/print_ready_reports/create_a_report/add_a_new_ms_word_report_in_creatio#HT_cases_print_forms_setup_word_add_fields) 

 to a template, drag a group of fields to the template page (
 [Fig. 1](#XREF_39707_11_16)
 ).
 





 Fig. 1
 

 Adding all table columns to the template
 

![scr_cases_print_forms_setup_word_template_add_all_tbl.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_edit_and_upload/scr_cases_print_forms_setup_word_template_add_all_tbl.png)



 As a result, the template will contain the table with all columns from the selected group. Titles of table columns will correspond to the titles of columns in Creatio.
 



 You can use standard MS Word tools to customize the added table. The text in titles of the table columns can be edited. Fields placed in table cells determine the data that will be displayed in the column.
 


#### 
 Add separate columns


1. Add a simple table with the required number of columns on the template page. Each column must comprise a title and one row (
 [Fig. 1](#XREF_12198_11_18)
 ).
 





 Fig. 1
 

 Adding a table to the template manually
 

![scr_cases_print_forms_setup_word_template_view_tbl_2.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_edit_and_upload/scr_cases_print_forms_setup_word_template_view_tbl_2.png)
2. Enter the text of the column titles (
 [Fig. 2](#XREF_14079_11_19)
 ).
 





 Fig. 2
 

 A table with static titles of columns
 

![scr_cases_print_forms_setup_word_template_view_tbl_3.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_edit_and_upload/scr_cases_print_forms_setup_word_template_view_tbl_3.png)
3. Drag a column title to an empty cell of the table which should display the data from this column (
 [Fig. 3](#XREF_60261_11_20)
 ).
 





 Fig. 3
 

 A table with fields added
 

![scr_cases_print_forms_setup_word_template_view_tbl_1.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_edit_and_upload/scr_cases_print_forms_setup_word_template_view_tbl_1.png)
4. Set up the template visual appearance by placing the table in the right part of the file (
 [Fig. 4](#XREF_14737_165)
 ).
 





 Fig. 4
 

 Setting up a template visual appearance
 

![scr_cases_print_forms_setup_word_template_view_rezult.png](/guides/sites/en/files/documentation/user/en/print_ready_reports/BPMonlineHelp/print-ready_reports_edit_and_upload/scr_cases_print_forms_setup_word_template_view_rezult.png)
5. Save the report template.
 



 In the generated report, the fields of the table will contain data from Creatio. The number of rows in the table will correspond to the number of records.







 Edit the existing template in the Creatio MS Word plug-in
---------------------------------------------------------------



 You can modify the layout of any MS Word report in Creatio at any time.
 


1. Open an empty MS Word document on your computer.
2. Click
 
 Connect
 
 on the Creatio plug-in toolbar.
3. Log in to the system with your Creatio credentials.
4. On the
 
 Creatio
 
 tab of the MS Word ribbon, click
 
 Select report
 
 .
   

 As a result, a list of available MS Word reports will open.
5. Select a report to configure and click
 
 OK
 
 . As a result, the current report template will open.
6. Click
 
 OK
 
 in the pop-up window. As a result, the previously configured template file will open.
7. Make the necessary changes to the template layout.
8. Click
 
 Save to Creatio
 
 on the
 
 Creatio
 
 tab of the MS Word ribbon.
 



 As a result, the plug-in will upload your report template to Creatio.







 Upload the updated template to Creatio
--------------------------------------------



 To add the edited template in Creatio:
 


1. Open an empty MS Word document on your computer.
2. Click
 
 Connect
 
 on the Creatio plug-in toolbar.
3. Log in to the system with your Creatio credentials.
4. Click
 
 Save in Creatio
 
 .
5. Click
 
 Save
 
 .
 



 As a result, a new template will be used the next time this report is generated.
 



 You can also upload the report in the report designer directly by clicking
 
 Upload template
 
 .




