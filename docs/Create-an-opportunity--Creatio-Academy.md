


 Manage all Creatio opportunities in the
 
 Opportunities
 
 section. Handle an opportunity from the moment the customer shows interest in cooperation up to closing the deal.
 



 The section includes several
 [quick filters](/docs/8-0/user/platform_basics/business_data/filters_shortcut/filters#title-1755-1) 
 .
 


* **By closing date** 
 (the
 
 Closed on
 
 field) – displays opportunities closed within the specified period. To view the opportunities closed on a specific day, set the day as both the start and the end date.
* **By owner** 
 (the
 
 Owner
 
 field) – displays opportunities owned by the selected contact.



 Create opportunities
 **manually** 
 or work with opportunities created
 **automatically** 
 when a lead is transferred to the “Awaiting sale” stage.
 



 Add an opportunity manually
-----------------------------



 Fill out several required fields on the mini page to add an opportunity. Then you can run the corporate sales process and enter the information on each opportunity stage gradually by following Creatio's tips.
 



 To register an opportunity:
 


1. Create a new record in the
 
 Opportunities
 
 section.
2. Fill out the required fields in the mini page:
 


	1. Specify the potential customer for whom the opportunity is created. In the
	 
	 Customer
	 
	 field, you can select a value from the existing contacts and accounts. Start entering the keyword to search for a record.
	2. In the
	 
	 Name
	 
	 field, enter the keywords to identify the record, e. g., customer name or need type.
	3. Fill out the
	 
	 Need type
	 
	 field to specify the product category of your company in which a customer is interested.
	4. In the
	 
	 Budget
	 
	 field, specify the approximate sum that the customer is ready to spend.
	5. In the
	 
	 Stage
	 
	 field, Creatio specifies “Qualification” as the first stage of the corporate opportunity handling process. You can specify a different stage if needed.
3. Save the page.
 



 As a result, a new opportunity will be added to the system. Now you can
 
[start the corporate sales process](/docs/8-0/user/sales_tools/long_sales/corporate_sale_process_shortcut/corporate_sale_process) 

 on the opportunity. If you have the “Create lead for opportunity” (“CreateLeadForOpportunity” code)
 
[system setting](/docs/7-17/user/setup_and_administration/system_settings_and_lookups/system_setting_reference/description_of_system_settings) 

 enabled, Creatio will automatically create a connected lead.



 Add an opportunity automatically
----------------------------------



 If you have the “Run opportunity process” (“StartOppBusinessProcess” code) system setting enabled, Creatio will register the opportunity automatically when you
 **advance the lead** 
 to the “Awaiting sale” stage.
 



 The corporate sales process will run automatically on the opportunity.
 



 Creatio will populate the following fields:
 


* The
 
 Name
 
 field value will be formed as a concatenation of the following values on the opportunity page:
 
 Customer
 
 / [Number of registered opportunities +1].
* Creatio will copy the list of products from the lead page to the opportunity.
* The following fields will be populated in Creatio Sales:
 
 Customer
 
 ,
 
 Customer budget
 
 ,
 
 Owner
 
 ,
 
 Need type
 
 ,
 
 Closing date
 
 and
 
 Direction
 
 .
* The following fields will be populated in Creatio Financial Service:
 
 Customer
 
 ,
 
 Department
 
 ,
 
 Owner
 
 and
 
 Created on
 
 fields as well as a number of fields on the
 
 Parameters
 
 detail.



 You can open the created opportunity from the lead page:
 
 Opportunity info
 
 →
 
 Opportunity/Order
 




 Set up a dynamic folder to track the new opportunities. For example, filter the opportunities by the creation date.
 




