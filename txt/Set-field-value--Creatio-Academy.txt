


 You can set up a business rule that will automatically populate page fields using the "Set field value" business rule. You can populate the field with a value from another field, or calculate the value dynamically, using a formula.
 





 Note.
 
 Business rules represent "page" (i. e., UI-level) logic. This means that the "Set field value" business rule only sets values in the page fields; it does not update the database column values. The user still needs to save the changes on the page to apply them to the database. Likewise, business rules can only be triggered by the changes made on the page. For example, changes made to the database column values through integration logic will not trigger business rules.
 




 Populate a field with the value from another field
----------------------------------------------------



 You can use the “Set field value” business rule to automatically populate a field with a value from another field of the current section or a field from an object linked to the current section.
 





 Example.
 
 A custom section has a
 
 Contact
 
 lookup field and a
 
 Mobile phone
 
 text field. Implement the following business logic: whenever the
 
 Contact
 
 field is populated, populate the
 
 Mobile phone
 
 field with the mobile phone of that contact.
 




 To implement the logic of the example, add a “Set field value” business rule and set up its conditions:
 


1. Open the needed section (e. g., the custom
 
 Requests
 
 section) and add a new business rule. Learn more about adding and setting up new business rules in a separate article:
 [Set up a new business rule](https://academy.creatio.com/documents?id=1680) 
 .
2. Specify the conditions that trigger the business rule in the “
 
 IF
 
 ” block of the business rule if needed. For example, to apply a “Contact is filled in” rule to the requests with the
 
 Contact
 
 field populated:
	1. Click
	 
	 Add condition
	 
	 . A new field appears.
	2. Select “
	 **Contact** 
	 ” in the
	 
	 Field
	 
	 field. Note that boolean fields cannot be used for setting up the condition since they are always deemed populated.
	3. Click the
	 
	 =
	 
	 and select
	 
	 is filled in
	 
	 in the drop-down menu.
3. Set up the action that triggers the needed business logic in the “
 
 THEN
 
 ” block of the business rule:
	1. Click
	 
	 Add action
	 
	 . In the action drop-down menu, select
	 
	 Set field value
	 
	 .
	2. Select the field to populate automatically in the
	 
	 Select field to populate
	 
	 field. For example,
	 
	 Mobile phone
	 
	 .
	3. Fill out the
	 
	 Specify the value to set
	 
	 field: click
	 ![btn_com_lookup.png](/docs/sites/en/files/images/NoCode_Customization/business_rules/btn_com_lookup.png)
	 ​​​​​​​ →
	 
	 Related objects
	 
	 →
	 
	 Contact
	 
	 →
	 
	 Mobile phone
	 
	 →
	 
	 Select
	 
	 .
4. Click
 
 Apply
 
 →
 
 Section Wizard
 
 →
 
 Save
 
 .




 Fig. 1 Setting the field value
 

![gif_chapter_business_rules_set_field_value.gif](/docs/sites/en/files/images/NoCode_Customization/business_rules/gif_chapter_business_rules_set_field_value.gif)


 As a result, if a user fills out the
 
 Contact
 
 field with a contact who has a mobile phone number, Creatio will populate the
 
 Mobile phone
 
 field of the request page with the corresponding number.
 



 Populate a field using a formula
----------------------------------



 You can use formulas when setting up the “Set field value” business rules. This enables you to implement custom calculation logic for numeric or date field values on record pages and populate such fields automatically.
 



 Using formulas for setting field values lets you implement advanced business logic, for example:
 


* calculate the product cost based on its price and the stock volume
* calculate the order sum in the base currency based on the current exchange rate and the order sum in the local currency
* calculate the actual duration of a task completion
* calculate the date of the next invoice payment, etc.



 Learn more about formulas in a separate article:
 [Formulas in business logic and pivot tables](https://academy.creatio.com/documents?id=2322) 
 .
 





 Example.
 
 Implement the following business logic for calculating the product price including tax: whenever the
 
 Tax rate
 
 field is populated in on a product page, the
 
 Price incl. tax
 
 field for this product is populated automatically.
 



1. Open the
 
 Products
 
 section and add a new business rule. Learn more about adding and setting up new business rules in a separate article:
 [Set up a new business rule](https://academy.creatio.com/documents?id=1680) 
 .
2. Specify the connection fields and set the condition that triggers the business rule in the “
 
 IF
 
 ” block of the business rule.
 


 Note.
 
 To use formulas with the date fields (e. g., for calculating the date difference), make sure both date fields are specified as “filled in” for the business rule. If one of the fields is not populated in Creatio, the business rule will not calculate the value.
 




 For example, to apply a “Price is filled in” and “Tax rate,% is filled in” rule to the product records with the
 
 Price
 
 and
 
 Tax rate, %
 
 fields populated:
 


	1. Click
	 
	 Add condition
	 
	 . A new field appears.
	2. Select “
	 **Price** 
	 ” in the
	 
	 Field
	 
	 field. Note that boolean fields cannot be used for setting up the condition since they are always deemed populated.
	3. Click
	 
	 =
	 
	 and select
	 
	 is filled in
	 
	 in the drop-down menu.
	4. Repeat the same settings for the
	 
	 Tax rate, %
	 
	 column.
3. Set up the action that triggers the needed business logic in the
 
 THEN
 
 block of the business rule:
	1. Click
	 
	 Add action
	 
	 . In the action drop-down menu, select
	 
	 Set field value
	 
	 .
	2. Select the field to populate automatically in the
	 
	 Select field to populate
	 
	 field. For example,
	 
	 Price incl. tax
	 
	 .
	3. Fill out the
	 
	 Specify the value to set
	 
	 field: click ​​​​​​​
	 ![formula_button.png](/docs/sites/en/files/images/NoCode_Customization/business_rules/formula_button.png)
	 →
	 
	 Formula
	 
	 → set up the formula in the
	 
	 Formula expression
	 
	 box that opens. Use the
	 
	 Parameter
	 
	 menu in the formula box to add numeric and date fields from the current page to your formula. For example, set up the formula for calculating the value in the
	 
	 Price incl. tax
	 
	 field based on the
	 
	 Price
	 
	 and
	 
	 Tax rate, %
	 
	 fields.
4. Click
 
 Apply
 
 →
 
 Section Wizard
 
 →
 
 Save
 
 .



 As a result, the
 
 Price incl. tax
 
 field on the product page will be populated with the calculated value automatically, if the
 
 Tax rate, %
 
 field value is populated.
 




 Fig. 2 Setting up a business rule for calculating a product price including tax
 

![gif_bus_rule_set_field_value_price2.gif](/docs/sites/en/files/images/NoCode_Customization/business_rules/gif_bus_rule_set_field_value_price2.gif)



 Similarly, you can set up a formula for calculating a time period. For example, calculate task duration based on its start and end time.
 




 Fig. 3 Setting up a business rule for calculating a time period using a formula
 

![gif_bus_rule_set_field_value_time_period.gif](/docs/sites/en/files/images/NoCode_Customization/business_rules/gif_bus_rule_set_field_value_time_period.gif)





