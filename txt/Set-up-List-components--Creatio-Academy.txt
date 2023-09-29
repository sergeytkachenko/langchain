


 Use
 
 List
 
 components to display list of any object's records and filter the records if needed.
 



 Set up a list that displays request records
---------------------------------------------





 Example.
 
 Set up the
 
 List
 
 component that displays request records on the page. Enable users to add new records using a mini page and view existing records using a full page. Create dedicated pages for external users. Connect the list to the
 
 Search
 
 component.
 





 Fig. 1 Set up a
 
 List
 
 component that displays request records
 

![scr_list_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_list_setup_area.png)


1. Add and set up the
 
 Search
 
 component.
2. Drag a
 
 List
 
 component to the canvas and open the component setup area
3. Select the list data source in the
 
 Object
 
 parameter or click
 ![icn_add_filter.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_add_filter.png)
 next to the parameter to add a new data source. For this example, select “Requests.”
4. Click the
 ![icn_form_page.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_form_page.png)
 button next to the
 
 Object
 
 parameter and set up the form pages to use together with the data source.
 


	1. Select the page that displays existing records in the
	 
	 Default page
	 
	 parameter or click
	 ![icn_add_filter.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_add_filter.png)
	 next to the parameter to add and set up a page. For this example, select the “Requests form page” page.
	2. Select the page that displays new records in the
	 
	 Add page
	 
	 parameter or click
	 ![icn_add_filter.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_add_filter.png)
	 next to the parameter to add and set up a page. For this example, add and set up the “Requests mini page” mini page based on the “Mini page” template.
	3. Click
	 
	 Pages setup for external users
	 
	 . This opens page parameters for external users.
	4. Click
	 ![icn_add_filter.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_add_filter.png)
	 next to the
	 
	 Default page
	 
	 parameter for external users to add and set up the “Requests form page for external users” page.
	5. Click
	 ![icn_add_filter.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_add_filter.png)
	 next to the
	 
	 Add page
	 
	 parameter for external users to add and set up the “Requests mini page for external users” page.
	6. Click
	 
	 Save
	 
	 .
5. Click
 ![icn_add_filter.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_add_filter.png)
 next to the
 
 Apply filter by page data
 
 parameter to filter list data by page data source,
 
 Approvals list
 
 ,
 
 Attachment list
 
 , or another
 
 List
 
 component. For this example, do not set up these filters. Learn more about setting up filters by page data in a different section:
 [Set up a [List] component that displays data of record approver contacts](#title-2761-2) 
 .
6. Click
 ![icn_add_filter.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_add_filter.png)
 next to the
 
 Apply pre-configured filter
 
 parameter → the
 
 Search
 
 component.
7. Click
 
 Setup filter
 
 to set up a static filter that is always applied to the list. The filter setup process is similar to classic UI. Learn more in a separate article:
 [Advanced filter](https://academy.creatio.com/documents?id=1017#title-1755-10) 
 . For this example, do not set up the static filter.
8. Clear the
 
 Row numbers
 
 checkbox to make the list rows unnumbered. For this example, leave the checkbox selected.
9. Clear the
 
 Multiselect
 
 checkbox to make the users unable to bulk select list records. For this example, leave the checkbox selected.
10. Clear the
 
 Inline editing
 
 checkbox to make the users unable to edit record data directly in the list. For this example, leave the checkbox selected.
11. Clear the
 
 Inline adding records
 
 checkbox to make the users unable to add new records directly in the list without opening a separate page. For this example, leave the checkbox selected.
12. Click the
 ![btn_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_visible.png)
 or
 ![btn_not_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_not_visible.png)
 button in the
 
 Visibility
 
 group to make the component visible or invisible by default on the page, respectively. For this example, leave the component visible.
13. Click
 
 Setup conditions
 
 in the
 
 Visibility
 
 group to set up element business rules. For this example, do not add business rules. Learn more about setting up business rules in a separate article:
 [Set up business rules](https://academy.creatio.com/documents?id=2409) 
 .
14. View the unique component code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar components on the page. For this example, leave the code as is.



 As a result, Creatio will add the
 
 List
 
 component that displays request records. Users will be able to add new records using a mini page and view existing records using a full page. External users will use dedicated pages. The
 
 Search
 
 component will be connected to the list.
 



 Set up a list that displays data of record approver contacts
--------------------------------------------------------------





 Example.
 
 Set up the
 
 List
 
 component that increases the transparency of request approval workflow by displaying data of record approver contacts.
 





 Fig. 2 Set up a
 
 List
 
 component that displays data of record approver contacts
 

![scr_filtered_list_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_filtered_list_setup_area.png)


1. Add and set up
 
 Approvals
 
 and
 
 Approvals list
 
 components.
2. Configure a business process that approves requests. Learn more about configuring approval processes in a separate article:
 [Configure a document approval process](https://academy.creatio.com/documents?id=2363) 
 .
3. Drag a
 
 List
 
 component to the canvas and open the component setup area
4. Select “Contact” in the
 
 Object
 
 parameter.
5. Filter the list data by the
 
 Approvals list
 
 component:
 


	1. Click
	 ![icn_add_filter.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_add_filter.png)
	 next to the
	 
	 Apply filter by page data
	 
	 parameter. This brings up new parameters.
	2. Select the
	 
	 Approvals list
	 
	 component in the
	 
	 Data source
	 
	 parameter.
	3. Click the
	 ![icn_list_filter.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_list_filter.png)
	 icon next to the
	 
	 Approval
	 
	 parameter →
	 
	 Related objects
	 
	 →
	 
	 Approver
	 
	 →
	 
	 Related objects
	 
	 →
	 
	 Contact
	 
	 →
	 
	 Id
	 
	 checkbox →
	 
	 Select
	 
	 .
	4. Select
	 
	 Id
	 
	 in the
	 
	 Contact
	 
	 parameter.
6. Click
 ![icn_add_filter.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_add_filter.png)
 next to the
 
 Apply pre-configured filter
 
 parameter to connect the list to filter components, for example,
 
 Search
 
 . For this example, do not connect the list to filter components.
7. Click
 
 Setup filter
 
 to set up a static filter that is always applied to the list. The filter setup process is similar to classic UI. Learn more in a separate article:
 [Advanced filter](https://academy.creatio.com/documents?id=1017#title-1755-10) 
 . For this example, do not set up the static filter.
8. Clear the
 
 Row numbers
 
 checkbox to make the list rows unnumbered. For this example, leave the checkbox selected.
9. Clear the
 
 Multiselect
 
 checkbox to make the users unable to bulk select list records. For this example, leave the checkbox selected.
10. Clear the
 
 Inline editing
 
 checkbox to make the users unable to edit record data directly in the list. For this example, leave the checkbox selected.
11. Clear the
 
 Inline adding records
 
 checkbox to make the users unable to add new records directly in the list without opening a separate page. For this example, leave the checkbox selected.
12. Click the
 ![btn_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_visible.png)
 or
 ![btn_not_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_not_visible.png)
 button in the
 
 Visibility
 
 group to make the component visible or invisible by default on the page, respectively. For this example, leave the component visible.
13. Click
 
 Setup conditions
 
 in the
 
 Visibility
 
 group to set up element business rules. For this example, do not add business rules. Learn more about setting up business rules in a separate article:
 [Set up business rules](https://academy.creatio.com/documents?id=2409) 
 .
14. View the unique component code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar components on the page. For this example, leave the code as is.



 As a result, Creatio will add the
 
 List
 
 component that increases the transparency of request approval workflow by displaying data of record approver contacts.
 




