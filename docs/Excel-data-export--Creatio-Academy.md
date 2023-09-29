


 Export Creatio data displayed as a list to an \*.xlsx file for processing and further use. Export to Excel is available for section
 [lists](/docs/8-0/user/platform_basics/user_interface/record_list/record_lists) 
 , details, and “List” dashboards.
 



 To export records, run the
 
 Export to Excel
 
 command in the action menu of a section (Fig. 1), detail (Fig. 2), or “List” dashboard (Fig. 3).
 




 Fig. 1 Export section list data to Excel
 

![export_section_list_to_excel.png](/docs/sites/en/files/images/Platform_basics/export_excel/export_section_list_to_excel.png)




 Fig. 2 Export detail data to Excel
 

![export_detail_list_to_excel.png](/docs/sites/en/files/images/Platform_basics/export_excel/export_detail_list_to_excel.png)




 Fig. 3 Export “List” dashboard data to Excel
 

![export_list_dashboard_to_excel.png](/docs/sites/en/files/images/Platform_basics/export_excel/export_list_dashboard_to_excel.png)





 Note.
 
 You must have permission to the “Export list records” (the “CanExportGrid” code)
 [system operation](/docs/8-0/user/setup_and_administration/user_and_access_management/access_management/system_operation_permissions_shortcut/system_operation_permissions) 
 to export the list. The file export speed depends on the “Number of records in Excel export batch” (the “ExcelExportBatchSize” code)
 [system setting](https://academy.creatio.com/documents?id=1259#title-1880-2) 
 .
 



 You can also grant permissions to export lists of specific objects to roles and individual users. Learn more in a separate article:
 [Data export permissions](https://academy.creatio.com/documents?id=2390) 
 .
 




 The file export speed depends on the number of columns and rows in the exported database, as well as the list settings. By default, Creatio terminates the export operation if it takes longer than 10 minutes. To increase the timeout value, contact Creatio support.
 



 After you run the
 
 Export to Excel
 
 action, Creatio will download the file that contains every list record. If you specify records via multiple selection, the file will contain only the selected records.
 



 Creatio will export only the columns that are displayed in the list. If the list has custom column titles, the exported file will display them as well.
 



 The export operation takes the data types into account and formats the data if necessary. For example, if the exported list includes a column of the “Date” type, the corresponding column in the Excel file will be formatted similarly.
 



 The columns in the exported file have an optimal width. If the exported values are wider than the column, the file will wrap them.
 



 Creatio does not export contact photos and account logos.
 




