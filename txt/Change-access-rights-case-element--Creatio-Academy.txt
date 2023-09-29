


 If you want to add or remove access permissions to records in Creatio objects, use the
 
 Change access rights
 
![chapter_case_designer_icon_change_access_rights.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_icon_change_access_rights.png)
 element. You can change access rights for multiple users or roles at the same time. To add or remove access sequentially, use several
 
 Change Access Rights
 
 elements.
 



 Set up the [Change access rights] element
-------------------------------------------



 Specify the permission parameters on the element setup area (Fig. 1).
 




 Fig. 1 The
 
 Change access rights
 
 element setup area
 

![chapter_case_designer_change_acsess_rights.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_change_access_rights.png)



 The name of the element is displayed at the top of the setup area. This makes the element easy to find on the case diagram.
 



 Fill out the following fields:
 


1. When is the step performed?
 
 – indicates whether to activate the element at the start of the stage or after a case step. Select “At the start of the stage” if the access rights must be changed at the start of the case stage. Select “After the previous step is complete” if the access rights must be changed after the previous step in the case stage. Specify the step in the
 
 Perform after step
 
 field.
2. Step type
 
 – specify if the step is required. Select “Required step” if the task must be completed to transition to the next stage. If it is not required to perform change access rights to transition to the next stage, select “Optional step.”
 


 Note.
 
 Users can advance to the final “unsuccessful” stage from any stage without completing the required steps.
3. In the
 
 Which object to apply access rights to?
 
 field, select the Creatio object for which you want to change permissions. Specify the filter conditions for records which you want to change access rights. For example, only for the “VIP” account records.



 Remove access permissions
---------------------------



 Access rights can be deleted for the user or all users, a certain role, as well as for several users selected via a filter.
 



 To select users for whom you wish to delete access rights, click the
 ![btn_button_connections00007.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/btn_button_connections00007.png)
 button (Fig. 2).
 




 Fig. 2 Select users for whom to remove access rights
 

![scr_chapter_process_designer_change_access_groups_users.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/scr_chapter_process_designer_change_access_groups_users.png)



 There are a few different options:
 


* For all roles and users
 
 – delete permissions to the selected operations for all users and roles.
* For roles
 
 – delete permissions for the selected organization structure item.
* For employee
 
 – delete permissions for the user. To ensure the correct element operation, specify the contact of the user whose permissions you would like to delete.
* For the employees who meet the filter conditions
 
 – delete permissions for all users that correspond to the filter conditions.



 To delete or modify the selected role, click the
 ![btn_parametres_window_edit.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/btn_parametres_window_edit.png)
 button and choose the action you want to perform from the menu.
 



 Select the operations for which you would like to remove access rights – read
 ![chapter_case_designer_icon_access_rights_read.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_icon_access_rights_read.png)
 , edit
 ![chapter_case_designer_icon_access_rights_edit.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_icon_access_rights_edit.png)
 , or delete
 ![chapter_case_designer_icon_access_rights_delete.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_icon_access_rights_delete.png)
 data (Fig. 3).
 





 Fig. 3
 
 Removing access rights
 

![scr_chapter_case_designer_change_access_operations.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/scr_chapter_case_designer_change_access_operations.png)





 Note.
 
 You can delete access permissions to records for several different roles or users. To do this, add the selected users or groups to the list and specify the rights that you want to delete. As a result, when this step is performed, the access rights will simultaneously change for all specified groups and users.
 




 Add access permissions
------------------------



 Select the users or roles to grant them access rights to read
 ![chapter_case_designer_icon_access_rights_read00008.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_icon_access_rights_read00008.png)
 , edit
 ![chapter_case_designer_icon_access_rights_edit00009.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_icon_access_rights_edit00009.png)
 , or delete
 ![chapter_case_designer_icon_access_rights_delete00010.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/chapter_case_designer_icon_access_rights_delete00010.png)
 data.
 



 There are a few different options:
 


* For roles
 
 – grant permissions for the selected organization structure item.
* For employee
 
 – grant permissions for the user. To ensure the correct element operation, specify the contact of the user for whom you would like to grant permissions.
* For the employees who meet the filter conditions
 
 – grant permissions for all users that correspond to the filter conditions.



 To delete or modify the selected role, click the
 ![btn_parametres_window_edit00011.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/btn_parametres_window_edit00011.png)
 button and choose the action you want to perform from the menu.
 



 Select the operation access level that will be set when performing an action:
 


* Granted
 
 – users will obtain permission to execute selected operations.
* Granted with right to delegate
 
 – users will obtain permission to execute operations and to grant this operation permission to other users.



 To select the access level, click the
 ![btn_process_level_operations.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/btn_process_level_operations.png)
 button (Fig. 4).
 




 Fig. 4 Add permissions to operations
 

![scr_chapter_process_designer_change_access_level.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_case_elements/scr_chapter_process_designer_change_access_level.png)





 Note.
 
 You can add access rights to records from several different roles or users. To do this, add the selected users or groups to the list and specify the rights that you want to add. As a result, when this step is performed, the access rights will simultaneously change for all specified groups and users.
 





