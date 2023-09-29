



 Creatio version 8.0.2 and later can store app metadata.
 




 In this case,
 **metadata** 
 is app details stored within the app itself regardless of an environment. App metadata is stored in the app-descriptor.json file of the primary app package. Since Creatio version 8.0.9, app can include multiple app-descriptor.json files. Learn more:
 [Store app data](https://academy.creatio.com/documents?id=2419&anchor=title-3990-3) 
 .
 



 App metadata stores the following
 **data** 
 :
 


* icon
* icon color
* name
* description
* code
* list of app packages



 Set up the parameter values in the Application Hub. You can fill out the parameters only when you create an app, but you can change them at any moment.
 





 Attention.
 
 The code is generated on app creation and cannot be changed later.
 




 Fill out the app metadata
---------------------------



 Fill out the corresponding app parameters when you create an app. Learn more in a separate article:
 [Create a custom app](https://academy.creatio.com/documents?id=2377) 
 .
 



 Since Creatio version 8.0.3, the app name can contain between 3 and 100 characters. You can use any alphanumeric and special characters.
 



 The app
 **code** 
 is used as the app ID. Also, the code is used in app schema names.
 



 Creatio generates the code based on the app name. Code generation has the following special features:
 


* Use at least one Latin word in the title since the code can contain only digits and Latin characters.
* To generate the code, at least 3 characters from the app name suitable for code generation are required. If the app name contains multiple spaces, Creatio removes them from the code and formats the code in camelcase. For example, the code of the “Financial benefits” app is “UsrFinancialBenef.”
* If the app name contains fewer than 3 characters suitable for code generation, Creatio generates the code in the format of “AppUsr\_gfgvd08j.”
* If you change the app name, Creatio updates the code accordingly. You can edit the code manually when you create an app. In this case, Creatio does not update the code on further name changes. After you create an app, it is not possible to change its code.



 If the code and unique ID of the app to install matches the code and unique ID of an existing app, Creatio updates the existing app. If the code of the app to install matches the code of an existing app but the unique ID differs, the app installation ends with an error. For example, if you have the “Test” (“UsrTest” code) app created on your Creatio instance, the “Test” (“UsrTest” code) app created on another Creatio instance will not be installed to your instance.
 



 Creatio displays the specified parameter values both in the development environment and any other environment where you install the app (Fig. 1).
 




 Fig. 1 Metadata of the “Financial benefits” app
 

![](/docs/sites/en/files/images/NoCode_Customization/metadata/scr_fin_benefits_matadata.png)



 Change the app metadata
-------------------------



 You can change the app metadata only in the development environment. To do this:
 


1. Click
 ![btn_system_designer_1.png](https://academy.creatio.com/docs/sites/en/files/inline-images/btn_system_designer_1.png)
 in the top right → “Application Hub.”
2. Open the “Financial benefits” app.
3. Click
 ![](/docs/sites/en/files/images/NoCode_Customization/metadata/scr_edit_metadata_button.png)
 and edit the app parameters. For example, name and icon color (Fig. 2).
 




 Fig. 2 Change the metadata of the “Financial benefits” app
 

![](/docs/sites/en/files/images/NoCode_Customization/metadata/scr_edit_matadata.png)
4. Specify the name of your company in the
 
 Developer
 
 parameter.
5. Save the changes.



 As a result, the app will display the changed parameter values in the development environment. When you install the app into or update it in any environment, Creatio updates the metadata (Fig. 3).
 




 Fig. 3 Metadata of the “Payroll” app
 

![](/docs/sites/en/files/images/NoCode_Customization/metadata/scr_salary_calculation_matadata.png)




