


 Most drop-down lists in Creatio draw their values from “lookups.” There is also a special “lookup” type of fields, where the user can select a record from a Creatio object. The objects dedicated to storing values for a specific field are called “lookups.”
 



 You can manage the values available in the drop-down lists and lookup fields by managing the records of the corresponding lookup objects. For example, after creating a new lookup field in your custom section via the Section Wizard, you will need to populate the lookup values in the
 
 Lookups
 
 section.
 





 Attention.
 
 Managing lookups requires access to the following system operation:
 
 Access to “Lookups” section
 
 (CanManageLookups). Additionally, if the lookup object is managed by operations, records, or columns - the user needs corresponding permissions to be able to manage records in that object.
 




 To
 **access the list of lookups** 
 , open the
 
 Lookups
 
 section either from the
 
 Studio
 
 workplace or the System Designer.
 





 Fig. 1
 
 Accessing the
 
 Lookps
 
 section from the
 
 Studio
 
 workplace
 

![open_lookups_studio.gif](/guides/sites/en/files/documentation/user/en/sys_settings_lookups/BPMonlineHelp/manage_lookup_values/open_lookups_studio.gif)





 Fig. 2
 
 Accessing the
 
 Lookps
 
 section from the System designer
 

![open_lookups_system_designer.gif](/guides/sites/en/files/documentation/user/en/sys_settings_lookups/BPMonlineHelp/manage_lookup_values/open_lookups_system_designer.gif)



 The
 
 Lookups
 
 section holds the list of registered lookups. Registering a lookup in the
 
 Lookups
 
 section enables the users to manage lookup content (records) and properties. Lookup remains functional if it is not registered in the
 
 Lookups
 
 section, however, unless the lookup object is used as a section or a detail – there is no way of editing the lookup content and properties.
 



 To manage the records of a specific lookup, you need to locate it in the list of the lookups first. Usually, the lookup object names reflect the names of the lookup fields whose values they store. For example, the lookup that stores the values for the
 
 Category
 
 field in the
 
 Activities
 
 section is called the “Activity category.”
 





 Note.
 
 You can check the name of the lookup object by modifying the corresponding lookup field in the Section Wizard. For more on working with fields, see the “
 
[Set up page fields](https://academy.creatio.com/documents?product=studio&ver=7&id=1399) 

 ” article.
 




 Use standard
 
[filters](https://academy.creatio.com/documents?product=studio&ver=7&id=1017) 

 and
 
[folders](https://academy.creatio.com/documents?product=studio&ver=7&id=1018) 

 to
 **locate the needed lookup** 
 . If you cannot find the needed lookup in the
 
 Lookups
 
 section, the lookup object may not have been registered in the section yet. Read more about registering lookups in the “Create new lookups” article.
 



 To
 **manage the lookup records** 
 , select the needed lookup in the list and click
 
 Open content
 
 . Most standard lookups use the standard editable list to add, edit or delete the lookup records. Note that you may need to add columns to the list before managing their contents. Some lookups may have dedicated edit pages for their records.
 



 To
 **change the lookup name, object, or page** 
 for editing its records, click
 
 Open properties
 
 .
 





 Fig. 3
 
 Changing lookup name, object or page
 

![manage_lookups.png](/guides/sites/en/files/documentation/user/en/sys_settings_lookups/BPMonlineHelp/manage_lookup_values/manage_lookups.png)



 To
 **delete a lookup** 
 from the
 
 Lookups
 
 section, click
 
 Delete
 
 . Deleting a lookup from the
 
 Lookups
 
 section does not delete the corresponding lookup object or affect the operation of the corresponding lookup fields in any way. You can always add the lookup to the
 
 Lookups
 
 section again.
 








