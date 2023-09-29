


 Setting up Creatio application server (web server) on IIS involves setting up application website in IIS and adding an application pool.
 





 Note.
 
 .NET 6 application deployment is available for Creatio 8.0.8 and later.
 




 Add an application pool
-------------------------



 To add an application pool:
 


1. Go to the
 
 Application Pools
 
 section in the
 
 Connections
 
 area of the IIS control window.
2. Select the
 
 Creatio
 
 pool.
3. Select the
 
 Integrated
 
 mode in the
 
 Managed pipeline mode
 
 field.
4. Fill out the
 
 .NET CLR version
 
 field:
 




 Fig. 1 Window for Applications Pool parameters
 

![scr_setup_applications_tool.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_applications_tool.png)


	* Specify “.NET CLR Version v.4.0.30319” for
	 **.NET Framework** 
	 .
	* Specify “No Managed Code” for
	 **.NET 6** 
	 .
5. Go to the ISAPI and CGI Restrictions on the web server level (Fig. 2) and check if the specified ASP.NET version is allowed.
 




 Fig. 2 ISAPI and CGI Restrictions menu
 

![scr_setup_isapi.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_isapi.png)
6. Make sure that the
 
 Allowed
 
 status is set in the
 
 Restriction
 
 field for the ASP.NET version (Fig. 3).
 




 Fig. 3 Status of the ASP.NET version
 

![scr_setup_isapi_allowed.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_isapi_allowed.png)
7. Open the Handler Mappings on the server level and make sure that all the required permissions are active (Fig. 48).
 




 Fig. 4 Handler Mappings menu
 

![scr_setup_handler.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_handler.png)
8. Click
 
 Edit Feature Permissions
 
 in the
 
 Actions
 
 area.
9. Make sure that all the required checkboxes are selected in the
 
 Edit Feature Permissions
 
 window (Fig. 5).
 




 Fig. 5
 
 Edit Feature Permissions
 
 window
 

![scr_setup_handler_settings.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_handler_settings.png)
10. Make sure that MIME-type for .svg and .json files is configured in the new application. This configuration can be performed both on the server (in this case, all applications on this server inherit it) and application level. To check the configuration:
 


	1. Go to MIME Types on the server or application level (Fig. 6).
	 
	
	
	
	
	 Fig. 6 MIME Types menu
	 
	
	![scr_setup_mime.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_mime.png)
	2. Make sure that configuration for .svg and .json files is available. If the configuration is available, go to step 12.
11. If the configuration is not available, click
 
 Add…
 
 in the
 
 Actions
 
 area. This opens a new window. Specify .svg and MIME type of data that corresponds to this extension (Fig. 7) in the window. Repeat the step for .json extension (“application/json” MIME type).
 




 Fig. 7 MIME data type for .svg files
 

![scr_setup_mime_add_svg.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_mime_add_svg.png)
12. Restart the website using the
 
 Restart
 
 command in the
 
 Manage Website
 
 area (Fig. 8).
 




 Fig. 8
 
 Restart
 
 command in the
 
 Manage Websites
 
 area
 

![scr_setup_restart_website.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_restart_website.png)
13. Open the site by going to the address or using the
 
 Browse
 
 command (Fig. 9). Make sure that the Creatio login page is displayed.
 




 Fig. 9
 
 Browse
 
 command in the
 
 Actions
 
 area
 

![scr_setup_browse.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_browse.png)





 Note.
 
 To log in to a newly deployed application, use the default Supervisor user account. Login: Supervisor; Password: Supervisor. We highly recommend changing the Supervisor password immediately.
14. To enable additional UI language:
 


	1. Go to the
	 
	 Languages
	 
	 section in the system designer.
	2. Select the needed language and click
	 
	 Open
	 
	 . This opens a page.
	3. Select the
	 
	 Active
	 
	 and
	 
	 Use by default
	 
	 checkboxes. Save the changes.
	 
	
	
	
	 To enable a language, the user who has run the IIS application pool needs to have access permissions to read, edit and delete application files and content subordinate catalogs (catalog .\Terrasoft.WebApp\conf).
15. Click
 
 System settings
 
 in the System Designer and change the
 
 Order of first/last names
 
 system setting value to “Last name, First name
 
 Middle name
 
 .” This is required to correctly display contact names in individual columns:
 
 Last name
 
 ,
 
 First name
 
 ,
 
 Middle name
 
 .



 Set up application website in IIS
-----------------------------------



 To create and set up a website:
 


1. Go to the IIS control window, right-click the
 
 Sites
 
 folder, and select the
 
 Add Website
 
 option from the context menu (Fig. 10).
 




 Fig. 10 The
 
 Add website
 
 option
 

![scr_setup_add_website.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_add_website.png)
2. Specify the name of the website, the path to the root folder that contains Creatio files, IP address and website port (Fig. 11). The default website path is C:\INETpub\wwwroot. If needed, specify your own IP address.
 




 Fig. 11 New website parameters window
 

![scr_setup_add_web_site_parametres.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_add_web_site_parametres.png)
3. For NET Framework only
 


 Right-click the created website in the
 
 Connections
 
 area and select the
 
 Add Application
 
 option (Fig. 12).
 




 Fig. 12
 
 Add Application
 
 option
 

![scr_setup_add_application.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_add_application.png)
4. Enter the “0” application name in the
 
 Alias
 
 field. Specify the “Terrasoft.WEBApp” directory (Fig. 13).
 




 Fig. 13 Application parameter selection window
 

![scr_setup_add_applications_settings.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_app_server_on_IIS/scr_setup_add_applications_settings.png)




