


 A new record in the
 
 Employees
 
 section is created based on an existing contact. The employee’s page will pull information such as personal data, contact and address information, significant events, and career changes from their respective contact page. Records can be
 [imported](https://academy.creatio.com/documents?product=base&ver=7&id=1252) 
 from Excel or added manually.
 



 To create a new record in the
 
 Employees
 
 section
 **manually** 
 :
 


1. Go to the
 
 Employees
 
 section and click the
 
 New employee
 
 button.
2. In the opened window, fill in the following fields:
 


	1. Contact
	 
	 – a Creatio contact based on which an employee record will be created. The field is required.
	2. Job title
	 
	 – employee’s job title, for example, “Department manager.”
	3. Full job title
	 
	 – exact job title, such as “Sales department manager.”
	4. Department
	 
	 – company’s organization structure unit where the employee works, for example, “Sales department.”
	 
	
	
	
	
	
	 Note.
	 
	 A list and hierarchical structure of departments is configured in the
	 
	 Organization structure items
	 
	 lookup. Read more in the “
	 [Getting started with the
	 
	 Employees
	 
	 section](/docs/8-0/user/crm_tools/employees/configure_the_section/configure_employees_section) 
	 ” article.
	5. Account
	 
	 – the name of the employer.
3. Click
 
 Save
 
 .
   

 As a result, the following data will be automatically passed to the new employee page from the contact page, if they were specified:
	1. Communication options.
	2. Addresses.
	3. Noteworthy events.
	4. data about the job experience
	5. data about the user, their organizational and functional roles.
4. Save the page.
 



 Next time you edit the data on the employee page, the changes will also be reflected on the employee’s contact page.





 Note.
 
 The data displayed on the action panel of the employee page is synchronized with the action panel of the respective contact page. For example, a task scheduled using the action panel on the employee page will also be available on the contact page.
 




 Populate the employee profile
-------------------------------



 To add or edit the general information about an employee:
 


1. Go to the
 
 Employees
 
 section and open the needed record.
2. Populate the following fields:
 


|  |  |
| --- | --- |
| 
 Photo
  | 
 Employee’s photo. Photos are pulled from the corresponding contact pages. Owner photos can only be changed on the corresponding
 
[contact page](/docs/8-0/user/crm_tools/accounts_and_contacts/create_a_contact/create_contact) 

 .
  |
| 
 Full name
  | 
 First and last name of the employee. The field displays information from the contact page. If you change the name on the employee page, the data on the contact page will also be updated.
  |
| 
 Position
  | 
 Employee's current position (e.g. “Director” or “Head of Department”). The field is populated with the
 
 Employee jobs
 
 lookup values.
  |
| 
 Full job title
  | 
 The field is populated automatically – it duplicates the title selected in the
 
 Employee jobs
 
 lookup. If necessary, the title may be edited.
  |
| 
 Organizational unit
  | 
 Company’s organizational unit where the employee works. The field is populated with the
 
 Organization structure items
 
 lookup values. If the manager of the organizational unit is specified in the lookup, their data will be automatically displayed in the manager’s profile on the employee's page.
  |
| 
 Account
  | 
 The employer’s account name is specified in this field. You may only select the accounts with the “Our Company” type. If you update this field, the account field of the contact page will also be updated.
  |
| 
 Business phone
  | 
 Employee's business phone number. The field displays the
 
 Communication options
 
 detail value of the
 
 Contact info
 
 tab of the employee and contact pages.
  |
| 
 Email
  | 
 Employee's email address. The field displays the
 
 Communication options
 
 detail value of the
 
 Contact info
 
 tab of the employee and contact pages.
  |
| 
 Birthdate
  | 
 Employee's birth date. The field displays the
 
 Noteworthy events
 
 detail value of the
 
 Contact info
 
 tab of the employee and contact pages.
  |
| 
 Gender
  | 
 Employee’s gender. The field displays the value of the
 
 Contact info
 
 tab of the contact page. This field can’t be edited on the employee page.
  |
| 
 Owner
  | 
 The Creatio user who is the author of this record in the
 
 Employees
 
 section and maintains the information about this employee. The field is populated automatically once the record is created.
  |
3. Verify the information about the manager of the employee. if the owner of the organizational unit is indicated in the
 
 Organization structure items
 
 lookup, their data will be automatically displayed in the owner’s profile on the employee's page. If the owner is not specified in the lookup, you can specify them manually, from the list of employees.
   

 After the
 
 Manager
 
 field is populated, the following fields will be populated automatically.
 


|  |  |
| --- | --- |
| 
 Photo
  | 
 Photo of the contact owner. Photos are pulled from the corresponding contact pages. Owner photos can only be changed on the corresponding
 
[contact page](/docs/8-0/user/crm_tools/accounts_and_contacts/create_a_contact/create_contact) 

 .
  |
| 
 Full name
  | 
 First and last name of the owner The field group displays the data that is specified on the contact page. This field is non-editable.
  |
| 
 Mobile phone
  | 
 The field group displays the data from the contact page. This field can not be edited on the employee page.
  |
| 
 Business phone
  |
4. On the
 
 Attachments and notes
 
 tab, add more information about the employee, as well as attachments and links to the web resources related to the employee.




 Add general employee information
-----------------------------------



 The
 
 Contact info
 
 tab contains general contact information about the employee (contact and address data, noteworthy events, etc.). The data on the
 
 Basic information
 
 tab is synchronized with the corresponding data on the
 
 contact
 
 page. If you change the communication options or any other data, enter new information on the employee page, and it will also be displayed on the
 
 contact
 
 page.
 


### 
 Add a communication option



 The
 
 Communication options
 
 detail contains the list of employee’s communication options, as well as the list of the restricted communication channels. The detail displays the
 
 Communication options
 
 detail values of the contact page. If you change the communication options on the employee page, the data on the contact page will also be updated.
 



 To add information on the detail fields, click
 
![btn_chapter_mobile_wizard_new_role.png](/sites/default/files/documents/docs/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_employees/btn_chapter_mobile_wizard_new_role.png)

 and select the needed option:
 





|  |  |
| --- | --- |
| 
 Business phone
  | 
 Phone numbers can be used to contact the employee. Communication option types are defined when a record is added (you can change them later).
  |
| 
 Mobile phone
  |
| 
 Home phone
  |
| 
 Skype
  | 
 Skype account of the employee.
  |
| 
 Email
  | 
 Website and email addresses of the employee.
  |
| 
 Web
  |
| 
 Facebook
  | 
 Social network profiles of the employee. This field is populated by searching for the social network profile of the employee on a separate page.
  |
| 
 Twitter
  |
| 
 Do not use email
  | 
 Checkboxes indicate which communication options should not be used to contact the employee. For example, if a contact does not wish to receive SMS, select the
 
 Do not use SMS
 
 checkbox.
  |
| 
 Do not use phone
  |
| 
 Do not use SMS
  |
| 
 Do not use mail
  |
| 
 Do not use fax
  |



### 
 Add address



 The
 
 Addresses
 
 detail contains the list of all available addresses of the employee. The detail displays the
 
 Addresses
 
 detail value of the
 
 Contact info
 
 tab of the contact page.
 



 To add information on the detail fields, click
 
![btn_chapter_mobile_wizard_new_role.png](/sites/default/files/documents/docs/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_employees/btn_chapter_mobile_wizard_new_role.png)

 and select the needed option:
 





|  |  |
| --- | --- |
| 
 Address type
  | 
 Type of address of an employee, e.g. “Home” or “Work.” Defined when a record is added. You can change it afterward.
  |
| 
 Address
  | 
 Street, building number, and other details of an employee's address.
  |
| 
 City
  | 
 Employee location. The
 
 State/province
 
 and
 
 City
 
 fields are connected to the
 
 Country
 
 field. For example, the
 
 Country
 
 field will be populated automatically when you populate the
 
 City
 
 field. Similarly, if you enter a province in the
 
 State/province
 
 , the
 
 Country
 
 field will be populated automatically. When you fill in the
 
 Country
 
 field, the
 
 State/province
 
 and
 
 City
 
 fields will display only those regions and cities, which correspond to the selected country. You can associate a region with a certain country in the
 
 States/provinces
 
 lookup, and associate a city with a country – in the
 
 Cities
 
 lookup.
  |
| 
 Country
  |
| 
 ZIP
  | 
 Postal code of an employee.
  |



### 
 Add noteworthy events



 The
 
 Noteworthy events
 
 detail contains the list of noteworthy events of an employee. The field displays the
 
 Noteworthy events
 
 detail values of the
 
[contact page](/docs/8-0/user/crm_tools/accounts_and_contacts/create_a_contact/create_contact) 

 .
 



 To add information on the detail fields, click
 
![btn_chapter_mobile_wizard_new_role.png](/sites/default/files/documents/docs/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_employees/btn_chapter_mobile_wizard_new_role.png)

 , select the type of the noteworthy event and specify the date on the page that opens.
 



 Validate the employee profile and roles
-----------------------------------------



 If an employee is a Creatio user, their information and roles are displayed on the
 
 User Account
 
 tab. Upon registering a new user account for an employee, all connected data will be displayed on the
 
 User account
 
 tab of the employee page automatically.
 



 The user login and the
 
 Active
 
 checkbox on the
 
 User Information
 
 detail cannot be edited.
 



 Edit the data on the
 
 Organizational roles
 
 and
 
 Functional roles
 
 details may be edited on the employee page. If edited, the data will be updated on the contact page as well.
 




