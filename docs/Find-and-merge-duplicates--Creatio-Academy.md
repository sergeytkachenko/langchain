


**Duplicate records** 
 may appear whenever you add new records to Creatio sections. Find and merge duplicates to maintain the quality of your Creatio data.
 


* [Bulk duplicate search](#title-747-18) 
 is run for the entire database, manually or
 [on schedule](#title-747-14) 
 .
* [Local duplicate search](#title-747-5) 
 is run for a particular new record automatically when you save the record.



 You can also
 [merge](#title-747-6) 
 any duplicate records manually without running the search. This option is available for all sections.
 



 By default, duplicate search is available in the
 
 Accounts
 
 ,
 
 Contacts
 
 and
 
 Leads
 
 sections. Creatio uses a set of pre-configured
 [rules](#title-747-10) 
 to search for duplicates. For example, duplicates may be identified by identical phone numbers or email addresses. Creatio lets you customize these rules in several ways:
 


* Customize out-of-the-box
 **contact, account, and lead** 
 duplicate search rules to suit your specific needs.
* Create custom rules for
 **any Creatio section** 
 , including custom sections.



 You can search for duplicates manually in any section that has at least one duplicate search rule. For example, the
 
 Contacts
 
 section includes the
 
 Show duplicate ‘Contacts’
 
 action. Once the search is complete, Creatio will display a list of records identified as duplicates.
 





 Attention.
 
 To ensure the correct operation of bulk duplicate search, on-site users must install additional components. Learn more in a separate article:
 [Bulk duplicate search](https://academy.creatio.com/documents?id=1959) 
 .
 




 Find and process duplicates
-----------------------------



 To open the duplicates, you must have permissions to read and edit the records of the section where you search for duplicates, as well as permission to the “Duplicates search” (the “CanSearchDuplicates” code) system operation. Learn more in a separate article:
 [System operation permissions](https://academy.creatio.com/documents?id=258) 
 .
 


### 
 Bulk duplicate search



 Creatio displays the duplicate search results on the found duplicates page (Fig. 1). To set up the columns of the duplicate list, click
 
 View
 
 →
 
 List setup
 
 in the top right.
 




 Fig. 1 The duplicate search results in the
 
 Contacts
 
 section
 

![scr_chapter_deduplication_wnd_results.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/scr_chapter_deduplication_wnd_results.png)


#### 
 Go to the page



 There are several ways to open this page:
 


* Select
 
 Show duplicates
 
 in the
 
 Actions
 
 menu of the section (Fig. 2).
 





 Note.
 
 The
 
 Show duplicates
 
 action is available if the section has at least one duplicate search rule.
 





 Fig. 2 Go to the found duplicates page using the section actions
 

![scr_chapter_deduplication_duplicates_page.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/scr_chapter_deduplication_duplicates_page.png)
* Open the System Designer by clicking
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/btn_system_designer.png)
 and click
 
 Setup duplicates rules
 
 . This will open a new page Select the
 
 Show duplicate accounts
 
 or
 
 Show duplicate contacts
 
 option in the
 
 Actions
 
 menu of the page (Fig. 3). This option is available for the
 
 Contacts
 
 and
 
 Accounts
 
 sections.
 




 Fig. 3 Go to the found duplicates page using the
 
 Setup duplicates rules
 
 section
 

![scr_chapter_deduplication_contacts_duplicates_page.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/scr_chapter_deduplication_contacts_duplicates_page.png)


#### 
 Find and merge duplicates



 To search for duplicates:
 


1. Open a section where you want to search for duplicates. For example, the
 
 Contacts
 
 section.
2. Select
 
 Show duplicate ‘Contacts’
 
 in the
 
 Actions
 
 menu (Fig. 2).
3. A found duplicates page will open. If the duplicate search was performed earlier (e. g., automatically), the page will display its results. You can process the previous duplicate search results before searching again.
4. Select
 
 Run duplicate search
 
 in the
 
 Actions
 
 menu of the found duplicates page.
5. Creatio will search for duplicates in the background. In the meantime, you can continue working in the system.
6. Once the duplicate search is complete, you will receive a notification on the
 ![btn_com_notification_center_system_notifications.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/btn_com_notification_center_system_notifications.png)
 tab of the notification center (Fig. 4).
 

 Fig. 4 The notification about the completed duplicate search
 

![scr_chapter_deduplication_notification.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/scr_chapter_deduplication_notification.png)
7. Click the link in the notification to view the duplicate search results. You can also go to the results page in several other ways (Fig. 2, Fig. 3).
 



 The results list displays the duplicate records found based on the active search rules. The records are grouped by similarity (Fig. 5).
 



 You can merge each group of records into a single record or indicate that the records in the group are not duplicates. In the latter case, Creatio will add the records to the exception list for the next search.
 




 Fig. 5 Select the duplicates to merge
 

![scr_chapter_deduplication_wnd_merge_btn.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/scr_chapter_deduplication_wnd_merge_btn.png)
8. To merge duplicates, select the necessary records and click
 
 Merge
 
 .
   

 As a result, Creatio will merge the selected records in the group into one record that contains the unique data from the merged records. If the selected records have different data in the same field, Creatio will prompt you to select the data to save.
9. To add records to the exception list, click the
 
 Not duplicates
 
 button for the group that contains unique records (Fig. 6).
 



 As a result, Creatio will not consider the records in the group as duplicates for the next duplicate search.
 




 Fig. 6 The records that are not duplicates
 

![scr_chapter_deduplication_wnd_skip_btn.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/scr_chapter_deduplication_wnd_skip_btn.png)


### 
 Local duplicate search


#### 
 Find duplicates of a new record



 Creatio runs a local duplicate search when you save a new record. If a duplicate search page opens while saving a new record in the mini page or record page, it is likely that the record already exists.
 





 Note.
 
 The opened page will display all similar records, even if you do not have the corresponding access permissions. However, you will be able to see only the columns that have matching data according to the active duplicate search rules.
 




 You can return to editing the record or save it. If you save the record, Creatio will display it in the bulk duplicate search results in the future.
 


#### 
 Find duplicates of an existing record



 Use the
 **duplicate record widget** 
 to open the duplicate processing page directly from the record page in the
 
 Contacts
 
 and
 
 Accounts
 
 sections (Fig. 7).
 



 Creatio displays the widget if the section has active duplicate search rules configured and
 [bulk](https://academy.creatio.com/documents?id=1959) 
 and
 [global](https://academy.creatio.com/documents?id=1712) 
 duplicate search set up.
 





 Note.
 
 On-site users should update global search to latest version before working with duplicates search.
 





 Fig. 7 The duplicate record widget on the contact page
 

![release_notes_open_duplicates.png](/docs/sites/en/files/images/Platform_basics/deduplication/release_notes_open_duplicates.png)



 If Creatio finds potential duplicates, the widget will display their number. Click the widget to go to the duplicate processing page. The record from which you opened the page will be marked as “Current” (Fig. 8).
 




 Fig. 8 The duplicate processing page
 


![current_duplicate.png](/docs/sites/en/files/images/Platform_basics/deduplication/current_duplicate.png)





 The further duplicate management procedure is identical to the
 [bulk search](#title-747-38) 
 .
 



 If the record is unique, the widget will specify that Creatio was unable to find the duplicates (Fig. 9). In this case, the widget does not open the duplicate processing page.
 




 Fig. 9 The duplicate record widget in a unique record
 

![no_duplicates.png](/docs/sites/en/files/images/Platform_basics/deduplication/no_duplicates.png)


### 
 Merge duplicates


#### 
 Merge records



 You can merge several records both after the bulk duplicate search and at any other time without running the bulk search. You can merge both
 **section records** 
 and
 **lookup values** 
 .
 



 To do this:
 


1. Enable the multiple selection mode by running the
 
 Select multiple records
 
 action in the relevant section list or lookup.
 





 Note.
 
 You can also select multiple records in the section list by pressing Ctrl or Shift. Hold down Ctrl to select multiple records in an arbitrary order. Hold down Shift to select a range of adjacent records.
2. Select the records to merge.
3. Select
 
 Merge records
 
 in the
 
 Actions
 
 menu (Fig. 10).
 




 Fig. 10 Merge the lookup values
 

![scr_chapter_deduplication_act_merge_records.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/scr_chapter_deduplication_act_merge_records.png)





 Note.
 
 By default, the
 
 Merge records
 
 action is available only to system administrators. You must grant permission to other users. To do this, open the “Duplicates search” system operation (the “CanSearchDuplicates” code) in the
 
 Operation permissions
 
 section, go to the
 
 Operation permission
 
 detail, and grant permission to the relevant users/roles.
 




 Creatio will merge the selected records. If the records have different values in the same fields, the duplicate merge box will open. Select the values to save in the merged record and click
 
 Merge
 
 .
 



 Creatio will send you a notification once the merge is complete. Refresh the page to view the results in the record list. A single merged record will remain.
 



 When you click
 
 Merge
 
 on the duplicate page, Creatio will save the unique data from all merged records to one resulting record automatically. As a result:
 


* The resulting record will be based on the earliest created record.
* Creatio will save the unique detail and field values of duplicate records in the resulting record. This means all activities, calls, leads, etc. connected to the merged records will be available on the details of the resulting record.
* Creatio will not duplicate identical phone numbers even if they have different types. For example, the same phone is listed as business and mobile.
* Creatio will not duplicate identical communication options, addresses, and noteworthy events.
* If some field values are different (e.g., full name, phone numbers, etc.), you will be able to select the values to save in the resulting record. You can also select the text note to keep after merging.
* All external links that point to the merged duplicate records will point to the resulting record.
* Creatio will save the feed posts of all merged records in the resulting record.
* If the records of other sections reference any of the merged records, e. g., in the
 
 Primary contact
 
 field or
 
 Contacts of accounts
 
 detail of the
 
 Accounts
 
 section, the resulting record will keep the connections to the records of other sections.


#### 
 Example of the merged record data



 If the merged records contain different values in the same field, specify which data to save in the resulting record as part of the merge.
 



 For example, Creatio has duplicate records that have the following data:
 





| 
 Field
  | 
 Duplicate 1
  | 
 Duplicate 2
  | 
 Duplicate 3
  | 
 Resulting record
  |
| --- | --- | --- | --- | --- |
| 

 Full name
 
 | 
 Andrew Barber
  | 
 Barber Andrew
  | 
 A. Barber
  | 
 Decided by the user
  |
| 

 Type
 
 | 
 –
  | 
 Customer
  | 
 Contact person
  | 
 Decided by the user
  |
| 

 Account
 
 | 
 –
  | 
 Infocom
  | 
 –
  | 
 Infocom
  |
| 

 Mobile phone
 
 | 
 –
  | 
 +1 206 5871036
  | 
 +1-206-587-10-36
  | 
 Decided by the user
  |
| 

 Business phone
 
 | 
 +1 206 480-3801
  | 
 –
  | 
 +1 206 480-3801
  | 
 Decided by the user
  |
| 

 Email
 
 | 
 a.barber1981@gmail.com
  | 
 a\_barber1981@gmail.com
  | 
 –
  | 
 Decided by the user
  |
| 

 Skype
 
 | 
 barber\_andrew
  | 
 –
  | 
 –
  | 
 barber\_andrew
  |




 If you try to merge the records, Creatio will open the Merge duplicates box (Fig. 8).
 




 Fig. 11 Resolve deduplication conflicts
 

![scr_chapter_deduplication_wnd_merge.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/scr_chapter_deduplication_wnd_merge.png)



 Select the
 ![btn_radiobutton.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/btn_radiobutton.png)
 button next to the values to save in the resulting record and click
 
 Merge
 
 .
 



 As a result, a single Creatio record will remain. All objects connected to the merged records will now be connected to this record. For example, if you select the buttons as shown on the Fig. 11, the resulting record will contain the following data:
 


* Full name
 
 : Andrew Barber
* Account
 
 : Infocom
* Job title
 
 Sales Manager
* Business phone
 
 +1 206 5871036
* Email
 
 andrew@infocom-global.com


### 
 The duplicate search procedure



 The duplicate search mechanism is identical to the global search mechanism.
 



 Creatio indexes data to remove all special characters and divide the remaining letters and numbers into sets of two or three characters. The characters are recorded in the index that the search mechanism uses.
 



 Creatio does not modify the section records as part of the indexing.
 



 The
 **local duplicate search** 
 procedure is as follows:
 


1. The user creates and saves a new record.
2. Creatio processes new data (removes all special characters, divides the remaining data into sets of two or three characters) and requests Elasticsearch to search for records that contain the characters the user entered.
3. Creatio displays the matches according to at least one active duplicate search rule that has the
 
 Use this rule on save
 
 checkbox selected. Matches that have a different word order will be displayed as well.



 Creatio runs the
 **bulk duplicate search** 
 in a similar way and takes the active duplicate search rules into account.
 



 The phone numbers are compared to each other regardless of their field:
 
 Business phone
 
 ,
 
 Mobile phone
 
 ,
 
 Home phone
 
 , etc.
 





 Note.
 
 The duplicate list does not display the records excluded via the
 
 Is not a duplicate
 
 button earlier.
 




 If the field contains several words, Creatio will consider records that have both full and partial matches as duplicates. For example, if you search using the “Contact duplicates, contact name” condition, “John Best” and “John” contacts will be considered as duplicates.
 



 If the search conditions overlap, Creatio will search for duplicates using the stricter rule. For example, you have the following duplicate search rules configured: “Contact duplicates, contact name,” “Contact duplicates. Contact name, Phone.” Creatio will consider only the records that have matching full names as duplicates since the corresponding rule is stricter.
 



 Set up the duplicate search
-----------------------------



 Creatio checks for duplicates using the existing search rules. The
 
 Accounts
 
 ,
 
 Contacts
 
 , and
 
 Leads
 
 sections include the duplicate search rules out-of-the-box.
 



 You can perform the following actions in Creatio:
 


* Create new duplicate search rules based on a text or a lookup field in any section.
* Enable or disable individual rules.
* Specify the rules to use while saving a record.
* Remove unused rules.
 





 Note.
 
 Default rules that search for contact and account duplicates in leads cannot be deleted. However, you can
 [disable](#title-747-13) 
 these rules.


### 
 Add a duplicate search rule





 Attention.
 
 Learn more about setting up the service for Creatio on-site in a separate article:
 [Bulk duplicate search](https://academy.creatio.com/documents?id=1959) 
 .
 



1. Click the
 ![btn_system_designer00001.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/btn_system_designer00001.png)
 button in the top right to open the System Designer.
2. Go to the “System setup” block and click “Setup duplicates rules.”
3. Click the
 
 New rule
 
 button.
4. Fill out the following fields on the rule setup page (Fig. 12):
	1. Select a section that will use this rule in the
	 
	 Rule type
	 
	 field. For example, “Products.” You can create a rule for sections that have the
	 
	 Indexing for full-text search
	 
	 checkbox selected in the Section Wizard.
	2. Click
	 ![btn_chapter_mobile_wizard_new_role.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/btn_chapter_mobile_wizard_new_role.png)
	 on the
	 
	 Attributes
	 
	 detail and add one or more columns by which to search for duplicates. Keep in mind that the
	 
	 Attributes
	 
	 detail accepts only text and lookup fields.
	   
	
	 If you select multiple attributes in a single rule, e. g., “Code” and “Name,” the duplicate search will combine them using the “AND” operator. I. e., Creatio will look for records that contain both duplicate code and name. If you create several rules that have only one attribute, e.g., “Code” in the first rule and “Name” in the second rule, the duplicate search will combine them using the “OR” operator. I. e., the search will display records that contain either duplicate code or duplicate name.
	 
	
	
	
	
	 Fig. 12 Create a new duplicate search rule
	 
	
	![scr_chapter_deduplication_create_new_rule.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/scr_chapter_deduplication_create_new_rule.png)
5. Select the
 
 Active
 
 checkbox.
6. Select the
 
 Use this rule on save
 
 checkbox to use this rule while saving the mini page or record page.
7. Click
 
 Save
 
 .
 



 Creatio will notify you that the changes will apply upon your next login. After your next login, Creatio will use the new rule for the duplicate search. The
 
 Show duplicates
 
 action will appear in the corresponding section.


### 
 Disable a duplicate search rule



 You can deactivate a rule permanently or temporarily. Creatio will not use it to search for duplicates. To do this:
 


1. Click the
 ![btn_system_designer00001.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/btn_system_designer00001.png)
 button in the top right to open the System Designer.
2. Open the “Setup duplicates rules” link.
3. Select a rule to deactivate and click
 
 Open
 
 .
4. Clear the
 
 Active
 
 checkbox.
5. Click
 
 Save
 
 .
   

 As a result, Creatio will not use the rule to search for duplicates. You can reactivate it at any time.





 Note.
 
 If you deactivate a duplicate search rule specified in a
 [Find and merge duplicates
 
 business process element](/docs/8-0/user/bpm_tools/process_elements_reference/system_actions/find_and_merge_duplicates/find_and_merge_duplicates_process_element) 
 , the element will no longer use it. If you deactivate all specified rules, the process that contains the element will fail to complete.
 




 Creatio warns you that a business process might use the duplicate search rule when you deactivate it. However, Creatio does not check whether any
 
 Find and merge duplicates
 
 element is using it currently.
 


### 
 Schedule the automatic duplicate search



 In Creatio, you can schedule an automatic duplicate search. For example, run it three times a week. To do this:
 


1. Click the
 ![btn_system_designer00001.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/btn_system_designer00001.png)
 button in the top right to open the System Designer.
2. Open the “Setup duplicates rules” link.
3. Select
 
 Setup automatic duplicate search
 
 from the
 
 Actions
 
 menu on the duplicate search rule page (Fig. 13).
 

 Fig. 13 Open the automatic duplicate search setup window
 

![scr_chapter_deduplication_setting_schedule.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/scr_chapter_deduplication_setting_schedule.png)
4. Set up the parameters of the automatic bulk duplicate search on the
 
 Schedule search duplicates settings
 
 page (Fig. 14):
 




 Fig. 14 Schedule the duplicate search
 

![scr_chapter_deduplication_wnd_schedule.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_deduplication/scr_chapter_deduplication_wnd_schedule.png)


	1. Select a section for which to schedule the search. The list displays only the sections that have at least one duplicate search rule configured.
	2. Select the time to run the search.
	3. Select the day of the week to run the search.
	4. Click
	 
	 Apply
	 
	 .
	 
	
	
	
	 As a result, Creatio will search for duplicates automatically on the selected days at the set time using the active rules. Keep in mind that Creatio does not merge duplicates automatically. You must process the found duplicates manually.
	 
	
	
	
	 To disable the automatic duplicate search, clear the time field or the checkboxes next to the days of the week and click
	 
	 Apply settings
	 
	 . Both options will disable the automatic duplicate search.





