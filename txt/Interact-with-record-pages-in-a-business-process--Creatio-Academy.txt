


 Using the business process elements, you can open a new or existing record for editing.
 





 Example.
 
 Create a business process that the user can use to register a new opportunity, add a contract and then close the opportunity.
 




 To add records in the system section, use the
 
 Open edit page
 
 element. To implement this logic, you need to open a new opportunity page for the user to let them enter all the necessary information. Then you will need to open a new order page and fill its fields with data from the opportunity. Finally, the page of created opportunity must open so that the user can change the opportunity stage.
 








 Open a new record page
-----------------------------



 To create a new opportunity in the process workflow:
 


1. Create a new process and add the
 
 Open edit page
 
 element to it.
2. Populate the
 
 Open edit page
 
 element setup area (Fig. 1):
 





 Fig. 1
 

 The
 
 Open edit page
 
 element setup area
 

![scr_process_creation_designer_edit_page_param.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_UI/scr_process_creation_designer_edit_page_param.png)


	1. Enter element caption.
	2. In the
	 
	 Which page to open?
	 
	 field, select “Opportunity edit page“.
	3. In the
	 
	 Editing mode
	 
	 field, select the “Add new record“ option.
	4. To automatically populate the
	 
	 Name
	 
	 field on the opened new opportunity page, add it to the
	 
	 Which default values to set in the fields of new records?
	 
	 block.
	5. Populate the
	 
	 Recommendation for filling page
	 
	 and
	 
	 Hint for user
	 
	 fields.
	6. Populate the
	 
	 Hint for user
	 
	 field to further describe actions to be performed by a user.
	7. In the
	 
	 When is the element considered complete?
	 
	 field, select “Immediately after saving the record“.
3. Save the process.
 



 As a result, when the process item is initiated, a new opportunity edit page will open (Fig. 2).
 




 Fig. 2
 

 A new opportunity page displayed as part of a process workflow
 



![scr_process_creation_designer_edit_page_new_sale.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_UI/scr_process_creation_designer_edit_page_new_sale.png)








 Create a new connected record
------------------------------------



 As part of process workflow, you can add records to Creatio sections using process element parameter values.
 





 Example.
 
 After registering a new opportunity, the user must add an order for the opportunity. The fields on the new order page must be populated with the opportunity data.
 




 To set up default field values for a new order page:
 


1. Add the
 
 Open edit page
 
 element to the outgoing sequence flow of the “Add opportunity“ element (Fig. 3).
 





 Fig. 3
 

 Adding
 
 Open edit page
 
 element for order registration
 

![scr_process_creation_designer_edit_page_new_after_sale.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_UI/scr_process_creation_designer_edit_page_new_after_sale.png)
2. Populate the
 
 Open edit page
 
 element setup area (Fig. 4).
 





 Fig. 4
 

 Populating the element setup area
 

![scr_process_creation_designer_add_document_opportunities.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_UI/scr_process_creation_designer_add_document_opportunities.png)





 Note.
 
 Record Id (record identifier) is a unique code used to identify records in the database.
 



	1. Enter element caption.
	2. In the
	 
	 Which page to open?
	 
	 field, select “Order edit page“.
	3. In the
	 
	 Editing mode
	 
	 field, select the “Add new record“ option.
	4. In the
	 
	 Which default values to set in the fields of new records?
	 
	 click
	 
	 Add field
	 
	 .
	5. Select the
	 
	 Opportunity
	 
	 column (Fig. 5).
	 
	
	
	
	
	
	 Fig. 5
	 
	
	 Selecting the
	 
	 Opportunity
	 
	 column to populate on a new page
	 
	
	![scr_process_creation_designer_choose_opportunity.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_UI/scr_process_creation_designer_choose_opportunity.png)
3. In the parameter value menu, click
 
 Process parameter
 
 and select the
 
 Create opportunity
 
 element as the source of the parameter value.
4. In the right area of the parameter value window, select
 
 Record Id
 
 (Fig. 6).
 





 Fig. 6
 

 Selecting a record id of an earlier created record
 

![scr_process_creation_designer_edit_page_choose_source.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_UI/scr_process_creation_designer_edit_page_choose_source.png)
5. Click the
 
 Select
 
 button.
6. Save the process diagram.
   

 As a result, when this process item is executed, a new order record will be created. In the
 
 Opportunity
 
 field of the order the needed opportunity will be specified.








 Edit a record
--------------------



 You can open edit pages for existing records with the
 
 Open edit page
 
 element.
 





 Example.
 
 As part of the process workflow, the user must edit the opportunity that was created earlier.
 




 Use the
 
 Open edit page
 
 element to open edit page of a specific record.
 



 To open the opportunity edit page:
 


1. Add the
 
 Open edit page
 
 element to the outgoing sequence flow of the
 
 New document
 
 element (Fig. 7).
 





 Fig. 7
 

 Sale process
 

![scr_process_creation_designer_add_page_after_document.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_UI/scr_process_creation_designer_add_page_after_document.png)
2. Populate the element setup area (Fig. 8):
 





 Fig. 8
 

 Parameters on the element setup area for editing an existing record
 

![scr_process_creation_designer_page_elem_edit_source.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_UI/scr_process_creation_designer_page_elem_edit_source.png)


	1. Enter element caption.
	2. In the
	 
	 Which page to open?
	 
	 field, select “Opportunity edit page“.
	3. In the
	 
	 Editing mode
	 
	 field, select “Edit existing record“.
	4. Click the
	 
	 Record Id
	 
	 field and select
	 
	 Process parameter
	 
	 in the parameter value menu.
	5. In the parameter value window, select
	 
	 Create opportunity
	 
	 .
	6. In the right area of the parameter value window, select
	 
	 Record Id
	 
	 (Fig. 9).
	 
	
	
	
	
	
	 Fig. 9
	 
	
	 Selecting a record id of an earlier created record
	 
	
	![scr_process_creation_designer_edit_page_choose_ident_edit_source.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_UI/scr_process_creation_designer_edit_page_choose_ident_edit_source.png)
3. Click the
 
 Select
 
 button of the parameter value window.
4. Save the process diagram.
   

 As a result, the edit page of tie opportunity, which was created earlier by the “Add opportunity“ element will open.








 Manage item completion conditions
----------------------------------------



 In the opportunity business process covered above, the “Close opportunity” element will be completed once the opportunity record is saved.
 





 Example.
 
 To complete the “Close opportunity” process step, the user must actually close the opportunity by changing its stage to “Closed won” or “Closed lost”.
 




 Use the
 
 Open edit page
 
 element to specify conditions for its completion.
 



 To have the opportunity process (Fig. 10) end only if the opportunity is closed:
 





 Fig. 10
 

 Opportunity process
 

![scr_process_creation_designer_process_sales.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_UI/scr_process_creation_designer_process_sales.png)


1. Select the “Close opportunity” element on the process diagram.
2. On the element setup area, select the “If the record matches conditions” in the
 
 When is the element considered complete?
 
 field.
3. Use filter to specify conditions that the opened record must meet for the element to be completed. To complete the element if the opportunity is assigned certain stages, set up filter by the
 
 Stage
 
 field (Fig. 11).
 





 Fig. 11
 
 Setting up item completion conditions
 

![scr_process_creation_choose_filters_for_ending.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_UI/scr_process_creation_choose_filters_for_ending.png)
4. Save the process diagram.




