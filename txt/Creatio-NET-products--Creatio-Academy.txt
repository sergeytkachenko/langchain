


 .NET is an open-source cross-platform software that can be deployed on
 **Linux** 
 and
 **Windows** 
 systems.
 



 We recommend using
 **Linux** 
 to deploy Creatio .NET products. This OS is highly reliable, well-performing, has an optimal cost and is actively being developed.
 



 Feature support in Creatio .NET products
------------------------------------------



 Creatio .NET product lineup supports almost every feature available in .NET Framework products. The following features will be implemented in .NET products in future Creatio releases:
 


* Oracle and Microsoft SQL DBMS
* Authentication of incoming integrations via OAuth 2.0
* Integration with SVN version control system
* Portal in the mobile app


#### 
 Notes




 Deploy the messaging service (Creatio Messaging Service) on Windows to integrate Avaya, TAPI telephony systems.
 




 Lifecycle of products that use .NET Framework and .NET Core
-------------------------------------------------------------



 Microsoft released .NET platform, thus integrating .NET Framework and .NET Core.
 



 This enables the platform to support the maximum number of the APIs that used to be available on .NET Framework and .NET Core. However, not all APIs are backwards compatible. You need to ensure .NET supports your customizations and adapt code developed using .NET Framework or .NET Core if needed.
 



 The long-term plan is to move the entire Creatio product lineup to .NET and retire support for .NET Framework.
 



 Develop features that support all platforms
---------------------------------------------



 To streamline the adaptation to .NET, we recommend developing new features that support both .NET Framework and .NET.
 



 Recommendations:
 


* Your external libraries have to support .NET Standard 2.0. This will let you use them with both .NET Framework and .NET.
* Your framework's API also has to support .NET Standard 2.0. You can check the compatibility using
 [Microsoft documentation](https://docs.microsoft.com/en-us/dotnet/api/?view=netstandard-2.0) 
 .
* When coding configuration web services, you need to inherit from Terrasoft.Web.Common.BaseService and use HttpContextAccessor for HttpContext access. Learn more in the developer documentation:
 [Custom web services](https://academy.creatio.com/documents?id=15262) 
 .





 Attention.
 
 If you use or plan to use Creatio Marketplace applications to expand Creatio’s functionality, you need to check whether they support Creatio .NET products.
 




 Migrate Creatio from .NET Core to .NET
----------------------------------------



 Most APIs from .NET Core are compatible with .NET. However, Microsoft introduced some API breaking changes that might require you to adapt code if a particular API was used in your Creatio customization. Learn more about migrating from .NET Core to .NET in a separate article:
 [Move Creatio .NET Core 3.1 to .NET 6](https://academy.creatio.com/documents?id=2449) 
 .
 



 Migrate Creatio from .NET Framework to .NET
---------------------------------------------



 Support for Creatio migration from .NET Framework to .NET is planned in the upcoming releases.
 



 Deploy Creatio .NET
---------------------



 Learn more about deploying Creatio .NET in a separate article:
 [General Creatio deployment procedure](https://academy.creatio.com/docs/node/2650) 
 .
 




