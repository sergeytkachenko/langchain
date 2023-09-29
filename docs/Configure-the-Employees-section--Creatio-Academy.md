


 Perform initial setup before working with the
 
 Employees
 
 section:
 


* Configure the list of job titles of your company employees.
* Configure the hierarchical structure of departments and divisions to display the company structure and career changes of the employees.






 Configure job titles of employees
--------------------------------------



 The staffing table of your company may be different from the staffing table of the other companies. Therefore, contact and employee positions are stored in separate lookups. To configure employee job titles according to your staffing table:
 


1. Open the System Designer by clicking
 ![system_designer.png](/sites/default/files/documents/docs/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_employees/system_designer.png)
 in the top right corner of the application window.
2. Click the “Lookups” link in the “System setup” block.
3. Select the
 
 Employees
 
 folder in the lookups section.
4. Open the
 
 Employee jobs
 
 lookup.
5. Add a new record to the lookup by clicking the
 
 New
 
 button.
6. Enter the job name and description.
7. Repeat steps 5 to 6 for all job titles in your company’s staffing table.






 Configure the department structure of your company
-------------------------------------------------------



 Configure the hierarchical structure of departments and other structural units to keep track of the information about the company’s employees and their career movements. To do this, edit the records in the
 
 Organization structure items
 
 lookup. To configure the structure:
 


1. Open the System Designer by clicking
 ![system_designer00001.png](/sites/default/files/documents/docs/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_employees/system_designer00001.png)
 in the top right corner of the application window.
2. Click the “Lookups” link in the “System setup” block.
3. Select the
 
 Employees
 
 folder in the lookups section.
4. Open the
 
 Organization structure items
 
 lookup.
5. Add a new record to the lookup by clicking the
 
 New
 
 button.
 





 Note.
 
 Start adding company departments to the hierarchical structure from top to bottom. This will help to set links between the departments and form the full names of departments and divisions.
6. Enter the name of the organizational unit, for example, “Board of Directors.”
   

 Specify the name of this organizational unit manager in the
 
 Head
 
 field. Click
 ![scr_cti_button_choose.png](/sites/default/files/documents/docs/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_employees/scr_cti_button_choose.png)
 and select the manager from the list of employees.
   

 If the
 
 Employees
 
 section is empty, you can add a department head in two ways:
 


	* Enter an employee name in the
	 
	 Head
	 
	 field. You will be prompted to create a record in the
	 
	 Employees
	 
	 section with a specified name (
	 [Fig. 1](#XREF_30820_162) 
	 ). A mini page of adding a record to the
	 
	 Employees
	 
	 department will open by clicking the prompt field. Fill out the contact page and click
	 
	 Save
	 
	 . The created contact will be specified in the
	 
	 Head
	 
	 field of the
	 
	 Organization structure items
	 
	 lookup.
	 
	
	Fig. 1
	 – Creating a new record in the
	 
	 Employees
	 
	 section from the
	 
	 Organization structure items
	 
	 lookup
	 
	
	
	![Add manager](/docs/sites/en/files/2020-12/scr_add_director.png)
	* Click
	 ![scr_cti_button_choose00002.png](/sites/default/files/documents/docs/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_employees/scr_cti_button_choose00002.png)
	 , then click
	 
	 New
	 
	 in the window that opens (
	 [Fig. 2](#XREF_47925_163)
	 ). A page for adding a new employee will open. Select the contact record to copy the contact data and communication options to the employee page. Specify an account, department, and position for the new employee. Save the page. As a result, a new employee will be specified as the department head in the
	 
	 Organization structure items
	 
	 lookup.
	 
	
	Fig. 2
	 – Adding a new record to the
	 
	 Employees
	 
	 section from the value selection window
	 
	
	![Add employee from lookup](/docs/sites/en/files/2020-12/scr_add_employee_from_lookup.png)
7. Configure the status of the created department in the company structure by specifying the parent department.
8. Repeat steps 5 through 8 for all departments of your company.
9. The full name of the organizational unit will be generated automatically. The values of the
 
 Name
 
 and
 
 Parent department
 
 fields will be used in its name.



 As a result, a full hierarchical structure of the company will be generated and displayed at the selection of the employee’s organizational unit (
 [Fig. 3](#XREF_64024_164)
 ). A manager’s profile will be populated on the employee’s page according to the information about an employee’s organizational unit.
 




Fig. 3
 – Organizational unit selection window of the employee’s page
 

![Seelct department](/docs/sites/en/files/2020-12/scr_select_department.png)






