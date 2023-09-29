


 The
 **audit log** 
 records system settings, events, and data. It logs events related to changes in the user role structure, the distribution of access permissions, changes in the system setting values, user authorization in Creatio, etc.
 



 The
 **change log** 
 records changes to business data. You can use it to track product price or account balance changes. Learn more:
 [Set up the change log](/docs/8-0/user/setup_and_administration/logging_tools/change_log/set_up_the_log/set_up_the_change_log) 
 .
 





 Note.
 
 Enable the “View “Audit log” section” (“CanViewSysOperationAudit” code) system operation to view the audit log. Enable the “Manage “Audit log” section” (“CanViewSysOperationAudit” code) system operation to view and archive the audit log records. Learn more:
 [System operation permissions](/docs/8-0/user/setup_and_administration/user_and_access_management/access_management/system_operation_permissions_shortcut/system_operation_permissions) 
 .
 




 The audit log is disabled by default. Follow the steps in this article to enable this feature.
 



 To enable the audit log using the system settings:
 


1. Click the
 ![system_designer.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/set_up_audit_log/system_designer.png)
 button to open the System designer.
2. Click “System settings” in the “System setup” block.
3. Select the “Audit log” folder subordinate to the “Administration” folder. This folder contains all system settings that control the audit log. Each logged event type has a dedicated system setting that enables or disables it. Learn more about the audit log system settings:
 [Description of system settings](/docs/7-17/user/setup_and_administration/system_settings_and_lookups/system_setting_reference/description_of_system_settings#title-1880-10) 
 .
4. Open the setting and select the
 
 Default value
 
 checkbox to enable it. For example, select the checkbox in the
 
 Log user authorization management events
 
 system setting (Fig. 1) to record user log in and log out events.
 





 Fig. 1
 
 An audit log system setting
 

![scr_chapter_system_operations_log_system_setting.png](/guides/sites/en/files/documentation/user/en/logging_tools/BPMonlineHelp/set_up_audit_log/scr_chapter_system_operations_log_system_setting.png)



 After disabling an audit log system setting, you may need to restart the Redis session server for the changes to take effect.
 





 Note.
 
 If the audit log is enabled on the configuration file level, Creatio will ignore the system setting values.
 





