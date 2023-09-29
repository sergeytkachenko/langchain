


 Use the
 
 Contracts
 
 section to manage the contracts that you sign with the customers as part of closing a sales deal.
 



 The section stores information about contract parties, purchase amount, addenda and specifications, scan copies, current status and links to other records, e.g., opportunities and documents.
 



 To create a contract:
 


1. Go to the
 
 Contracts
 
 section.
2. Click the
 
 New contract
 
 button.
   

 A new contract page opens, with the automatically generated contract number. Creatio generates document numbers according to the  “ContractCodeMask”
 
[system setting](https://academy.creatio.com/documents?product=administration&ver=7&id=269) 

 . A new document page will have the following default values in its fields:
 


	1. Type
	 
	 – select “Contract.” This value cannot be changed after you save the new record.
	2. Start date
	 
	 – the user’s current date.
	3. Owner
	 
	 – the current user’s contact.
	4. Status
	 
	 – the default status for all new contracts is “Draft.” The field uses the
	 
	 Contract statuses
	 
	 lookup.
3. Account
 
 – specify the customer’s account. Tis is the other party of the contract.
4. Account's banking details
 
 – customer’s payment details. You can select data from the
 
 Banking details
 
 detail of the
 
 Account info
 
 tab on account page.
5. Our company
 
 – the account that represents your party in the contract. You can select from accounts of the “Our company” type.
6. Our banking details
 
 – the field unlocks once you populate the
 
 Our company
 
 field. You can select data from the
 
 Banking details
 
 detail of the
 
 Account info
 
 tab on your company page.
7. Amount
 
 – specify the contract currency and amount. If a contract is added based on an order, the
 
 Amount
 
 field value is calculated automatically and reflects the total cost of the ordered products. You can select only those ordered products you need to connect to the contract. Read more in the “
 
[Create a contract from an order](/docs/8-0/user/sales_tools/short_sales_orders_and_invoices/create_a_contract/create_a_contract_from_an_order) 

 ” article.
8. Add links to other connected records on the
 
 Connected to
 
 detail.
9. Add subsequent agreements, addenda or specifications to the
 
 Subordinate contracts
 
 detail. Only contract records with the “Specification” and “Addendum” types are available on the
 
 Subordinate contracts
 
 detail.
   

 To add a
 **new** 
 subordinate contract, click the
 ![btn_com_add_tab.png](/guides/sites/en/files/documentation/user/en/document_flow/BPMonlineHelp/document_flow_create_contract/btn_com_add_tab.png)
 button. The
 
 Parent contract
 
 field on the subordinate contract page will be populated automatically.
   

 To connect an
 **existing** 
 subordinate contract to the current contract, click the
 ![btn_com_roles_actions_menu.png](/guides/sites/en/files/documentation/user/en/document_flow/BPMonlineHelp/document_flow_create_contract/btn_com_roles_actions_menu.png)
 button and select the “Connect to existing” option from the menu.
10. If there are orders linked to the contract, go to the
 
 Contract details
 
 tab and link the products sold. When adding a contract based on an order, you can select several ordered products. The selected products will be automatically added to the
 
 Products
 
 detail of the
 
 Contract details
 
 tab. Click the
 ![btn_com_add_tab00001.png](/guides/sites/en/files/documentation/user/en/document_flow/BPMonlineHelp/document_flow_create_contract/btn_com_add_tab00001.png)
 button to add the rest of ordered products.
11. If you need to approve a contract, for example, agree upon its terms with other employees, use Creatio approvals. As part of the standard approval procedure, an “approver” employee sets the approval result (approved or rejected). Approving contracts is identical to approving orders and invoices. Working with approvals is covered in the “
 
[Approvals](/docs/8-0/user/platform_basics/communications/approvals_shortcut/approvals) 

 ” article.
12. Click
 
 Save
 
 .




