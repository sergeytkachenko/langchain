


 By default, all Creatio users have permission to run business processes. This is managed by the “Can run all business processes” operation permission (“CanRunBusinessProcesses” code).
 



 You can also set up permissions to run a specific business process to allow a user or user role to run only the business processes necessary for their duties. You can only configure the permissions to run a business process if it is launched manually. These permissions are effective for
 **all versions** 
 of the process.
 



 To do this:
 


1. Open the
 
 Process library
 
 section from the
 
 Studio
 
 workplace.
2. Select the desired process and click the
 
 Properties
 
 button.
3. Open the
 
 Permissions to run
 
 tab on the page that opens.
4. Click the
 ![btn_com_add_tab_7.png](https://academy.creatio.com/docs/sites/default/files/inline-images/btn_com_add_tab_7.png)
 button. In the pop-up box, select the users or user roles to grant them permission to run this process (Fig. 1).




 Fig. 1 Setting up the permissions to run a process
 

![set_process_permissions.gif](/docs/sites/en/files/images/BPM_Tools/bp_permissions/set_process_permissions.gif)



 As a result, the specified users and user roles will be able to run this process even if you did not specify them in the “Can run all business processes” operation permission (“CanRunBusinessProcesses” code).
 



 Use the
 
 Position
 
 column to set up the permission priority. The higher the rule in the list, the higher its priority. The “0” value in the
 
 Priority
 
 field corresponds to the top-priority rule. Change a rule’s position using the
 ![btn_move_up_detail.png](/docs/sites/default/files/images/BPM_Tools/bp_permissions/btn_move_up_detail.png)
 and
 ![btn_move_down_detail.png](/docs/sites/default/files/images/BPM_Tools/bp_permissions/btn_move_down_detail.png)
 buttons.
 





 Note.
 
 When installing a business process from a package, Creatio will apply the process permissions automatically as well.
 






