


 To set up an Infinity X integration, take the following steps:
 


1. Prepare Infinity for integration.
 [Read more >>>](#title-1581-1)
2. Set up Creatio Messaging Service (CMS).
 [Read more >>>](#title-1581-2)
3. Set up message exchange library.
 [Read more >>>](#title-1581-3)
4. Set up Infinity X parameters.
 [Read more >>>](#title-1581-4)



 In Creatio, the Infinity integration functionality requires a separate license. You need to generate a license request, send it to our service team, upload the received license file into the system, and distribute the licenses among the users. Learn more in separate articles:
 [Creatio licensing](https://academy.creatio.com/documents?id=1264) 
 ,
 [Manage user licenses](https://academy.creatio.com/documents?id=1472) 
 .
 



 The integration is only possible if complete preliminary Infinity setup was performed by the phone integration administrator.
 





 Attention.
 
 If you set up the telephony for a Creatio production environment, deploy Creatio Messaging Service on a separate node rather than on the Creatio application server. To ensure the fault tolerance of your phone integration, we recommend setting up at least two nodes with Creatio Messaging Service, as well as a balancer that would redirect users in case of lost connection with one of the nodes.
 




 1. Prepare Infinity X
-----------------------



 Create an account in Infinity X with the role “Third-Party integration connection”. This account will be used on the integration service level. It is not recommended to use this user account for other purposes, or log in under this user account, as this may cause integration errors.
 



 2. Set up Creatio Messaging Service (formerly Terrasoft Messaging Service)
----------------------------------------------------------------------------



 The messaging service connects to Infinity and distributes call events between Creatio users.
 





 Attention.
 
 Install Creatio Messaging Service on a .NET Framework Windows server to integrate Infinity X PBX.
 



1. Make sure that your computer runtime environment has the following before installing Creatio Messaging Service (CMS):
 


	* a .NET Framework package version 4.7.2 or later on the server where you are going to install Creatio Messaging Service
	* at least 2 Gb of RAM and 20 Gb of free drive space
2. Send the following files from the “Client” folder created during the Infinity X setup to Creatio support:
	* Cx.Integration.BaseConnector.dll
	* Cx.Integration.AgatInfinityConnectorInterfaces.dll
	* Cx.Integration.AgatInfinityConnectorFactory.dll
3. Creatio support will send you an archive with CMS files to upload and install on the server. Unpack the archive to a folder to ensure a smooth CMS installation. If you run the installation directly from the archive, the install wizard might not operate as intended.
 





 Attention.
 
 Deploy CMS on the server connected to both the Creatio application server and the PBX. Learn more in a separate article:
 [Telephony integration basics](https://academy.creatio.com/documents?id=15751) 
 .
4. Run the Creatio Messaging Service Install.msi file on the machine intended as the message exchange server and proceed with the installation.
5. Make sure that the “TerrasoftMessagingService” service is running in the Windows Services application. If the “TerrasoftMessagingService” service is not running, start it manually.
6. Copy the “Client” folder (created during the Infinity X setup) to a separate folder, e.g., the folder with the CMS service.
7. Open the folder with the service files: ~\BPMonline Messaging Service.
8. Specify the following parameters in the Infinity block of the Terrasoft.Messaging.Service.exe.config file:
 


	1. infinityXClientPath. The path to the “Client” folder. If the “Client” folder is located in the CMS service folder, the parameter value will be as follows: infinityXClientPath="\Client"
	2. thirdPartyIntegrationLogin. The login of the user with the “Third-Party integration connection” role.
	3. thirdPartyIntegrationLogin. The password of the user with the “Third-Party integration connection” role.
9. Restart the “TerrasoftMessagingService” service.
10. Test the phone integration.



 3. Set up the message exchange library
----------------------------------------



 Message exchange library selection and setup is performed once by the system administrator.
 


1. Open the system designer by clicking
 ![btn_system_designer00001.png](/sites/default/files/documents/docs/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_telephony_setup/btn_system_designer00001.png)
 in the top right corner of the application window.
2. Click “System settings” in the “System setup” block.
3. Set the default value of the “Default messages exchange library” (“SysMsgLib” code) system setting to “Telephony integration library based on Infinity protocol”.
4. Specify the message service connection parameters. To do this, open the “Message exchange server” (“SysMsgServerNode” code) system setting. In the
 
 Default value
 
 field, specify the network address of the message exchange server in the following format: “ws://0.0.0.0:2013” if your website is served over HTTP or “wss://0.0.0.0:2013” if your website is served over HTTPS, where:
 


	* “0.0.0.0” is the IP address that your Creatio users use to access your message exchange server.
	* “2013” is the port used by default for connecting to the messaging service. You can change the port number in the “Terrasoft.Messaging.Service.exe.config” file.
	 
	
	
	
	
	
	 Note.
	 
	 If your website is available by HTTPS and secure (WWS) connection is used for WebSockets, you will need to install a security certificate on the message exchange server and specify it in the configuration files of the message service. For more information about the setup process, contact Creatio technical support at support@creatio.com.
5. Click
 
 Save
 
 .



 4. Set up the Infinity parameters
-----------------------------------



 Apply these settings for each Creatio user who received Infinity integration license. Use the user login credentials to access the system.
 


1. Open the user profile page by clicking the
 
 Profile
 
 image button on the main page of the application.
2. Click the
 
 Call Center parameters setup
 
 button. This opens a page.
3. Fill out the required values on the page that opens:
 


	1. Select the
	 
	 Disable Contact Centre integration
	 
	 checkbox to disable Creatio integration with the telephony. The call button will not be displayed on the communication panel of the application.
	2. Specify application IP address and port in the
	 
	 Infinity server address
	 
	 field. Learn more about the ports required for implementing the full functionality of Infinity X in
	 [Creatio Community](https://community.creatio.com/articles/which-ports-are-needed-infinity-x) 
	 .
	3. Specify the telephone number of the line which will be used for the call in the
	 
	 Line
	 
	 field.
	 
	
	
	
	
	
	 Attention.
	 
	 A separate line is used for each user. It is not recommended to specify the same line for several users, as it may cause errors.
	4. Select
	 
	 Enable debugging
	 
	 checkbox to display troubleshooting information within the browser console. This troubleshooting information can be used when the phone integration runs into problems and the customer addresses the service team.
4. Click
 
 Save
 
 .
5. Refresh the browser page to apply the changes.




