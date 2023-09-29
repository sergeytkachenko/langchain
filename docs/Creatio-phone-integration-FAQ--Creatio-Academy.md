


 Which telephone systems can be integrated with Creatio?
---------------------------------------------------------



 By default, Creatio is integrated with Webitel telephone service. If necessary, you can integrate other telephone systems with Creatio. The list of supported telephone systems is available in the
 [Feature comparison for supported phone systems](/docs/7-18/user/more_apps/phone_integration_connectors/comparison_of_phone_systems/feature_comparison_for_supported_phone_systems) 
 article.
 



 How can I integrate cloud telephone providers?
------------------------------------------------



 Creatio interacts with phone providers through an IP-PBX. To integrate with a cloud telephone system, set up one of the
 [supported IP-PBX](/docs/7-18/user/more_apps/phone_integration_connectors/comparison_of_phone_systems/feature_comparison_for_supported_phone_systems) 
 . The setup procedures for integration with different phone systems are available in separate articles.
 



 If you are not using connectors listed in the comparison table for phone integration features, you can use any of the connectors available on
 
[Creatio Marketplace](https://marketplace.creatio.com/) 

 .
 



 Which features do the supported connectors have?
--------------------------------------------------



 The feature comparison for integration with different telephone systems, as well as their integration requirements, are available in the
 [Feature comparison for supported phone systems](/docs/7-18/user/more_apps/phone_integration_connectors/comparison_of_phone_systems/feature_comparison_for_supported_phone_systems) 
 article.
 



 How can I update Creatio Messaging Service (formerly Terrasoft Messaging Service)?
------------------------------------------------------------------------------------


1. Contact Creatio support to receive the new version of Creatio Messaging Service installation files or download them via the URL:
 [Download Creatio Messaging Service](https://academy.creatio.com/sites/default/files/documents/downloads/CreatioMessagingService/7.18.0.808.zip) 
 .
2. Save the Terrasoft.Messaging.Service.exe.config settings file.
3. Stop the “TerrasoftMessagingService” service in the Windows Services application.
4. Uninstall Creatio Messaging Service.
5. Restart the phone integration server.
6. Install the new version of Creatio Messaging Service. Unpack the archive to a folder to ensure a smooth installation. If you run the installation directly from the archive, the archiver application may interfere with the install wizard.
7. Compare the settings in the new and the old version. Transfer the settings to the new version if needed.
8. Make sure that the “TerrasoftMessagingService” service is running in the Windows Services application. If the “TerrasoftMessagingService” service is not running, start it manually.
9. Test the phone integration.



 Can I dial an external phone number with an extension external number, bypassing the secretary/answering machine?
-------------------------------------------------------------------------------------------------------------------



 This depends on the settings in the PBX API. Most APIs do not have this function. If the PBX API has this function, you will need to perform additional settings on the phone integration server.
 



 How can I add a custom process to the CTI panel?
--------------------------------------------------



 Products that include the
 [Agent Desktop](/docs/8-0/user/service_tools/contact_center_tools/agent_desktop_setup/overview/general_agent_desktop_settings) 
 functionality come with several
 [business processes](https://academy.creatio.com/docs/user/bpm_tools) 
 out-of-the-box. Agents can run these processes directly from the CTI panel during calls. For example, in service products, these are
 
 Create new case
 
 and
 
 Start consultation for an existing case
 
 processes (Fig. 1).
 





 Fig. 1
 
 Business processes in the CTI panel
 

![scr_section_service_requests_buttons_on_call.png](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_telephony_faq/scr_section_service_requests_buttons_on_call.png)



 To add a business process to the CTI panel, you need to add the process to the
 
 CTI panel actions
 

[lookup](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/lookup_values/manage_lookup_values) 

 . As a result, the process will become available in the
 
 Processes
 
 area of the CTI panel for the Contact Center agents.
 





 Note.
 
 In Creatio, “contact center agents” are users who are members of the
 [organizational role](/docs/7-18/user/setup_and_administration/user_and_access_management/user_management/organizational_roles_shortcut/organizational_roles) 
 specified in the “Folder – Contact Center agents” (ContactCenterOperatorsFolder)
 [system setting](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/manage_system_settings_shortcut/manage_system_settings) 
 . By default, the role is “CC agents.”
 




 Add the following
 
[process parameters](/docs/7-17/user/bpm_tools/business_process_setup/parameters/process_parameters) 

 to bind the process to other Creatio records:
 


* “
 **CallId** 
 ” of the “Unique identifier” data type. This parameter is automatically populated with the unique identifier of the corresponding
 
 Calls
 
 section record.
* “
 **ContactId** 
 ” of the “Lookup” data type. Populate this parameter with the unique ID of the caller/call recipient’s contact.
* “
 **AccountId** 
 ” of the “Lookup” data type. Populate this parameter with the unique ID of the caller/call recipient’s account.
* “
 **PhoneNumber** 
 ” of the “Text (250 characters)” data type. Populate this parameter with the telephone number of the caller/call recipient.



 You can use this data to automatically populate the fields of the new record created during the process execution.
 




