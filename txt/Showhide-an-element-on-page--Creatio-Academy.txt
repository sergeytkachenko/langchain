


 You can set up a business rule that will make certain elements on record pages visible or hidden under specific conditions. These elements include: fields, details, field groups and tabs.
 





 Case .
 
 Show the
 
 Sick leave, days left
 
 field on a request page for all requests whose
 
 Originator type
 
 is an employee.
 




 To implement this, you need to make the
 
 Sick leave, days left
 
 field visible only if the value in the request
 
 Status
 
 field is “In progress.” To do this:
 


1. Open the needed section (e.g., the
 
 Requests
 
 custom section) and add a new business rule.. You can learn more about adding and setting up a new business rule in the
 
[Set up a new business rule](https://academy.creatio.com/documents?product=base&ver=7&id=1680) 

 article.
2. In the “
 **IF** 
 ” block of the business rule, set the filter to define the conditions for triggering the business rule. For example, to apply a rule to the requests with the “Employee” originator type:
 


	1. Click
	 **Add condition.**
	2. In the field that appears, select the
	 **“Originator type” column** 
	 as the lookup value. Note that boolean fields cannot be used for setting up the condition since they equal either “true” or “false,” i.e., they are always filled in.
	3. Leave the “=” (equal) sign as it is.
	4. Click the
	 ![btn_business_rule_question.png](/docs/sites/en/files/images/NoCode_Customization/business_rules/btn_business_rule_question.png)
	 icon and select the
	 **“Lookup” field type** 
	 in the drop-down list. A set of fields for specifying lookup values will appear to the right. Select
	 **“Employee”** 
	 as the lookup value from the drop-down list.
	 
	
	
	
	
	 Show/hide field - configuring the “IF” condition of the business rule
	 
	
	![gif_chapter_business_rules_if_condition_setup1.gif](/docs/sites/en/files/images/NoCode_Customization/business_rules/gif_chapter_business_rules_if_condition_setup1.gif)
3. In the “
 **THEN** 
 ” block of the business rule, set up the action that would implement the needed business logic.
 


	1. Click
	 
	 Add action
	 
	 → “
	 **Show element on the page.** 
	 ”
	2. In the
	 
	 Which element will be shown?
	 
	 block, select the element type to show. For example, leave the
	 
	 Field
	 
	 element type as it is.
	3. Select field to display on the page, e.g.,
	 **Sick leave, days left** 
	 .
	4. Click
	 
	 Apply
	 
	 →
	 
	 Section Wizard
	 
	 →
	 **Save** 
	 .
	 
	
	
	
	
	 Show/hide field - configuring the “THEN” condition of the business rule
	 
	
	![gif_chapter_business_rules_then_condition_setup1.gif](/docs/sites/en/files/images/NoCode_Customization/business_rules/gif_chapter_business_rules_then_condition_setup1.gif)



 As a result, the
 
 Sick leave, days left
 
 field will display only for requests where the
 
 Originator type
 
 field contains “Employee.” If the
 
 Originator type
 
 field contains any other value, the
 
 Sick leave, days left
 
 field will be hidden.
 






