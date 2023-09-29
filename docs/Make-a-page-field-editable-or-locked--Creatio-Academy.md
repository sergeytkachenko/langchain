


 You can set up a business rule that will make certain fields locked or editable on a record page under specific conditions.
 





 Example.
 
 In the
 
 Requests
 
 section, the users must not be able to change the applicant of completed requests. The users must still be able to change the applicants of requests that are in any other status.
 




 To implement the logic of the case, you need to make the
 
 Applicant
 
 field editable only for those requests where the value in the
 
 Status
 
 field is “New,” “Under evaluation,” “In progress,” “Canceled” or “Denied.” This will automatically lock the
 
 Applicant
 
 field for any requests where the value in the
 
 Status
 
 field is “Completed.”   To set up this business rule:
 


1. Open the needed section (e.g., the
 
 Requests
 
 custom section) and add a new business rule. You can learn more about adding and setting up a new business rule in the “
 
[Set up a new business rule](https://academy.creatio.com/documents?product=base&ver=7&id=1680) 

 ” article.
2. In the “
 **IF** 
 ” block of the business rule, set the filter to define the conditions for triggering the business rule. For example, to apply a rule to the requests with the “Completed” status (Fig. 1):
 


	1. Click
	 **Add condition.**
	2. In the field that appears, select the
	 **“Status”** 
	 column as the lookup value.
	3. Hover your cursor over the “=” (equal) sign and click the arrow that appears next to it to open the drop-down menu. Select the “≠” (not equal) option from the drop-down menu.
	 
	
	
	
	
	
	 Note.
	 
	 You can use the “Make field editable” business rule to both lock and unlock fields. Whenever the IF condition of the rule is fulfilled, the field will be editable. Otherwise, the field will be locked.
	4. Click the
	 
	![btn_business_rule_question.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/make_field_editable_or_locked/btn_business_rule_question.png)
	
	 icon and select the
	 **“Lookup” field type** 
	 in the drop-down list.
	 
	
	
	
	 A set of fields for specifying lookup values will appear to the right.
	5. Select “
	 **Completed** 
	 ” as the lookup value from the drop-down list.
	 
	
	
	
	
	
	 Fig. 1
	 
	
	 Make field editable/locked - configuring the “IF” condition of the business rule
	 
	
	
	![gif_chapter_business_rules_if_condition_setup.gif](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/make_field_editable_or_locked/gif_chapter_business_rules_if_condition_setup.gif)
3. In the “
 **THEN** 
 ” block of the business rule, set up the action that would implement the needed business logic (Fig. 2):
 


	1. Click
	 
	 Add action
	 
	 → “
	 **Make field editable.** 
	 ”
	2. In the
	 
	 Which field will be editable
	 
	 field, select the field to lock/unlock, e.g.,
	 **Applicant**
	3. Click
	 
	 Apply
	 
	 →
	 
	 Section Wizard
	 
	 →
	 **Save** 
	 .
	 
	
	
	
	
	
	 Fig. 2
	 
	
	 Make field editable/locked - configuring the “THEN” condition of the business rule
	 
	
	
	![gif_chapter_business_rules_then_condition_setup.gif](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/make_field_editable_or_locked/gif_chapter_business_rules_then_condition_setup.gif)



 As a result, the
 
 Applicant
 
 field will be editable if the request status is not equal to “Completed” – i.e., “New,” “Under evaluation,” “In progress,” “Canceled” or “Denied.” If the request status is “Completed,” the
 
 Applicant
 
 field will be locked.
 




