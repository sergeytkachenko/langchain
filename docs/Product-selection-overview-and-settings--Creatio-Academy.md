


 The product selection functionality enables customer assistants to speed up their workflow, as well as to customize and streamline the request-based search for suitable offers. You can use the base version of Creatio product selection or integrate it into any business logic. For example, use it in business processes or consulting cases for contacts, and opportunities for legal entities.
 



 To work with product selection:
 


1. Set up the
 **product catalog** 
 . This will enable the customer assistant to present the products of your bank to the customers better.
 


	1. [Establish the product categories and types](/docs/8-0/user/finance_and_banking/financial_products/product_catalog_finance/product_categories_and_types/form_bank_product_categories_and_types) 
	 .
	2. [Form the product conditions](/docs/8-0/user/finance_and_banking/financial_products/product_catalog_finance/product_conditions/form_product_conditions) 
	 .
	3. [Add the product descriptions](/docs/8-0/user/finance_and_banking/financial_products/product_catalog_finance/product_description/add_product_selection_description) 
	 .
2. Set up
 **sales of the selected product** 
 . This will save time on filling out the applications (for contacts) or opportunities (for legal entities). To register a product sale, set up a business process for creating an application or an opportunity to which to pass the product data using parameters, and specify it in the “Process for registration selected product” (“SelectedProductRegistrationProcess” code)
 [system setting](/docs/7-17/user/setup_and_administration/system_settings_and_lookups/system_setting_reference/description_of_system_settings#title-1880-35) 
 . This process will run when the user initiates the product selection via the
 
 Products
 
 section’s action.
3. Create a
 **business process or case** 
 with the selection of products and the subsequent creation of an application or opportunity set up. Enable the assistants to run the process from any Creatio section (optional). This will let you include product selection in your bank’s processes. For example, consultations with contacts or presentations for legal entities. The process should take into account not only product selection but also subsequent application. In this case, Creatio will process the selection results based on the custom business logic regardless of the value of the “Process for registration selected product” (“SelectedProductRegistrationProcess” code) system setting. Learn more:
 [Set up a product selection process](/docs/8-0/user/finance_and_banking/financial_products/product_selection_finance/example_process/set_up_a_product_selection_business_process) 
 .



 The product selection functionality is ready for use right after the setup. Learn more:
 Select a bank product
 .
 



 You can personalize the product selection using
 **product recommendations** 
 . In that case, the AI tools will predict the offers with the highest conversion potential.
 



 The recommendation prediction setup consists of the following steps:
 


1. Set up the recommendation prediction model. This will let you select products the customer is the most likely to purchase based on the information about the previous deals.
2. Configure a prediction business process. This will let you update the recommendation data regularly.



 Learn more:
 [Bank product recommendations (Next Best Offers)](/docs/8-0/user/finance_and_banking/financial_products/product_selection_finance/recommendations_next_best_offers/next_best_offers) 
 .
 




