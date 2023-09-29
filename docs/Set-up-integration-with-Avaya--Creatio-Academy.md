


 To set up an Avaya integration, take the following steps:
 


1. Set up Creatio Messaging Service.
 [Read more >>>](#title-1574-1)
2. Set up the message exchange library.
 [Read more >>>](#title-1574-2)
3. Set up the Avaya parameters.
 [Read more >>>](#title-1574-3)



 In Creatio, the Avaya integration functionality requires a separate license. You need to generate a license request, send it to our service team, upload the received license file into the system, and distribute the licenses among the users. Read more:
 [Creatio licensing](/docs/7-18/user/setup_and_administration/licensing/licensing_overview/creatio_licensing) 
 and
 [Manage user licenses](/docs/7-18/user/setup_and_administration/licensing/manage_licenses/manage_user_licenses) 
 .
 



 The integration is only possible if complete preliminary Avaya setup was performed by the phone integration administrator.
 





 Attention.
 
 If you set up the telephony for a Creatio production environment, deploy Creatio Messaging Service on a separate node rather than on the Creatio application server. To ensure the fault tolerance of your phone integration, we recommend setting up at least two nodes with Creatio Messaging Service, as well as a balancer that would redirect users in case of lost connection with one of the nodes.
 




 1. Set up Creatio Messaging Service (formerly Terrasoft Messaging Service)
----------------------------------------------------------------------------



 The messaging service allows you to connect Creatio to Avaya via the DMCC .NET API integration protocol and distribute the call events between Creatio users.
 





 Attention.
 
 Install Creatio Messaging Service on a .NET Framework Windows server to integrate Avaya PBX.
 




 DMCC .NET API integration protocol requires licenses. The number of licenses should correspond to the number of Creatio users who simultaneously use Avaya phone integration. See
 
[Avaya documentation](https://support.avaya.com/documents/) 

 for more information.
 





 Note.
 
 Your PBX must include Avaya Application Enablement Services (AES) component for Avaya phone integration. The integration is available for AES server version 5.2 and later.
 



1. Before installing Creatio Messaging Service (CMS), make sure that your computer runtime environment has:
 


	* A .NET Framework package version 4.7.2 or later on the server where you are going to install Creatio Messaging Service.
	* At least 2 Gb of RAM and 20 Gb of free drive space.
2. Contact Creatio support to receive the messaging service installation files or download the files via the URL:
 [Download Creatio Messaging Service](https://academy.creatio.com/sites/default/files/documents/downloads/CreatioMessagingService/7.18.0.808.zip) 
 . Unpack the archive to a folder to ensure a smooth installation. If you run the installation directly from the archive, the archiver application may interfere with the install wizard.
 


 Attention.
 
 Deploy CMS on the server connected to both the Creatio application server and the PBX. Read more:
 [Telephony integration basics](/docs/7-18/developer/application_components/telephony_integration/telephony_integration_basics/overview) 
 .
3. Run the Creatio Messaging Service Install.msi file on the machine intended as the message exchange server and proceed with the installation.
4. Make sure that the “TerrasoftMessagingService” service is running in the Windows Services application. If the “TerrasoftMessagingService” service is not running, start it manually.
5. Open the folder with the service files: ~\BPMonline Messaging Service. Specify the following parameters for Avaya connector in the “Terrasoft.Messaging.Service.exe.config” configuration file:
 






```

<avaya serverIp="" port="4721" useSecureSockets="False" ctiUser="" psw="" protocolVersion="http://www.ecma-international.org/standards/ecma-323/csta/ed3/priv6" switchName="CM"
```





 See the
 **list of configuration file parameters** 
 in the table below.
 





| 
 Parameter caption
  | 
 Parameter function
  |
| --- | --- |
| 
 avaya serverIp
  | 
 AES server address.
  |
| 
 port
  | 
 Connection port to AES server. Default value: “4721” for the unsecured connection or “4722” for the secured connection.
  |
| 
 useSecureSockets
  | 
 The checkbox for the encrypted connection usage requires adding a certificate. By default, “False.”
  |
| 
 ctiUser
  | 
 Avaya AES (Avaya AES user login) username.
  |
| 
 psw
  | 
 Avaya AES user password.
  |
| 
 protocolVersion
  | 
 The protocol used to connect to AES server. the default value: “http://www.ecma-international.org/standards/ecma-323/csta/ed3/priv6.”
  |
| 
 switchName
  | 
 Avaya (hostname Avaya switch) hostname switch.
  |
6. Test the phone integration.





 Note.
 
 Follow this
 [instruction](/docs/8-0/user/more_apps/phone_integration_connectors/faq/creatio_phone_integration_faq#title-1974-14) 
 if you need to update the Creatio Messaging Service.
 




 2. Set up the message exchange library
----------------------------------------



 Message exchange library selection and setup is performed once by the system administrator.
 


1. Open the system designer by clicking
 ![btn_system_designer00001.png](/sites/default/files/documents/docs/product/bpm'online%20administration/administration/7.16.0/BPMonlineHelp/chapter_telephony_setup/btn_system_designer00001.png)
 in the top right corner of the application window.
2. Click “System settings” in the “System setup” block.
3. In the “Default messages exchange library” (“SysMsgLib” code) system setting, set the default value to “Telephony integration library based on Avaya (DMCC) protocol.”
4. Specify the message service connection parameters. To do this, open the “Message exchange server” (“SysMsgServerNode” code) system setting. In the
 
 Default value
 
 field, specify the message exchange network address in the following format: “ws://0.0.0.0:2013” if your website is served over HTTP or “wss://0.0.0.0:2013” if your website is served over HTTPS, where:
 


	* “0.0.0.0” – IP address that your Creatio users use to access your message exchange server.
	* “2013” – the port used by default for connecting to the messaging service. You can change the port number in the “Terrasoft.Messaging.Service.exe.config” file.


 Note.
 
 If your website is served over HTTPS and secure (WSS) connection is used for WebSockets, you will need to install a security certificate on the message exchange server and specify it in the configuration files of the message service. Learn more:
 [Configure a WSS phone service connection](https://academy.creatio.com/documents?id=1755) 
 .
5. Click
 
 Save
 
 .



 3. Set up the Avaya parameters
--------------------------------



 These settings should be applied for each Creatio user who received Avaya integration license. Use the user login credentials to access the system.
 


1. Open the user profile page by clicking the
 
 Profile
 
 image button on the main page of the application.
2. Click the
 
 Call Center parameters setup
 
 button.
3. On the opened page, fill out the required values:
 


	1. Disable Call Center integration
	 
	 – this checkbox allows you to disable Creatio integration with the phone integration. The call button will not be displayed on the communication panel of the application.
	2. Agent's Id
	 
	 ,
	 
	 Password
	 
	 – agent's data on Avaya server.
	3. Number
	 
	 – agent's number on the Avaya server.
	4. Enable debugging
	 
	 – this checkbox allows you to display troubleshooting information within the browser console. This troubleshooting information can be used when the phone integration runs into problems and the customer addresses the service team.
4. Click
 
 Save
 
 .
5. Refresh the browser page to apply the changes.




