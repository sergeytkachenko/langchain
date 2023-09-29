


 Use Creatio
 
 command line
 
 (the field labeled “What can I do for you?”) to quickly access the frequently used operations, such as opening a record page or running a business process.
 



 The command line is similar to the search line of web search engines. For example, enter the name and click
 

![btn_perform_command.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_command_line/btn_perform_command.png)


 or press the
 
 Enter
 
 key, to find a contact record.
 



 Execute other commands in the same way. For example, enter the command “Create Contact” to instantly open a new contact page or “Run Process” to launch the corresponding business process. The command line can recognize several variations of the same command. For example, both the “Create Contact“ and the “Add Contact“ are valid commands.
 



 If you enter a partial command, the system will offer you a list of several options. For example, if you enter “Create A”, the system will offer the following options: “Create Account” and “Create Activity”.
 



 You can search the system data by entering a search query in the command line. Creatio always searches in all sections (including custom sections).
 



 Localizable data in search results can be displayed in the language of the user. For example, if the
 
 Full name
 
 field is localized, French users will see its value in French, and English users will see it in English.
 





 Note.
 
 On-site users need to perform preliminary registration of the global search. Learn more in the “
 
[Global search setup](https://academy.creatio.com/documents?product=administration&ver=7&id=1712) 

 ” article.
 






 Search records
------------------


* Command line search utilizes the global search feature. The records are searched by their text and lookup fields as well as the following details:
 
 Addresses
 
 ,
 
 Communication options
 
 , and
 
 Banking details
 
 . For example, you can find an account by its alternative name, phone number, address, or account number.
* Files and links on the
 
 Attachments and notes
 
 tab of the record page can be found by their name or description.
* Search requests are processed taking into account common typos and morphology of different word forms in English (other languages are not currently supported). The query is not case-sensitive. You only need to enter the search text, for example, contact last name or the name of the knowledge database article. For a more accurate search, add more details to your search query, for example, “Ronald young director future vision".





 Note.
 
 To include certain section’s data in global search results, open the section wizard for the necessary section and select the
 
 Indexing for full-text search
 
 checkbox. Learn more about indexing in the “
 
[Configure section properties](https://academy.creatio.com/documents?product=administration&ver=7&id=1397) 

 ” article.
 




 The search results are displayed as a list of records containing the text of the search query or a part of it. The text that matches the search query is highlighted in bold for each found record (Fig. 1).
 





 Fig. 1
 

 A list of search results
 


![list_of_search_results.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_command_line/list_of_search_results.png)




 The results are ranked by relevance both in the actual results list and with any configured filters. For example, if the search is performed from the
 
 Contacts
 
 section the records of this section are displayed at the beginning of the list, and records from other sections of the system will be displayed below. For example, if you set up a filter by contact on the search result page, contacts with matching names will be displayed at the top of the list.
 



 If a user does not have permissions for a specific object column, e.g., for viewing an invoice amount, such column is not displayed on the page of global search results.
 





 Example.
 
 Let's find a contact by its phone number.
 



1. Enter the phone number in any format in the command line. You can enter only part of the number, with or without special delimiter characters.
2. Click
 

![btn_perform_command00001.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_command_line/btn_perform_command00001.png)


 or press the
 
 Enter
 
 key.
 



 After processing the search query, a list of results will be displayed with the contact you were looking for at the top of the list and other records that contain the entered phone number afterward.


### 
 Set up global search



 Select the “Show localized data in the global search results”
 [system setting](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/manage_system_settings_shortcut/manage_system_settings) 
 (UseLocalizableGlobalSearchResult) to display
 **localizable data** 
 in the search results. If the setting is disabled, localized data will be displayed according to the language selected for the system user specified in the “System operations user” system setting (SystemUser).
 





 Note.
 
 Data localization is enabled using development tools. Read more in the “
 [Enabling multi-language object schema](https://academy.creatio.com/documents?id=15274) 
 ” article.
 




 The rules for displaying search results are determined using the
 
 Global search default entity weight
 
 (GlobalSearchDefaultEntityWeight) and
 
 Global search default primary column weight
 
 (GlobalSearchDefaultPrimaryColumnWeight) system settings.
   

 Enable the
 
 Display search results with partial match
 
 system setting (UseInexactGlobalSearch) to display search results accounting for
 **morphology, typos, and fuzzy matches** 
 .
   

 Set a value for the “Match threshold for displaying in search results (percent]” system setting (GlobalSearchShouldMatchPercent) to manage the number of displayed search results with a
 **partial match** 
 and increase the chances of finding data for inaccurate search requests.
 



 Go to sections
----------------



 You can use the
 
 Go to section
 
 command of the command line to quickly display the contents of any folder in any section. For example, while working with the
 
 Activities
 
 section, you can easily open the “Customers” folder in the
 
 Accounts
 
 section. To do this, enter the command: “Go to section Accounts Customers”.
 



 When you enter the command, the drop-down list will display commands for opening other folders in that particular section.
 








 Add records
------------------



 To create records from the command line, use the
 
 Add
 
 command. When you enter it, the drop-down list will display commands for creating records in various sections, such as “Add Activity”, “Add Contact”, etc.
 



 The name of the new record can also be specified as part of the command. For example, enter “Add Contact Jones” to create a contact whose last name is “Jones”. As a result, a contact page will be opened containing “Jones” in the
 
 Full name
 
 field.
 








 Run business processes
-----------------------------



 To start a business process, enter the
 
 Run process
 
 command and the process name in the command line. For example, if there is a “New employee registration“ process set up in the system, enter the “Run process New employee registration“.
 





 Note.
 
 The list of processes available for selection in the command line is defined in the
 
 Process library
 
 section. Managing your business processes is described in the “
 [BPMN process administration](https://academy.creatio.com/docs/user/bpm_tools/business_process_administration) 
 ” guide.
 









 Set up custom commands
-----------------------------



 To create new commands for the command line, enter "create custom command." You can specify the command text (for example, “My tasks”), select the keyword (for example, “Go to section”), and then stipulate additional parameters depending on the selected keyword (for example, you can choose the
 
 Activities
 
 section and dynamic folder “My tasks”).
 



 Keywords represent types of operations that can be performed by the command line.
 


* Search – to find records.
* Go to section – to navigate through sections and folders.
* Add – to create records in system sections.
* Run process – to launch a business process.



 Log out of Creatio and log back in to make the newly registered command available in the command line.
 








