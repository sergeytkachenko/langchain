


 Manage access to the information you add to Creatio. For example, when registering a new account record, you can specify users who have access to it.
 



 There are three record operation types: read, edit, and delete. For example, access to the “read” operation means that the user or user group can view the record in the section and open its page.
 



 Learn more:
 [Record permissions](/docs/8-0/user/setup_and_administration/user_and_access_management/access_management/record_permissions_shortcut/record_permissions) 
 .
 



 You can select one of the following access levels for each operation:
 


* **Granted** 
 – permissions to read, change, or delete a record.
* **Granted/Delegation permitted** 
 – permissions to perform the record operations, as well as to manage the operation permissions.



 By default, Creatio grants full operation permissions with the ability to delegate permissions to the following roles:
 


* the record author and the management role of the author
* the record owner and the management role of the owner



 The system administrator can set up default record permissions for other users. Learn more:
 [Record permissions](/docs/8-0/user/setup_and_administration/user_and_access_management/access_management/record_permissions_shortcut/record_permissions) 
 .
 



 Open the record page and select
 
 Set up access rights
 
 in the
 
 Actions
 
 menu to manage the record access permissions.
 



 Set up the access permissions
-------------------------------


1. Open the page of the relevant record.
2. Select
 
 Set up access rights
 
 in the
 
 Actions
 
 menu (Fig. 1). This will open a new page.
 

 Fig. 1 Navigate to the access permission setup
 

![scr_access_to_records_actions_menu.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_access_to_records/scr_access_to_records_actions_menu.png)
3. Click the
 
 Add
 
 button and select the record operation type on the page that opens. For example, select
 
 Edit access right
 
 to grant permission to edit the record. This will open a box.
4. Select the user or user group that must receive the access permissions in the box that opens. For example, select the “All employees” user group to grant the edit permission to all company employees. As a result, Creatio will add the new rule to the corresponding detail of the access permissions page. The rule will determine the user or user group's permissions to the corresponding operation on the record. By default, the operation access permission is always “Granted.”
5. Click
 
 Save
 
 .



 Modify the access permissions
-------------------------------


1. Open the edit page of the relevant record.
2. Select
 
 Set up access rights
 
 in the
 
 Actions
 
 menu. This will open the access permissions page.
3. Select the record to modify in the
 
 Read
 
 ,
 
 Edit
 
 , or
 
 Delete
 
 detail on the page. For example, select the record that contains the name of the user in the
 
 Edit
 
 detail to allow the user to delegate permissions to edit the record.
4. Select the desired access level in the
 
 Access level
 
 menu. For example, select
 
 Granted/delegation permitted
 
 to allow the user to manage the access permissions to the operation (Fig. 2).
 

 Fig. 2 Modify the record access permissions
 

![scr_access_to_records_edit_access.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_access_to_records/scr_access_to_records_edit_access.png)
5. Click
 
 Save
 
 .



 Revoke the access permissions
-------------------------------


1. Open the edit page of the relevant record.
2. Select
 
 Set up access rights
 
 in the
 
 Actions
 
 menu. This will open the access permissions page.
3. Select the access permission to revoke in the
 
 Read
 
 ,
 
 Edit
 
 , or
 
 Delete
 
 detail on the page and delete it. For example, select the “All employees” record in the
 
 Edit
 
 detail and click
 
 Delete
 
 to restrict all users from editing the record.




