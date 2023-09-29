


 Creatio uses the WebSocket protocol to run custom processes, manage notifications, and integrate with telephony. To ensure all system functions operate correctly, enable WebSockets and configure them on the Creatio application server.
 



 The application server must have
 **Windows Server 2012** 
 ,
 **Windows Server 2016** 
 or
 **Windows 8/10** 
 deployed and Internet Information Services (IIS) version 8 or later installed. Creatio configuration files are set up out-of-the-box. You only need to perform the setup on the server side. However, if you deploy and set up Creatio for the first time, we recommend that you check the configuration file settings and make sure that the WebSockets operate correctly. Learn more:
 [Check WebSocket settings for Windows Server 2012 or Windows server 2016](https://academy.creatio.com/documents?id=1631&anchor=title-271-1) 
 .
 



 To use the encrypted HTTPS connection, perform additional setup. Learn more in a separate article:
 [Switch a Creatio website from HTTP to HTTPS](https://academy.creatio.com/documents?id=1632) 
 .
 





 Attention.
 
 If you use a proxy server in your local network, set it up to proxy the WebSocket protocol. The setup instructions are normally available in the proxy server documentation.
 




 This article covers the WebSocket setup procedure on the application side
 **in Creatio configuration files** 
 .
 





 Note.
 
 Learn more about installing components that enable WebSocket protocol into the server in a separate article:
 [Enable required Windows components](https://academy.creatio.com/documents?id=2081) 
 .
 




 Check WebSocket settings for Windows Server 2012 or Windows Server 2016
-------------------------------------------------------------------------



 To check WebSocket settings in Creatio deployed on a server running Windows Server 2012 or Windows Server 2016:
 


1. Open the Web.config file in the Creatio root directory and make sure inheritance is disabled. The request length limits and execution timeout must also be specified.
 






```

<location path="." inheritInChildApplications="false">
    <system.web>
      ...
      <httpRuntime maxRequestLength="73400" executionTimeout="28800" targetFramework="4.7" />
```
2. Open the Web.config file in
 
 Path to Creatio root folder
 
 \Terrasoft.WebApp\ directory and make sure the default wsService type value is “
 **Terrasoft.Messaging.MicrosoftWSService.MicrosoftWSService, Terrasoft.Messaging.MicrosoftWSService** 
 ”. The HTTP request length and execution timeouts, as well as additional module calls, must also be specified.
 





 Attention.
 
 We recommend using “MicrosoftWSService” instead of “SuperWSService” for Microsoft Windows Server 2012.
 






 Note.
 
 The portForClientConnection="0" value means the web application port is used.
 







```

<wsService type="Terrasoft.Messaging.MicrosoftWSService.MicrosoftWSService,
Terrasoft.Messaging.MicrosoftWSService" encrypted="false" portForClientConnection="0" />
...
<location path="." inheritInChildApplications="false">
    <system.web>
     ...
      <httpRuntime maxRequestLength="102400" executionTimeout="28800"
 targetFramework="4.6.2" />
      <httpHandlers>
        ...
        <add verb="GET" path="*ViewModule.aspx.ashx" type="Terrasoft.Messaging.MicrosoftWSService.WSHandler,
Terrasoft.Messaging.MicrosoftWSService" />
...
<system.webServer>
    ...
    <handlers>
      ...
      <add name="WSHandler" verb="*" path="*ViewModule.aspx.ashx"
type="Terrasoft.Messaging.MicrosoftWSService.WSHandler, Terrasoft.Messaging.MicrosoftWSService" />

```







 Note.
 
 You can check the WebSocket connection in the browser console. If the connection is successful, the console will contain a record in the following format: WebSocket-connection opened for url:ws://demo.creatio.com/0/Nui/ViewModule.aspx.ashx



 WebSocket setup FAQ
---------------------


### 
 How can I make sure the WebSockets are set up correctly?



 You can make sure the WebSockets are set up correctly in several ways:
 


* Use the
 [Excel data import](https://academy.creatio.com/documents?id=1252) 
 functionality. If the WebSockets are set up correctly, Creatio will import the data.
* Run the following command at the browser console: Terrasoft.ServerChannel.ping(). If the WebSockets are set up correctly, the server will return “pong” (Fig. 1). If the server returns any other response, review the WebSocket configuration.
 

 Fig. 1 Test the WebSocket setup using the browser console
 

![scr_chapter_websockets_check_working.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/setup_websockets/scr_chapter_websockets_check_working.png)
* Manually run a business process that contains the start timer and auto-generated page. If the WebSockets are set up correctly, the auto-generated page will open.





 Note.
 
 Learn more about business process elements in a separate guide:
 [Process elements reference](https://academy.creatio.com/docs/user/bpm_tools/process_elements_reference) 
 .
 



### 
 I set up WebSockets, but they will not work. Why?



 If the WebSockets will not work after the setup, make sure:
 


* The server has all WebSocket protocol components deployed. Learn more in a separate article:
 [Enable required Windows components](https://academy.creatio.com/documents?id=2081) 
 .
* The WebSocket usage protocol is installed into the proxy server if you use it in your local network.
* Your antivirus and firewall do not block the WebSocket operation. If you cannot disable these programs on the server, add the IP address and port of your Creatio site to the list of exceptions for inbound and outbound connections.
* Your browser extensions and add-ons, including VPN, do not block the WebSocket operation.




