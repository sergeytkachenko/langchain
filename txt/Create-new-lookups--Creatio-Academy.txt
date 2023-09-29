


 The procedure for adding custom lookups depends on whether Creatio already contains an object which needs to be linked to the lookup or not.
 


* **If the lookup object does not yet exist** 
 , it will be created and registered automatically by the Section Wizard when you add a new lookup field to a page and save your changes. In this case, you may need to go to the
 
 Lookups
 
 section and populate the lookup with records.
* **If the lookup object already exists** 
 , you need to register a corresponding new lookup in the
 
 Lookups
 
 section to be able to manage its records.






 Creating lookups via Section Wizard
----------------------------------------



 A lookup is created automatically upon selecting the
 
 Add new lookup
 
 option when you add a new lookup field in
 **Section Wizard** 
 .
 





 Case.
 
 The
 
 Requests
 
 custom section has been configured in Creatio. Add a field displaying the request type to the request page. The field will be populated from a lookup.
 




 To implement the case:
 


1. In the
 
 Requests
 
 section, open a record and click the
 **View** 
 →
 **Open section wizard** 
 .
2. Set up the necessary field in page designer:
 


	1. On the left side of the page, select the
	 
	 Lookup
	 
	 column in the
	 
	 New column
	 
	 selection area and drag it to the record page.
	2. In the opened window, populate the required fields. If you want your lookup field to be required, select the
	 
	 Is required
	 
	 checkbox.
	 
	
	
	
	
	
	 Note.
	 
	 Detailed information about “Lookup” column parameters is available in a separate article.
	 
	Read more >>>
	
	
	
	
	
		* In the
		 
		 Lookup
		 
		 field group, select the
		 **Add new lookup** 
		 option and specify the title and name of the lookup you want to create (
		 [Fig. 1](#XREF_32461_438)
		 ). The
		 
		 Title
		 
		 field corresponds to the lookup title in Creatio and the object title, while the
		 
		 Name
		 
		 field corresponds to the object name and table name in the database.
	
	
	 Fig. 1
	 
	
	 Creating a new lookup
	 
	
	![scr_section_lookups_add_lkp_column.png](/guides/sites/en/files/documentation/user/en/sys_settings_lookups/BPMonlineHelp/add_lookups/scr_section_lookups_add_lkp_column.png)


1. Click the
 
 Save
 
 button.
2. Save the changes in the section wizard.
 



 As a result, after you save the changes in section wizard, the created lookup will automatically be registered in Creatio and bound to the package where the wizard saves changes.



 After that, you need to populate the lookup and specify the request types. To do this:
 


1. Open system designer by clicking the
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/sys_settings_lookups/BPMonlineHelp/add_lookups/btn_system_designer.png)
 button in the left top corner of the application and select the
 **Lookups** 
 link in the
 
 System setup
 
 block.
2. Find the created
 
 Request types
 
 lookup via the quick filter by title and
 **open its content** 
 .
3. To create the request types in the lookup, click the
 
 New
 
 button (
 [Fig. 2](#XREF_83787_439)
 ).
 





 Fig. 2
 

 The
 
 Request types
 
 lookup population
 

![scr_section_lookups_lkp_filling.png](/guides/sites/en/files/documentation/user/en/sys_settings_lookups/BPMonlineHelp/add_lookups/scr_section_lookups_lkp_filling.png)



 As a result, you will be able to use the lookup information from the created
 
 Request types
 
 lookup when populating the
 
 Type
 
 field on the request page (
 [Fig. 3](#XREF_65561_440)
 ).
 





 Fig. 3
 

 The
 
 Type
 
 lookup field
 

![scr_section_lookups_lkp_result.png](/guides/sites/en/files/documentation/user/en/sys_settings_lookups/BPMonlineHelp/add_lookups/scr_section_lookups_lkp_result.png)





 Adding a lookup based on an existing object
-----------------------------------------------



 To register a lookup for an
 **existing object** 
 in Creatio, do the following:
 


1. Open system designer by clicking the
 ![btn_system_designer00001.png](/guides/sites/en/files/documentation/user/en/sys_settings_lookups/BPMonlineHelp/add_lookups/btn_system_designer00001.png)
 button in the left top corner of the application and select
 
 Lookups
 
 in the
 
 System setup
 
 block.
2. Click the
 
 New lookup
 
 button and specify the lookup name and the object containing the lookup data structure (
 [Fig. 1](#XREF_55950_441)
 ).
 





 Fig. 1
 

 – Registering a lookup for the existing object
 

![scr_section_lookups_lkp_registration.png](/guides/sites/en/files/documentation/user/en/sys_settings_lookups/BPMonlineHelp/add_lookups/scr_section_lookups_lkp_registration.png)





 Note.
 
 Detailed information about the lookup properties is available in a separate article.
 
Read more >>>






 As a result, the lookup will be registered and populated with the data in correspondence with the object structure.
 




