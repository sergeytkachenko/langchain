


 What is the maximum number of custom sections that one can add to a Creatio application?
------------------------------------------------------------------------------------------



 There are no restrictions on the maximum number of custom sections. However, we strongly recommend that you weigh the need of adding a new section carefully since too many sections might affect the Creatio performance.
 





 Note.
 
 The list of available sections in the Creatio portal is limited and depends on the portal configuration.
 




 How do I connect a detail to a section?
-----------------------------------------



 You can connect existing details to your section using the Section Wizard. Read more:
 [Add an existing detail on a record page](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/set_up_a_detail/add_an_existing_detail_on_a_record_page) 
 .
 



 How do I set up section cases?
--------------------------------



 Open the section, click
 
 View
 
 →
 
 Set up section cases
 
 . You can also access cases by clicking
 
 Cases
 
 in Section Wizard. Read more:
 [Case Designer](/docs/8-0/user/bpm_tools/dynamic_case_setup/case_designer_workflows/overview/case_designer) 
 .
 





 Note.
 
 When working with a new custom section, you will need to configure the section primary properties before you start configuring cases.
 




 Why do I get the “Field "...": Enter a value” error when saving new records in my custom section?
---------------------------------------------------------------------------------------------------



 You might receive such an error if a required field was not populated before saving a new record. Make sure you add fields for all required columns to your section page or mini page in Section Wizard. The required fields are marked with an asterisk (\*) character in the list of available columns (Fig. 1).
 





 Fig. 1
 
 A required column in the list of available columns of the Page Designer
 

![chapter_section_wizard_required_field.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/section_wizard_FAQ/chapter_section_wizard_required_field.png)



 Section Wizard or Page Designer will not open or load. Why?
-------------------------------------------------------------



 You may not be able to open the Section Wizard due to the errors in the package dependencies in the Configuration.
 



 If you change the value of the
 
 Current package
 
 system setting, the dependencies between the packages in the configuration may become incorrect. This leads to issues with the Section Wizard operation.
 



 To fix the package dependency errors, open the
 
 System Designer
 
 →
 
 System Settings
 
 →
 **Current package** 
 and change its value to “Custom”. Then you will be able to access the Section Wizard.
 



 However, if you need to change the current package value for some other package, e. g., your development package, make sure you set the dependencies correctly. Read more:
 
[The
 
 Custom
 
 package](/docs/7-17/developer/development_tools/packages/packages#title-1200-8) 

 .
 



 How do I delete a section?
----------------------------



 To delete a custom Creatio section, delete the corresponding records from the database and delete the custom schemas from the
 
 Advanced settings
 
 section. Note that deleting a section from a workplace's section list does not delete it from the database. Read more:
 [Delete a section](https://academy.creatio.com/documents?id=15502#title-1311-1) 
 .
 




