


 When working with Creatio, you may need to view the changes made to your data and see who made these changes and when. For example, you can check which contact records were changed last month.
 



 The data change history is available in the
 
 Change log
 
 section (
 [Fig. 1](#XREF_16493_618)
 ).
 





 Fig. 1
 

 The
 
 Change log
 
 section view
 

![scr_section_change_log_crd_example.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/view_change_log/scr_section_change_log_crd_example.png)



 The change log contains information about adding, modifying, and deleting records (entries) in the database tables for Creatio objects. This includes sections, details, lookups, as well as other objects.
 



 There are two ways you can open a change log for viewing its records:
 


* Open the
 **Change log** 
 section from the System Designer and select an object to view its logs
* Open the change log of a specific record directly from the
 **record page** 
 .





 Method 1. View the record changes from the change log
---------------------------------------------------------





 Example.
 
 View the contact records that were changed last month.
 



1. Open the System Designer, e.g., by clicking
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/view_change_log/btn_system_designer.png)
 .
2. Under
 
 Users and administration
 
 , click
 
 Change log
 
 .
 





 Note.
 
 To view the changes, make sure you have the
 
 Access to "Change log" section
 
 (CanManageChangeLog) system operation permission.
   

 Learn more about using system operations in the “
 
[System operation permissions](https://academy.creatio.com/documents?product=base&ver=7&id=258) 

 ” article.
3. Set the filter - for our example, select “Sections”.
4. Find the needed object using the search bar or manually. In our example, we use the “Contact” object.
 



 Click the object title to open the change log page.
5. Click the
 
 Log data
 
 tab and set the date filter (
 [Fig. 1](#XREF_97711_624)
 ). In our example, it is the time period from February 2nd to March 2nd, 2020.
 





 Fig. 1
 

 Filtering changes by date for the “Contact” object
 

![scr_section_change_log_wnd_filter_date.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/view_change_log/scr_section_change_log_wnd_filter_date.png)



 As a result, the list of records that were changed within the specified period will be displayed (
 [Fig. 2](#XREF_39700_623)
 ). The icons next to dates display the type of the performed operations: deleting, adding or editing.
 





 Fig. 2
 

 Viewing the change log
 

![scr_section_change_log_crd_view_section.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/view_change_log/scr_section_change_log_crd_view_section.png)
6. Use the
 **search bar** 
 to quickly find the needed record by title. In our case - by the contact’s full name (
 [Fig. 3](#XREF_26701_625)
 ). To learn the details of the performed changes, click the name in the
 
 Record
 
 column.
 





 Fig. 3
 

 Quick search by record name
 

![scr_section_change_log_crd_find.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/view_change_log/scr_section_change_log_crd_find.png)





 Method 2. View logs of a specific record directly from the record page
--------------------------------------------------------------------------





 Example.
 
 See the change log of the field values on the page of a specific contact for the last month.
 



1. Open the page of the needed record.
2. Click
 
 Actions
 
 →
 
 View change log
 
 (
 [Fig. 1](#XREF_37370_623)
 ).
 





 Fig. 1
 

 The
 
 View change log
 
 action
 

![scr_section_change_log_crd_view_record.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/view_change_log/scr_section_change_log_crd_view_record.png)





 Note.
 
 If you cannot see the
 
 View change log
 
 command in the
 
 Actions
 
 menu, make sure you have permission to the
 
 View change log
 
 (CanViewChangeLog) system operation.
   

 Learn more about using system operations in the “
 
[System operation permissions](https://academy.creatio.com/documents?product=base&ver=7&id=258) 

 ” article.
3. The page that opens will display information about the selected record:
 


	1. dates of the changes
	2. authors of the changes
	3. record name
	4. list of the changed columns
	5. values before the change
	6. values after the change
4. Set the date filter to display only the changes for the last month. (
 [Fig. 2](#XREF_24479_624)
 ). In our example, it is the time period from February 2nd to March 2nd, 2020.
 





 Fig. 2
 

 Filtering changes by date for the log of a specific record
 

![scr_section_change_log_wnd_contact_filter_date.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/view_change_log/scr_section_change_log_wnd_contact_filter_date.png)



 As a result, you will see the changes that were made in the logged fields within the specified period (
 [Fig. 3](#XREF_55468_624)
 ).
 





 Fig. 3
 

 Record logs
 

![scr_section_change_log_view_column_record.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/view_change_log/scr_section_change_log_view_column_record.png)




