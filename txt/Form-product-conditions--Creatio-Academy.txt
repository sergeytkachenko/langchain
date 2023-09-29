


 In Creatio, a set of product details comprises the complete profile of a product. These details consist of:
 


* Customer parameters – requirements that the customer must meet to be able to purchase the product. Customer parameters include age limitations, working experience, etc.
* Product features – static parameters that characterize the product. Product features include product currency, early repayment, etc.
* Sales conditions – product details that change depending on each particular sale. For example, the interest rate for a 12-month loan will be different from that of an 18 months loan.
* Documents package – the list of documents that the customer must provide to purchase the product. For example, if a customer needs to provide an internal passport, an extract from a salary account, or other documents to purchase a banking product.
* Condition change criteria – additional conditions that can affect the product details. For example, condition change criteria include a positive credit history, which can justify decreasing the interest rate.



 Each record on the
 
 Product details
 
 detail is a separate set of conditions. A product can have multiple sets of conditions with different terms.
 



 Set up customer parameters
----------------------------



 This article covers the setup procedure for the customer’s parameters. For example, the customer has the following parameters:
 


* Age: 21 to 65 years.
* Residency status: resident.
* Employment status: has been employed for no less than 12 months with the current employer.
* Has been a resident for no less than 6 months.



 To specify the customer parameters:
 


1. Go to the [Products] section, create a new product, or open the needed product page.
2. Click the
 ![btn_chapter_mobile_wizard_new_role_1.png](/docs/sites/default/files/inline-images/btn_chapter_mobile_wizard_new_role_1.png)
 button on the [Product details] detail (Fig. 1).
 



 Fig. 1 – Adding a product condition
 

![Product condition page](/docs/sites/en/files/2020-11/scr_section_products_terms_and_conditions.png)
3. On the [Product details] page (Fig. 2) enter the start and end dates for the product conditions.
 



 Fig. 2 – Product condition page
 

![Product condition page](/docs/sites/en/files/2020-11/scr_section_products_new_terms_for_client.png)
4. Click the [Add parameter] button on the [Customer characteristics] tab.
5. Select “Male age, years“, for example, in the empty field (Fig 3.).
 

 Fig. 3 – Selecting characteristics
 

![Select age](/docs/sites/en/files/2020-11/scr_section_products_choose_women_age.png)



 As a result, the
 
 Male age, years
 
 field will appear on the
 
 Customer parameters
 
 tab.
6. Change the view of the value entry field to enter values:
	1. Place the cursor over the selected value.
	2. Click
	 ![btn_products_change_field.png](/docs/sites/default/files/inline-images/btn_products_change_field.png)
	 .
	3. Select [Value range (minimum/maximum)] (Fig. 4).
	 
	
	 Fig. 4 – Changing the field view
	 
	
	![Specify value range](/docs/sites/en/files/2020-11/scr_section_products_value_range.png)
	4. Enter the required range of values (Fig. 5).

 Fig. 5 – Specifying a value range
 

![Specify vallue range](/docs/sites/en/files/2020-11/scr_section_products_women_ages.png)
7. Click the [Add parameter] button. Select the [Resident] parameter, for example, and set the value to “Yes” (Fig. 6).
 

 Fig. 6 – Specifying a Boolean value
 

![Specify boolean](/docs/sites/en/files/2020-11/scr_section_products_client_resident.png)
8. Click the [Add parameter] button. Select the “Total work record” and specify ”12” in the field that appears to the right, for example (Fig 7).
 

 Fig. 7 – Specifying a fixed numeric value
 

![Specify fixed numeric](/docs/sites/en/files/2020-11/scr_section_products_total_years.png)
9. Add and fill in the parameters for residence in the same manner.
10. Click [Save].



 As a result, the specified customer parameters (Fig. 8) will apply when matching products to applications.
 




 Fig. 8 – Example of customer parameters
 

![Example of customer parameters](/docs/sites/en/files/2020-11/scr_section_products_clieent_characteristic.png)



 Set up product features
-------------------------



 Use the
 
 Product features
 
 tab to set up the static characteristics of a product (Fig. 9).
 




 Fig. 9 – An example of a product feature list
 

![Example of a product feature list](/docs/sites/en/files/2020-11/scr_section_products_products_features.png)



 For example, product features may include repayment conditions, currency, repayment schedule, etc.
   

 Creating a list of product features is identical to creating a list of the customer’s parameters as described above.
 



 Set up product opportunity conditions
---------------------------------------



 The
 
 Sales condition
 
 page is designed for setting up those product characteristics that change depending on the specifics of a sale, for example, the correlation between the interest rate and the term of the loan, special conditions for different customer categories, etc.
   

 Here we will set up an example of sales conditions for a loan product in which the interest rate depends on the customer segment, loan term, and amount.
 


1. Go to the [Products] section and open the needed product page.
2. Click the
 ![btn_chapter_mobile_wizard_new_role_1.png](/docs/sites/default/files/inline-images/btn_chapter_mobile_wizard_new_role_1.png)
 button on the [Product details] detail (Fig. 10).
 

 Fig. 10 – Adding a product condition
 

![Add product conditions](/docs/sites/en/files/2020-11/scr_section_products_terms_and_conditions_0.png)
3. Go to the [Sales conditions] tab.
4. Click the
 ![btn_chapter_mobile_wizard_new_role_1.png](/docs/sites/default/files/inline-images/btn_chapter_mobile_wizard_new_role_1.png)
 button on the [Sales conditions] tab (Fig. 11).
 

 Fig. 11 – Adding opportunity conditions
 

![Add opportunity conditions](/docs/sites/en/files/2020-11/scr_section_products_sales_conditions.png)
5. On the opened page:
	1. Enter the sales condition name, for example, “For corporate customers”.
	2. Click the [New parameter] button (Fig. 12).

 Fig. 12 – Creating opportunity conditions
 

![Create opportunity conditions](/docs/sites/en/files/2020-11/scr_section_products_add_new_parameter_condition.png)
6. In the appeared field select the “Customer segment” and specify the “Corporate customer” value for it (Fig. 13).
 

 Fig. 13 – Selecting a value
 

![Select customer value](/docs/sites/en/files/2020-11/scr_section_products_choose_corporate_clients.png)
7. Click the [Add parameter] button and select “Interest rate, yearly”.
8. Change the view of the value entry field to enter values:
	1. Place the cursor over the selected value.
	2. Click
	 ![btn_products_change_field_0.png](/docs/sites/default/files/inline-images/btn_products_change_field_0.png)
	 .
	3. Select [Table view] (Fig. 14).

 Fig. 14 – Selecting table view to create opportunity conditions
 

![Select table view](/docs/sites/en/files/2020-11/scr_section_products_client_group_table.png)



 As a result, the
 
 Interest rate, yearly
 
 parameter will switch to the table view (Fig. 15).
 




 Fig. 15 – Table view
 

![Table view](/docs/sites/en/files/2020-11/scr_section_products_table.png)
9. Select [Loan term, months] in the right part of the table (Fig. 16).
 

 Fig. 16 – Opportunity condition in a table view
 

![Opportunity condition in a table view](/docs/sites/en/files/2020-11/scr_section_products_create_table.png)
10. Specify the terms in months for which the loan can be granted in months (Fig. 17).
 

 Fig. 17 – Specifying the loan terms
 

![Specify the loan terms](/docs/sites/en/files/2020-11/scr_section_products_add_periods.png)
11. In the left part of the table, select the “Amount” value, and specify available ranges for the credit amount (Fig. 18).
 

 Fig. 18 – Formulating the credit amount ranges
 

![Formulate the credit amount ranges](/docs/sites/en/files/2020-11/scr_section_products_create_tables_summ.png)
12. Specify the interest rates for each intersection of the loan term and the amount (Fig. 19).
 

 Fig. 19 – Formulating interest rates that depend on the loan terms and amounts
 

![Formulate interest rates that depend on the loan terms and amounts](/docs/sites/en/files/2020-11/scr_section_products_create_table_percent.png)
13. Click the [Save] button to save the generated table of the opportunity conditions.



 As a result, opportunity conditions will be formed for the corporate customers of your bank (Fig. 20). For example, if a corporate customer applies for a loan of 300 000 USD for 12 months, the interest rate will be automatically set to 18%.
 




 Fig. 20 – Formulated product opportunity conditions
 

![Formulated product opportunity conditions](/docs/sites/en/files/2020-11/scr_section_products_table_finish.png)



 Set up the document package
-----------------------------



 Use the
 
 Documents package
 
 tab to set up the list of documents required for the product.
   

 The document package can be created automatically or manually. The automatic formulation of the document package is used if a standard document package is required for a product. You can set up the standard document package in the
 
 Product categories and types
 
 lookup.
   

 The document package is manually created if a customer must provide additional documents.
 


### 
 How to set the standard document package



 To enable automatic adding of standard documents to the
 
 Product details
 
 page, set up the
 
 Product categories and types
 
 lookup first. After this, select the
 
 Generate package
 
 item in the menu of the
 
 Documents package
 
 tab to add documents from the standard package to the product.
   

 To set up a document package:
 


1. Choose the relevant condition from the[Product details] detail and click the link in the name to go to its respective page.
2. Choose the [Document package] in the opened [Product details] page.
3. Click the
 ![btn_products_change_field_0.png](/docs/sites/default/files/inline-images/btn_products_change_field_0.png)
 button and select the [Generate package] command (Fig. 21).
 

 Fig. 21 – Adding a default document package for a product
 

![Add a default document package for a product](/docs/sites/en/files/2020-11/scr_section_products_document_package_automatic.png)



 As a result, the list of the documents that were set up in the
 [Product categories and types
 
 lookup](https://academy.creatio.com/docs/node/1733/) 
 for this product will be added to the
 
 Documents package
 
 tab (Fig. 22).
 




 Fig. 22 – Documents in the product document package
 

![Documents in the product document package](/docs/sites/en/files/2020-11/scr_section_products_list_of_documents.png)


### 
 Add documents manually



 Additional documents are added to the standard package manually. For example. a document certifying military obligation may be required for men below 27 years of age. Let's consider an example of adding an extract from salary accounts for clients who are employees of the bank. To do this:
 


1. On the product page, open the current product condition by clicking the link in the title. Click the
 ![btn_chapter_mobile_wizard_new_role_1.png](/docs/sites/default/files/inline-images/btn_chapter_mobile_wizard_new_role_1.png)
 button on the [Document package] tab of the [Product details] page (Fig. 23).
 

 Fig. 23 – Manually adding documents
 

![Add documents manually](/docs/sites/en/files/2020-11/scr_section_products_manual_package.png)
2. On the [Document in the package] (Fig. 24) page, enter the name of the document, for example, "Statement from the salary account".
 

 Fig. 24 – The [Document in package] page
 

![The [Document in package] page](/docs/sites/en/files/2020-11/scr_section_products_document_in_package.png)
3. Select the belonging group of the document, for example, "Income confirmation". The group list is set up in the [Document groups] lookup.
4. Select a product sale stage, at which the document must be submitted.
5. Select the role (“Borrower”, “Debtor”, “Warrantor”, etc.) who must submit the document.
6. Type of the document, e.g., “Customer document” or “Regulation”.
7. Select the document template if the document is a Creatio printable.
8. If the document is required and must be submitted during contracting, select the [Required] checkbox.
9. Configure the conditions in the filtering block. Create a filter by contact type. (Fig. 25). To do this, specify the "Contact“ object and the "Type” column in the filter column selection window.
 

 Fig. 25 – Using the quick filter example
 

![Quick filter example](/docs/sites/en/files/2020-11/scr_section_products_filters.png)
10. Click [Save].



 As a result, the document will be added to the
 
 Documents package
 
 detail. The document will be available only for individuals of the “Bank's client” type.
 



 Set up condition change criteria
----------------------------------



 The
 
 Condition change criteria
 
 tab of the
 
 Product details
 
 page contains additional criteria that can affect the sales conditions of the product. For example, the interest rate of a loan may be lowered if the customer has an exceptionally high credit score.
   

 Use the
 [Product categories and types
 
 lookup](https://academy.creatio.com/docs/node/1733/) 
 to set up the list of available criteria.
   

 To add condition change criteria to a product:
 


1. Go to the [Products] section and open the needed product page.
2. Click the
 ![btn_chapter_mobile_wizard_new_role_1.png](/docs/sites/default/files/inline-images/btn_chapter_mobile_wizard_new_role_1.png)
 button on the [Product details] tab.
3. Go to the [Condition change criteria] tab.
4. Click the
 ![btn_chapter_mobile_wizard_new_role_1.png](/docs/sites/default/files/inline-images/btn_chapter_mobile_wizard_new_role_1.png)
 button on the [Condition change criteria] detail of the [Product details] page.
5. Fill out the fields on the opened [Condition change criteria in the product conditions] page (Fig. 26).
 

 Fig. 26 – Example of the condition change criteria in a product
 

![Example of the condition change criteria in a product](/docs/sites/en/files/2020-11/scr_section_products_change_criteria.png)


	1. Select a value from the lookup in the [Change criteria] field.
	2. Enter the value for the criteria. For example, select the checkbox for Boolean criteria.
	3. In the [Variable parameter] field, select the product feature that is affected by the criteria. For example, select “Interest rate, per year.” The values are selected from the [Default feature] lookup.
	4. In the [Correcting value] field, enter the value by which the variable parameter value must be adjusted.
	   
	
	 To decrease the variable parameter value, enter the correcting value a preceding “-” character. Otherwise, the variable parameter value will be increased by the correcting value.
6. Click [Save].




