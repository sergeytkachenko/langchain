


 You can localize custom Creatio elements, e.g., sections, lookups into languages available in the
 
 Languages
 
 section. The translation is performed in the
 
 Translations
 
 section of the System Designer (you can also open the
 
 Languages
 
 section by clicking the
 
 Go to translation
 
 button).
 



 The records in the
 
 Translation
 
 section represent a list of strings requiring translation. You can enter translations directly in the list, without opening new pages.
 





 Note.
 
 Strings from the non-customizable interface (most of it is located on the “Advanced settings” page) are called “Core” resources. Core strings are not available in the
 
 Translation
 
 section. Core resources are stored in the form of MS Visual Resources (.resources files) along with Creatio executable files on the application server. The .resources files are localized using specialized localization tools (for example, Passolo, Catalyst, etc.).
 




 You can also localize Freedom UI elements in the Freedom UI Designer. Learn more in a separate article:
 [Localize a Freedom UI element](https://academy.creatio.com/documents?id=2441) 
 .
 





 Enter translations
----------------------



 The translation is performed using the
 **following columns** 
 :
 


* Key
 
 – a system string name that shows the context of the string. This is a non-editable column.
 
Read more >>>
* English (United States) - Default
 
 – the default language in Creatio is English.
* You can add a separate set of columns for each additional language. Use the
 
 View
 
 >
 
 Select fields to display
 
 command to set up the displayed languages in the translation section (usually, adding the target translation columns is enough).
* Verified
 
 – use this column for translation review. The checkbox will be automatically cleared for new translation strings and strings where source has changed since the translation verification.
* Modified on
 
 – standard Creatio column showing the date and time when the current record was last modified.



 If the untranslated text is short and fully displayed in the
 
 Translations
 
 section string, translate it right in the editable list. More complex texts are easier to translate in the translation string edit window (
 [Fig. 1](#XREF_16097_158)
 ).
 





 Fig. 1
 

 Translation string edit window
 

![translate_in_dialog_box.png](/guides/sites/en/files/documentation/user/en/custom_localization/BPMonlineHelp/localize_UI/translate_in_dialog_box.png)


### 
 Translate the interface and system elements in Creatio


1. Use the standard filters to select records for translation.
2. Click the string to modify, then click the
 ![btn_edit.png](/guides/sites/en/files/documentation/user/en/custom_localization/BPMonlineHelp/localize_UI/btn_edit.png)
 button to switch to edit mode.
3. Translate the text and save the changes.
4. Click the
 
 Next >
 
 button to display next sting in the edit window and the
 
 < Back
 
 button to display the previous string in the list.
5. When the translation is complete, close the translation edit window and click the
 
 Apply translations
 
 button. The newly translated strings will be displayed in the system next time a user with the corresponding language selected in their profile logs in.
 





 Note.
 
 The
 
 Translation
 
 section is designed for localization of custom functions. To translate the whole system to a new language, we recommend exporting translation strings and using professional localization tools.


### 
 Display untranslated strings



 To display untranslated strings, use the “Untranslated” filter and specify the target translation language. For example, in the “Untranslated” filter you have specified Spanish. The list will display strings that have a name or description of an item in Russian in the  “Russian (Russia) - default" column, and the “English (United States)” column will not be filled in or will have the same value as “Russian (Russia) - default" column .
 


### 
 Update the list of translations



 After creating a new section or column or adding new values to the lookup, new strings will appear in the system. To work with an up-to-date list of untranslated strings, update the translation list. To do this, click the
 
 Actions
 
 button, select
 
 Update translation list
 
 . This action starts searching for new untranslated strings. We recommend you to update your list every time you start translating.
 





 Note.
 
 The translation list update occurs every time you enter the
 
 Translations
 
 section.
 








 Search translation strings using filters
----------------------------------------------



 The
 
 Translation
 
 section has a set of standard filters that you can use to search for specific translation strings. Since the
 
 Key
 
 column contains information about the string context, you can filter strings by this column to select only strings that are used in a specific part of the system: page, detail, mini page, etc. page, detail, mini page, etc.
 





 Note.
 
 The translation string key structure and meaning are covered in a
 
[separate article](https://academy.creatio.com/documents?product=base&ver=7&id=1685) 

 .
 




 To filter the strings, first you need to determine the schemas that implement the functions that you need to localize. To do this, use the
 
 Configuration
 
 tab of the
 
 Advanced settings
 
 window. Alternatively, you can access the required function (for example, open the page that you need to localize) and check its schema name in the browser address bar. For example, when the
 
 Contacts
 
 section is open, the following URL in the address bar looks like this: “http://creatioapp.com/0/Nui/ViewModule.aspx#SectionModuleV2/
 **ContactSectionV2** 
 /”. The name of the
 
 Contacts
 
 section schema is “ContactSectionV2”.
 





 Note.
 
 When searching schema names in the
 
 Configuration
 
 section, be sure to check if the search results contain schema names with “V2” suffix. If search results contain schema names both with and without suffix (for example, “ContactSection” and “ContactSectionV2”), make sure that you translate strings for the schema with the “V2” suffix.
 






 Note.
 
 Strings whose keys contain “Configuration”, followed by the schema name and the word “Caption” (for example, “Configuration:SchemaName:Caption”) contain schema titles (displayed in the
 
 Configuration
 
 section) and do not require translation.
 



### 
 How to filter configuration resources



 Configuration resources include list column and page field names, tab captions, field group names, etc. For example:
 


* To translate the
 **column names** 
 in the
 
 Contacts
 
 section and the corresponding field names on the contact page, apply the following filter by the
 
 Key
 
 column: “Configuration%Contact%Column%”.
* To translate the
 **section page** 
 of the
 
 Contacts
 
 section, apply the following filter by the
 
 Key
 
 column: “Configuration%ContactSectionV2%”.
* To translate the contact
 **mini page** 
 , apply the following filter by the
 
 Key
 
 column: “Configuration%Contact%MiniPage%”.
* To translate contact
 **section record page** 
 , apply the following filter by the
 
 Key
 
 column: “Configuration%Contact%ContactPageV2”%. A section record page can have significant number of translation strings if separate pages are used for different types of records.
* To translate
 **detail list and record page** 
 , apply the following filter condition: “Configuration:Contact%Detail%”. In the list of filtered records, locate the name of the required detail schema. Then, apply a new filtering condition with the name of the needed detail schema, such as “Configuration%ContactCareer%” (for strings of the
 
 Job experience
 
 detail).
* If a section contains
 **built-in reports** 
 , apply the following filter condition to select their translation strings: “Configuration%Contact%Report%”.



 Additionally, to select strings used in the contact synchronization functions, use the following filter: “Configuration:Contact%SyncSettings%”. Use the “Configuration:%NotificationProvider%” filter to localize notifications.
 





 Attention.
 
 Translation string text may contain variables represented by numbers in braces, such as {0}. Make sure that translation includes all variables from its source text.
 



### 
 How to filter data resources (localized lookup records)



 To localize lookup values for a specific section, first determine which lookups are used in the section. To do so, filter translation strings by the
 
 Key
 
 column, using the following filter: “Data:Lookup.Name%”. The resulting string list will contain names of all registered lookup schemas. You can also use the folders in the
 
 Lookups
 
 section of the system designer to check which lookups are associated with which section or function. Use lookup schema names to filter records from the needed lookups. For example, the “Data:Job%” filter condition will return all records from the
 
 Job titles
 
 lookup.
 



 The
 
 Contacts
 
 section, for instance, uses the following lookups:
 


* Contact types
 
 – ContactType.
* Contact roles
 
 – ContactDecisionRole.
* Salutations
 
 – ContactSalutationType.
* Contact genders
 
 – Gender.
* Job titles
 
 – Job.
* Departments
 
 – Department.



 Lookups are not necessarily used on the record pages. For example, the
 
 Reasons for job change
 
 (JobChangeReason) lookup is used on the
 
 Job experience
 
 detail in the
 
 Contacts
 
 section.
 


### 
 How to maximize translation efficiency using static folders



 Use static folders to avoid creating complex filters. You can manually add specific strings for translation (for example, all lookups used in specific section) and then work only with the trans strings in the folder.
 



 To create a static folder, in the
 
 Filter
 
 menu, select
 
 Show folders
 
 (
 [Fig. 1](#XREF_20667_105)
 ).
 





 Fig. 1
 

 Enabling folder tree
 

![scr_chapter_multilanguage_strings_filtering_show_groups.png](/guides/sites/en/files/documentation/user/en/custom_localization/BPMonlineHelp/localize_UI/scr_chapter_multilanguage_strings_filtering_show_groups.png)



 Click
 
 New folder
 
 and select
 
 Static
 
 (
 [Fig. 2](#XREF_96522_106)
 ).
 





 Fig. 2
 

 Adding a static folder
 

![scr_chapter_multilanguage_strings_filtering_add_static_group.png](/guides/sites/en/files/documentation/user/en/custom_localization/BPMonlineHelp/localize_UI/scr_chapter_multilanguage_strings_filtering_add_static_group.png)



 Enter the name of the new folder and click
 
 OK
 
 .
 



 Apply a filter to select required strings, then add filtered strings to the folder. Apply next filter and add filtered strings to the folder (
 [Fig. 3](#XREF_19343_107)
 ).
 





 Fig. 3
 

 Adding records to the static folder
 

![scr_chapter_multilanguage_strings_filtering_add_records_to_group.png](/guides/sites/en/files/documentation/user/en/custom_localization/BPMonlineHelp/localize_UI/scr_chapter_multilanguage_strings_filtering_add_records_to_group.png)



 This way you can create and save a list of strings used in a specific section or other system function and later use a single folder to access them all.
 







 Identify errors with applying translations
------------------------------------------------



 After completing the translation and clicking the
 
 Apply translations
 
 button, some UI elements may remain untranslated because of errors in the process of applying translations (e.g., the schema of the translated resource has been deleted, etc.).
 





 Note.
 
 If a translation resource has been deleted, the corresponding translation strings will be deleted as well when the translations are applied. This does not result in a translation application error.
 




 If an error occurs when applying translations from a string, Creatio records the error text in the
 
 Error message
 
 column in the
 
 Translation
 
 section list (
 [Fig. 1](#XREF_23989_224_Error_message)
 ). To display the
 
 Error message
 
 column in the list of translation strings, add the
 
 Error message
 
 column to the list view via the
 
 Select fields to display
 
 command of the
 
 View
 
 menu.
 





 Fig. 1
 


 Error message
 
 column in the section list
 

![scr_chapter_multilanguage_errors.png](/guides/sites/en/files/documentation/user/en/custom_localization/BPMonlineHelp/localize_UI/scr_chapter_multilanguage_errors.png)



 Use the
 
 Translation apply errors
 
 folder (
 [Fig. 2](#XREF_30270_225_Folder_with)
 ) to quickly view all strings with error messages. To open the
 
 Translation apply errors
 
 folder, click the
 
 Show folders
 
 option in the
 
 Filter
 
 menu of the
 
 Translation
 
 section.
 





 Fig. 2
 

 Folder with translation apply errors
 

![scr_chapter_multilanguage_error_folder.png](/guides/sites/en/files/documentation/user/en/custom_localization/BPMonlineHelp/localize_UI/scr_chapter_multilanguage_error_folder.png)



 You can create additional folders using a filter by the
 
 Error message
 
 column to view specific translation errors.
 



 If the
 
 Error message
 
 column is empty for a translation string, then it has been properly applied and should be displayed in the UI.
 




