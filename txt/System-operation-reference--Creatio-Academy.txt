


 System operations to which you can manage access are described below.
 



 User and role administration
------------------------------





| 
 System operation name and code
  | 
 Description
  |
| --- | --- |
| 
 Manage user list
 
 “Can
 
 Manage
 
 Users”
  | 
 Permissions to add, modify and delete
 [user accounts](https://academy.creatio.com/docs/documents?id=1426) 
 in the System Designer's user and role management sections.
  |
| 
 Manage user licenses
 
 “Can
 
 Manage
 
 Lic
 
 Users”
  | 
 Access to the
 
[License manager](https://academy.creatio.com/docs/documents?id=1472) 

 section. The users that have permission to manage licenses can log into Creatio and redistribute the licenses even if Creatio has been locked due to exceeding the number of distributed licenses.
  |
| 
 Change delegated permissions
 
 “Can
 
 Change
 
 Admin
 
 Unit
 
 Granted
 
 Right”
  | 
 The ability to delegate the access rights of some users to others using the
 
[Delegate permissions](https://academy.creatio.com/docs/documents?id=1998) 

 detail on the user page.
  |




 Managing portal users
-----------------------





| 
 System operation name and code
  | 
 Description
  |
| --- | --- |
| 
 Manage portal users
 
 “Can
 
 Administrate
 
 Portal
 
 Users”
  | 
 Permissions to add, modify and delete portal user accounts in the System Designer's user and role management sections.
  |
| 
 Access to portal main page setup module
 
 “Can
 
 Manage
 
 Portal
 
 Main
 
 Page”
  | 
 Permission to set up the
 [portal main page](https://academy.creatio.com/docs/documents?id=1790) 
 .
  |




 General access
----------------



 General access operations refer to all records in all objects. General access is usually provided to system administrators.
 





 Attention.
 
 Access to these operations overrides object permissions (object operations, records and columns). For example, if a user has access to the
 
 View any data
 
 operation, this user will be able to view records of all objects, even those in which the read operation is restricted.
 






| 
 System operation name and code
  | 
 Description
  |
| --- | --- |
| 
 View any data
 
 “Can
 
 Select
 
 Everything”
  | 
 Permission to view any data in any object.
  |
| 
 Add any data
 
 “Can
 
 Insert
 
 Everything”
  | 
 Permission to add records to any object.
  |
| 
 Edit any data
 
 “Can
 
 Update
 
 Everything”
  | 
 Permissions to edit any data in any object.
  |
| 
 Delete any data
 
 “Can
 
 Delet
 
 eEverything”
  | 
 Permission to delete any records in any object.
  |




 Columns, system operations and default permissions
----------------------------------------------------





| 
 System operation name and code
  | 
 Description
  |
| --- | --- |
| 
 Change system operations permissions
 
 “Can
 
 Change
 
 Admin
 
 Operation
 
 Grantee”
  | 
 Ability to manage
 [access permissions](https://academy.creatio.com/docs/documents?id=258) 
 to system operations. The scope of rights granted by this operation includes the right to register additional system operations.
  |




 Access to special sections
----------------------------





| 
 System operation name and code
  | 
 Description
  |
| --- | --- |
| 
 Access to “Access rights” workspace
 
 “Can
 
 Manage
 
 Administration”
  | 
 Access to the
 
[Object permissions](https://academy.creatio.com/docs/documents?id=262) 

 and
 
[Operation permissions](https://academy.creatio.com/docs/documents?id=258) 

 sections. Required for sysAdminUnit record management. Grant access to specific administering operations separately.
  |
| 
 Access to “Process design” section
 
 “Can
 
 Manage
 
 Process
 
 Design”
  | 
 Access to the
 [Process Designer](https://academy.creatio.com/docs/documents?id=7003) 
 , and the ability to add and modify business processes.
  |
| 
 Access to “Change log” section
 
 “Can
 
 Manage
 
 Change
 
 Log”
  | 
 Access to the
 
[Change log](https://academy.creatio.com/docs/documents?id=506) 

 section.
  |
| 
 Access to “System settings” section
 
 “Can
 
 Manage
 
 Sys
 
 Settings”
  | 
 Access to the
 
[System settings](https://academy.creatio.com/docs/documents?id=269) 

 section.
  |
| 
 Access to “Lookups” section
 
 “Can
 
 Manage
 
 Lookups”
  | 
 Access to the
 
[Lookups](https://academy.creatio.com/docs/documents?id=271) 

 section.
  |
| 
 Can manage configuration elements
 
 “Can
 
 Manage
 
 Solution”
  | 
 Access to the System designer's
 
[Configuration](https://academy.creatio.com/documents?id=15101) 

 section.
  |
| 
 View “Audit log” section
 
 “Can
 
 View
 
 Sys
 
 Operation
 
 Audit”
  | 
 Permission to to view the contents of the
 
[Audit log](https://academy.creatio.com/docs/documents?id=2320) 

 section.
  |
| 
 Manage “Audit log” section
 
 “Can
 
 Manage
 
 Sys
 
 Operation
 
 Audit”
  | 
 Permission to view the contents of the
 
 Audit log
 
 section and to archive the log.
  |




 Access to duplicates search
-----------------------------





| 
 System operation name and code
  | 
 Description
  |
| --- | --- |
| 
 Duplicates search
 
 “Can
 
 Search
 
 Duplicates”
  | 
 Permission to search for duplicates in sections with active
 [duplicate search rules](https://academy.creatio.com/documents?id=1591) 
 .
  |
| 
 Duplicates processing
 
 “Can
 
 Merge
 
 Duplicates”
  | 
 Permission to merge duplicate records on the duplicate search results page. Additionally, permission to merge records manually in all accessible sections and lookups.
  |
| 
 Access to “Duplicates rules setup”
 
 “Can
 
 Manage
 
 Duplicates
 
 Rules”
  | 
 Permission to add and edit duplicate search rules.
  |




 Access to integration settings
--------------------------------





| 
 System operation name and code
  | 
 Description
  |
| --- | --- |
| 
 Access to OData
 
 “Can
 
 Use
 
 OData
 
 Service”
  | 
 Permission to use OData protocol for external integration.
  |




 General actions
-----------------





| 
 System operation name and code
  | 
 Description
  |
| --- | --- |
| 
 Email providers list setup
 
 “Can
 
 Manage
 
 Mail
 
 Servers”
  | 
 Permission to create a list of email servers used to send and receive emails.
  |
| 
 Shared mailbox synchronization setup
 
 “Can
 
 Manage
 
 Shared
 
 Mailboxes”
  | 
 Permission to manage shared mailboxes (mailboxes with the
 
 Allow shared access
 
 checkbox enabled).
  |
| 
 Change access rights to record
 
 “Can
 
 Change
 
 Entity
 
 Schema
 
 Record
 
 Right”
  | 
 Lets users grant
 [record permissions](https://academy.creatio.com/documents?id=1966) 
 . The
 
 Use operation permissions
 
 switch must be toggled on in the corresponding object for record permissions to work.
  |
| 
 Ignore access check by IP address
 
 “Suppress
 
 IP
 
 Restriction”
  | 
 When a user who has access to this operation logs in to the system, the IP address restrictions will be ignored.
  |
| 
 Export list records
 
 “Can
 
 Export
 
 Grid”
  | 
 Permission to export list data in a \*.xlsx file. If a user does not have permission for this operation, the
 
[Export to Excel](https://academy.creatio.com/documents?id=1864) 

 action in sections and the “List” dashboard tile menu is disabled.
  |
| 
 Permission to run business processes.
 
 “Can
 
 Run
 
 Business
 
 Processes”
  | 
 Permission to run business processes in Creatio. All users have permission to perform this operation by default.
  |
| 
 Cancel running processes
 
 “Can
 
 Cancel
 
 Process”
  | 
 Permission to cancel a running business process in the process log.
  |
| 
 Access to workplace setup
 
 “Can
 
 Manage
 
 Workplace
 
 Settings”
  | 
 Permission to create and set up
 [workplaces](https://academy.creatio.com/documents?id=1248) 
 , i. e., managing the section list available in the side panel.
  |
| 
 Access to comments
 
 “Can
 
 Edit
 
 Or
 
 Delete
 
 Comment”
  | 
 Permission to edit and delete comments on the feed messages.
  |
| 
 Permission to delete messages and comments
 
 “Can
 
 Delete
 
 All
 
 Message
 
 Comment”
  | 
 Permission to delete messages and comments left by other users in the
 
 Feed
 
 section, on the
 
 Feed
 
 tab of the Notification Panel, and on the
 
 Feed
 
 tab of the view and edit pages of system sections. Users can edit and delete their own messages and comments even if they do not have access permissions to this system operation.
  |





