


 You can filter records in the list for sections and details in Creatio. The following tools can be used to search and filter records in sections:
 


* Quick filter
* Standard filter
* Advanced filter



 To filter records on the details, a standard filter is used.
 



 Controls for managing filters are located in the upper part of the section page or directly on the detail (Fig. 1).
 





 Fig. 1
 
 Filter area
 

![scr_filters_menu.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_menu.png)



 To manage standard and advanced filters in sections, use the
 
 Filter
 
 menu. To change the parameters of the applied filter either for the section or for the detail, click the filter and edit the needed fields in the filter area.
 



 The filter settings are saved when updating the page when switching sections or re-logging into the system. To remove a filter, click the
 ![btn_com_quick_filter_cancel.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_com_quick_filter_cancel.png)
 button in its right part (Fig. 2).
 





 Fig. 2
 
 Canceling one filter
 

![scr_filters_filter_delete.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_filter_delete.png)





 Note.
 
 The
 
 Filter
 
 menu is also used to manage folders. If some folders have been marked as favorite, their list will be displayed in the
 
 Filter
 
 menu. More information about the
 
[working with folders](/docs/8-0/user/platform_basics/business_data/folders_shortcut/folders) 

 can be found in a separate article.
 




 Quick filter
--------------



 Certain sections in Creatio have quick filters. Use a
 
 quick filter
 
 to filter data by the most frequently used conditions (Fig. 3).
 





 Fig. 3
 
 Using the quick filter
 

![scr_filters_quick_filter_example.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_quick_filter_example.png)



 For example, the
 
 Activities
 
 section contains a quick filter as it is needed to analyze employee's activity during a specified period of time. By default, quick filters are enabled. Quick filter parameters may vary depending on the section.
 


### 
 Quick filter by time period



 You can filter records by time period, for example, to display the activities for the current or previous week.
 



 There are three quick filter presets:
 


* ![btn_com_filter_day.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_com_filter_day.png)
 – shows records for the current day.
* ![btn_com_filter_week.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_com_filter_week.png)
 – shows records for the current week.
* ![btn_com_menu_period.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_com_menu_period.png)
 – shows records for the standard period, for example, “Yesterday”, “Current week”, “Next week”, “Previous month”, and so on. You can also set a custom period by specifying its start and end dates using the built-in calendar.





 Note.
 
 Previous, current, and next week (month) are actual calendar weeks (months). For example, if the previous month was December, then when you select the “Previous month” period in the
 
 Activities
 
 section, the activities will be displayed for the period of time between 1st and 31st of December.
 



 Use the
 
[advanced filter](/docs/8-0/user/platform_basics/business_data/filters_shortcut/filters#title-1755-10) 

 to display records by quarter, half-year, or other custom periods in the list.
 




 To set up a custom filter period, select the start and end date of the period using the built-in calendar. You can open the calendar by clicking the start or end date of the period (Fig. 4).
 





 Fig. 4
 
 Opening the calendar filter
 

![scr_filters_quick_filter_calendar.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_quick_filter_calendar.png)


### 
 Quick filter by owner



 Apply a filter by owner to display records by one or more record owners. In the
 
 Activities
 
 section, the filter is called
 
 By employee
 
 , and it displays records by participants.
 



 To view data by a certain owner, select the user's name in the
 ![btn_com_menu_filter_owner_73.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_com_menu_filter_owner_73.png)
 filter menu. To view data about several owners, select the
 
 Add owner
 
 or
 
 Add employee
 
 option from the menu and specify the user in the opened window.
 



 To cancel a filter by owner, select the
 
 Clear
 
 option from the filter menu.
 



 Standard filter
-----------------



 The
 
 standard filter
 
 is used to search for records either in the section or on the details by the values specified in one or more columns. For example, to search for all companies of a specified type or activities that have a specified status and priority.
 





 Fig. 5
 
 Standard filter in the
 
 Activities
 
 section
 

![scr_filters_standard_filter_example.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_standard_filter_example.png)


### 
 Applying standard filters in sections


1. From the
 
 Filter
 
 menu, select the
 
 Add condition
 
 option (Fig. 6).
 





 Fig. 6
 
 Adding standard filter conditions for the section
 

![scr_filters_standard_filter_select.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_standard_filter_select.png)
2. In the appeared fields, specify a filter condition. Select a column that you want to search records by and specify the column value (fully or partially). To apply the filter conditions, click the
 ![btn_com_apply.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_com_apply.png)
 button (Fig. 7).
 





 Fig. 7
 
 Applying standard filter conditions for the section
 

![scr_filters_standard_filter_apply.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_standard_filter_apply.png)



 As a result, the section list will display the records that match the applied filter condition.
 


### 
 Applying multiple standard filters for the section



 You can apply more than one standard filter in a section. To add more filters, select the
 
 Add condition
 
 option from the
 
 Filter
 
 menu once again and specify a filter condition. Once several standard filters are applied, the list will contain only those records that match all filter conditions.
 


### 
 Applying a standard filter for the detail


1. Select the
 
 Apply filter
 
 option from the
 ![btn_detail_menu.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_detail_menu.png)
 menu (Fig. 8).
 





 Fig. 8
 
 Adding standard filter conditions for the detail
 

![scr_filters_set_detail_filter.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_set_detail_filter.png)
2. In the appeared fields, specify a filter condition. Select a column that you want to search records by and specify the column value (fully or partially). To apply the filter conditions, click the
 ![btn_com_apply00001.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_com_apply00001.png)
 button (Fig. 9).
 





 Fig. 9
 
 Applying standard filter conditions for the detail
 

![scr_filters_set_detail_filter2.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_set_detail_filter2.png)



 As a result, the detail list will display the records that match the applied filter condition.





 Note.
 
 Applying filter conditions is possible only for the details with
 [lists](/docs/8-0/user/platform_basics/user_interface/record_list/record_lists) 
 .
 



### 
 Applying multiple standard filters for a detail



 You can apply more than one standard filter for a detail. To add more filters, click the
 ![btn_detail_filter.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_detail_filter.png)
 button and specify a filter condition. Once several standard filters are applied, the detail will contain only those records that match all filter conditions.
 


### 
 Removing the filter panel from the detail



 The filter panel will be automatically hidden after the page update. To hide the filter panel manually, select the
 
 Hide filter
 
 option in the
 ![btn_detail_menu00002.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_detail_menu00002.png)
 menu (Fig. 10).
 





 Fig. 10
 
 Hiding filter panel on the detail
 

![scr_filters_hide_detail_filter.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_hide_detail_filter.png)





 Attention.
 
 This action is available if no other filter conditions are applied.
 






 Note.
 
 The filter conditions will not be reset if you can expand and collapse the detail (by clicking the
 ![btn_detail_show_and_hide.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_detail_show_and_hide.png)
 button).
 




 Advanced filter
-----------------



 If you need to apply a more complex filter with several search parameters and conditions, use the
 
 advanced filter
 
 . For example, you can use it in the
 
 Activities
 
 section to display all meetings with new customers.
 



 To apply the advanced filter, select the
 
 Switch to advanced mode
 
 option from the
 
 Filter
 
 menu (Fig. 11).
 





 Fig. 11
 
 Switching to the advanced filter mode
 

![scr_filters_advanced_filter_select_2.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_select_2.png)



 If you will require the configured filters in the future, you can save a dynamic folder by them.
 


### 
 Applying an advanced filter by object columns



 You can apply filter by one of the current section columns (for example, you can filter activities by the
 
 End date
 
 column of the “Activity” section or contacts by the
 
 Job Title
 
 column of the “Contact” section).
 



 For example, to filter the uncompleted activities that were changed within the last two weeks in the
 
 Activities
 
 section:
 


1. Open the
 
 Activities
 
 section. From the
 
 Filter
 
 menu, select the
 
 Switch to advanced mode
 
 option (Fig. 11).
2. In the filter setup area, click the <Add condition> link.
3. In the opened window, select the needed column from the
 
 Column
 
 drop-down list, for example,
 
 Status
 
 , and click the
 
 Select
 
 button (Fig. 12).
 





 Fig. 12
 
 Selecting a column for the advanced filter
 

![scr_filters_advanced_filter_select_column.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_select_column.png)
4. On the filter page, select the needed parameters:
 


	1. Select the condition type by clicking its symbol, for example, “=”.
	2. Click the <?> link. On the opened window, specify the values for the selected column, for example, “Not started” and “In progress”. Click the
	 
	 Select
	 
	 button (
	 
	 Fig. 13
	 
	 ).
	 
	
	
	
	
	
	 Fig. 13
	 
	 Selecting a value for a column
	 
	
	![scr_filters_advanced_filter_select_column_value.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_select_column_value.png)
5. Similarly, add the remaining conditions. For example, specify the threshold dates for the records that were modified.
6. Specify the logical operator for the added conditions, for example, “AND”, by clicking it (Fig. 14).
 





 Fig. 14
 
 Selecting a logical operator
 

![scr_filters_advanced_filter_select_operator.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_select_operator.png)





 Note.
 
 By default, the filter area contains one empty root group with the logical operator “AND”. The “AND” logical operator is applied if the record must match all conditions in the group. Apply the “OR” logical operator if the record must match at least one of the conditions in the group.
 



 When using the "≠" condition, records with unfilled fields are now taken into account.
7. Click the
 
 Apply
 
 button.
 



 As a result, only uncompleted activities that were changed within the specified period will be displayed in the
 
 Activities
 
 section.


### 
 Applying an advanced filter by connected object column



 You can filter records by the columns of the current record and by the columns of the objects connected to it. Another example, activities can be filtered by the category of the connected account (the
 
 Type
 
 column of the
 
 Accounts
 
 section). For example, to filter activities in the
 
 Activities
 
 section by a certain type of company:
 


1. Open the
 
 Activities
 
 section. From the
 
 Filter
 
 menu, select the
 
 Switch to advanced mode
 
 option (Fig. 11).
2. Click the <Add condition> link.
3. On the opened column selection page:
 


	1. Click the
	 ![btn_com_expand.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_com_expand.png)
	 button next to the object name.
	2. In the added field, select the connected object, for example, “Account”.
	3. In the
	 
	 Column
	 
	 field, specify the column of the connected object, for example, “Category”.
	4. Click the
	 
	 Select
	 
	 button (Fig. 15).
	 
	
	
	
	
	
	 Fig. 15
	 
	 Selecting a column of the connected object
	 
	
	![scr_filters_advanced_filter_select_related_column.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_select_related_column.png)
4. On the filter setup area, select the needed parameters:
 


	1. Click the symbol of the filter condition to change its type. By default, the “=” condition is indicated.
	2. Click the <?> link. In the opened window, select the needed value for the selected column, for example, “Category = VIP”. Click the
	 
	 Select
	 
	 button.
5. Click the
 
 Apply
 
 button (Fig. 16).
 





 Fig. 16
 
 Applying filter conditions
 

![scr_filters_advanced_filter_save_related.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_save_related.png)



 As a result, only activities that are connected to accounts of the "VIP" category will be displayed in the section list.





 Note.
 
 For example, when the filter is set up for <Account.Type ≠ Customer>, activities will be displayed for the accounts that are not customers and those with the
 
 Type
 
 field unfilled.
 




 If you use filtered data on a regular basis, click the
 
 Save as
 
 button to create a dynamic folder using this filter.
 


### 
 Applying the advanced filter with grouping filter conditions



 You can create advanced filters with several logical operators. For example, you can display all customer
 
 accounts
 
 who reside in New York and those that have no city specified:
 


1. Open the
 
 Accounts
 
 section. From the
 
 Filter
 
 menu, select the
 
 Switch to advanced mode
 
 option (Fig. 11).
2. Apply the “Type = Customer” condition:
 


	1. Click the <Add condition> link.
	2. In the opened window, select the account column, for example, “Type”. Click the
	 
	 Select
	 
	 button.
	3. In the filter setup area, click the <?> link. In the opened window, select the needed value for the selected column “Category = VIP”. Click the
	 
	 Select
	 
	 button.
3. Add the “City = New York” condition in the same manner.
4. To apply the “City is not filled in” condition:
 


	1. Click the <Add condition> link.
	2. In the opened window, select the “City” column. Click the
	 
	 Select
	 
	 button.
	3. In the filter setup area, click the condition type and select the “is not filled in” condition from the menu.
5. Group the needed conditions and set a different logical operator for them:
 


	1. Holding down the Ctrl key, select the conditions to group (Fig. 17).
	 
	
	
	
	
	
	 Fig. 17
	 
	 Selecting filter conditions to be grouped
	 
	
	![scr_filters_advanced_filter_select_conditions.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_select_conditions.png)
6. From the
 
 Actions
 
 menu, select the
 
 Group
 
 option (Fig. 18).
 





 Fig. 18
 
 Grouping filter conditions
 

![scr_filters_advanced_filter_group.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_group.png)
7. Set “AND” as the logical operator of the root group and “OR” as the logical operator for the newly created group by clicking the operator name (Fig. 19).
 





 Fig. 19
 
 Setting a logical operator for the group of filter conditions
 

![scr_filters_advanced_filter_group_operator.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_group_operator.png)
8. Click the
 
 Apply
 
 button.
 



 As a result, only the accounts of the “Customer” type for which the “New York” value or no value is specified in the
 
 City
 
 field will be displayed in the section.



 Applying an aggregate filter
------------------------------



 The aggregate filter allows to filter object records by the connected records in objects with the reverse connection. The following filter conditions can be applied in the aggregate filter:
 


* Count
 
 – a certain number of the connected records exists in the object with the reverse connection for the filtered records. For example, you can filter users who are specified in the
 
 Owner
 
 field for five or more accounts.
* Maximum/minimum
 
 – for the filtered records, the object with the reverse connection contains records with a specific maximum (minimum) value in the numeric or the date column. For example, you can select employee users whose last task was completed last week.
* Sum, average
 
 – for the filtered records, the object with the reverse connection contains the connected records with the particular sum of values or the average value in the numeric column. For example, you can filter employee users whose average task duration is greater than two hours.



 Applying the aggregate filter is identical to applying the filter by connected object columns. For example, you need to obtain a list of users who are owners of the accounts of the “Customer” type. Applying the following aggregate filter will help you compile this list:
 


1. Open the section whose records must be filtered, for example,
 

 Contacts
 

 . From the
 
 Filter
 
 menu, select the
 
 Switch to advanced mode
 
 option (Fig. 11).
2. Click the <Add condition> link.
3. In the opened column selection window (Fig. 20):
 





 Fig. 20
 
 Setting up a reverse connection object column in the aggregate filter
 

![scr_filters_aggregate_filter_select_related_column.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_aggregate_filter_select_related_column.png)


	1. Click the
	 ![btn_com_expand00003.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_com_expand00003.png)
	 button next to the object name.
	2. In the added field, select the object with the reverse connection. For example, to apply an aggregate filter by the
	 
	 Owner
	 
	 column of the
	 
	 Accounts
	 
	 section, select “Account (by column Owner)”.
	3. In the
	 
	 Column
	 
	 field, specify the column of the object with the reverse connection, for example, “Quantity“.
	4. Click the
	 
	 Select
	 
	 button.
4. In the filter setup area (Fig. 21):
 


	1. Select the filter conditions. In this case, the condition is “Quantity > 0”.
	2. Apply the necessary additional conditions: For example, if you need to display only those contacts that are owners for accounts of the “Customer” type, add this condition to the filter.
	 
	
	
	
	
	
	 Fig. 21
	 
	 Applying filter conditions for an aggregate filter
	 
	
	![scr_filters_aggregate_filter_applied.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_aggregate_filter_applied.png)
5. Click the
 
 Apply
 
 button.
 



 As a result, the record will be displayed in the
 

 Contacts
 

 section, only if there is an account for which this contact is specified in the
 
 Owner
 
 field.



 Applying filter by time period
--------------------------------



 You can filter records by a specific period or an exact date. For example, display all records added to the section for the last week.
 



 Following types of filters by period are available:
 


* [Filter by exact date](#title-1755-16)
* [Filter by standard period](#title-1755-17)
* [Filter by annual events](#title-1755-18)


### 
 Filter by exact date



 To display data whose date falls within a certain period of time, specify this period in the filter conditions. For example, you can view the activities that took place during your business trip three weeks ago.
 


1. Open the
 
 Activities
 
 section.
2. From the
 
 Filter
 
 menu, select the
 
 Switch to advanced mode
 
 option (Fig. 22).
 





 Fig. 22
 
 Switching to the advanced filter mode
 

![scr_filters_advanced_filter_select.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_select.png)



 When the filter area opens, select the beginning of the period you want to display records for. To do this:
 


	1. Click the <Add condition> link (Fig. 23). In the opened window, select the needed date column, for example, "Start", to sort activities by the start date.
	 
	
	
	
	
	
	 Fig. 23
	 
	 Adding column to filter condition
	 
	
	![scr_filters_advanced_filter_add_column.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_add_column.png)
	2. Select the logical operator next to the added column (Fig. 24), for example, “≥” (greater than or equal to), to set this period as the filter start date.
	 
	
	
	
	
	
	 Fig. 24
	 
	 Selecting filter condition type
	 
	
	![scr_filters_advanced_filter_add_condition_type.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_add_condition_type.png)
3. From the <?> link menu, select the
 
 Specify exact date
 
 option (Fig. 25).
 





 Fig. 25
 
 Specifying the exact date of filter period
 

![scr_filters_advanced_filter_specify_exact_date.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_specify_exact_date.png)
4. In the opened window, click the
 ![btn_com_filter_calendar.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/btn_com_filter_calendar.png)
 button to open the built-in filter calendar, and select the needed date (Fig. 26).
 





 Fig. 26
 
 Built-in filter calendar
 

![scr_filters_advanced_filter_calendar.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_calendar.png)
5. Specify the filter end date.
 


	1. Add the “End” column to the filter condition to sort activities by the start date.
	2. Then select the “≤” (less than or equal to) condition type.
	3. Select the date from the built-in calendar.
6. Make sure that the “AND” logic operator is set for the added filter conditions.
7. Apply the filter by clicking the corresponding button.
 





 Fig. 27
 
 Applying filter
 

![scr_filters_advanced_filter_apply_filter.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_apply_filter.png)



 As a result, only activities that started within the specified period will be displayed in the
 
 Activities
 
 section.
 


### 
 Standard filter periods



 To facilitate working with filters, use standard filter periods. For example, you can easily display records for the previous, current or next week.
 



 Standard periods are available in the <?> link menu of the filter condition (Fig. 28).
 





 Fig. 28
 
 Selecting standard filter period
 

![scr_filters_advanced_filter_specify_custom_period.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_specify_custom_period.png)


##### 
 Hour



 The menu includes options that allow you to display records for the previous, current or next hour. In addition, you can display records for a certain number of previous or next hours. In addition, you can set the exact time to the minute as a filter value.
 



 To do that, select the
 
 Exact time
 

 option and enter the needed time value in the following format – H:MM, for example, “2:43 PM”. Also, you can select a standard time value from the drop-down list.
 



 To define the number of previous or next hours, select the
 
 Previous hours
 

 or
 
 Following hours
 

 option respectively. Enter the needed number in the appeared field. Only integer numbers are acceptable.
 



 Please, note that the previous, current or following hour is not an hour from the current moment, but a full hour starting from the 1st till the 60th minute, for example, from 9:00 to 9:59. Therefore, if the current time is 2:34, the following hour is the period from 3:00 to 3:59, not from 2:34 to 3:33.
 


##### 
 Day



 The menu consists of options that allow you to display records for the previous, current or next day. In addition, you can display records for a certain number of previous or next days. You can also use a specific day of the month or week as a filter value.
 



 To set a specific day of the month as a filter value, select the
 
 Day of the month
 

 option and enter the needed date in the appeared string.
 



 To set a specific day of the week as a filter value, click
 
 Day
 
 →
 
 Day of the week
 

 and select the needed day.
 


##### 
 Week



 The menu includes options that allow you to display records for the previous, current or next week.
 



 Previous, current or next week is a calendar period from Monday till Sunday. It is not a 7-day period starting from the current day. For example, if today is Wednesday, the next week is the period from next Monday till Sunday, not the following 7 days from the current day.
 


##### 
 Month



 The menu includes options that allow you to display records for the previous, current or next month. You can also use a specific month as a filter value.
 



 To set a specific month as a filter value, click
 
 Month
 
 >
 
 Month
 

 and select the needed month.
 



 Previous, current or next month is a calendar period. For example, if the previous month was December, then when you select the “Previous month” period, the records for the period from December, 1st till December, 31st will be displayed.
 


##### 
 Quarter



 The menu includes commands that enable you to view records for the previous, current or next quarter.
 



 The previous, current or next quarter is a 3-month period: the 1st quarter includes the 1st, 2nd and 3rd months of the year (January, February, March), the 2nd quarter includes the next three months (April, May, June) and so on. For example, if it's August, the next quarter is the period that includes October, November and December (the 4th quarter).
 


##### 
 Half-year



 The menu includes options that allow you to display records for the previous, current, or next half-year.
 



 Previous, current or next half-year is a 6-month period: the period from January to June is considered the 1st half-year. The 2nd half-year is the period from July to December. For example, if it's August (included in the 2nd half-year), then the next half-year is the time period from January to June of the next year.
 


##### 
 Year



 The menu includes options that allow you to display records for the previous, current, or next year. You can also use a specific year as a filter value.
 



 Previous, current, and next year is a calendar period. For example, if it is August 2021, the next year is the period from January through December of 2022. It is not a 12-month period starting from August 2021.
 


#### 
 Filter by annual events



 The filter takes into account only the day and month of the filtered dates. This filter can be used to track events that repeat each year, such as holidays or noteworthy events of contacts.
 



 Annual event macros are available in the <?> link menu of the filter condition (Fig. 29).
 





 Fig. 29
 
 Filter by annual events.
 

![scr_filters_advanced_filter_annual.png](/sites/default/files/documents/docs_en/product/bpm'online base/base/7.16.0/BPMonlineHelp/chapter_filters/scr_filters_advanced_filter_annual.png)



 The menu consists of the following options:
 


* Every year, today. Displays a list of records whose date matches the current date not counting the year. I. e., the contact's birthday is today.
* Every year, exactly in <?>
 
 . Displays a list of records whose date will come after a specified number of days not counting the year. I. e., the contact's birthday is exactly in 5 days.
* Every year, within “X” next days <?>
 
 . Displays a list of records which date falls on one of the next days not counting the year. I. e., the contact's birthday is within 5 days or less.
* Every year, within “X” previous days <?>
 
 . Displays a list of records which date falls on one of the previous days not counting the year. I. e., the contact's birthday was 5 days ago or less.




