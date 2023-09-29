



 This functionality is available for Creatio 8.0.2 and later.
 




 Business rules control the page UI behavior and business logic. You can specify conditions and actions to take when those conditions are met. This lets you customize page behavior to better suit your needs, streamline data entry, enforce data standards, and improve data quality.
 



 To access business rule configuration on an app page:
 


1. Click
 ![btn_system_designer.png](/docs/sites/en/files/images/NoCodePlatform/business_rules/btn_system_designer.png)
 in the top right →
 
 Application Hub
 
 .
2. Open the needed app or
 [create a custom app](https://academy.creatio.com/documents?id=2377) 
 .
3. Open the page or create a custom page.
4. Click the
 ![btn_open_business_rules_designer.png](/docs/sites/en/files/images/NoCodePlatform/business_rules/btn_open_business_rules_designer.png)
 button in the top right (Fig. 1).
 




 Fig. 1 Open the business rules setup page
 

![scr_freedomui_open_business_rules.png](/docs/sites/en/files/images/NoCodePlatform/business_rules/scr_freedomui_open_business_rules.png)



 View the list of business rules
---------------------------------



 You can set up business rules on the page or object level. After you set up a page-level rule, Creatio applies it to the elements only on the selected page. After you set up an object-level rule, Creatio applies it to every Freedom UI page that uses the corresponding object, including editable lists. You can set up multiple business rules for a page or object. The list of business rules is displayed on the business rules setup page (Fig. 2).
 




 Fig. 2 List of business rules
 

![scr_freedomui_business_rules_list.png](/docs/sites/en/files/images/NoCodePlatform/business_rules/scr_freedomui_business_rules_list.png)





 Attention.
 
 If multiple rules affect the same page element, only the first rule is activated.
 



* Click
 
 Add rule
 
 to
 **create** 
 a new business rule.
* Select a rule in the list and click its name to
 **view** 
 or
 **edit** 
 the rule.
* Select a rule in the list and click the
 
 Enabled
 
 toggle in the setup area to
 **turn the rule on or off** 
 (Fig. 3).
 




 Fig. 3 Turn on the rule
 

![scr_freedomui_turn_on_rule.png](/docs/sites/en/files/images/NoCodePlatform/business_rules/scr_freedomui_turn_on_rule.png)
* Select a rule in the list and click
 ![btn_dots_menu_blue.png](/docs/sites/en/files/images/NoCodePlatform/business_rules/btn_dots_menu_blue.png)
 →
 
 Copy
 
 to
 **copy** 
 the rule.
* Select a rule in the list and click
 ![btn_dots_menu_blue.png](/docs/sites/en/files/images/NoCodePlatform/business_rules/btn_dots_menu_blue.png)
 →
 
 Delete
 
 to
 **delete** 
 the rule.



 Show/hide an element on a Freedom UI page
-------------------------------------------



 You can set up a business rule that shows or hides page elements under specific conditions.
 





 Example.
 
 Show the
 
 Sick leave, days left
 
 field on a request page for requests whose
 
 Originator type
 
 attribute is an employee.
 





 Fig. 4 Page rule that shows/hides the element
 

![scr_freedomui_show_field_rule.png](/docs/sites/en/files/images/NoCodePlatform/business_rules/scr_freedomui_show_field_rule.png)



 To implement this, the
 
 Sick leave, days left
 
 field must be visible only if the value of the
 
 Originator type
 
 field is “Employee.” To do this:
 


1. Open the needed section (e. g., the “Requests” custom app) and add a business rule.
2. Set the filter to define the conditions that trigger the business rule in the
 **“IF”** 
 block. For this example apply the rule to requests that have the “Employee” originator type:
	1. Click
	 
	 Add condition
	 
	 . This adds a condition row.
	2. Select the
	 **“Originator Type” attribute** 
	 in the new row.
	3. Leave the “=” (equal) sign as it is.
	4. Click the
	 ![btn_business_rule_question.png](/docs/sites/en/files/images/NoCode_Customization/business_rules/btn_business_rule_question.png)
	 icon and select the
	 **“Lookup” field type** 
	 in the drop-down list. This adds a lookup value field to the right.
	5. Select the
	 **“Employee” lookup value** 
	 .
3. Set up the action that implements the needed business logic in the
 **“THEN”** 
 block. For this example, show the
 
 Sick leave, days left
 
 field:
 


	1. Click
	 
	 Add action
	 
	 →
	 **“Show elements.”**
	2. Select the element type to show in the
	 
	 Which element will be shown?
	 
	 block. For this example, select
	 
	 Input
	 
	 . This opens a window.
	3. Select the field to show on the page, e. g.,
	 
	 Sick leave, days left
	 
	 , and click
	 
	 Select
	 
	 .
4. Click
 
 Save
 
 .



 As a result, Creatio will show the
 
 Sick leave, days left
 
 field only for requests whose
 
 Originator type
 
 field is set to “Employee.” If the
 
 Originator type
 
 field is set to any other value, Creatio will hide the
 
 Sick leave, days left
 
 field.
 



 Make a field required or optional
-----------------------------------




 This rule type is available for Creatio 8.0.4 and later.
 




 You can set up a business rule that makes elements required under specific conditions.
 





 Example.
 
 Make the
 
 Start date
 
 and
 
 Due date
 
 fields on a request page required for requests whose
 
 Type
 
 attribute is “Vacation.”
 





 Fig. 5 Page rule that makes the element required
 

![scr_freedomui_make_field_required_rule.png](/docs/sites/en/files/images/NoCodePlatform/business_rules/scr_freedomui_make_field_required_rule.png)



 To do this:
 


1. Open the needed section (e. g., the “Requests” custom app) and add a business rule.
2. Set the filter to define the conditions that trigger the business rule in the
 **“IF”** 
 block. For this example apply the rule to requests that have the “Vacation” type:
	1. Click
	 
	 Add condition
	 
	 . This adds a condition row.
	2. Select the
	 **“Type” attribute** 
	 in the new row.
	3. Leave the “=” (equal) sign as it is.
	4. Click the
	 ![btn_business_rule_question.png](/docs/sites/en/files/images/NoCode_Customization/business_rules/btn_business_rule_question.png)
	 icon and select the
	 **“Lookup” field type** 
	 in the drop-down list. This adds a lookup value field to the right.
	5. Select the
	 **“Vacation” lookup value** 
	 .
3. Set up the action that implements the needed business logic in the
 **“THEN”** 
 block. For this example, make the
 
 Start date
 
 and
 
 Due date
 
 fields required:
 


	1. Click
	 
	 Add action
	 
	 →
	 **“Make elements required.”**
	2. Select the element type to make required in the
	 
	 Which element will be required?
	 
	 block. This opens a window.
	3. Select the fields to make required on the page, e. g.,
	 
	 Start date
	 
	 and
	 
	 Due date
	 
	 , and click
	 
	 Select
	 
	 .
4. Click
 
 Save
 
 .



 As a result, Creatio will make the
 
 Start date
 
 and
 
 Due date
 
 fields required for requests whose
 
 Type
 
 field is set to “Vacation.” If the
 
 Type
 
 field is set to any other value, the fields mentioned will be optional.
 



 Make a field editable or read-only
------------------------------------




 This rule type is available for Creatio 8.0.4 and later.
 




 You can set up a business rule that makes elements editable or read-only under specific conditions.
 





 Example.
 
 Make the
 
 Owner
 
 field on a request page read-only for requests whose
 
 Status
 
 attribute is “Done” or “Canceled.”
 





 Fig. 6 Page rule that makes the element read-only
 

![scr_freedomui_make_field_read_only_rule.png](/docs/sites/en/files/images/NoCodePlatform/business_rules/scr_freedomui_make_field_read_only_rule.png)



 To do this:
 


1. Open the needed section (e. g., the “Requests” custom app) and add a business rule.
2. Set the filter to define the conditions that trigger the business rule in the
 **“IF”** 
 block. For this example apply the rule to requests that have the “Done” or “Canceled” status:
	1. Click
	 
	 Add condition
	 
	 . This adds a condition row.
	2. Select the
	 **“Status” attribute** 
	 in the new row.
	3. Leave the “=” (equal) sign as it is.
	4. Click the
	 ![btn_business_rule_question.png](/docs/sites/en/files/images/NoCode_Customization/business_rules/btn_business_rule_question.png)
	 icon and select the
	 **“Lookup” field type** 
	 in the drop-down list. This adds a lookup value field to the right.
	5. Select the
	 **“Done” lookup value** 
	 .
	6. Click
	 
	 Add condition
	 
	 . This adds a condition row.
	7. Select the
	 **“Status” attribute** 
	 in the new row.
	8. Leave the “=” (equal) sign as it is.
	9. Click the
	 ![btn_business_rule_question.png](/docs/sites/en/files/images/NoCode_Customization/business_rules/btn_business_rule_question.png)
	 icon and select the
	 **“Lookup” field type** 
	 in the drop-down list. This adds a lookup value field to the right.
	10. Select the
	 **“Canceled” lookup value** 
	 .
3. Set up the action that implements the needed business logic in the
 **“THEN”** 
 block. For this example, make the
 
 Owner
 
 field read-only:
 


	1. Click
	 
	 Add action
	 
	 →
	 **“Make elements read-only.”**
	2. Select the element type to make required in the
	 
	 Which element will be read-only?
	 
	 block. This opens a window.
	3. Select the fields to make required on the page, e. g.,
	 
	 Owner
	 
	 , and click
	 
	 Select
	 
	 .
4. Click
 
 Save
 
 .



 As a result, Creatio will make the
 
 Start date
 
 and
 
 Due date
 
 fields required for requests whose
 
 Type
 
 field is set to “Vacation.” If the
 
 Type
 
 field is set to any other value, the fields will be editable.
 




