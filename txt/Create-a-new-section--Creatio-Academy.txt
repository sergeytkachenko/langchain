


 Each Creatio application contains a set of out-of-the-box sections. The pre-configured sections depend on the Creatio product and the installed Marketplace add-ons. You can add new custom sections to your application.
 





 Example.
 
 Add a custom
 
 Requests
 
 section to manage employee internal requests in Creatio.
 




 To add a new section:
 


1. Click
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_new_section/btn_system_designer.png)
 → “System Designer” → “Section Wizard”.
 





 Attention.
 
 You can open the Section Wizard only if you have permissions to the
 
 Access to “Configuration” section
 
 system operation.
2. You can create a section based on a new or an existing Creatio object. Click
 
 Select existing object
 
 and select the relevant object to create a section based on an existing object (Fig. 1).
 





 Fig. 1
 
 Creating a section based on an existing object
 

![scr_section_wizard_main_properties.png](/guides/sites/en/files/images/NoCode_Customization/section_wizard/section_wizard.png)



 For this example, create a
 
 Requests
 
 section based on an existing object.
 



 The further setup is similar for both cases.
3. Fill out the primary properties of the new section (Fig. 2).
 


	1. In the
	 
	 Title
	 
	 field, enter the name for the new section, e. g., “Requests.”
	2. In the
	 
	 Code
	 
	 field, enter the unique name that Creatio will use to generate section objects. For example, for a custom section named
	 
	 Requests
	 
	 , the section code can be "UsrRequests." The code can only contain integers and Latin characters. After saving the changes or switching to the edit mode, the field becomes locked.
	 
	
	
	 Note.
	 
	 The section code must contain a prefix, which identifies the author of the configuration changes. The prefix is specified in the “Prefix for object name” system setting. The default prefix is “Usr.”
	 
	
	
	
	
	
	
	 Attention.
	 
	 Make sure that you do not use any of the following prefixes or suffixes:
	 
	
	
	
	 Prefixes: “Base,” “Sys,” “Vw.”
	 
	
	
	
	 Suffixes: “InFolder,” “Lcz,” "Settings.”
	 
	
	
	
	 Otherwise, you will not be able to import the section records from Excel.
	3. Select the
	 
	 Indexing for full-text search
	 
	 checkbox, if you want to display the section data in the global search results.
	4. Replace the default
	 **section icon** 
	 displayed in the side panel: hover over it and click
	 ![btn_add_userpic.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_new_section/btn_add_userpic.png)
	 →
	 
	 Upload a new image
	 
	 .
	 
	
	
	
	
	
	 Note.
	 
	 We recommend using a white icon on a transparent background. Image format: PNG or SVG, size: 38x38 px. You can use the
	 
	[Marketplace icon library](https://marketplace.creatio.com/template/section-icons-creatio) 
	
	 to search for section icons.
	5. In the
	 
	 Workplace
	 
	 field, select a workplace from the drop-down list of available workplaces. A section can later be included in other workplaces. One section can belong to several workplaces.
	 
	
	
	
	
	
	 Note.
	 
	 Learn more about configuring workplaces in the
	 
	[Workplace setup](https://academy.creatio.com/documents?product=administration&ver=7&id=1248) 
	
	 article.
	6. After you add the new section, customize the primary section page.
	 
	[Read more >>>](https://academy.creatio.com/documents?product=administration&ver=7&id=1398)
	7. To use mini pages in the section, select the corresponding checkboxes. You can set up mini pages for adding, editing and viewing section records.
	 
	[Read more >>>](https://academy.creatio.com/documents?product=administration&ver=7&id=1949)
	8. Select the
	 
	 Enable approval in section
	 
	 checkbox to enable approval functions in the section.
	 
	
	
	
	
	
	 Note.
	 
	 Learn more about working with approvals in Creatio in the
	 
	[Approvals](https://academy.bpmonline.com/documents?product=base&ver=7&id=1831) 
	
	 article.
4. Click
 
 Save
 
 to apply the changes.





 Fig. 2
 
 Setting up the section properties
 

![scr_section_wizard_main_properties.png](/guides/sites/en/files/images/NoCode_Customization/section_wizard/create_new_section.png)



 As a result, the new
 
 Request
 
 section will be created and added to the workplace you specified in step 4. In the back-end, the corresponding
 
[objects](https://academy.creatio.com/online-courses/creatio-object-data-model) 

 will be added for the new section automatically:
 


* <Code> – e. g., UsrRequests – the section object that will contain the section data structure.
* <Code>File – e. g., UsrRequestsFile – the object for storing section attachments.
* <Code>Folder – e. g., UsrRequestsFolder – the object for storing the
 
[folder](https://academy.creatio.com/documents?product=administration&ver=7&id=1018) 

 structure of the section.
* <Code>InFolder – e. g., UsrRequestsInFolder – the object for storing information on which section record is placed in which folder.
* <Code>Tag – the object for storing section tags.
* <Code>InTag – the object for storing information on which section record is tagged with which tags.
* <Code>RequestsVisa – the object for storing information on section approvals.



 To see the section in the application workplace, update the page and clear the cache. Alternatively, you can log out of the application and log back in, which will make Creatio clear the cache and apply the changes.
 



 Developers can use the Section Wizard to quickly access the section page source code if they need to view or modify it.
 



 Creatio saves the configuration changes made in the Section Wizard to the package specified in the “Current package” (the “CurrentPackageId” code) system setting. By default, it is the “Custom” package that is designed to store the revisions made in the Section Wizard locally without transferring them to other Creatio instances.
 



 If you need to transfer the revisions made in the Section Wizard from the development to the production environment, create a new package to store the changes and specify it in the “Current package” (the “CurrentPackageId” code) system setting. Learn more:
 [Packages basics](/docs/7-17/developer/development_tools/packages/packages) 
 (developer documentation).
 



 If value of the “Current package” (the “CurrentPackageId” code) system setting is empty or the specified package is unavailable for the user, Creatio will ask you to select one of the available packages when you open the Section Wizard.
 



 Manage packages in the
 [Configuration
 
 section](/docs/7-17/developer/development_tools/creatio_ide/develop_in_creatio_ide/development_in_creatio_ide) 
 , and manage system settings in the
 [System settings
 
 section](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/manage_system_settings_shortcut/manage_system_settings) 
 .
 




