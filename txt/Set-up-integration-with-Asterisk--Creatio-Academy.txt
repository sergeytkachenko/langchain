


 To set up an Asterisk integration, take the following steps:
 


1. Prepare Asterisk for integration.
 [Read more >>>](#title-2358-1)
2. Set up Creatio Messaging Service.
 [Read more >>>](#title-2358-3)
3. Set up the message exchange library.
 [Read more >>>](#title-2358-4)
4. Set up the Asterisk parameters.
 [Read more >>>](#title-2358-5)



 In Creatio, the Asterisk integration functionality requires a separate license. You need to generate a license request, send it to our support team, upload the received license file into the system, and distribute the licenses among users. Learn more in separate articles:
 [Creatio licensing](https://academy.creatio.com/documents?id=1264) 
 and
 [Manage user licenses](https://academy.creatio.com/documents?id=1472) 
 .
 



 The integration is only possible if complete preliminary Asterisk setup was performed by the phone integration administrator.
 





 Attention.
 
 If you set up the telephony for a Creatio production environment, deploy Creatio Messaging Service on a separate node rather than on the Creatio application server. To ensure the fault tolerance of your phone integration, we recommend setting up at least two nodes with Creatio Messaging Service as well as a balancer that redirects users in case connection with one of the nodes is lost.
 




 1. Prepare Asterisk for integration
-------------------------------------



 The
 **AMI (Asterisk Manager Interface)** 
 interface interacts with Asterisk. Use AMI to connect to Asterisk servers, configure and manage client programs.
 



 To prepare Asterisk for integration, create an AMI user for Creatio by specifying their parameters in the
 **manager.conf** 
 file, for example:
 






```

[creatio]
secret = creatio
deny=0.0.0.0/0.0.0.0
permit=0.0.0.0/0.0.0.0
read = call,agent,originate
write = call,agent,originate

```





 Replace the
 
 deny
 
 and
 
 permit
 
 values with the corresponding addresses.
 





 Attention.
 
 Software phones or agent phones can place calls on hold. Communication panel handles the call status change. The panel indicates that calls are placed on hold and resumed, but it cannot place calls on hold.
 




 2. Set up Creatio Messaging Service (formerly Terrasoft Messaging Service)
----------------------------------------------------------------------------



 The messaging service lets you connect Creatio to Asterisk via AMI protocol and distribute call events between Creatio users. Some of the settings differ depending on the platform on which the Asterisk telephony service is deployed: .NET Framework or .NET Core or .NET 6.
 


### 
 Set up Creatio Messaging Service on .NET Framework


1. Before installing the Creatio Messaging Service (CMS), make sure that your computer runtime environment meets the software requirements:
 


	* a .NET Framework package version 4.7.2 or later on the server where you are going to install Creatio Messaging Service
	* at least 2 Gb of RAM and 20 Gb of free drive space
2. Contact Creatio support to receive the messaging service installation files or download the files via the URL:
 [Download the archive](https://academy.creatio.com/sites/default/files/documents/downloads/CreatioMessagingService/8.0.1.199.zip) 
 . Unpack the archive to a folder to ensure a smooth installation. If you run the installation directly from the archive, the archiver application might interfere with the install wizard.
 





 Attention.
 
 Deploy CMS on the server connected to both the Creatio application server and the PBX. Learn more in a separate article:
 [Telephony integration basics](https://academy.creatio.com/documents?id=15751) 
 .
3. Run the
 **Creatio Messaging Service Install.msi** 
 file on the machine intended as the message exchange server and proceed with the installation.
4. Make sure that the
 **TerrasoftMessagingService** 
 service is running in the Windows Services application. If the
 **TerrasoftMessagingService** 
 service is not running, start it manually.
5. Open the folder that contains the service files: ~\Terrasoft Messaging Service. Specify the following parameters for Asterisk connector in the
 **Terrasoft.Messaging.Service.exe.config** 
 configuration file:
 






```

<asterisk filePath="" url="Asterisk server name or URL" port="Asterisk server port" userName="Asterisk login" secret="Asterisk password" originateContext="Outbound context" autoPauseOnCommutationStart="true" queueExtensionFormat="Local/{0}@from-queue/n" asyncOriginate="true" sendRingStartedOnRingingState="true" traceQueuesState="false" protocol="The protocol type used: SIP/ or PJSIP/" packetInfoConfig="Additional packet parameters to handle within the configuration" />

```




```

<asterisk filePath="" url="10.0.15.185" port="5038" userName="creatio" secret="creatio" originateContext="from-internal" autoPauseOnCommutationStart="true" queueExtensionFormat="Local/{0}@from-queue/n" asyncOriginate="true" sendRingStartedOnRingingState="true" traceQueuesState="false" protocol="PJSIP/" packetInfoConfig=""/>

```





 See the
 **index of Asterisk connector parameters** 
 in the following table:
 





| 
 Parameter caption
  | 
 Parameter function
  |
| --- | --- |
| 
 filePath
  | 
 Use the parameter for system diagnostics. It lets you repeat a set of events from the pre-configured scenario file. The default value must be empty.
  |
| 
 url
  | 
 The IP address of the Asterisk server.
  |
| 
 port
  | 
 AMI protocol port. By default,
 
 5038
 
 .
  |
| 
 originateContext
  | 
 Initiates a call to a phone number from Creatio. Contains the name of the context from which to call the user phone number. The default value for FreePBX is
 
 from-internal
 
 .
  |
| 
 autoPauseOnCommutationStart
  | 
 Ensures Asterisk queues work as intended. If enabled, Creatio puts the agent on a pause in all queues after they answer a call. Required to avoid the agent getting a second call while handling the first call or putting the first call on hold.
  |
| 
 queueExtensionFormat
  | 
 The format that determines the call channel while receiving calls from the queue. The default value for LocalChannel in FreePBX is
 
 Local/{0}@from-queue
 
 .
  |
| 
 sendRingStartedOnRingingState
  | 
 Ensures the call retrieval from the queue is handled correctly. If you select the checkbox, Creatio displays the call for the user after receiving the
 
 NewState
 
 AMI event that has the
 
 Ringing
 
 parameter. By default, “On.”
  |
| 
 traceQueuesState
  | 
 Diagnoses the agent status in the queue. Use the parameter to debug the queue if the agent receives a second call from the queue while handling the first call in Creatio. Agent status data is written to the connector log file. By default, “Off.”
  |
| 
 protocol
  | 
 The protocol type: SIP or PJSIP. Contact your PBX administrator to find out the needed protocol type.
  |
6. Restart the CMS and test the phone integration. The connection to Asterisk is established on CMS startup but packet handling begins after an agent goes online.





 Note.
 
 Follow this
 [instruction](https://academy.creatio.com/documents?id=2343&anchor=title-1974-14) 
 if you need to update Creatio Messaging Service.
 







### 
 Set up Creatio Messaging Service on .NET Core or .NET 6





 Attention.
 
 You can set up Messaging Host (Creatio Messaging Service) on .NET Core in Creatio version 7.16.3 – 8.0.8. Support for .NET Core 3.1 will be retired in Creatio version 8.0.9. We recommend moving to .NET 6 when updating Creatio to version 8.0.8. You can set up Messaging Host (Creatio Messaging Service) on .NET 6 in Creatio version 8.0.8 and later.
 



1. Install Docker. To install Docker on Linux, follow the guide in the
 [Docker documentation](https://docs.docker.com/install/) 
 . To check the installed Docker version, run the following command at the Linux terminal:
 






```

docker --version

```
2. Install Docker Compose. To install Docker Compose on Linux, follow the guide in the
 [Docker documentation](https://docs.docker.com/install/) 
 . To check the installed Docker Compose version, run the following command at the Linux terminal:
 






```

docker-compose --version

```
3. Install and set up the Docker Compose components. Deploy the container of the messaging service via the Docker Compose utility. Download the archive via the following link:
 [Download the archive](https://academy.creatio.com/sites/default/files/documents/downloads/messaging.host.docker-compose.7.16.3.1.zip) 
 . Unpack the archive that contains the configuration files and scripts to any directory, for example, /opt/messaging.host.
 





 Note.
 
 The configuration files contain all necessary default settings for a Linux-based server.
 




**The structure of the archive that contains the configuration files and scripts** 
 :
 



**/etc/** 




**...\appsettings.json** 
 : service configuration.
 



**...\nlog.config** 
 : setup of the service logging level.
 



**docker-compose.yml** 
 : configuration of the Docker Compose utility.
 



**.env** 
 : environment variables to run the components.
4. Use Linux terminal to go to the /docker-compose directory of the unpacked archive, for example, /opt/messaging.host/docker-compose.
5. Run the
 
 sudo docker-compose pull
 
 command at the terminal. Wait until the required service component images are downloaded from the
 [Docker Hub](https://hub.docker.com/) 
 completely.
 





 Attention.
 
 If the server Internet access is restricted, download the needed images manually to a machine that has free access (see the docker-compose.yml configuration file) and transfer the images as files to the target machine using the
 [sudo docker export](https://docs.docker.com/engine/reference/commandline/export/) 
 and
 [sudo docker import](https://docs.docker.com/engine/reference/commandline/import/) 
 commands.
6. Specify the following parameters for Asterisk connector in the
 **etc/appsettings.json** 
 configuration file:
 






```

{
    "url": "Asterisk server name or URL",
    "port": "Asterisk server port",
    "userName": "Asterisk login",
    "secret": "Asterisk password",
    "originateContext": "Outbound context",
    "autoPauseOnCommutationStart": "true",
    "queueExtensionFormat": "Local/{0}@from-queue/n",
    "asyncOriginate": "true",
    "sendRingStartedOnRingingState": "true",
    "traceQueuesState": "false",
    "protocol": "The protocol type used: SIP/ or PJSIP/",
    "packetInfoConfig": "Additional packet parameters to handle within the configuration",
    "filePath": ""
}

```




```

{
    "url": "10.0.15.185",
    "port": "5038",
    "userName": "creatio",
    "secret": "creatio",
    "originateContext": "from-internal",
    "autoPauseOnCommutationStart": "true",
    "queueExtensionFormat": "Local/{0}@from-queue/n",
    "asyncOriginate": "true",
    "sendRingStartedOnRingingState": "true",
    "traceQueuesState": "false",
    "protocol": "PJSIP/",
    "packetInfoConfig": "",
    "filePath": ""
}

```
7. Run the
 
 sudo docker-compose up -d
 
 command to launch the service. A logs directory will be created in the current catalog.
 



 See the
 **list of Asterisk connector parameters** 
 in the following table:
 





| 
 Parameter caption
  | 
 Parameter function
  |
| --- | --- |
| 
 url
  | 
 The IP address of the Asterisk server.
  |
| 
 port
  | 
 AMI protocol port. By default,
 
 5038
 
 .
  |
| 
 originateContext
  | 
 Initiates a call to a phone number from Creatio. Contains the name of the context from which to call the user phone number. The default value for FreePBX is
 
 from-internal
 
 .
  |
| 
 autoPauseOnCommutationStart
  | 
 Ensures Asterisk queues work as intended. If enabled, Creatio puts the agent on a pause in all queues after they answer a call. Required to avoid the agent getting a second call while handling the first call or putting the first call on hold.
  |
| 
 queueExtensionFormat
  | 
 The call channel format while receiving the call from the queue. The default value for LocalChannel in FreePBX is
 
 Local/{0}@from-queue
 
 .
  |
| 
 sendRingStartedOnRingingState
  | 
 Ensures the call retrieval from the queue is handled correctly. If you select the checkbox, Creatio displays the call for the user after receiving the
 
 NewState
 
 AMI event that has the
 
 Ringing
 
 parameter. By default, “On.”
  |
| 
 traceQueuesState
  | 
 Diagnoses the agent status in the queue. Use the parameter to debug the queue if the agent receives a second call from the queue while handling the first call in Creatio. Agent status data is written to the connector log file. The default value is “Off”.
  |
| 
 protocol
  | 
 The protocol type: SIP or PJSIP. Contact your PBX administrator to find out the needed protocol type.
  |
| 
 filePath
  | 
 Use the parameter for system diagnostics. It lets you repeat a set of events from the pre-configured scenario file. The default value must be empty.
  |
8. Restart the CMS and test the phone integration. The connection to Asterisk is established on CMS startup but packet handling begins after an agent goes online.



 3. Set up the message exchange library
----------------------------------------



 Message exchange library selection and setup is performed once by the system administrator. Some of the settings differ depending on the platform on which the Asterisk telephony service is deployed: NET Framework or .NET Core or .NET 6.
 


### 
 Set up the library on .NET Framework


1. Open the
 
 System Designer
 
 , for example, by clicking
 ![btn_system_designer00001.png](/sites/default/files/documents/docs/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_telephony_setup/btn_system_designer00001.png)
 in the top right corner of the application.
2. Click “System settings” in the “System setup” block.
3. Open the “Default messages exchange library” (“SysMsgLib” code) system setting and set its default value to “Asterisk 13/16/18 (AMI) telephony integration library.”
4. Open the “Message exchange server” (“SysMsgServerNode” code) system setting and specify the connection parameters of the system messages service. Specify the network address of the message exchange server in the
 
 Default value
 
 field. Use the following format: “ws://
 
 server
 
 :2013” for sites served over HTTP or “wss://
 
 server
 
 :2013” for sites served over HTTPS, where:
 


	* server
	 
	 is the domain name of the server that hosts the message exchange service. We do not recommend using IP addresses or “localhost.”
	* 2013
	 
	 is the default port to connect to the messaging service. You can change the port number in the
	 **Terrasoft.Messaging.Service.exe.config** 
	 file. We do not recommend using “localhost” as it might cause errors when connecting to the phone integration server. When using a wss connection, make sure that server address matches the address in the SSL certificate.


 Note.
 
 If your website is served over HTTPS and secure (WSS) connection is used for WebSockets, install a security certificate on the message exchange server and specify the certificate in the configuration files of the message service. For more information about the setup process, contact Creatio support.


### 
 Set up the library on .NET Core or .NET 6





 ATTENTION.
 
 You can set up Messaging Host on .NET Core in Creatio version 7.16.3 – 8.0.8. Support for .NET Core 3.1 will be retired in Creatio version 8.0.9. We recommend moving to .NET 6 when updating Creatio to version 8.0.8. You can set up Messaging Host on .NET 6 in Creatio version 8.0.8 and later.
 



1. Open the
 
 System Designer
 
 , for example, by clicking
 ![btn_system_designer00003.png](/sites/default/files/documents/docs/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_telephony_setup/btn_system_designer00003.png)
 in the top right corner of the application.
2. Click “System settings” in the “System setup” block.
3. Open the “Default messages exchange library” (“SysMsgLib” code) system setting and set its default value to “Asterisk 13/16/18 (AMI) telephony integration library.”
4. Open the “Message exchange server” (“SysMsgServerNode” code) system setting and specify the connection parameters of the message service. Specify the network address of the message exchange server in the
 
 Default value
 
 field. Use the following format: “http://
 
 server
 
 :2013” for sites served over HTTP or “http://
 
 server
 
 :2014” for sites served over HTTPS, where:
 


	* server
	 
	 is the domain name of the server that hosts the message exchange service. We do not recommend using IP addresses or “localhost.”
	* 2013
	 
	 or
	 
	 2014
	 
	 is the default port to connect to the messaging service. You can change the port number in the
	 **docker-compose.yml** 
	 configuration file. We do not recommend using “localhost” as it might cause errors when connecting to the phone integration server. When using an HTTPS connection, make sure that server address matches the address in the SSL certificate.
	 
	
	
	
	
	
	 Note.
	 
	 If your website is served over HTTPS and secure connection is used for WebSockets, install a security certificate on the message exchange server and specify the certificate in the docker-compose configuration. For more information about the setup process, contact Creatio support.



 4. Set up the Asterisk parameters
-----------------------------------



 Apply the Asterisk parameters to every Creatio user who received Asterisk integration license. To do this:
 


1. Open the user profile page by clicking the
 
 Profile
 
 image button on the main page of the application.
2. Click the
 
 Call Center parameters setup
 
 button. This opens a page.
3. Fill out the following fields:
 


	1. Select the
	 
	 Disable Call Center integration
	 
	 checkbox to disable Creatio integration with the phone service. This hides the call button from the Creatio communication panel.
	2. Specify the Asterisk user line number in the
	 
	 Number
	 
	 field. The line number matches the phone number by default. For example, to track the SIP/305 user line, specify
	 
	 305
	 
	 , and to track the SIP/office line, specify the
	 
	 office
	 
	 .
	 
	
	
	
	
	
	 Attention.
	 
	 Each user uses an individual line. We do not recommend specifying the same line for multiple users as it can cause errors.
	3. Specify the context of the outgoing call in the
	 
	 Outgoing call context
	 
	 field if the context for the user must differ from the system context specified in the
	 **Terrasoft.Messaging.Service.exe.config** 
	 file.
	4. Select the
	 
	 Enable debugging
	 
	 checkbox to display troubleshooting information in the browser console. You can use the information if you encounter phone integration and customer contact issues.
4. Click
 
 Save
 
 .
5. Refresh the browser page to apply the changes.




