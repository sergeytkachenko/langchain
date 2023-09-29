


 The Exchange Listener synchronization service synchronizes Creatio with
 [MS Exchange](/docs/7-18/user/setup_and_administration/base_integrations/microsoft_email_contacts_and_calendar/set_up_microsoft_exchange_and_office_365/set_up_the_ms_exchange_and_microsoft_365_services) 
 and
 [IMAP/SMTP](/docs/7-17/user/setup_and_administration/base_integrations/imap_smtp_email/add_imap_smtp_email_provider) 
 mail services using a subscription mechanism.
 



 This article covers deploying the Exchange Listener synchronization service for Creatio installed on-site.
 



 The service consists of two required components:
 


* The Exchange Listener primary module.
* NoSQL Redis DBMS.



 The
 **Exchange Listener module** 
 initiates the outgoing connection to EWS API. It uses the mailbox credentials and creates a subscription to “new message” events. The open subscription remains in the component memory to ensure fast response time when new emails arrive. When a corresponding event is received, the email instance loads.
 



 Using an
 **in-memory repository will be enough** 
 for deploying the service.
 



**Redis DBMS** 
 enables creating a scalable and fault-tolerant system of processing nodes. The Redis repository holds information about the mailboxes that are served. This lets any container process Creatio queries for adding a new subscription or check the status of a specific subscription regardless of the subscription node.
 



 Redis
 **requirements** 
 :
 


* Anonymous access allowed.
* Separate database available for the Exchange Listener service operation.



 Exchange Listener deployment methods
--------------------------------------



 We recommend
 **using the Kubernetes orchestrator and Helm package manager** 
 to deploy the service.
 [Read more >>>](#title-253-2) 




 You can also
 **use Docker** 
 to speed up the deployment in the development environment.
 [Read more >>>](#title-253-4) 



### 
 Deploy the synchronization service via Kubernetes



 To deploy the Exchange Listener synchronization service in Docker:
 


1. Set up the target environment first:
 


	1. The Kubernetes cluster. Read more about how to set up and manage the cluster on the
	 [Kubernetes documentation website](https://kubernetes.io/docs/home/) 
	 .
	2. The Helm package manager. Read more about installing the package manager on the
	 [Helm documentation website](https://helm.sh/docs/intro/install/) 
	 .
2. Install Redis. Use the
 [GitHub website](https://github.com/helm/charts/tree/master/stable/redis) 
 to learn more about how to install Redis using Helm.
   

 Example of a command for installing Redis:
 






```

helm install --namespace default --set auth.enabled=false --set=slave.persistence.enabled=false --set master.persistence.enabled=false --set cluster.enabled=false redis bitnami/redis
```





 Where:
 



**default** 
 – the name of the namespace where Redis will be installed.
 



**redis** 
 – an arbitrary name for the Redis instance.
3. Install the Exchange Listener module. To install the module,
 [download the helm package](https://academy.creatio.com/sites/default/files/documents/downloads/ExchangeListener/exchangelistener-0.8.52.tgz) 
 . Find the available parameters of the helm package in the table below.
 


 Attention.
 
 For newer Kubernetes versions, specify the API version and add the following parameter:
 







```

--set apiVersion=apps/v1
```





 Example of a command for installing Exchange Listener using the service address and relative path:
 






```

helm install --set env.host=<redis\_host> --set ApiUrl=<kubernetes\_url> --set ingress.enabled=true --set ingress.path=<listener\_path> --set apiVersion=apps/v1 --namespace <namespace name> exchangelistener </path/to/helm/exchangelistener.tgz>
```



 Where:
 



**<redis\_host>** 
 – Redis server address.
 



**<Kubernetes\_url>** 
 – Kubernetes URL or IP address.
 



 Exchange Listener address:
 **<kubernetes\_url>/<listener\_path>** 
 .
 



 To check whether the Exchange Listener service is available, execute the following request: <kubernetes\_url>/<listener\_path>/api/listeners/status (Fig. 1).
 



 Example of installing the Exchange Listener using Node IP and port address:
 






```

helm install --set env.host=<redis_host> --set service.type=<node_IP> --set service.nodePort=<node_port> --set apiVersion=apps/v1 --namespace <namespace name> exchangelistener </path/to/helm/exchangelistener.tgz>
```





 Exchange Listener address –
 **<node\_IP:node\_port>** 
 .
 



 To check whether the address is available, execute the following request: <node\_IP:node\_port>/api/listeners/status (Fig. 1).
 




 Fig. 1 Example of the Exchange Listener service response
 

![chapter_exchange_listener_answer.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/exchange_listener/chapter_exchange_listener_answer.png)





 Note.
 
 To disable the “Creatio” label for downloaded emails, add --set FeaturesMarkEmailsAsSynchronized=false parameter to helm install command when deploying the service.
 




 Available parameters of the Exchange Listener helm package
 





| 
 Parameter
  | 
 Parameter description
  | 
 Default value
  |
| --- | --- | --- |
| 
 replicaCount
  | 
 Number of StatefulSet processors
  | 
 2
  |
| 
 service.type
  | 
 Service type. You can find more information about the Kubernetes service types in the
 [Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types) 
 .
  | 
 ClusterIP
  |
| 
 service.nodePort
  | 
 If the service.type parameter equals NodePort, specify the external service port in this parameter.
 

 Read more about the NodePort type in the
 [Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/service/#nodeport) 
 .
  | 
 |
| 
 env.host
  | 
 Host address for Redis.
  | 
 |
| 
 env.port
  | 
 Host port for Redis.
  | 
 6379
  |
| 
 env.base
  | 
 Database number for Redis.
  | 
 0
  |
| 
 ingress.enabled
  | 
 Use address overriding via ingress.
  | 
 false
  |
| 
 ApiUrl
  | 
 Service address if ingress.enabled=true
  | 
 |
| 
 ingress.path
  | 
 Service relative path.
  | 
 |
| 
 log4Net.level
  | 
 Logging level by default.
  | 
 Info
  |




 Use the
 [requirements calculator](https://academy.creatio.com/docs/requirements/calculator) 
 to check the server requirements.
 


### 
 Deploy the synchronization service in Docker



 To set up the service, use a server (computer or virtual machine) with Linux or Windows OS installed.
 





 Attention.
 
 We recommend deploying the synchronization service in Docker only for installing in the development environment. This method differs by the high speed of deployment but it does not guarantee meeting the requirements of the product environment, namely: function fault tolerance, scaling for processing big volumes of requests, and a single approach to manage the components using the container orchestration. For the product environment, we strongly recommend using the Kubernetes and Helm package manager.
 




 To deploy the Exchange Listener synchronization service in Docker:
 


1. Set up the target environment first:
 


	1. Docker container platform. Read more about how to install and set up the platform on the
	 [Docker documentation website](https://docs.docker.com/get-started/) 
	 .
	2. Redis DBMS. To install the Redis Server, use the
	 [Windows setup file](https://github.com/MicrosoftArchive/redis/releases) 
	 or the
	 [Linux Guide](https://redis.io/download) 
	 . Make sure you deploy an anonymous Redis DBMS. Learn more about deploying Redis DBMS in Docker on the
	 [Docker Hub](https://hub.docker.com/_/redis/) 
	 community website.
2. Install and run the Exchange Listener module. To do this, download and deploy the Docker container image.
 



 Below is the example of a command for downloading and running the image via the command line and Docker installed.
 






```

docker run \
-d \
# Port forwarding
-p <localhost_port>:80 \
--restart unless-stopped \
# Connecting to Redis
--env ExchangeListenerRedisHost=<redis_host>:<redis_port> \
--env ExchangeListenerRedisDatabase=<redis_database_number> \
--env PodName=ExchangeListener \
--name ExchangeListener \
# The up-to-date ExchangeListener image in Docker Hub
bpmonline/exchangelistener:<listener_version>
```



 Where:
 



**<localhost\_port>** 
 – local server port.
 



**<redis\_host>** 
 – Redis server address.
 



**<redis\_database\_number>** 
 – DB number of the Redis server.
 



**<service\_name>** 
 – service name (entered manually).
 



**<listener\_version>** 
 – the Listener microservice version.
 





 Note.
 
 Use the
 
[Docker Hub community](https://hub.docker.com/r/bpmonline/exchangelistener/tags) 

 to see the up-to-date Exchange Listener version.
 




 To check whether the deployed Docker container is available, run the following command:
 






```

docker ps -a -–filter "name=<service_name>"
```





 Exchange Listener service address –
 **localhost:<localhost\_port>** 
 .
 



 To check whether Exchange Listener service address is available, execute the following request: <Localhost:<localhost\_port>/api/listeners/status (Fig. 2).
 



 Set up the Exchange Listener service on Creatio's end
-------------------------------------------------------


1. Make sure the ExchangeListenerService anonymous service is available at
 
 Creatio application address
 
 /0/ServiceModel/ExchangeListenerService.svc (Fig. 2).
 




 Fig. 2 Example of a response from ExchangeListenerService
 

![chapter_exchange_listener_creatio.png](/docs/sites/en/files/images/Setup_and_Administration/exchange_listener/chapter_exchange_listener_creatio.png)
2. Set the needed system setting values. To do this:
 


	1. Open the System Designer, e. g., by clicking
	 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/exchange_listener/btn_system_designer.png)
	 .
	2. Click “System settings” in the “System setup” block.
	3. Set the system setting values as follows:
	 
	
	
	
	 “
	 **ExchangeListenerServiceUri** 
	 ” (“ExchangeListenerServiceUri” code). The format of the system setting value:
	 
	 the service address used at installation
	 
	 /api/listeners.
	 
	
	
	
	 “
	 **Creatio exchange events endpoint URL** 
	 ” (“BpmonlineExchangeEventsEndpointUrl” code). The format of the system setting value:
	 
	 the anonymous ExchangeListenerService address
	 
	 /NewEmail. For example, https://mycreatio.com/0/ServiceModel/ExchangeListenerService.svc/NewEmail.



 Exchange Listener Service Diagnostics
---------------------------------------



 The Exchange Listener service diagnostics page provides tools for troubleshooting the Exchange Listener service.
 



 Use the service page to:
 


* Check if the features essential for Exchange Listener are enabled.
* Verify the service availability.
* Receive subscription information.
* Validate the “ExchangeListenerServiceUri” system setting.
* Check the health of a mailbox.



 To access the Exchange Listener Service Diagnostics page, add the “/0/ClientApp/#/IntegrationDiagnostics/” string to the URL of your Creatio website in the browser address bar and select Enter. For example:
 






```

http://mycreatio.com/0/ClientApp/#/IntegrationDiagnostics/ExchangeListener
```





 The diagnostics page contains several readout blocks and diagnostics controls (Fig. 3). By default, most of the readout blocks do not display diagnostics data unless you click
 
 Run diagnostics
 
 in that block.
 




 Fig. 3 Exchange Listener service diagnostics
 


![chapter_exchange_listener_diagnostics_page_full](/docs/sites/en/files/images/Setup_and_Administration/Exchange_Listener_synchronization_service/chapter_exchange_listener_diagnostics_page_full.png)






|  |  |
| --- | --- |
| 
 Feature state
  | 
 This readout block runs diagnostics automatically on page load.
 

 Checks if required Exchange Listener features are enabled in your Creatio application:
 * ExchangeListenerEnabled.
* EmailIntegrationV2.
* SendEmailsV2.


 Learn more about how to enable Creatio features:
 [Feature Toggle. Mechanism of enabling and disabling functions](/docs/7-18/developer/interface_elements/interface_control_tools/existing_feature/overview) 
 .
  |
| 
 Service availability verification
  | 
 Checks if the Exchange Listener service is accessible from your Creatio application.
  |
| 
 Receiving subscription information
  | 
 Checks the connection to the remote server.
  |
| 
 Validation of the “ExchangeListenerServiceUri” system setting
  | 
 Checks if the Exchange Listener service endpoint specified in the “ExchangeListenerServiceUri” system setting is valid.
  |
| 
 Checking mailbox health
  | 
 Checks the operation of MS Exchange mailboxes. Select the
 
 Send test email
 
 checkbox to send a test email to the specified address when clicking the
 
 Run diagnostics
 
 link.
  |





