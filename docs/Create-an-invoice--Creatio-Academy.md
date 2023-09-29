


 In Creatio, you can add and issue invoices. Invoices contain information about the customer, supplier, connected contract as well as the products in the order, the order amount, and the payment conditions. Aside from creating an invoice manually, you can automatically add an invoice based on an order - both for all its products in general, and for specific steps of the installment plan based on payment.
 



 Use the
 
 Invoices
 
 section to work with invoices. The section supports the following
 
[quick filters](https://academy.creatio.com/documents?product=base&ver=7&id=1232) 

 :
 


* By invoice issue date (the
 
 Date
 
 field of the invoice page).
* By owner (the
 
 Owner
 
 field of the invoice page).





 Create an invoice from the [Invoices] section
-------------------------------------------------


1. Open the
 
 Invoices
 
 section.
2. Click
 
 New invoice
 
 .
   

 As a result, a page with the invoice number will open. The number is generated in accordance with the “Invoice number mask” system setting  (InvoiceCodeMask).
3. Specify the customer to whom the invoice is issued in the
 
 Customer
 
 required field. In the field, you can select a value from the existing contacts and accounts.
4. The
 
 Customer details
 
 field becomes available if the customer account is selected on the invoice page. If the selected company has only one record on this detail, then the
 
 Banking details
 
 field will be automatically filled in with that data.
5. In the
 
 Supplier
 
 field, specify the company that is the source of the invoice.
6. The
 
 Amount
 
 field value features the total cost of the ordered products calculated automatically. The field is editable if the
 
 Products
 
 details has no records. The amount can be specified in any currency.
7. On the
 
 Payment
 
 detail, specify the order payment status, either planned or actual.
8. Add other records relevant to the record on the
 
 Connected to
 
 detail.
9. Select the
 
 Owner
 
 checkbox in the
 
 Reminders
 
 detail to create a reminder for the owner of the invoice. The reminder will be displayed on the
 
[communication panel](https://academy.creatio.com/documents?product=base&ver=7&id=1011) 

 when the specified point in time is reached.
10. Add the list of goods and services included in the order on the
 
 Products
 
 detail. There are several methods of doing this:
 


	1. Click
	 ![btn_com_add_tab.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_create_invoice/btn_com_add_tab.png)
	 to open the product selection page.
	2. Click
	 
	 Add
	 
	 in the detail action menu.
	 
	
	
	
	 If necessary, add a discount on specific products in the
	 
	 Discount,%
	 
	 field. Learn more in the “
	 
	[Add products to an invoice or an order](/docs/8-0/user/sales_tools/short_sales_orders_and_invoices/add_products/add_products_to_an_invoice_or_an_order#HT_specs_orders_product_selection) 
	
	 ” article.
11. If you need to agree and approve an invoice (e.g., approve invoice amount with managers), use Creatio approvals. To do this, use the
 
 Send for approval
 
 action on the invoice page. As a result, a page will open. Use it to select an employee to send the invoice to and define other approval parameters.
   

 More information about this feature is available in the “
 
[Approvals](/docs/8-0/user/platform_basics/communications/approvals_shortcut/approvals) 

 ” article.





 Issue an invoice based on an order
--------------------------------------



 To create an invoice based on an order:
 


1. Go to the
 
 Orders
 
 section and open the required record.
2. Select the
 
 New invoice based on this order
 
 action from the
 
 Actions
 
 menu (
 [Fig. 1](#XREF_24126_1)
 ).
 





 Fig. 1
 

 Adding contract based on order
 

![action_create_invoice_.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_create_invoice/action_create_invoice_.png)



 As a result, the page with the invoice created based on the order will open. The fields will be populated using the order data like this:
 


1. The
 
 Products
 
 detail is filled with all products from the corresponding detail of the order.
2. The
 
 Customer
 
 and
 
 Owner
 
 fields are filled in with the values from the corresponding fields from the order page.
3. The
 
 Amount
 
 ,
 
 Amount, base currency
 
 values of the invoice page are calculated as the total cost of the products.
4. The number of the connected order is displayed in the
 
 Order
 
 field.
 



 Also, the invoice number is generated automatically on the contract page according to the “Invoice number mask” system setting (InvoiceCodeMask). The
 
 Start date
 
 field is filled in with the current date, the
 
 Payment status
 
 field will contain “Draft” and the
 
 Supplier
 
 field is filled in with the "Our company" account type.













 Issue an invoice based on a payment in the order
------------------------------------------------------------



 Add an invoice automatically based on any step of the order installment plan with the “Payment“ type in Creatio. To do this:
 


1. Go to the
 
 Orders
 
 section and open the required record with the populated
 
 Installment plan
 
 detail.
 





 Note.
 
 Learn more about creating an order installment plan in the “
 
[Add an order installment plan](/docs/8-0/user/sales_tools/short_sales_orders_and_invoices/installment_plan/add_an_order_installment_plan#HT_specs_orders_products_page) 

 ” article.
2. Click the
 
 Order details
 
 tab.
3. Select the needed step with the “Payment“ type and click
 ![btn_com_lookup.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_create_invoice/btn_com_lookup.png)
 in the
 
 Invoice
 
 column.
   

 In the opened lookup window, issue a new invoice for an installment plan step (
 [Fig. 1](#XREF_98792_7)
 ) or bind an installment plan step to an existing connected invoice.
 





 Fig. 1
 

 Adding an invoice
 

![faq_installment_plan_create_invoice.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_create_invoice/faq_installment_plan_create_invoice.png)



 After adding an invoice, a link with the invoice number will be displayed in the detail list. Click the link to open the invoice page (
 [Fig. 2](#XREF_23497_8)
 ).





 Fig. 2
 

 Opening the invoice page
 

![faq_installment_plan_created_invoice.png](/guides/sites/en/files/documentation/user/en/short_sales/BPMonlineHelp/short_sales_create_invoice/faq_installment_plan_created_invoice.png)



 An invoice page that was added based on the data from the installment plan step is filled in automatically with the following data from the order page:
 


1. If you add products to an installment plan step, they will be automatically added to the
 
 Products
 
 detail of the corresponding invoice.
2. The value in the
 
 Amount
 
 field on the invoice page can be calculated in two ways:
 


	1. If the products were not added at the corresponding step, the
	 
	 Amount
	 
	 field of the invoice page will be populated with the corresponding value from the
	 
	 Expected amount
	 
	 field from the installment plan step.
	2. If the products were not added at the corresponding step, the
	 
	 Amount
	 
	 field of the invoice page will be calculated as the total cost of the selected products.
3. The
 
 Customer
 
 and
 
 Owner
 
 fields are filled in with the values from the corresponding fields from the order page.
4. The number of the connected order is displayed in the
 
 Order
 
 field.
 



 Also, the invoice number is generated automatically on the contract page according to the pre-configured mask. The
 
 Start date
 
 field is filled in with the current date, the
 
 Payment status
 
 field will contain “Draft” and the
 
 Supplier
 
 field is filled in with the "Our company" account type.




