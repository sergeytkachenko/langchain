


 Creatio enables you to add an individual installment plan on the
 
 Order details
 




 You can populate the installment plan either manually or automatically, based on the previously added template. For example, if your company uses a product delivery scheme of 50% prepayment from the cost of the products in the order, you can
 
[set](#HT_faq_installment_plan_setup) 

 the corresponding template of the installment plan and use it on the order page.
 





 Populate the installment plan
---------------------------------



 Arrange the delivery and payment of goods at the stage of order processing. To do this:
 


1. Open the corresponding order page, go to the
 
 Order details
 
 tab.
2. On the
 
 Installment plan
 
 detail, click
 ![btn_chapter_mobile_wizard_new_role.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/btn_chapter_mobile_wizard_new_role.png)
 and select
 
 Add process step
 
 .
3. Populate each installment plan step:
 


	1. Type
	 
	 – “Delivery” or “Payment.”
	2. Name
	 
	 – specify the step name, for example, “Prepaid” or “Full delivery.”
	3. Deferment (days)
	 
	 – specify the number of days to calculate the obligation due date, starting from the date of the previous entry.
	4. Products
	 
	 – specify products to pay or deliver during this step. Click the link to open the product
	 
	[distribution window](#HT_faq_installment_plan_product_distribution) 
	
	 where you can edit the list of products for the current step.
	5. %
	 
	 – specify the expected delivery or payment amount in percentage.
	6. Invoice
	 
	 – select or
	 
	[add an invoice](/docs/8-0/user/sales_tools/short_sales_orders_and_invoices/create_an_invoice_shortcut/create_an_invoice#HT_faq_installment_plan_invoice) 
	
	 connected with the current step of the installment plan. The field is editable when the “Payment” step is selected.
4. Click
 ![btn_save_record.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/btn_save_record.png)
 to save the step values.
 



 The value of the
 
 Due date
 
 field is calculated automatically depending on the previous entry date and the number of deferment days.  The value of the
 
 Expected amount
 
 field is calculated as the amount of the remaining balance for payments and deliveries within the order.
 



 Set the actual dates and amounts as the order progresses. If you change the timeframe of an existing step, all timeframes of the subordinate steps will be recalculated automatically. Creatio will help calculate the expected amount within the entry as a remaining balance of the order payments and deliveries.







 Use the installment plan templates
----------------------------------------



 You can populate the
 
 Installment plan
 
 detail of the order page automatically based on the previously added template. There is a possibility to use a certain template by default or select one from the pre-set templates.
 





 Note.
 
 It is recommended to populate the installment plan for the orders with the formed list of products and services on the
 
 Products
 
 detail.
 



### 


 Set a template for the installment plan



 Use the
 
 Installment plan templates
 
 lookup to set the installment plan template.
 





 Case.
 
 For example, set up a template for a three-step installment plan:
 



1. 50% prepayment
2. Complete delivery of all items within 5 days
3. Payment of the remaining 50% on the next day after delivery.


1. Open the System Designer by clicking
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/btn_system_designer.png)
 in the top right corner of the application window.
2. Go to the
 
 System setup
 
 block –> click
 
 Lookups
 
 .
 





 Note.
 
 You can set up access rights to this action using the
 
 Access to “Lookups“ section
 

[system operation](https://academy.creatio.com/documents?product=administration&ver=7&id=258) 

 .
3. Select the
 
 Installment plan templates
 
 lookup and click the
 
 Open content
 
 button.
4. On the opened page, click the
 
 Add
 
 button.
5. Specify the caption of the new template, for example, “50% prepayment”.
6. Click the
 ![btn_chapter_mobile_wizard_new_role00001.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/btn_chapter_mobile_wizard_new_role00001.png)
 button of the
 
 Installment plan template steps
 
 detail.
 





 Note.
 
 The
 
[editable list](https://academy.creatio.com/documents?product=base&ver=7&id=1919) 

 is used on the
 
 Installment plan template steps
 
 detail.
7. Specify the parameters of the first step:
 


	1. Specify the “Payment“ step type.
	2. Specify the step caption, for example, “Prepaid“.
	3. Select the “Fixed date“ deferment type.
	4. Specify the payment of 50% of the total cost.
	5. Save the changes by clicking the
	 ![btn_save_record00002.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/btn_save_record00002.png)
	 button.
8. Add the second “Full delivery“ step and specify its parameters.
9. Add the third “Full payment“ step and specify its parameters.
 



 As a result of setting up the “50% prepayment” template, the
 
 Installment plan template steps
 
 detail will be shown as in
 [Fig. 1](#XREF_54886_1_50)
 .
 





 Fig. 1
 

 Example of the installment plan for the "50% prepayment" scheme
 

![faq_installment_plan_steps.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/faq_installment_plan_steps.png)



 You can set up several installment plan templates according to the working process of your company. For example, create a template for the 100% prepayment scheme with monthly payments during the year that can be implemented in several steps.
 


### 
 Use a default template



 To automatically generate an installment plan on the order page using a default template:
 


1. Open the System Designer by clicking
 ![btn_system_designer00003.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/btn_system_designer00003.png)
 in the top right corner of the application window.
2. Click
 
 System settings
 
 in the
 
 System setup
 
 block.
3. Open the page of the
 
 Default installment plan template
 
 system setting.
4. In the
 
 Default value
 
 field, select one of the previously configured templates that will be used on the order page by default.
 



 As a result, while adding a new order and saving the order page, the
 
 Installment plan
 
 detail will be automatically filled in according to the default template.


### 
 Select the template manually



 To manually add the installment plan on the order page using a selected template:
 


1. Go to the
 
 Orders
 
 section and open the required record.
2. On the
 
 Installment plan
 
 detail, click the
 ![btn_chapter_mobile_wizard_new_role00004.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/btn_chapter_mobile_wizard_new_role00004.png)
 button and select the required installment plan template from the list of available templates, for example, "50% prepayment" (
 [Fig. 1](#XREF_65182_2)
 ).
 





 Fig. 1
 

 Selecting the template for the installment plan auto-fill
 

![faq_installment_plan_action.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/faq_installment_plan_action.png)



 As a result, the
 
 Installment plan
 
 detail will be filled in automatically according to the selected template.
 



 To replace an existing installment plan template, select a template from the list (the
 ![btn_chapter_mobile_wizard_new_role00005.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/btn_chapter_mobile_wizard_new_role00005.png)
 button). As a result, the installment plan will be formed according to the new template on the
 
 Installment plan
 
 detail (previous installment plan will be deleted). If invoices have been issued based on the original installment plan steps, they will need to be connected to the corresponding steps of the new installment plan.
 


### 
 How the values are calculated when using a template



 Upon filling in the
 
 Installment plan
 
 detail of the order page using the template, the following automatic calculations are performed:
 


* The planned end date for each step is calculated against the current date with the number of deferment days specified in the template;
* If the
 
 Products
 
 detail has already been filled in previously on the order page, then the expected amount will be distributed by the steps according to the share and the total cost of the products specified in the template (
 [Fig. 1](#XREF_40997_3)
 ).





 Fig. 1
 

 Example of filling in the
 
 Installment plan
 
 detail using the template
 

![faq_installment_plan_detail.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/faq_installment_plan_detail.png)



 If needed, you can edit the detail manually, in this case, the values of the connected fields will be recalculated automatically. For example, upon changing the number of deferment days, the recalculation of the due date will take place and if you edit the percentage share of the payment or delivery, the expected amount will be redistributed (
 [Fig. 2](#XREF_46810_4)
 ).
 





 Fig. 2
 

 Example of rescheduling values on the
 
 Installment plan
 
 detail
 

![faq_installment_plan_detail_updated.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/faq_installment_plan_detail_updated.png)







 Distribute the products by the installment plan steps
-----------------------------------------------------------



 The product distribution for the last step of the installment plan is automated in Creatio. Also, you can quickly add products to the installment plan step manually directly from the
 
 Installment plan
 
 detail list.
 



 Upon populating the installment plan via a template, Creatio will add products to the installment plan in two cases:
 


* If the step of this type is the only one. For example, 100% prepayment. In this case, all products added to the order will be included in this step.
* If the step of this type is the only one for which the products are not added. For example, if the delivery takes place during two iterations and you have added the required products manually for the first step of the delivery, the rest of the products will be distributed automatically for the second step.



 Otherwise, you will need to add the products manually. To do this:
 


1. Go to the
 
 Orders
 
 section and open the required record with the generated list of products.
2. Populate the
 
 Installment plan
 
 detail on the order page. You can populate the
 
 Installment plan
 
 detail automatically using the pre-set template.
3. To add products to the list available on this step, click
 
 Add
 
 in the
 
 Products
 
 column (
 [Fig. 1](#XREF_32236_5)
 ).
 





 Fig. 1
 

 Adding products to the installment plan step
 

![faq_installment_plan_add_products.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/faq_installment_plan_add_products.png)



 As a result, an additional product distribution window (
 [Fig. 2](#XREF_88160_6)
 ) will open. Select the products and enter their quantity.
 





 Fig. 2
 

 Product distribution window
 

![faq_installment_plan_product_distribution_window.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_installment_plan/faq_installment_plan_product_distribution_window.png)



 The products that were added on the
 
 Products
 
 detail of the order page are available in the list.
 



 The
 
 Available
 
 field value is based on the total number of the product items specified on the
 
 Products
 
 detail of the order page. If some of the products have been distributed at the previous steps of the installment plan, this value is subtracted from the total number of products in the order and the result is displayed in the
 
 Available
 
 column. The number of products at the step can not exceed the total number of products available.
 



 The total cost of the specified number of products is calculated automatically based on the price per unit and the number of products.
 




