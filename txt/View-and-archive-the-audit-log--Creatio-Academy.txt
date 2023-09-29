


 You can view the system operations audit log that automatically registers events related to the modification of user roles, distribution of access permissions, change of system setting values, and users' authorization in the system.
 



 Access the audit log
----------------------



 Open the System designer. For example, click the
 ![system_designer.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/view_and_archive_audit_log/system_designer.png)
 button. Then, open the “System settings” section in the “System setup” block. Click “Audit log” in the “Users and administration” block.
 





 Note.
 
 Enable the “View “Audit log” section” (“CanViewSysOperationAudit” code) system operation to view the audit log. Enable the “Manage “Audit log” section” (“CanViewSysOperationAudit” code) system operation to view and archive the audit log records. Learn more:
 [System operation permissions](/docs/8-0/user/setup_and_administration/user_and_access_management/access_management/system_operation_permissions_shortcut/system_operation_permissions) 
 .
 





 The
 
 Audit log
 
 view displays the list of the most recently logged events. The
 
 Log archive
 
 view displays the list of events archived via the
 
 Archive log
 
 action. Creatio stores the archived events in a separate table.
 



 The
 
 Audit log
 
 section list displays the following data:
 





 Note.
 
 Configure the balancer to make the audit log display the user IP addresses in Creatio .NET Core or .NET 6 deployed on-site with horizontal scaling. Learn more:
 [Set up the IP addresses in the audit log for .NET Core and .NET 6](https://academy.creatio.com/documents?id=2110#title-2491-19) 
 .
 



* Type
 
 – the
 
 Event types
 
 lookup contains the available event types. For example, “User authorization,” “User session,” etc.
* Event date
 
 – the event start date and time.
* Result
 
 – the
 
 Event results
 
 lookup contains the available system event results. For example, the user login attempt may finish with the “Authorization” result or the “Authorization denied” result upon failure.
* IP address
 
 – the IP address of the user who performed the operation that resulted in the event. For example, the IP address of the user who attempted to log in to Creatio.
 


 Note.
 
 If the user connects via a VPN or the request is routed through proxy servers, the field will list the IP address of each proxy server. In that case, the rightmost IP address will belong to the last proxy server and the leftmost IP address will belong to the first traceable server.
* Owner
 
 – the user who performed the operation that resulted in the event. For example, the name of the employee who attempted to log in to Creatio.
* Description
 
 – the detailed event description. For example, “User authorization John Best. IP address: 192.168.0.7.” Creatio generates the event description automatically.



 Archive the audit log
-----------------------



 The
 
 Archive log
 
 action in the system operation audit log copies the log records to a separate archive table.
 



 To archive the audit log:
 


1. Click
 ![audit_log_list_view.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/view_and_archive_audit_log/audit_log_list_view.png)
 to open the list view of the
 
 Audit log
 
 section.
2. Click
 
 Actions
 
 →
 
 Archive log
 
 .
3. Set up the parameters on the newly opened
 
 Archive parameters
 
 page (Fig. 2).
 





 Fig. 2
 
 – The
 
 Archive parameters
 
 page
 

![scr_cases_setup_access_rights_archive_params.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/view_and_archive_audit_log/scr_cases_setup_access_rights_archive_params.png)
4. Period from
 
 ,
 
 till
 
 – specify the period of the events to archive. Creatio will only archive the events within the specified range.
5. Type
 
 – specify the type of the events to archive. Creatio will archive only the events of the specified types. You can select multiple types.
 





 Note.
 
 The archiving action is logged as “Access rights audit log.” Creatio will display a message with the number of archived records upon completion.
 




 As a result, you will be able to see the list of archived events whose dates fall within the specified period in the “Log archive” view (
 ![audit_log_archive_view.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/view_and_archive_audit_log/audit_log_archive_view.png)
 ) of the
 
 Audit log
 
 section.




