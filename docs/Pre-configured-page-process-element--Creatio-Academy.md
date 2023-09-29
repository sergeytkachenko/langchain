


 Open a custom page as part of a business process using the
 
 Pre-configured page
 
 element (Fig. 1). You can design a new page or open an existing page.
 




 Fig. 1 The
 
 Pre-configured page
 
 element on a process diagram
 

![scr_process_designer_preconfigured_page_case.png](https://academy.creatio.com/docs/sites/en/files/images/BPM_Tools/pre_configured_page_process_element/scr_process_designer_preconfigured_page_case.png)



 A pre-configured page makes it easy for users to interact with the UI elements as part of a business process. For example, an agent has to invite customers to an event, update the email subscription, and verify the customer contact information as part of an outgoing call campaign. This requires creating and updating records in
 
 Contacts
 
 and
 
 Events
 
 Creatio sections. The sections have separate edit pages. Use the
 
 Pre-configured page
 
 element (Fig. 1) to create a single custom page (Fig. 2) for the required actions.
 





 Note.
 
 The
 
 Events
 
 section is available in Marketing Creatio product and Creatio CRM lineup.
 





 Fig. 2 The pre-configured page opened as part of a business process
 




![scr_process_designer_preconfigured_page_process.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_preconfigured_page_process.png)








 Note.
 
 We recommend using the
 [Open edit page](/docs/8-0/user/bpm_tools/process_elements_reference/user_actions/open_edit_page/open_edit_page_process_element)
 element to display standard pages. For example, a contact or an invoice page. We recommend using the
 [Auto-generated page](/docs/8-0/user/bpm_tools/process_elements_reference/user_actions/auto_generated_page/auto_generated_page_process_element)
 element if you need a simple custom page without elaborate components, such as tabs, details, widgets, and business rules.
 




 Specify the pre-configured page parameters in the element setup area (Fig. 3). The
 
 Pre-configured page
 
 element setup area largely depends on the selected page.
 




 Fig. 3 The
 
 Pre-configured page
 
 element setup area
 




![chapter_process_designer_preconfigured_page_7.18.png](https://academy.creatio.com/docs/sites/en/files/images/BPM_Tools/user_elements_bp/chapter_process_designer_preconfigured_page_7.18.png)





1. Enter the element caption at the top of the element setup area. Creatio will display the caption on the process diagram.
2. Which page to open?
 
 – select an existing page or create a new page to open. If the page has its own parameters, they will be displayed along with other properties in the
 
 Page parameters
 
 block. Click the
 ![btn_button_preconfigured_new00009.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_button_preconfigured_new00009.png)
 button to create a new page in the Page Designer. Click the
 ![btn_edit_page.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_edit_page.png)
 button to modify the currently selected page.
3. Who performs the task?
 
 – select one of the options and fill out the field that opens:
	* “User” – specify the user who will see the page in the
	 
	 Contact
	 
	 field.
	* “Employee's manager” – specify the user whose manager will see the page in the
	 
	 Contact
	 
	 field.
	* “Role” – specify the role the users with which will see the page in the
	 
	 Role
	 
	 field.
	 
	
	
	
	 You can specify a dynamic parameter value or select a constant in the parameter value box.
4. Show page automatically
 
 – select the checkbox to display the page automatically as soon as the process initiates the action.
5. Recommendations for filling in the page
 
 – enter the recommendations to display on the page. The recommendation text is a single line string, which does not support line breaks regardless of syntax. To display the text in the assignee's language, make sure the “Create business process tasks in the owner's language” (“UsePerformerCultureInUserTask” code) system setting is enabled and the
 
 Translation
 
 section includes the translation. Learn more:
 [Localize UI via the
 
 Translation
 
 section](/docs/8-0/user/customization_tools/custom_localization/translate_the_ui/localize_ui_via_the_%5Btranslation%5D_section) 
 .
 





 Note.
 
 If the assignee is a group whose members use different Creatio languages, the recommendation will use the default culture.
6. User hints
 
 – enter additional information about the task. Click the
 ![btn_com_information00010.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_com_information00010.png)
 button on the page to view the hint.
7. Connected object
 
 – specify the section to which the process action is connected. You can fill out this field using the parameter value box.
8. Record of connected object
 
 – specify the connected section record. You can fill out this field using the parameter value box.
 
 If the user saves the pre-configured page as part of the process, Creatio will add the records of the connected object and connected object instance to the
 
 Connected objects
 
 block of the
 
 Process log
 
 section.
 



 The
 
 Run process
 
 menu will be available on the connected record page.
9. Page parameters
 
 – the block displays the
 [page parameter fields](#title-2076-28) 
 you add to the page. You can set the field values in several ways:
 


	* Specify the
	 [default values](#title-2076-33) 
	 .
	* Receive the values specified by the user as part of the process. To do this, pass the needed parameter values from the corresponding elements to the page parameters.
	* Use
	 [collection parameters](/docs/8-0/user/bpm_tools/business_process_setup/collections/process_collections) 
	 that contain complex values, each representing several entries. For example, a list of contacts with the name, address, and phone number for each contact. To set up a collection parameter in the page, find the page view model in the
	 
	 Configuration
	 
	 section by title, add the “Serializable list of composite values” parameter with the needed sub-parameters to the model, and code the custom business logic.
10. Run following elements in the background
 
 – select the checkbox to run the elements connected to the outgoing flows in the background.
11. Create activity
 
 – select the checkbox to create a corresponding activity as part of this process step. If you select the checkbox, the following fields will appear:
	1. Start in
	 
	 – specify the period after which the activity must start, in minutes, hours, days, weeks, or months. The countdown starts after the activity is created. Creatio uses this parameter to populate the
	 
	 Start
	 
	 field of the activity page.
	 
	
	
	 Note.
	 
	 The value of the activity page's
	 
	 Start
	 
	 field is the sum of the current user time and the
	 
	 Start in
	 
	 field value. For example, if you specify “30 minutes” in the
	 
	 Start in
	 
	 field, and the task was created at 12:00 PM, the value of the task's
	 
	 Start
	 
	 field will be “12:30 PM.”
	2. Planned duration
	 
	 – enter the activity duration, in minutes, hours, days, weeks, or months. Creatio uses this parameter to populate the
	 
	 Due
	 
	 field of the activity page.
	 
	
	
	 Note.
	 
	 The value of the activity page's
	 
	 Due
	 
	 field is the sum of the
	 
	 Start
	 
	 and
	 
	 Planned duration
	 
	 field values.
	3. Remind in
	 
	 – specify the period that ends before the activity starts. After this period, the notification for the owner or the role will be created automatically.
	4. Show in calendar
	 
	 – select the checkbox to display the task in the
	 
	 Calendar
	 
	 view of the
	 
	 Activities
	 
	 section.
	5. Connected to
	 
	 – connect the task to other Creatio entities. For example, an account. Creatio will display the task on the
	 
	 Activities
	 
	 detail of the connected record. By default, the element setup area displays account and contact connections. Click the
	 ![btn_button_connections.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_button_connections.png)
	 button to connect the task to other Creatio entities.



 Open the Page Designer
------------------------



 You can create custom pre-configured pages in the
 **Page Designer** 
 (Fig. 4), which is similar to the one used in the
 [Section Wizard](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/section_setup/create_a_section/add_a_new_section) 
 .
 




 Fig. 4 The Pre-configured Page Designer
 

![scr_process_designer_preconfigured_page_wizard.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_preconfigured_page_wizard.png)



 To open the Page Designer:
 


* Click
 ![btn_com_add_tab00011.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_com_add_tab00011.png)
 in the
 
 Which page to open?
 
 field to create a new pre-configured page. If you have already filled out the field, clear it first.
* Click
 ![btn_edit_page00012.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/btn_edit_page00012.png)
 in the
 
 Which page to open?
 
 field (Fig. 5) to edit an existing page. If the page was created in the Page Designer, the Designer will open.




 Fig. 5 Open the Page Designer
 

![scr_chapter_process_designer_prec_page_open_designer.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_prec_page_open_designer.png)



 Select the page template
--------------------------



 You can select a template each time you create a new pre-configured page. The template determines the layout of UI elements, e. g., tabs, profile area, etc., on the page. The template cannot be changed after you click the
 
 Select
 
 button on the template selection box.
 





 Note.
 
 The pre-configured page templates are
 [view model schemas](/docs/8-0/developer/front_end_development/client_schema/overview) 
 , which can be customized using development tools.
 




 Add a data source
-------------------



 If you plan to add or update Creatio records using a pre-configured page, consider adding the corresponding Creatio object as the data source. For example, add the “Contact” object as the data source to add or modify a contact record.
 



 Click
 
 Add data source
 
 (Fig. 6) in the Page Designer menu to add a page data source.
 




 Fig. 6 Add a page data source
 

![scr_process_designer_prepage_add_datasource.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_prepage_add_datasource.png)



 The data source page will open. Fill out the page fields:
 





|  |  |
| --- | --- |
| 
**The object from which to read data** 
 | 
 Select a section, detail, or lookup object, whose records will be added or updated on the pre-configured page. For example, select the “Contact” object to set up a page where the user will be able to add or modify a contact record.
  |
| 
**Data source name** 
 | 
 If necessary, enter a custom name for the data source. Creatio will display this name in the Page Designer menu.
  |
| 
**The parameter of the page to which the current record is transferred** 
 | 
 Enter the name of the
 
 Pre-configured page
 
 element parameter that will store the Id of the added or modified data source object's record.
 

 Select an existing parameter from the lookup or add a new parameter by entering its name. Creatio will add the corresponding field to the
 
 Page parameters
 
 menu of the Page Designer, as well as the
 
 Page parameters
 
 block of the
 
 Pre-configured page
 
 element setup area.
 

 The parameter value depends on whether you need to add a new record to the data source object or modify an existing record.
 * Leave this parameter empty
 **to add new records** 
 using the pre-configured page. In this case, any information the user enters in the data source fields will be saved as a new record. Creatio will pass the Id of the saved record to this parameter when the
 
 Pre-configured page
 
 element completes its execution.
* Map this parameter to the
 [Id of the needed record](/docs/8-0/user/bpm_tools/business_process_setup/parameters/process_parameters) 
**to modify existing records** 
 . In this case, the data source fields will display the values of the selected record's fields. Modifying these values on the page will modify the corresponding record.
 |




 You can add multiple data sources to a single page. The Page Designer displays page data sources in the menu, marked with the
 ![icn_precon_page_data_source.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/icn_precon_page_data_source.png)
 icon.
 



 Add fields
------------



 To add a field to a page, drag it from the Page Designer menu to the template area. You can add two types of fields to a pre-configured page:
 


* ![icn_precon_page_data_source00013.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/icn_precon_page_data_source00013.png)
**Data source fields** 
 that correspond to the columns of the object selected as the page data source. Use these fields to add or update Creatio records. For example, add a
 
 Full name
 
 field from the
 
 Contact
 
 data source to edit the contact's full name.
* ![icn_precon_page_parameters.png](/guides/sites/default/files/documentation/user/ru/bpms/BPMonlineHelp/chapter_process_designer/icn_precon_page_parameters.png)
**Page parameter fields** 
 represent parameters of the current
 
 Pre-configured page
 
 element. If you add a new page parameter field, Creatio will add the corresponding parameter to the
 
 Page parameters
 
 block in the
 
 Pre-configured page
 
 element setup area. Use the page parameter fields to pass any information that goes beyond the scope of objects used as page data sources.
 



 Adding fields in the Page Designer is similar to adding fields in the Section Wizard. Learn more:
 [Set up page fields](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/fields/set_up_page_fields) 
 .



 For example, add the
 
 Contact
 
 data source and its
 
 Full name
 
 and
 
 Full job title
 
 fields to the pre-configured page to verify the contact name and job title during a call. You can add process-specific information, such as an
 
 Agreed to participate in the campaign
 
 checkbox, as a page parameter field.
 



 Edit the page view model directly in the
 
 Configuration
 
 section to set up
 [collection parameters](/docs/8-0/user/bpm_tools/business_process_setup/collections/process_collections) 
 .
 



 Add dashboards (widgets)
--------------------------



 You can add summary analytics data from any Creatio section to the pre-configured page. Save the page in the Page Designer for the first time to be able to add dashboards. Adding dashboards is similar to adding dashboards in the Section Wizard. Learn more:
 [Add analytics to a record page](/docs/8-0/user/customization_tools/analytics/add_page_analytics/add_analytics_to_a_record_page) 
 .
 



 Add details and field groups
------------------------------



 You can add field groups, tabs, and details to the tab area of the pre-configured page. This area is available in all templates, except “Grid page.” Add details similarly to adding details in the section wizard. Learn more:
 [Set up page field groups](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/field_groups/set_up_page_field_groups) 
 . Create new details to add to a pre-configured page in the
 [Detail Wizard](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/create_a_detail/create_new_detail) 
 .
 



 When adding details to a pre-configured page, select a pre-configured page parameter, which will be used to filter detail records. Usually, these are the parameters, where the Id of the current data source record is passed.
 



 For example, when you add a
 
 Contact
 
 data source, Creatio will add the
 
 Contact
 
 parameter that stores the contact Id as well. If you need to add the
 
 Contact addresses
 
 detail to display the information of a particular contact, select the
 
 Contact
 
 parameter in the
 
 Object column
 
 field on the detail settings page.
 



 Set up buttons
----------------



 You can add buttons to the pre-configured page and define their logic. Buttons can save and/or close the page, as well as serve as conditions for process branching with
 [conditional flows](/docs/8-0/user/bpm_tools/process_elements_reference/flows/conditional_flow_shortcut/conditional_flow) 
 . Add buttons to the area below the page title. By default, the
 
 Save
 
 and
 
 Close
 
 buttons are available on the page.
 



 Double-click a button to modify its properties. Select a button and click “X” in the top right corner to delete it.
 



 The main button functionality properties are as follows:
 





|  |  |
| --- | --- |
| 
**Completes the process step** 
 | 
 If you select this checkbox, the button will close the page and terminate an element with a specific result you can use in conditional flows, similar to the
 
 Perform task
 
 element. You can use any button that closes the page in a conditional flow.
  |
| 
**Validates and saves the entered data** 
 | 
 If you select this checkbox, the button will check if the user filled out the required fields and save the field data once clicked.
  |
| 
**Generates a signal** 
 | 
 Enter the signal the button will generate once clicked, similar to the
 [Throw signal](/docs/8-0/user/bpm_tools/process_elements_reference/events/throw_signal/throw_signal_intermediate_event)
 element.
  |
| 
**Active** 
 | 
 If you select this checkbox, the button will be active when the page opens. For example, add buttons that are inactive by default and become active according to the page business rules.
  |




 Add business rules
--------------------



 Add business rules to the pre-configured page using the
 
 Business rules
 
 tab of the Page Designer. The procedure is similar to adding business rules in the Section Wizard. Learn more:
 [Set up a new busines rule](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/business_logic/setup/set_up_a_new_business_rule) 
 .
 



 For example, make the
 
 Subscribe to bulk email
 
 field editable only if the
 
 Agreed to email campaign
 
 checkbox is selected (Fig. 7).
 




 Fig. 7 A business rule
 

![scr_process_designer_preconfigured_page_business_rules.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_preconfigured_page_business_rules.png)



 Set up default field values
-----------------------------



 Set up default values for the page
 **parameter fields** 
 using the
 
 Pre-configured page
 
 element parameters. Each field in the
 
 Page parameters
 
 →
 
 Existing parameters
 
 menu corresponds to a parameter of the
 
 Page parameters
 
 block of the
 
 Pre-configured page
 
 element setup area (Fig. 8).
 




 Fig. 8 The page parameter fields in the Page Designer (left) and page parameters in the
 
 Pre-configured page
 
 element setup area (right)
 

![scr_process_designer_prepage_parameter_fields.png](https://academy.creatio.com/docs/sites/en/files/images/BPM_Tools/pre_configured_page_process_element/scr_process_designer_prepage_parameter_fields.png)



 These parameters have several functions:
 


* The parameter values determine the default values of the corresponding pre-configured page fields when the page opens as part of the process.
* The values entered in the corresponding page fields as part of the process will be recorded as the element parameter values when the element completes its execution. You can map these parameter values further down the process.



 For example, a page has a
 
 Contact
 
 data source and contains several fields from the “Contact” object, as well as the
 
 Communication options
 
 detail. To populate these fields and the detail with the data of a particular contact, pass the Id of the needed contact to the
 
 Contact
 
 parameter (Fig. 9).
 




 Fig. 9 Set up the pre-configured page element parameters
 

![scr_process_designer_preconfigured_page_parameters.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_preconfigured_page_parameters.png)



 If you leave the
 
 Contact
 
 parameter empty, Creatio will save any information entered in the “Contact” object fields and the “Communication options” detail as the data of a new contact. Learn more:
 [Process parameters](/docs/8-0/user/bpm_tools/business_process_setup/parameters/process_parameters) 
 .
 



 Element activation
--------------------



 When Creatio activates the incoming flows if the
 
 Pre-configured page
 
 element:
 


* In the regular mode, the element opens the specified page for the user. Creatio adds the corresponding task to the
 
 Business process tasks
 
 tab of the communication panel.
* In the background mode, the element does not open the page, however, Creatio adds the corresponding task to the
 
 Business process tasks
 
 tab of the communication panel. The process user can click the task to open the pre-configured page.



 Element completion
--------------------



 The element is deemed complete when the user clicks a button that closes the page. If the user leaves the page otherwise, e. g. by clicking a different section on the sidebar, runs a global search, etc., Creatio will close the page but will not deem the element complete. The process task will remain on the
 
 Business process tasks
 
 tab of the communication panel.
 



 Upon completion, Creatio will record any values entered on the page to the corresponding parameters or data source objects and activate the outgoing flows.
 




