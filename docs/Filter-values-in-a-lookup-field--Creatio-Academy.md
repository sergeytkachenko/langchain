


 You can set up a business rule that will apply filter to the list of values in the lookup field. This will make the list shorter.
 





 Example.
 
 Implement the following logic in the custom
 
 Requests
 
 section: only contacts with the “Employee” type are available in the
 
 Owner
 
 field.
 




 To implement the logic of the case, add a business rule that would filter the values in the
 
 Owner
 
 lookup field. To do this:
 


1. Open the needed section (e.g., the
 
 Requests
 
 custom section) and add a new business rule. You can learn more about adding and setting up a new business rule in the “
 
[Set up a new business rule](https://academy.creatio.com/documents?product=base&ver=7&id=1680) 

 ” article.
2. In the “THEN” block of the business rule, set up the action that would implement the needed business logic (Fig. 1):
 


	1. Click
	 **Add action.**
	2. In the drop-down menu of possible actions, select “
	 **Add field values filter.** 
	 ”
	 
	
	
	
	
	
	 Note.
	 
	 The “Add field values filter” business rule action is unconditional. When you select this action, the “IF” block of the business rule becomes grayed out and cannot be edited.
	3. In the
	 
	 Which field to filter and which connection in this field’s lookup to use for filtering?
	 
	 field, click
	 ![btn_com_lookup.png](/docs/sites/en/files/images/NoCode_Customization/business_rules/btn_com_lookup.png)
	 .
	4. In the opened window, click + next to “Requests” → select
	 **Owner** 
	 as the connected object field.
	5. In the
	 
	 Column
	 
	 field, select
	 
	 Type
	 
	 from the drop-down list → click
	 
	 Select
	 
	 .
	6. Click the
	 ![btn_business_rule_question.png](/docs/sites/en/files/images/NoCode_Customization/business_rules/btn_business_rule_question.png)
	 icon and select the
	 **“Lookup”** 
	 in the drop-down list. A set of fields for specifying lookup values will appear to the right.
	7. In the
	 
	 Which field to filter by
	 
	 filed to the right, select
	 **“Employee”** 
	 .
3. Click
 
 Apply
 
 →
 
 Section Wizard
 
 →
 **Save** 
 .
 





 Fig. 1
 

 Filter lookup values - configuring the “THEN” condition of the business rule
 

![gif_chapter_business_rules_filter_lookup_values.gif](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/filter_values_in_lookup_field/gif_chapter_business_rules_filter_lookup_values.gif)



 As a result, only the contacts of the “Employee” type will be available for selection in the
 
 Owner
 
 field of the request page.
 



 Clear and populate fields automatically
-----------------------------------------



 When working with filtering values in Creatio, you can automatically clear and populate fields on a record page.
 



 For example, you can set up a business rule that will automatically populate the [Account] field on a request page if the request owner is specified. This rule will also filter the owners by the account if the [Account] field is populated on a request page.
 



 Additionally, you can set up clearing the [Owner] field on a request page automatically if the account value is changed.
 



 To implement this logic:
 


1. Open the needed section (e.g., the [Requests] custom section) and add a new business rule. You can learn more about adding and setting up new business rules in the “
 [Set up a new business rule](https://academy.creatio.com/docs/node/1759) 
 ” article.
2. In the “THEN” block of the business rule, set up the action that would implement the needed business logic:
	1. Click
	 **[Add action]** 
	 .
	2. In the drop-down menu, select “
	 **Add field values filter** 
	 .”
	 
	
	
	 Note.
	 
	 The “Add field values filter” business rule action is unconditional. When you select this action, the “IF” block of the business rule becomes grayed out and cannot be edited.
	3. In the [Which field to filter and which connection in this field’s lookup to use for filtering?] field, click
	 ![btn_com_lookup.png](/docs/sites/en/files/images/Business%20rules/btn_com_lookup.png)
	 .
	4. In the opened window, click “+” next to “Requests” → select
	 **[Owner]** 
	 as the connected object.
	5. In the [Column] field, select [Account] from the drop-down list → click [Select].
	6. Click the
	 ![btn_business_rule_question.png](/docs/sites/en/files/images/Business%20rules/btn_business_rule_question.png)
	 icon and select “
	 **Field** 
	 ” in the drop-down list.
	7. In the [Select field] window that pops up, select “Account” on the [Requests fields] tab.
3. Select the [Clear when the Account field is modified] checkbox to clear the [Owner] field on a request page automatically if the account value for this specific contact is changed.
4. Select the [Populate when the Owner field is populated] checkbox to populate the [Account] field on a request page automatically if the request owner is specified.
 

 Setting up a business rule for clearing and populating fields automatically
 

![auto_clear_populate_rule.png](/docs/sites/en/files/images/NoCode_Customization/business_rules/auto_clear_populate_rule.png)






 As a result, the [Owner] field on the request page will be cleared each time the account is changed for the corresponding contact. The [Account] field will be populated automatically if the owner of the request is specified.








