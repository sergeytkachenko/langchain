


 You can configure the basic business logic of the record pages by adding or modifying
 **business rules** 
 . Business rules affect the behavior of fields of the page.
 



 To access business rule configuration in a section page:
 


1. Open the section where you want to customize the business logic.
2. In the section, click
 
 View
 
 →
 
**Open Section Wizard** 

 .
3. In the “Section pages” block of the Section Wizard:
 


	1. if you have only one edit page in your section, click
	 **Edit page
	 
	 ;**
	2. if you have several edit pages in your section, click
	 **the link of a corresponding page** 
	 in the list (Fig. 1).
	 
	
	
	
	
	
	 Fig. 1
	 
	
	 Selecting a section edit page from the list
	 
	
	![scr_section_wizard_multiple_section_pages00010.png](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_section_wizard/scr_section_wizard_multiple_section_pages00010.png)
4. Go to the
 
**Business rules** 

 tab. As a result, the list of business rules for the current page (Fig. 2) will open.
 





 Note.
 
 Business rules are available for all section pages, detail pages, as well as custom pages designed as part of business processes.
5. To add a new business rule, click
 
**Add business rule** 

 . The business rule setup page will open.





 View the list of page business rules
----------------------------------------



 You can set up several business rules for a page. All business rules display on the
 
 Business rules
 
 tab of the Page Designer (Fig. 2).
 





 Fig. 2
 

 The
 
 Business rules
 
 tab of the Page Designer
 

![scr_section_wizard_open_rules_step.png](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_section_wizard/scr_section_wizard_open_rules_step.png)


* Click
 
 Add business rule
 
 to create a new business rule.
* Select a rule in the list and click
 
 Disable
 
 /
 
 Enable
 
 to deactivate or activate it.





 Note.
 
 Your Creatio configuration may have a “legacy” hard-coded business rules. Creatio will attempt to convert them to the regular rules, but it may not always be possible due to the implementation of the “legacy” rules. Creatio will attempt to convert them to the regular rules, but it may not always be possible due to the implementation of the “legacy” rules.  If a hard-coded business rule was not recognized by the section wizard, then the name of this business rule will contain the message "(Incorrect rule)." The rule will be executed, but it cannot be opened or disabled in the section wizard. You only will be able to delete this rule with custom tools.
 










 Business rule conditions
--------------------------------



 Conditions in business rules are similar to advanced filters: they match a set if actual (current) values against the target values. If the values match, the condition is deemed fulfilled. On the business rule edit page, the conditions are grouped under the
 
 IF
 
 node.
 



 The table below lists the types of elements that can be matched against each other in a business rule condition:
 






| 
 Type of value
  | 
 Notes
  |
| --- | --- |
| 
 Field
  | 
 A column in an object that is the data source of the current page. For example, the data source of the
 
 Accounts
 
 section record page is the “Account” object. You can select columns of the linked objects (e.g., use the data of the account’s primary contact).
  |
| 
 System setting
  | 
 A system setting, that in this context is treated as a field with a certain value. Be sure to specify the system setting code (as opposed to its localizable title). You will need to specify the system setting code manually. The list of system settings is available in a
 [separate article](/docs/7-18/user/setup_and_administration/system_settings_and_lookups/manage_system_settings_shortcut/manage_system_settings) 
 .
 

 Business rules work only with system settings that have
 
 Cached
 
 checkbox selected.
  |
| 
 System variable
  | 
 A system variable that in this context is treated as a field with a certain value that changes dynamically. For example, the “Current Date” variable is a “Date” type field that always contains the current date.
 

 Available system variables:
 * “Current Time”
* “Current Date”
* “Current Time and Date”
* “Current user” (the current user account, stored in the SysAdminUnit object)
* “Current user contact” (the contact specified on the current user’s page in the
 
 System users
 
 section)
* “Current user account”
 |
| 
 Attribute
  | 
 The attribute value (for example, a virtual column). This option is intended for developer customization and requires development tools.
  |
| 
 Constant
  | 
 A static value of the following types: text, integer, decimal, date and time, date, time, lookup, Boolean. Use constants to match field values, system settings, system variables and attributes against a static value. A constant can be of any of the field data types supported in the section.
  |





 The conditions for execution of business rules are combined using common logical operators: "AND" / "OR." A business rule can have only one logical operator, which applies to all conditions of the business rule. The logical “AND” operator is used if the rule must be executed only if all conditions are met. Apply the “OR” logical operator if the rule must match at least one of the conditions.
 



 A condition for executing a business rule usually consists of three parts: the left side, the type of comparison and the right side of the condition.
 




 Business rule actions
------------------------



 Actions apply “on the fly,” whenever a business rule conditions are satisfied. Business rules can apply actions that implement the following behavior of the page fields:
 






| 
 Type of action
  | 
 Notes
  |
| --- | --- |
| 
 Show field on the page
  | 
 Show and hide a page field. An active business rule with this action shows the specified field on the page if the conditions of the rule are fulfilled. Otherwise, the field will be hidden.
  |
| 
 Make field required
  | 

 Make field required
 
 – indicates that field is required when the conditions are met.
  |
| 
 Make field editable
  | 
 Lock and unlock a page field (make it grayed-out or editable). An active business rule will make the field editable, as long as the conditions of the rule are fulfilled. If the conditions of the rule are not met, the field will become grayed-out. If the conditions of the rule are not met, the field will become grayed-out.
  |
| 
 Add field values filter
  | 
 Filter the options in drop-down lists of lookup fields. An active business rule will apply the filter to the values available in the drop-down list of the lookup field. This type of action does not require a condition and will always apply to the page, as long as the corresponding business rule is enabled.
  |
| 
 Set field value
  | 
 Fills the specified field with the value of the specified Creatio object. If the conditions of the rule are not met, the field will not be populated automatically.
  |






















