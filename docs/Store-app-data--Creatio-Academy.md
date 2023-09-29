


 Since Creatio 8.0 Atlas, Creatio has started transfer to composable architecture and introduced a composable app level. A Freedom UI app can consist of one or more packages. A
 **package** 
 is a collection of app elements that implements a particular block of functionality.
 



 Current app package
---------------------



 A package was the only way to transfer changes between environments in Creatio version 7.18.5 or earlier. All implemented customizations were saved to a package that was specified in the “Current package” (“CurrentPackageId” code) system setting. Since Creatio 8.0 Atlas, the app is the main way to transfer changes between environments. This lets you streamline customization, because all changes as well as information about relationships with other apps are automatically saved in the app. Creatio stores Freedom UI app data based on the current app package. A
 **current app package** 
 is the package that stores app elements created or modified using the Application Hub. Creatio sets the current app package the first time you open an app or modify any element in the app. Each app has a current app package.
 





 Note.
 
 Since Creatio 8.0 Atlas, if you go back to customizing the app after some time, Creatio saves changes made using the Application Hub to the app package, and changes made using the UI and Creatio IDE to a different package. To avoid errors when saving and transferring changes, specify the package of the app in the “Current package” (“CurrentPackageId” code) system setting before you begin. As a result, Creatio will save all changes to the app package from the system setting regardless of the customization tool.
 




 Creatio marks a package as a current app package as follows:
 


* If an app has
 **one unlocked package** 
 , Creatio marks this package as the current app package.
* If an app has
 **multiple unlocked packages** 
 , Creatio marks an arbitrary package as the current app package.
* If an app
 **does not have an unlocked package** 
 , for example, a base product app or Marketplace app, Creatio creates a new package automatically and marks this package as the current app package.


### 
 Change the current app package



 You can change the current app package that stores customizations. To do this:
 


1. Click
 ![](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “System setup” → “Lookups.”
2. Click
 
 New lookup
 
 on the
 
 Lookups
 
 section toolbar and fill out the
 **lookup properties** 
 :
 


	* Enter an arbitrary name in the
	 
	 Name
	 
	 property. For example, “App package.”
	* Select “Package in installed application” in the
	 
	 Object
	 
	 property.
3. Click
 
 Save
 
 on the lookup setup page's toolbar.
4. Open the
 
 App package
 
 lookup.
5. Add a filter “Installed application = [Name of the app to add or modify the current app package].”
6. Clear or select the
 
 Application current package
 
 checkbox depending on your business goals.



 As a result, all changes executed using the Application Hub will be saved to the new current app package.
 



 If you delete a current app package using the Creatio IDE, Creatio locks this action and displays an error. You cannot delete a package using Freedom UI Designer.
 



 When you change the current app package, you might need to move functionality between packages. This will cause dependencies to change. Make sure that dependencies do not cause errors.
 


### 
 Move the functionality between packages


1. Find the app package on the
 
 Advanced settings
 
 tab in the Application Hub.
2. Click
 ![](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “Admin area” → “Advanced settings.”
3. Select the needed package from the package list.
4. Find the schema that causes the cyclic chain in the package contents.
5. Click
 ![btn_multiple.png](/docs/sites/en/files/images/Platform_basics/cyclic_sequences/btn_multiple.png)
 → “Move to another package.” This opens a box.
6. Select the package that you found on step 1 in the box and save the changes.



 Primary app package
---------------------



 A primary app package is the package that stores app metadata in the app-descriptor.json file. Each app can have multiple primary app packages. By default, Creatio marks the package added when you create an app as the primary app package. For example, the “UsrRequests” package is primary package for the
 
 Requests
 
 app.
 



 When you modify the app metadata, Creatio marks a package as a primary app package as follows:
 


* If an app has an
 **unlocked package** 
 , Creatio marks this package as the primary app package and generates a new app-descriptor.json file in this package. Other app-descriptor.json files are still available in the corresponding locked primary packages.
* If an app
 **does not have an unlocked package** 
 , Creatio creates a new package automatically, marks this package as the primary app package and generates a new app-descriptor.json file in this package. In this case, the package is both current and primary.



 Since version 8.0.9 Atlas, you can
 **move the app-descriptor.json file between packages** 
 for apps that comprise multiple packages. To do this:
 


1. Click
 ![](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “System setup” → “Lookups.”
2. Click
 
 New lookup
 
 on the
 
 Lookups
 
 section toolbar and fill out the
 **lookup properties** 
 :
 


	* Enter an arbitrary name in the
	 
	 Name
	 
	 property. For example, “App package.”
	* Select “Package in installed application” in the
	 
	 Object
	 
	 property.
3. Click
 
 Save
 
 on the lookup setup page's toolbar.
4. Open the
 
 App package
 
 lookup.
5. Add a filter “Installed application = [Name of the app to change the primary app package].”
6. Сlear or select the
 
 Primary
 
 checkbox depending on your business goals.



 As a result, the app-descriptor.json file that contains updated metadata parameters will be generated in the new primary app package. The app-descriptor.json file will be removed from the previous unlocked primary package.
 



 You can set only an unlocked package as primary. If the package to set as primary is locked, Creatio does not generate the app-descriptor.json file.
 



 Ways to store Freedom UI app data
-----------------------------------



 You can
 **modify an app** 
 using the following tools:
 


* Freedom UI Designer. Use it to modify the structure of a Freedom UI app.
* Creatio UI. Use it to modify data connected to a Freedom UI app.
* Creatio IDE. Use it to implement additional functionality that cannot be implemented using Freedom UI Designer. For example, package install scripts.



 The way Creatio stores data is based on the tool you use to modify the Freedom UI app.
 


### 
 Store app data modified using the Freedom UI Designer



 The mechanism that stores app data modified using the Freedom UI Designer works as follows (Fig. 1):
 




 Fig. 1 Mechanism that stores app data modified using the Freedom UI Designer
 

![](/sites/default/files/documentation/sdk/ru/BPMonlineWebSDK/Screenshots/WaysToStoreFreedomUiAppData/8.0/scr_SaveTheDataUsingFreedomUiDesigner.png)


### 
 Store app data modified using Creatio UI



 The mechanism that stores app data modified using the Creatio UI works as follows (Fig. 2):
 




 Fig. 2 Mechanism that stores app data modified using the Creatio UI
 

![](/sites/default/files/documentation/sdk/ru/BPMonlineWebSDK/Screenshots/WaysToStoreFreedomUiAppData/8.0/scr_SaveTheDataUsingUi.png)


### 
 Store app data modified using the Creatio IDE



 The mechanism that stores app data modified using the Creatio IDE works as follows (Fig. 3):
 




 Fig. 3 Mechanism that stores app data modified using the Creatio IDE
 

![](/sites/default/files/documentation/sdk/ru/BPMonlineWebSDK/Screenshots/WaysToStoreFreedomUiAppData/8.0/scr_SaveTheDataUsingCreatioIde.png)



 I. e., when you create or modify an app element, Creatio stores the element in the package where the schema was opened.
 




