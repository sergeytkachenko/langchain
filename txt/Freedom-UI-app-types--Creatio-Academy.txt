


 Since version 8.0 Atlas, Creatio has started transfer to composable architecture and introduced a composable app level.
 **Composable architecture** 
 lets you accelerate the app design process and maximize the component reusability. Creatio platform delivers a library of composable elements that no-code creators can use to assemble function blocks, apps, and full-fledged products using no-code. The composable no-code architecture brings agility to a new level. Since all components are pluggable, replaceable, and reusable, the significant amount of configuration, customization, and development work is now replaced by assembling your apps from available blocks and components.
 



 A
 **Freedom UI composable app** 
 is the main unit of no-code development. An app solves business problems and contains dedicated functionality, such as a set of tools for employee request management. For example,
 
 Customer 360
 
 is the first out-of-the-box Freedom UI app developed using the composable approach and only no-code tools. The app lets you manage contacts and accounts in Freedom UI and replaces the
 
 Contacts
 
 and
 
 Accounts
 
 Classic UI sections with their
 
 Customer 360
 
 counterparts for new customers and new Creatio instances. During the transition to composable architecture, you can work with the
 
 Customer 360
 
 app or
 
 Contacts
 
 and
 
 Accounts
 
 Classic UI sections in existing Creatio instances. Use this period to transfer your customizations of
 
 Contacts
 
 and
 
 Accounts
 
 Classic UI sections to the new app. To do this, follow the instructions in a separate guide:
 [Element setup examples](https://academy.creatio.com/docs/user/nocode_platform/element_setup_examples) 
 .
 



 Compared to packages, which are the main unit of development in Creatio versions 7.18.5 and earlier, a Freedom UI app has the following
 **advantages** 
 :
 


* An app is created in a few clicks. All Freedom UI app sections are created in the Application Hub.
* An app package is created automatically.
* An app can comprise one or more packages.
* The
 
 Navigation and sections
 
 tab in the Application Hub displays all app sections.
* The app package dependencies are set automatically.
* If the app contains multiple schemas that replace the same page, the
 
 Pages
 
 tab in the Application Hub displays the last page schema that replaces all other schemas in the hierarchy.
* If the app contains multiple versions of the same process, the
 
 Business processes
 
 tab in the Application Hub displays the latest business process version.
* An app can include any configuration elements. For example, an app can contain both a business process or web service and one or more app sections.
* An app includes metadata. Learn more in a separate article:
 [Set up the app metadata](https://academy.creatio.com/documents?id=2405) 
 .
* An app can be transferred between environments in a few clicks. Learn more in a separate article:
 [Manage apps](https://academy.creatio.com/documents?id=2444&anchor=title-2232-10) 
 .



 Application Hub lets you work with the following Freedom UI
 **app types** 
 :
 


* Studio Enterprise app.
 [Read more >>>](#title-2532-8)
* Base product apps.
 [Read more >>>](#title-2532-3)
* Marketplace apps.
 [Read more >>>](#title-2532-5)
* Custom apps.
 [Read more >>>](#title-2532-6)



 A Creatio instance is a Freedom UI app collection that differs based on Creatio product and version. For example, Studio platform version 8.0.6 contains Studio Enterprise base product app (Fig. 1):
 




 Fig. 1 Studio platform app in the Application Hub
 

![](/sites/default/files/documentation/sdk/ru/BPMonlineWebSDK/Screenshots/FreedomUiAppsBasics/8.0/scr_StudioBuildApps.png)



 The CRM bundle version 8.0.6 contains Customer 360 app, Marketing, Sales Enterprise, Service Enterprise, and Studio Enterprise base product apps (Fig. 2):
 




 Fig. 2 CRM bundle apps in the Application Hub
 

![](/sites/default/files/documentation/sdk/ru/BPMonlineWebSDK/Screenshots/FreedomUiAppsBasics/8.0/scr_CrmBuildApps.png)



 Studio Enterprise app
-----------------------



 Studio Enterprise app is a base product app that implements the core functionality and is required for any Creatio instance. The Studio Enterprise app functionality is implemented in base packages. You can customize out-of-the-box functionality. The customizations extend functionality by replacing the base configuration element schemas and do not modify base packages and their configuration elements. To customize the functionality, follow the instructions in separate articles:
 [Freedom UI Designer](https://academy.creatio.com/documents?id=2376) 
 ,
 [Replace configuration elements](https://academy.creatio.com/documents?id=15105) 
 (developer documentation).
 



 Base product apps
-------------------



 Sales, Service, and Marketing are base product apps that solve problems in a specific industry and have their own business value. Upcoming Creatio releases will divide Sales, Service, Marketing app functionality into composable apps. Base product apps are implemented in base packages. You can customize out-of-the-box functionality. The customizations extend functionality by replacing the base configuration element schemas and do not modify base packages and their configuration elements. To customize the functionality, follow the instructions in separate articles:
 [Freedom UI Designer](https://academy.creatio.com/documents?id=2376) 
 ,
 [Replace configuration elements](https://academy.creatio.com/documents?id=15105) 
 (developer documentation).
 



 Marketplace apps
------------------



 You can install the verified Marketplace app into Creatio from the Creatio Marketplace. This lets you find a solution for your industry, integrate Creatio with external services, or extend the functionality of the Creatio platform using ready-to-use Marketplace app developed by different vendors.
 



 Similar to base product apps, you can customize out-of-the-box functionality. The customizations extend functionality by replacing the base configuration element schemas and do not modify Marketplace app packages and their configuration elements. To customize the functionality, follow the instructions in separate articles:
 [Freedom UI Designer](https://academy.creatio.com/documents?id=2376) 
 ,
 [Replace configuration elements](https://academy.creatio.com/documents?id=15105) 
 (developer documentation). Learn more about Marketplace apps in the developer documentation:
 [Marketplace app development](https://academy.creatio.com/docs/developer/marketplace_app_development) 
 .
 



 You can publish apps on the Creatio Marketplace. Make sure your app meets the requirements listed in the developer documentation:
 [Requirements for published Marketplace app resources](https://academy.creatio.com/documents?id=15008) 
 .
 



 Custom apps
-------------



**Custom apps** 
 are apps created manually using the Application Hub in Creatio 8.0 Atlas and later or custom packages created using the Creatio IDE or Section Wizard and deployed in Creatio version 7.18.5 and earlier. Customers, partners, or third-party developers can create custom apps and modify custom app packages, their configuration elements, and metadata. You can customize the functionality of an exported custom app. The customizations extend functionality by replacing the base configuration element schemas and do not modify custom app packages after you export the packages to another environment. To customize the functionality, follow the instructions in separate articles:
 [Freedom UI Designer](https://academy.creatio.com/documents?id=2376) 
 ,
 [Replace configuration elements](https://academy.creatio.com/documents?id=15105) 
 (developer documentation).
 




