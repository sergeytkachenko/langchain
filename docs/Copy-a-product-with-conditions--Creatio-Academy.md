


 You can quickly make a new set of complex product conditions by copying an existing set:
 


* Make a new set of conditions for a product based on the existing set. Only users with permission to add new records in the [Product conditions] detail can copy product conditions.
* Add a new product based on an existing one and keep its set of conditions. Only users with permission to add new records in the [Products] section and the [Product conditions] detail can copy product conditions.



 Copy the conditions of the current product
--------------------------------------------



 To do this (Fig. 1):
 




 Fig. 1 – Copying product conditions
 


![Copying product conditions](/docs/sites/en/files/2020-11/gif_specs_products_copy_conditions_bank.gif)



1. Open the [Products] section.
2. Open the page of the product that has the needed set of conditions.
3. Select the sets of conditions to copy in the [Product conditions] detail list. You can copy any of the sets available on the detail, including sets that are not current.
4. Click
 
![btn_email_menu.png](/docs/sites/default/files/inline-images/btn_email_menu.png)

 → [Copy]. Note that only conditions with a specified end date can be copied. A product can only have one set of current conditions at a time. As a result, all data on this detail will be copied except for the [Start date] and [End Date] fields.
5. On the record page, specify the start date for the set of conditions. The dates in the new sets of product conditions must not overlap with the dates of the existing sets of that product.
6. Edit the conditions if necessary.
7. Save the record.



 Create a new product based on an existing product
---------------------------------------------------



 You can quickly create new products by copying existing products along with their conditions (Fig. 2):
 




 Fig. 2 – Copying the product and the set of conditions
 


![Copying the product and the set of conditions](/docs/sites/en/files/2020-11/gif_specs_products_copy_product_bank.gif)



1. Open the [Products] section.
2. Open the section list and select the product to copy.
3. Click [Copy] on the record page toolbar.
	1. Click [No] in the popup box to copy the product without the product’s conditions.
	2. Click [Yes] to copy both the product and the product conditions.
	   
	
	 As a result, Creatio will copy the current conditions, the conditions whose start date is yet to come, and all data on the [General info] tab of the product page except for the status, start date, and end date. Creatio will also not copy the conditions whose start date has come. By default, the new product will be assigned the “In progress” status. You can change the status that is automatically assigned to new products in the “Product default status” system setting (“ProductStatusDef”). We do not recommend designating the “Current” status as default. A newly created or copied product may not be ready for immediate use.
4. Edit the copied product and product conditions and specify the start date.
5. Click [Save].




