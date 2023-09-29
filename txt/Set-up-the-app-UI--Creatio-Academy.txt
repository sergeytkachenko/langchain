


 A newly-created app already contains a particular set of components that depends on the selected template. For example, Creatio adds elements that display analytics from the “Dashboards” template and list page and record page that have a minimum set of components from the “Records & business processes” template. Configure the app further in the No-Code Designer.
 



 Creatio displays editable apps in the Application Hub. Click
 ![btn_system_designer.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/btn_system_designer.png)
 in the top right to open it (Fig. 1).
 




 Fig. 1 The Application Hub
 

![add_new_app_2.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/add_new_app_2.png)



 You can also
 [create](https://academy.creatio.com/documents?id=2377) 
 a new app or
 [install](https://academy.creatio.com/documents?id=1836) 
 an existing app here.
 



 When you edit an app created using the Freedom UI, you can modify the general information of the app: name, description, and icon.
 



 This article covers the UI setup using the app for employee payroll management as an example.
 





 Example.
 
 Set up the UI of the “Payroll” section in the “Financial benefits” app. The section must contain a list page and form page.
 



 On the list page, configure the set of columns to display, as well as section folders.
 



 Add input fields, expansion panels, tabs, buttons, labels, and dashboards to the form page.
 



 Calculate the benefits using a business process. Launch the business process via the button on the form page.
 






 Note.
 
 Learn more about setting up components in a separate article:
 [Freedom UI Designer](https://academy.creatio.com/documents?id=2376) 
 .
 




 In general, the setup of the app UI involves the following steps:
 


1. Structure the app by adding the relevant sections and other elements In this example, these are
 
 Payroll
 
 ,
 
 Bonuses
 
 ,
 
 Docking
 
 sections.
2. Set up the form page. This example covers the step using the form page of the
 
 Payroll
 
 section as an example.
3. Configure the list page. This example covers the step using the
 
 Payroll
 
 section as an example.
4. Add the relevant elements to pages:
	* fields and data sources
	* business processes and cases
	* dashboards
	* buttons, labels, lists, and other list page and form page components that meet the corporate style requirements



 To implement the example, use a custom “Financial benefits” app created from the “Records & business processes” template. Learn more about creating apps in a separate article:
 [Create a custom app](https://academy.creatio.com/documents?id=2377) 
 .
 



 Step 1. Configure the app structure
-------------------------------------


1. Open the Application Hub by clicking
 ![btn_system_designer.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/btn_system_designer.png)
 in the top right.
2. Open the “Financial benefits” app.
3. Go to the
 
 Navigation and sections
 
 block →
 
 New Freedom UI section
 
 → create a
 
 Payroll
 
 section:
	1. Select the section icon.
	2. Enter the section name in the
	 
	 Name
	 
	 field.
	3. Specify the purpose of the section in the
	 
	 Description (optional)
	 
	 field (optional).
	4. Click
	 
	 Create
	 
	 (Fig. 2).
	 
	
	 Fig. 2 Add a section
	 
	
	![new_section.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/new_section.png)
4. Add more pages using available templates (optional).
5. Repeat steps 3 through 5 for other sections you need to add to the app.



 Step 2. Set up the app form page
----------------------------------


1. Open the form page of the “Financial benefits” app.
2. Set up the page layout. The page UI already includes the set of components taken from the template. For example, an area that has a flex container and buttons, as well as two areas on the left, and an area on the right (Fig. 3).
 

 Fig. 3 A minimum set of form page components
 

![designer_page_template_1_0.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/designer_page_template_1_0.png)



 Add a full width area to the bottom of the page by dragging the area from the component library. The area must house other elements that let you divide the content structurally and visually.
 





 Note.
 
 If you need to add several elements of the same type to the page, you can add only the first element to the canvas, then copy the element the needed amount of times by hovering over it and clicking
 ![btn_copy.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/btn_copy.png)
 . After that, edit the settings of each added element.
3. The top left area must contain the employee profile data:
	1. Add a
	 
	 Label
	 
	 element. For example, set its text to “Employee data.”
	2. Attach the following fields to the area and set them up:
		* Employee
		 
		 (lookup)
		* Job title
		 
		 (lookup)
		* Department
		 
		 (lookup)
		* Employment contract type
		 
		 (lookup)
		* Compensation type
		 
		 (lookup)
		 
		
		 Fig. 4 Add fields to the area
		 
		
		![designer_page_template_add_fields_0.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/designer_page_template_add_fields_0.png)
	3. Configure the input fields for the payroll period data in the bottom left area similarly.
		* Payroll period
		 
		 (lookup)
		* Work days in period
		 
		 (number)
		* Owner
		 
		 (lookup)
		* Benefits paid
		 
		 (boolean)
4. Add 4 tabs to the bottom area:
 
 Payroll, gross
 
 ,
 
 Deductions
 
 ,
 
 Bonuses
 
 ,
 
 Docking
 
 . Rename or delete the default tabs. Add expansion panels and fields that display the relevant data to the tabs.
 



 The
 
 Bonuses
 
 tab must use data from the
 
 Bonuses
 
 section of the “Financial benefits” app. To streamline the addition of records, attach the “Bonuses over payroll period” expansion panel to the tab and add the
 
 +
 
 icon button to the header. The button must open the page that adds a record of the specified object on click (Fig. 5).
 




 Fig. 5 Set up tabs
 

![designer_page_template_add_group_fields_1.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/designer_page_template_add_group_fields_1.png)
5. Add dashboards from the
 
 Charts
 
 group to the right area:
	* “Metric.” Must display the pay rate of the employee.
	* “Metric.” Must display the number of vacation days available for the employee over the selected period.
	* “Metric.” Must display the number of vacation days the employee used over the selected period.
	* “Metric.” Must display the number of sick days available for the employee over the selected period.
	* “Metric.” Must display the number of sick days the employee used over the selected period.
	* “Spline.” Must display the employee productivity broken down by the year comparative to the previous year.
6. Add the “Recalculate” button to the top area. The button must launch the
 [existing business process](https://academy.creatio.com/documents?id=7168) 
 that updates data (Fig. 6).
 

 Fig. 6 Add dashboards and a button
 

![designer_page_template_add_dashboards_0.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/designer_page_template_add_dashboards_0.png)
7. Click
 
 Save
 
 in the top left.



 Step 3. Set up the app mini page
----------------------------------


1. Go to the
 
 Pages
 
 block →
 
 New page
 
 → select the mini page template.
2. Click
 
 Add data source
 
 in the top left →
 
 Existing data source
 
 → select the data source of the current app.
3. Set up the mini page layout. You can attach any Freedom UI component to the mini page, but you cannot resize the canvas.
 



 The template already includes a base set of components that enable users to navigate the page. Add and set up the following essential fields to the mini page:
 


	1. Employee
	 
	 (dropdown)
	2. Owner
	 
	 (dropdown)
	3. Payroll period
	 
	 (dropdown)
	4. Benefits paid
	 
	 (checkbox)

 Fig. 7 Set up the app mini page
 

![scr_mini_page.png](/docs/sites/en/files/images/NoCodePlatform/set_up_the_app_ui/scr_mini_page.png)
4. Click
 
 Save
 
 in the top left.
5. Go to the
 
 Data model
 
 block in the No-Code Designer → the data model of the current app →
 
 Pages
 
 tab.
6. Select the mini page in the
 
 Add page
 
 field (Fig. 8).
 

 Fig. 8 Set up the app mini page
 

![scr_page_setup.png](/docs/sites/en/files/images/NoCodePlatform/set_up_the_app_ui/scr_page_setup.png)
7. Click
 
 Save
 
 .



 Step 4. Set up the list
-------------------------


1. Go to the
 
 Pages
 
 block → the list page created for the relevant section. The page UI already contains a minimum set of components (Fig. 9). You can copy, edit, move, or delete any element.
 

 Fig. 9 The minimum number of components on the list page
 

![designer_page_template_section.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/designer_page_template_section.png)
2. Set up the
 
 Folders
 
 component that lets you segment the section records. Set the component up so that each of the “2020,” “2021,” “2022” folders contains the nested “1st quarter,” “2nd quarter,” “3rd quarter,” “4th quarter” folders. The
 
 Folder management menu
 
 component lets you hide the folder tree.
3. Set up the
 
 Financial benefits
 
 section list:
 


	1. Freeze the
	 
	 Created on
	 
	 column by clicking
	 ![btn_more.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/btn_more.png)
	 →
	 
	 Freeze
	 
	 (Fig. 10).
	 
	
	 Fig. 10 Freeze a column
	 
	
	![designer_page_template_pin_button.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/designer_page_template_pin_button.png)
	2. Select
	 
	 Hide
	 
	 in the same menu of the
	 
	 Created by
	 
	 column to hide this information from the user-facing list.
	3. Add the
	 
	 Full employee name
	 
	 ,
	 
	 Job title
	 
	 columns to the list. To do this, click
	 ![btn_add.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/btn_add.png)
	 → select the relevant fields →
	 
	 Select
	 
	 (Fig. 11).
	 
	
	 Fig. 11 Select the columns
	 
	
	![designer_page_template_choose_column_0.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/designer_page_template_choose_column_0.png)
4. Add “Current payroll period” and “Number of payrolls calculated for the current period” dashboards (Fig. 12).
 

 Fig. 12 Add dashboards to the list page
 

![designer_page_dashboards_section.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/designer_page_dashboards_section.png)
5. Click
 
 Save
 
 to apply the changes to the section UI.




