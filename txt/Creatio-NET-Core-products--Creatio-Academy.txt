




 Attention.
 
 The deprecated .NET Core framework will be retired in Creatio version 8.1. We using .NET 6 to deploy Creatio version 8.0.8 and later.
 




 .NET Core platform is an open-source cross-platform software that can be deployed on
 **Linux** 
 ,
 **Windows** 
 ,
 **Mac OS** 
 systems.
 



 We recommend using
 **Linux** 
 to deploy Creatio .NET Core products. This OS is highly reliable, well-performing, has an optimal cost and is actively being developed.
 




 Feature support in Creatio .NET Core products
------------------------------------------------






| 
 Feature
  | 
 .NET Core Support
  |
| --- | --- |
| **Windows authentication**  | 
 Supported since version 7.16.4.
  |
| 
**Configuration development** 


 (
 
 Configuration
 
 section, object designer)
  | 
 Supported since version 7.17.0.
  |
| **LDAP integration**  | 
 Supported since version 7.17.2.
  |
| 
**Fault-tolerant Redis Sentinel configuration** 
 | 
 We do not plan to support it. More modern fault-tolerant
 [Redis Cluster](/docs/8-0/user/on_site_deployment/caching_server/redis_cluster_shortcut/redis_cluster) 
 configuration is supported since Creatio version 7.18.0.
  |
| 
**Telephony integration** 
 | 
 Asterisk connector is supported since version 7.16.3.
 

 Learn more about how the integration with other supported telephony connectors works in the
 [footnotes](#title-3085-9) 
 below.
 

 We plan to support Cisco Finesse integration without using IIS and ARR in the future releases.
  |
| 
**Oracle DBMS** 
 | 
 We plan to support it in the future releases.
  |
| 
**Exchange\Office365 calendar and contact synchronization** 
 | 
 Supported since version 7.18.2.
  |
| 
**Google Calendar and contact synchronization** 
 | 
 We plan to support it in the future releases.
  |
| 
**Facebook integration** 
 | 
 We plan to support it in the future releases.
  |
| 
**Lead registration from social networks** 
 (Facebook and LinkedIn)
  | 
 We plan to support it in the future releases.
  |




#### 
 Notes




 Deploy the messaging service (Creatio Messaging Service) on Windows to integrate Avaya, TAPI telephony systems.
 



 You need to deploy the Microsoft IIS web server and its expansion — Application Request Routing (ARR) — on Windows to integrate Cisco Finesse.
 





 The lifecycle of products using .NET Framework and .NET Core platforms
-------------------------------------------------------------------------



 Microsoft released the
 **.NET 5** 
 platform, thus integrating .NET Framework and .NET Core platforms.
 



 This allows the platform to support the maximum number of the APIs that used to be available on the .NET Framework platform. However, it is important to note that the API is not backwards compatible, therefore you need to adapt the .NET Core features previously developed using .NET Framework to ensure .NET Core and .NET 5 support.
 



 We plan to move the Creatio product lineup to the unified .NET platform in the future.
 




 Developing features with simultaneous .NET Framework and .NET Core support
-----------------------------------------------------------------------------



 To streamline the adaptation to .NET Core and .NET 5, we recommend developing new features with simultaneous .NET Framework and .NET Core platform support.
 



 Recommendations:
 


1. Your external libraries have to support .NET Standard 2.0. This will let you use them with both .NET Framework and .NET Core.
2. Your framework's API also has to support .NET Standard 2.0. You can check the compatibility using
 [Microsoft documentation](https://docs.microsoft.com/en-us/dotnet/api/?view=netstandard-2.0) 
 .
3. When coding configuration web services, you need to inherit from Terrasoft.Web.Common.BaseService and use HttpContextAccessor for HttpContext access. Read more:
 [Custom web services](/docs/7-18/developer/back_end_development/web_services/overview) 
 .





 Attention.
 
 If you use or plan to use Creatio Marketplace applications to expand Creatio’s functionality, you will need to specify whether they support Creatio .NET Core products.
 




 Migrating Creatio from .NET Framework to .NET Core
----------------------------------------------------



 We plan to support Creatio migration from .NET Framework to .NET Core in the upcoming releases.
 



 Deploying Creatio .NET Core application
-----------------------------------------



 You can find the instructions on deploying Creatio in the
 [Deploy Creatio .NET Core application server on Linux](/docs/8-0/user/on_site_deployment/application_server_on_linux/net_core_server/installation/deploy_the_creatio_net_core_application_on_linux) 
 article.
 




