


 Add a Creatio contract from an order and automatically transfer ordered products to the contract, completely or selectively.
 



 To do this:
 


1. Go to the
 
 Contracts
 
 section.
2. Click the
 
 New contract
 
 button.
3. Fill out the following required fields:
 


	1. Account
	2. Our company
4. Make sure the values of the following automatically populated fields are relevant:
 


	1. Type
	2. Status
	3. Start date
5. Go to the
 
 Order
 
 field and specify the order whose products to add to the contract.
6. Click the
 
 Save
 
 button. This will open a dialog box.
7. Select the needed option in the box (Fig. 1).
 




 Fig. 1 Create a contract based on an order
 

![contract_create.png](/docs/sites/en/files/images/Sales_Tools/create_contract/contract_create.png)


	* All
	 
	 : the
	 
	 Contract details
	 
	 tab on the contract page will display all products connected to the order.
	* Select
	 
	 : this will open another box. Select products to transfer to the contract.



 As a result, Creatio will open the page of the new contract, populated with additional order page data:
 


1. The
 
 Account
 
 ,
 
 Contact
 
 ,
 
 Owner
 
 fields use the values of the corresponding order page fields.
2. The values of the
 
 Amount
 
 ,
 
 Amount, base currency
 
 fields are calculated as the total cost of the transferred products.
3. The
 
 Order
 
 field displays the number of the connected order.



 Also, Creatio generates the contract number on the contract page automatically based on the “Contract number mask” (the “ContractCodeMask” code) system setting. The
 
 Start date
 
 field is populated using the current date, the
 
 Type
 
 field is set to “Contract,” and the
 
 Status
 
 field is set to “Draft.”
 




