



 This article describes integration with Cisco Finesse version 11.5 and later. We recommend using new phone service versions to ensure secure and reliable operation. If you need to set up integration with Cisco Finesse version 11.0 and earlier for testing purposes or to look for errors, follow the
 [instructions for Creatio version 7.16](https://academy.creatio.com/documents?product=administration&ver=7.16&id=1369) 
 .
 




 To set up integration with Cisco Finesse, take the following steps:
 


1. Set up the service message exchange library.
 [Read more >>>](#title-1576-2)
2. Set up the Cisco Finesse parameters
 [Read more >>>](#title-1576-3)



 In Creatio, the Cisco Finesse integration functionality requires a separate license. To license the phone service, generate a license request, send it to our support team, upload the received license file to Creatio, and distribute the licenses among users. Learn more in separate articles:
 [Creatio licensing](https://academy.creatio.com/documents?id=1264) 
 ,
 [Manage user licenses](https://academy.creatio.com/documents?id=1472) 
 .
 



 Before you set up the integration, make sure that the phone service administrator has already configured Cisco Finesse.
 





 Attention.
 
 To ensure the integration operates as intended, enable the
 [CORS technology](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1201/Admin/guide/cfin_b_1201-administration-guide-release-1201/cfin_b_1201-administration-guide-release-1201_appendix_01111.html#reference_F298A59463A427B9D63A327832964A76) 
 support in Cisco Finesse settings. You can do this using the following commands
 




 utils finesse cors enable\_all
 





 utils service restart Cisco Finesse Tomcat
 





 utils service restart Unified CCX Notification Service
 





 Select the message exchange library
-------------------------------------



 The setup is performed once by the system administrator.
 


1. Open the System Designer, e. g., by clicking
 ![btn_system_designer00001.png](/docs/sites/en/files/images/More_Apps/phone_integration_connectors/cisco_finesse/btn_system_designer00001.png)
 in the top right.
2. Click “System settings” in the “System setup” block.
3. Set the “Default messages exchange library” (“SysMsgLib” code) system setting to “Cisco Finesse telephony integration library (Finesse 11.5+).”
4. Click
 
 Save
 
 .



 Set up the Cisco Finesse parameters
-------------------------------------



 Set up the common parameters
------------------------------



 The setup is performed once by the system administrator for all Creatio users.
 


1. Open the System Designer, e. g., by clicking
 ![btn_system_designer00001.png](/docs/sites/en/files/images/More_Apps/phone_integration_connectors/cisco_finesse/btn_system_designer00001.png)
 in the top right.
2. Click “System settings” in the “System setup” block.
3. Specify the address of your Cisco Finesse server in the “Finesse 11.5+ server address” (“FinesseServerAddress” code) system setting. Use the following format: https://
 
 :8445. For example, https://hq-uccx.abc.inc:8445.
4. Click
 
 Save
 
 .
5. Specify the WSS protocol address of your Cisco Finesse server in the “Finesse 11.5+ websocket address” (“FinesseWebsocketAddress” code) system setting. Use the following format: wss://
 
 :8445. For example, wss://hq-uccx.abc.inc:8445.
6. Click
 
 Save
 
 .



 Set up the individual parameters
----------------------------------



 The setup is performed for each Creatio user who received the Cisco Finesse integration license. Use the user login credentials to log in to Creatio.
 


1. Open the user profile page, e. g., by clicking
 
 Your profile
 
 on the Creatio homepage.
2. Click
 
 Call Center parameters setup
 
 . This opens a page.
3. Fill out the required fields:
 


	1. Select the
	 
	 Disable Contact Centre integration
	 
	 checkbox to disable Creatio integration with the phone service. This hides the call button from the Creatio communication panel.
	2. Specify the Cisco Finesse user parameters in the
	 
	 Agent Id
	 
	 ,
	 
	 Extension
	 
	 ,
	 
	 Password
	 
	 fields.
	3. Select
	 
	 Enable debugging
	 
	 checkbox to display troubleshooting information within the browser console. For example, you can use the information if you encounter phone service and customer contact issues.
4. Click
 
 Save
 
 .
5. Refresh the browser page to apply the changes.




