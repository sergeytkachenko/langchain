


 The context of the translation string is represented with the
 
 Key
 
 column. Use the
 
 Key
 
 column in the
 
 Translation
 
 section to determine the context of each translation string. There are two general types of translation strings:
 **configuration resources** 
 and
 **data resources** 
 , each having a specific key structure.
 





 Note.
 
 Before starting the localization, we recommend getting a basic understanding of the
 
[system architecture](https://academy.creatio.com/documents?id=15051) 

 , and the general functions of the
 
[Configuration
 
 section](https://academy.creatio.com/documents/technic-sdk/7-16/configuration-section-data-tab) 

 .
 






 Structure of the configuration resource keys
------------------------------------------------



 Configuration resources contain translations for buttons, columns, notifications and other interface elements. The structure of their keys is:
 **:
 
 :**
 .
 




 – is always “Configuration”. It indicates that the string is a configuration resource.
 




 – internal name of the schema in which the translation string is located. “Schemas” are the “building blocks” of a Creatio configuration. There are three types of schemas: objects (they represent database tables), pages and processes. For example, “Activity” is the “Activity” object schema, “ActivityPageV2” is activity edit page schema, and “ActivitySectionV2” is the section page of the
 
 Activities
 
 section.
 





 Note.
 
 The list of all schemas is available in the
 
 Advanced settings
 
 section, on the
 
 Configuration
 
 >
 
 Schemas
 
 tab.
 






 Note.
 
 You can view internal names of schemas created for custom sections in the Section Wizard. Schema names for custom sections are generated automatically, based on the value in the
 
 Code
 
 field, entered on the first step of the Section Wizard.
 





 – location of the string within the schema.
   

 The following
 **types of keys** 
 are used in the configuration resources:
 


* + “Caption” – schema name. For example, the string “Configuration:ActivityPageV2:Caption” contains caption of the “ActivityPageV2” schema.
* + “Columns” – key for strings that contain column names of an object schema. The “Columns” keys have the following structure: “Columns.<column internal name>.Caption“. For example, the “Configuration:Activity:Columns.Author.Caption” string contains the caption of the “Author” column in the “Activity” object. Object column titles are used as the names of the corresponding fields on the section lists, record pages and details. Thus, by localizing a column in an object, you will localize the corresponding captions in the section and detail lists and pages.
* + “LocalizableStrings” – key for localizable strings that were added directly by developers. These strings can be found in any schema (object, page, business process). Usually, these are not standard translation strings (i.e. Not object fields) in the page schemas, such as menus, messages, etc. The key has the following structure: “LocalizableStrings.<Internal name of the string>.Value“. The internal name of the string is specified by the developer or generated automatically by the Section Wizard. For example, the string “Configuration:ActivityPageV2:LocalizableStrings.CallTabCaption.Value” contains caption of the
	 
	 Calls
	 
	 tab of the activity page.



 Keys for configuration resource strings that are unique to
 **business processes** 
 are as follows:
 


* + “Parameters” – the string contains process parameter names and values. The process parameter name key syntax is as follows: “Parameters.<Parameter internal name>.Caption“. The key syntax process parameter names is as follows: “Parameters.<Parameter internal name>.DisplayValue“. For example, the string “Configuration:CreateInvoiceFromOrder:Parameters.CurrentOrder.Caption” contains the name of the “CurrentOrder” parameter in the “New invoice based on this order” process.
* + “EventsProcessSchema” – key of an embedded process string. Embedded processes handle business logic of objects and usually contain localizable error and message texts. The syntaxis of the embedded process string keys is similar to that of the regular process strings (with the addition of “EventsProcessSchema” at the beginning of the key).
* + “BaseElements” – the string contains information about process elements. The key syntax depends on the information type. For example, the key “BaseElements.<element internal name>.Caption” identifies an element caption on the business process diagram, “BaseElements.<element internal name>.Parameters.<element parameter internal name>.Caption” – key for a process element parameter name string, “BaseElements.<element internal name>.Parameters.<element parameter internal name>.Value” — key for a process element parameter value string.





 Note.
 
 Business process schema names are available in the
 
 Name
 
 column of the
 
 Process library
 
 section (you will need to add this column to the list via the
 
 Select fields to display
 
 command, or open a process properties page).
 
 Read more >>>
 







 Note.
 
 The translation strings whose key ends with “DisplayValue” contain process diagram captions (seen on the diagram only) and do not require translation.
 




 Below are examples of
 **configuration resource keys** 
 and their meaning.
 


* + Configuration:ActivityPageV2:LocalizableStrings.ActivityParticipantTabCaption.Caption – the name of the
	 
	 Participants
	 
	 tab on the activity page.
 “Configuration” – configuration resource key.
 



 “ActivityPageV2” – activity page schema.
 



 ”LocalizableStrings” – localizable string.
 



 “ActivityParticipantTabCaption” – localizable string internal name, identifying it as the
 
 Participants
 
 tab.
 



 “Caption” – the string is the caption.
* + Configuration:Account:Columns.Type.Caption – the title of the
	 
	 Type
	 
	 column in the “Account” object.
 “Configuration” – configuration resource key.
 



 “Account” – ”Account” object schema.
 



 “Columns” – object column.
 



 “Type” – column name.
 



 “Caption” – column title.
* + Configuration:ImportSettingsPage:EventsProcessSchema.LocalizableStrings.ErrorMessage.Value – error message in the embedded process of the “ImportSettingsPage” schema.
 “Configuration” – configuration resource key.
 



 “ImportSettingsPage” – import settings page schema.
 



 “EventsProcessSchema” – identifies that this is a string from an embedded process.
 



 ”LocalizableStrings” – localizable string.
 



 “ErrorMessage” – error message.
 



 “Value” – message text.
* + Configuration:AutoGeneratedPageUserTask:Parameters.InformationOnStep.Caption – name of the
	 
	 Information on step
	 
	 parameter of the
	 
	 Auto-generated page
	 
	 business process element.
 “Configuration” – configuration resource key.
 



 “AutoGeneratedPageUserTask” – identifies that this is a schema of the
 
 Auto-generated page
 
 process element.
 



 “Parameters” – the string contains parameter information.
 



 “InformationOnStep” – internal name of the
 
 Information on step
 
 process element parameter.
 



 “Caption” – parameter title.





 Fig. 1
 
 Examples of translation strings and their location in the interface of the contact page
 

![scr_chapter_multilanguage_keys_configuration_keys_list.png](/guides/sites/en/files/documentation/user/en/custom_localization/BPMonlineHelp/determine_translation_context/scr_chapter_multilanguage_keys_configuration_keys_list.png)





 Structure of the data resource keys
---------------------------------------



 Data resource keys identify data, such as lookup records, that must be localized. The key format is
 **:.
 
 :**










 .
 








 – is always “Data”. It indicates that the string is a data resource string.
 













 – name of the table (object) that contains the localized string. For example, “AddressType“ refers to the lookup table that contains address types.
 








 – table column name in the database. For example,
 
 Description
 
 or
 
 Name
 
 .
 




 – unique Id of the localized record. Record ID is a unique code that can be viewed in the database or in the browser address bar by opening a specific record.
 



 Below are examples of data resource keys and their meaning.
 


* + Data:ActivityCategory.Name:42c74c49-58e6-df11-971b-001d60e938c6 – a activity category name.
 “Data” – this is a data resource.
 



 “ActivityCategory” – the table (object) is “Activity category”.
 



 “Name:” – the localized value is in the “Name” column.
 



 “42c74c49-58e6-df11-971b-001d60e938c6” – record Id.
* + Data:ContactType.Name:60733efc-f36b-1410-a883-16d83cab0980 – a contact type name.
 “Data” – this is a data resource.
 



 “ContactType” – the table (object) is “Contact type”.
 



 “Name” – the localized value is in the “Name” column.
 



 “60733efc-f36b-1410-a883-16d83cab0980” – record Id.
* + Data:SysDashboard.Caption:e2895654-6ce4-4ef8-a126-5f75f49d9073 — a “Dashboard” tab name.
 “Data” – this is a data resource.
 



 “SysDashboard” – table (object) is “SysDashboard” (this object contains dashboard settings).
 



 “Caption” – the localized value is in the “Caption” column.
 



 “E2895654-6ce4-4ef8-a126-5f75f49d9073” – the record Id.





 Fig. 1
 
 Examples of data resource translation strings in the
 
 Translation
 
 section and in on the account page
 

![scr_chapter_multilanguage_keys_data_keys_list.png](/guides/sites/en/files/documentation/user/en/custom_localization/BPMonlineHelp/determine_translation_context/scr_chapter_multilanguage_keys_data_keys_list.png)




