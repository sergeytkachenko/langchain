


 You can configure a WSS phone service connection. This procedure is relevant for Asterisk, Avaya, TAPI, CallWay, and Infinity phone service users.
 





 Note.
 
 Configure the
 [WebSockets technology](/docs/8-0/user/on_site_deployment/application_server_on_windows/set_up_websockets_shortcut/set_up_websockets) 
 to ensure the correct operation of the phone service in Creatio.
 




 Modify the
 **Terrasoft.Messaging.Service.exe.config** 
 configuration file on the phone server to configure the secure connection with the phone service:
 


1. Delete or comment out the following configuration block in the <servers> section:
 



```

<server name="ClientWebSocketService"

serviceName="ClientWebSocketService" ip="Any" port="2013" mode="Tcp"

idleSessionTimeOut="10000" maxCommandLength="4096"

maxConnectionNumber="10000">

</server>
```
2. Contact an official certification center to receive a PFX certificate. A system administrator must obtain the certificate.
3. Remove the comment from the following block in the <servers> section:
 



```

<server name="ClientWebSocketService"

serviceName="ClientWebSocketService" ip="Any" port="2013" mode="Tcp"

 idleSessionTimeOut="10000" maxCommandLength="4096" security="tls" >



   <certificate filePath="certificate.pfx" password="111"></certificate>

</server>
```
4. Specify the PFX digital certificate you received from the certification center, as well as the access password in the <certificate> section. Place the certificate in the folder with the Creatio Messaging Service binary files.
 





 Attention.
 
 It is not recommended to use self-signed certificates, because this may violate security conditions.
5. After modifying the configuration file, change the address of the connection to the phone server in the “Message exchange server” (“SysMsgServerNode” code)
 [system setting](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/manage_system_settings_shortcut/manage_system_settings) 
 from ws:// to
 **wss://** 
 .




