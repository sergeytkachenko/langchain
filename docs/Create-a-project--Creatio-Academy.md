



 For new Creatio instances this functionality is available for Creatio version 8.0.9 and earlier. Existing Creatio instances keep the Classic UI section after updating to Creatio version 8.0.10 and later.
 




 A project is an activity intended to achieve specific results, for example, create a new product or develop a new service. Thus, a project can involve constructing a house, developing a software product, or implementing a new automated system in the company.
 



 Use the
 
 Projects
 
 section to form a project structure, plan working time, allocate necessary resources, track deadlines, and keep a record of expenses.
 



 This section has several pre-set
 [quick filters](https://academy.creatio.com/documents?id=1232) 
 :
 


* By project start and end date (the
 
 Start
 
 and
 
 Worked till
 
 fields of the project page). The project will be displayed in the section if the dates in the filter fall to the project time period.
* By owner (the
 
 Owner
 
 field of the project page).



 Add a new project
-------------------


1. Go to the
 
 Projects
 
 section.
2. Click
 
 New
 
 . This will open a new page.
3. Fill out the general project information on the page that opens:
 


|  |  |
| --- | --- |
| 
 Name
  | 
 The project name. Required.
  |
| 
 Status
  | 
 Project completion status. For example, “Planned,” “In progress,” or “Completed.” By default, set to “Planned.” Required.
  |
| 
 Owner
  | 
 Employee in charge of the project. By default, set to the name of the current user. Required.
  |
4. Fill out the key project details on the
 
 General information
 
 tab:
 


|  |  |
| --- | --- |
| 
 Account
  | 
 Account and/or contact that is the project customer. Filling out one of these fields is required.
  |
| 
 Contact
  |
| 
 Start date
  | 
 Planned start and end dates of the project.
  |
| 
 Due date
  |
| 
 Type
  | 
 Type of the project. For example, “Internal project” or “Complex project.” Required.
  |
| 
 Duration
  | 
 Project task duration, in hours and minutes. The field is non-editable and is calculated automatically as a sum of working hours within the planned start and end dates of the project.
  |
| 
 Deadline
  | 
 Scheduled project completion date.
  |
5. Specify connected opportunities and contractors in the
 
 Connected to
 
 detail:
 


|  |  |
| --- | --- |
| 
 Opportunity
  | 
 The opportunity as part of which to perform the project.
  |
| 
 Supplier
  | 
 The company acting as a supplier in the project. Usually, this is your company.
  |
6. Go to the
 
 Attachments and notes
 
 tab and add more information about the project, as well as attachments and links to the web resources related to the project.
7. Click
 
 Save
 
 in the top left corner.





 Note.
 
 Click
 
 Copy
 
 in the section list to copy an existing project. This will also copy all tasks related to the project. The key dates of the project copy and its subordinate tasks will be offset using the current date as the start date. For example, if the project start date is 03/01/2020, the end date is 03/15/2020 and the project was copied on 03/10/2020, the start date of the project copy will be set to 03/10/2020, and the end date – to 03/25/2020.
 




 Configure the project structure
---------------------------------



 Set up the list of tasks related to the project implementation on the
 
 Structure
 
 tab of the project page.
 



 To add a new project task:
 


1. Go to the
 
 Structure
 
 tab of the project.
2. Click
 ![btn_chapter_mobile_wizard_new_role.png](/sites/default/files/documents/docs/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_employees/btn_chapter_mobile_wizard_new_role.png)
 on the
 
 Structure
 
 details and select
 
 Add root project task
 
 .
 



 To add a subordinate task to a root task, select the root task in the detail list, and select
 
 Add subordinate project task
 
 in the detail action menu.
3. Fill out the fields on the page that opens. Learn more in a separate article:
 [Manage project tasks](https://academy.creatio.com/documents?id=1220) 
 .
4. Click
 
 Save
 
 .



 As a result, Creatio will add a new task to the project structure.
 



 Select a task record and click
 
 Up
 
 or
 
 Down
 
 to
 **move the task in the task list** 
 . You can move items of the same level only.
 





 Note.
 
 The filter on the
 
 Structure
 
 detail applies only to root tasks. Subordinate tasks are not filtered.
 




 Start a project and track its execution
-----------------------------------------



 The
 
 Status
 
 field is set to “Planned” for a new project record. To start a project, change the field value to “In progress.”
 



 The
 
 Completion %
 
 field on the
 
 General information
 
 tab displays the actual percentage of project completion at the moment. Set this value manually or select the
 
 Calculate automatically
 
 checkbox. When the checkbox is selected, the field becomes non-editable, and its value is calculated as the percentage ratio of total actual working time and total estimated working time, based on the
 [List of resources
 
 detail](https://academy.creatio.com/documents?id=1220) 
 .
 




