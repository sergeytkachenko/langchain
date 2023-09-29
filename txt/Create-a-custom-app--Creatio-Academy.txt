



 This functionality is available for beta testing in Creatio version 7.18.5. We appreciate your feedback! Contact us by email:
 [beta@creatio.com](mailto:beta@creatio.com) 
 .
 




 In Creatio,
 **apps** 
 are function blocks that solve business problems. For example, an app can be a set of payroll management tools. An app can consist of one or more content packages. Currently, Creatio adds a single package to which the developed functionality is saved.
 



 The package name is generated automatically and is non-editable. You can view the name in the
 
 Advanced settings
 
 block of the App Designer.
 



 Creatio displays the app section in the
 
 My applications
 
 workplace.
 



 You can go to section list and record page setup from within the app.
 





 Note.
 
 If you are going to transfer the app to other development environments, specify the app package in the “Current package” (the “CurrentPackageId” code) system setting before you start working on the app.
 




 Apps can include:
 


* a section that contains a list and a page implemented in the new UI framework
* business processes
* custom REST and SOAP service integrations
* other schema types that are a part of Creatio configuration: objects, data binding, SQL scripts, etc.



 App creation and setup constitute a unified ecosystem, which lets you streamline the development process as much as possible.
 



 To create a new app:
 


1. Open the System Designer. For example, click the
 ![btn_system_designer_1.png](/docs/sites/en/files/inline-images/btn_system_designer_1.png)
 button in the top right.
2. Go to the “Applications” block → “Installed applications.”
3. Click the
 
 Add application
 
 button. This opens a menu.
4. Select
 
 Create new application
 
 in the menu. This opens a page.
5. Take the following steps on the page that opens:
	1. Specify the app name in the
	 
	 Give it a name
	 
	 field. Creatio will display the name in the app list and on the side panel The app name must be unique. The field is required.
	2. Specify the business problem the app solves in the
	 
	 Describe what it’s for (optional)
	 
	 field.
	3. Click
	 
	 Create
	 
	 (Fig. 1).




 Fig. 1 Adding an app
 

![](/docs/sites/en/files/images/Release_notes/release_notes_7_18_5/gif_create_new_application.gif)



 As a result, a new app will be created. The app comes with the following components:
 


* section list page
* section record page
* detail
* section object
* My applications
 
 workplace binding





 Note.
 
 The app template contains the workplace binding. If the workplace does not exist yet, Creatio will add it when creating an app. If the workplace already exists, Creatio will add the app section to the workplace when creating an app.
 




 You can add other elements to the app as well. For example, go to the
 
 Integrations
 
 block of the left menu to add REST and SOAP services, go to the
 
 Business processes
 
 block to set up a business process. Go to the
 
 Advanced settings
 
 block to add elements similarly to adding elements in the
 
 Configuration
 
 section. Learn more in developer documentation:
 [Develop in Creatio IDE](/docs/7-18/developer/development_tools/creatio_ide/develop_in_creatio_ide/overview) 
 .
 



 You can add the following elements:
 


* object
* replacing object
* source code
* module, etc.



 Click the
 
 Add
 
 button to add elements.
 



 You can also import objects from packages. Learn more in developer documentation:
 [Deployment in Creatio IDE](/docs/7-18/developer/development_tools/delivery/creatio_ide/overview) 
 .
 



 To go to the executable part of the app, click the
 
 Run application
 
 button.
 




