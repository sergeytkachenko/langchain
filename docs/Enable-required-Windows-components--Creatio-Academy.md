


 Make sure that you install the following components into the web server before you create and set up a website:
 


* Windows components. Microsoft Visual C++ 2010 component is required.
* Web Server IIS components.



 Required Windows components for Creatio NET Framework
-------------------------------------------------------



 To ensure correct compilation of the application, download and install .NET 6 SDK and .NET Framework SDK v 4.7.2.
 



 Grant permissions to read, create, and delete files and subfolders of the \Terrasoft.WebApp\Terrasoft.Configuration catalog to the user who runs the application pool in IIS.
 



[Download 64-bit .NET 6 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) 




[Download 64-bit .NET Framework SDK v 4.7.2](https://dotnet.microsoft.com/download/thank-you/net472-developer-pack) 






 Attention.
 
 Production environment for Creatio .NET Framework requires a Windows Server OS. You can deploy application server on Windows 10 only for development and pre-production environments.
 






| 
 Component
  | 
 Component items
  |
| --- | --- |
| 
 Common HTTP Features
  | 
 Static Content
 

 Default Document
 

 HTTP Errors
 

 HTTP Redirection
  |
| 
 Application Development
  | 
 ASP.Net
 

 .Net extensibility
 

 ISAPI extensions
 

 ISAPI Filters
 

 WebSocket Protocol
  |
| 
 Microsoft .Net framework 3.5.1
  | 
 Windows Communication Foundation HTTP Activation
 

 Windows Communication Foundation Non-HTTP Activation
  |
| 
 Microsoft .Net Framework 4.7 Advanced Services and up (Windows 8, Windows 10, Windows Server 2012, Windows Server 2016).
  | 
 ASP.NET 4.6.2 or 4.7;
 

 WCF services
 

 HTTP Activation
 

 Message Queuing (MSMQ) Activation
 

 Named Pipe Activation
 

 TCP Activation
 

 TCP Port Sharing
  |
| 
 Health and Diagnostics:
  | 
 HTTP Logging
 

 Logging Tools
 

 Request Monitor
 

 Custom Logging
  |
| 
 Security
  | 
 Basic Authentication
 

 Request Filtering
 

 IP and Domain Restriction
  |




 Required Windows Components for Creatio .NET 6
------------------------------------------------




 This functionality is available for Creatio 8.0.8 and later.
 




 To ensure correct compilation of the application, download and install .NET 6 SDK and .NET 6 Hosting bundle.
 



 Grant permissions to read, create, and delete files and subfolders of the \Terrasoft.WebApp\Terrasoft.Configuration catalog to the user who runs the application pool in IIS.
 



[Download 64-bit .NET 6 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) 




[Download .NET 6 Hosting bundle](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-aspnetcore-6.0.14-windows-hosting-bundle-installer) 






 Attention.
 
 Production environment for Creatio .NET 6 requires a Windows Server OS. You can deploy application server on Windows 10 or Windows 11 only for development and pre-production environments.
 






| 
 Component
  | 
 Component items
  |
| --- | --- |
| 
 Common HTTP Features
  | 
 Static Content
 

 Default Document
 

 HTTP Errors
 

 HTTP Redirection
  |
| 
 Application Development
  | 
 ASP.Net
 

 .Net extensibility
 

 ISAPI extensions
 

 ISAPI Filters
 

 WebSocket Protocol
  |
| 
 Microsoft .Net Framework 4.8 Advanced Services and later
  | 
 Windows Communication Foundation HTTP Activation
 

 Windows Communication Foundation Non-HTTP Activation
  |
| 
 Microsoft .Net Framework 4.7 Advanced Services and up (Windows 8, Windows 10, Windows Server 2012, Windows Server 2016).
  | 
 ASP.NET 4.8;
 

 WCF services
 

 HTTP Activation
 

 Message Queuing (MSMQ) Activation
 

 Named Pipe Activation
 

 TCP Activation
 

 TCP Port Sharing
  |
| 
 Health and Diagnostics:
  | 
 HTTP Logging
 

 Logging Tools
 

 Request Monitor
 

 Custom Logging
  |
| 
 Security
  | 
 Basic Authentication
 

 Request Filtering
 

 IP and Domain Restriction
  |




 Enable required Windows components on Windows Server 2016
-----------------------------------------------------------



 To check the availability of the needed components:
 


1. Enter the “control panel” in the
 
 Start
 
 menu and select
 
 Control Panel
 
 (Fig. 1).
 





 Control Panel
 
 section in the
 
 Start
 
 menu
 

![scr_setup_main_menu_windows_server.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_main_menu_windows_server.png)
2. Select
 
 Turn Windows features on or off
 
 in the control panel (Fig. 2).
 




 Fig. 2 Selecte
 
 Turn Windows features on or off
 


![scr_setup_turn_windows_windows_server.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_turn_windows_windows_server.png)
3. Select
 
 Role-based or feature-based installation
 
 →
 
 Next
 
 in the
 
 Add Roles and Features Wizard
 
 (Fig. 3).
 




 Fig. 3 Select the role-based installation
 

![scr_setup_role_based_model_win2016.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_role_based_model_win2016.png)
4. Select the destination server from the available server pool and click
 
 Next
 
 (Fig. 4).
 




 Fig. 4 Select the destination server
 

![scr_setup_select_destination_server_win2016.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_select_destination_server_win2016.png)
5. Select the “Web Server (IIS)” role to apply to the selected server. Click
 
 Next
 
 (Fig. 5).
 




 Fig. 5 Select the Web Server (IIS) role
 

![scr_setup_server_selecting_iis_role_win2016_next.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_server_selecting_iis_role_win2016_next.png)
6. Click
 
 Add features
 
 (Fig. 6).
 




 Fig. 6 Confirm selected features
 

![scr_setup_server_add_features_win2016.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_server_add_features_win2016.png)
7. Select features and click
 
 Next
 
 (Fig. 7).
 




 Fig. 7 Select features
 

![scr_setup_server_selecting_iis_role_win2016_next_features.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_server_selecting_iis_role_win2016_next_features.png)
8. Click
 
 Next
 
 to proceed to the next step (Fig. 8).
 




 Fig. 8 Confirm the web server role
 

![scr_setup_server_finalize_win2016.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_server_finalize_win2016.png)
9. Make sure that you select the same components as on the Fig. 9.
 




 Fig. 9 Required components
 

![scr_setup_iis_required_componnets_win2016.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_iis_required_componnets_win2016.png)
10. Click
 
 Install
 
 (Fig. 10).
 




 Fig. 10 Confirm installation
 

![scr_setup_installing_iis_win2016.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_installing_iis_win2016.png)
11. Reboot the server.



 Enable required Windows Components on Windows 10
--------------------------------------------------



 To check the availability of the needed components:
 


1. Enter the “control panel” in the
 
 Start
 
 menu and select
 
 Control Panel
 
 (Fig. 11).
 





 Fig. 11
 

 Control Panel
 
 section in the
 
 Start
 
 menu
 

![scr_setup_main_menu.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_main_menu.png)
2. Select the
 
 Programs
 
 option in the control panel (Fig. 12).
 




 Fig. 12
 
 Programs
 
 menu
 

![scr_setup_programs.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_programs.png)
3. Select the
 
 Turn Windows features on or off
 
 option from the
 
 Programs and Features
 
 menu (Fig. 13).
 




 Fig. 13 Select the
 
 Turn Windows features on or off
 
 option
 

![scr_setup_turn_windows.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_turn_windows.png)
4. Select all required components in the
 
 Windows Features
 
 window (Fig. 14).
 




 Fig. 14 Select Web Server IIS and Windows components
 

![scr_setup_turn_windows_on.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/enable_required_windows_components/scr_setup_turn_windows_on.png)




