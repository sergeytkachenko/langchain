


 You can set up a business rule that will disable saving records if certain fields are not populated.
 





 Example.
 
 Make the
 
 Description
 
 field required for all new records in the custom
 
 Requests
 
 section.
 




 To implement the logic of the case, you need to make the
 
 Description
 
 field required if the value in the
 
 Status
 
 field is “New.” To do this, add a separate business rule and set up its conditions:
 


1. Open the needed section (e.g., the
 
 Requests
 
 custom section) and add a new business rule.. You can learn more about adding and setting up a new business rule in the “
 [Set up a new business rule](https://academy.creatio.com/documents?product=base&ver=7&id=1680) 
 ” article.
2. In the “
 **IF** 
 ” block of the business rule, set the filter to define the conditions for triggering the business rule. For example, to apply a rule to the requests with the “New” status (Fig. 1):
 


	1. Click
	 **Add condition.**
	2. In the field that appears, select the
	 **“Status”** 
	 column as the lookup value.
	3. Leave the “=” (equal) sign as it is.
	4. Click the
	 ![btn_business_rule_question.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/make_field_required_or_optional/btn_business_rule_question.png)
	 icon and select the
	 **“Lookup” field type** 
	 in the drop-down list.
	 
	
	
	
	 A set of fields for specifying lookup values will appear to the right.
	5. Select “
	 **New** 
	 ” as the lookup value from the drop-down list.
	 
	
	
	
	
	
	 Fig. 1
	 
	
	 Make field required - configuring the “IF” condition of the business rule
	 
	
	![gif_chapter_business_rules_if_condition_setup2.gif](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/make_field_required_or_optional/gif_chapter_business_rules_if_condition_setup2.gif)
3. In the “
 **THEN** 
 ” block of the business rule, set up the action that would implement the needed business logic (Fig. 2):
 


	1. Click
	 
	 Add action
	 
	 . In the drop-down menu of possible actions, select “
	 **Make field required.** 
	 ”
	2. In the
	 
	 Which field will be required
	 
	 field, select the field that should be made mandatory, e.g.,
	 **Description**
	3. Click
	 
	 Apply
	 
	 →
	 
	 Section Wizard
	 
	 →
	 **Save** 
	 .
	 
	
	
	
	
	
	 Fig. 2
	 
	
	 Making a page field required/optional: configuring the “THEN” condition of the business rule
	 
	
	![gif_chapter_business_rules_then_condition_setup2.gif](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/make_field_required_or_optional/gif_chapter_business_rules_then_condition_setup2.gif)



 As a result, the
 
 Description
 
 field will be required if the request status is “New.” Creatio will not let you save a record unless you populate the
 
 Description
 
 field.
 




