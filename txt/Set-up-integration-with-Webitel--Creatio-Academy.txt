

### 



 Available Webitel base phone integration settings



 Webitel phone integration is a built-in service and is available for internal calls without the need for additional setup. To make and receive external calls in Webitel, you will need to install the Webitel connector from the Creatio marketplace and set up the phone integration. More information about the installation of the marketplace applications is available in the
 
[separate article](/docs/7-18/user/customization_tools/marketplace_applications/install_applications_from_the_marketplace) 

 .
 






 Note.
 
 If you purchase Webitel Call Manager cloud, all setup will be performed by Webitel support. If you purchase Webitel Call Manager on-site, you can order setup service from Webitel or study the
 
[requirements](https://docs.webitel.com/display/WEBITEL/System+requirements) 

 and perform the setup according to the
 
[Webitel setup guide](https://docs.webitel.com/display/WEBITEL/Instalation+on+local+Server) 

 .
 





 A green indicator at the top right corner of the application indicates that phone integration runs correctly in Creatio (
 [Fig. 1](#XREF_66311_117)
 ).
 





 Fig. 1
 

 Agent status indicator
 

[![scr_chapter_telephony_setup_status_indicator.png](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_telephony_setup/scr_chapter_telephony_setup_status_indicator.png)](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_telephony_setup/scr_chapter_telephony_setup_status_indicator.png)



 To work with the service, populate the “Webitel users” lookup. You have to register your company's employees in Creatio to enable them to make internal calls directly from the application.
 






 Note.
 
 See more details on how to register Creatio users in the “
 
[Add a new user in Creatio](/docs/7-17/user/setup_and_administration/user_and_access_management/user_management/add_users_shortcut/add_users#title-287-2) 

 ” article.
 





 When adding a Creatio user, the system will automatically assign a Webitel extension number. It will be displayed on the
 **Communication options** 
 detail of the contact page. By default, the phone number assignment starts from 100. Upon the next user registration, the following ordinal numbers will be assigned, for example, 101, 102, 103, etc.
 






 Note.
 
 The telephone number is generated automatically based on the specified template. You can change the auto-numbering using the "Webitel user number mask" system setting.
 




### 
 Setting up Webitel internal phone parameters


1. Open the user profile page by clicking the
 
 Profile
 
 image button on the main page of the application.


1. Click the
 
 Call Center parameters setup
 
 button.


1. Select or remove the required checkboxes:
 


	1. Disable Contact Center integration
	 
	 – select to disable a built-in Webitel integration. The call button will not be displayed on the communication panel of the application.
	2. Enable debugging
	 
	 – this checkbox allows you to display troubleshooting information within the browser console. This troubleshooting information can be used when the phone integration runs into problems and the customer addresses the service team.
	3. Use Web phone
	 
	 – this checkbox enables you to use a webphone. Clear the checkbox if you need to use the down-line phone.
	4. Use video
	 
	 – this checkbox enables making video calls on internal numbers.


1. Click
 
 Save
 
 .


1. Refresh the browser page to apply the changes.




