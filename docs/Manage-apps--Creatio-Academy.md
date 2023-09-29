


 Use the
 
 Application Hub
 
 section to manage Creatio apps and add-ons. In Creatio, apps are function blocks that solve business problems. For example, an app can be a set of request management tools. An app can consist of one or more content packages. Packages are added automatically when you create a new app.
 



 The
 
 Application Hub
 
 section lets you:
 


* View the index of installed apps.
* Create and set up a custom app manually.
 [Read more >>>](#title-2232-6)
* Create and set up a custom app using AI.
 [Read more >>>](#title-2304-11)
* Install Marketplace apps for permanent or trial use.
 [Read more >>>](#title-2304-1)
* Install previously created and configured apps from file.
 [Read more >>>](#title-2304-2)
* Download apps.
 [Read more >>>](#title-2232-8)
* Deploy apps.
 [Read more >>>](#title-2304-5)
* Uninstall apps.
 [Read more >>>](#title-2304-5)



 Create an app manually
------------------------



 You can create apps of any complexity in a single place using the
 
 Application Hub
 
 , which lets you streamline the development process as much as possible. Apps can include:
 


* sections that are displayed as navigation menu items and comprise various custom UI elements
* various pages, e. g, lists, form pages, dashboards
* business processes
* custom REST and SOAP service integrations
* other schema types that are a part of Creatio configuration, e. g., objects, data bindings, SQL scripts, etc.



 To create a new app manually:
 


1. Click
 ![btn_system_designer_8_shell.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “Application management” → “Application Hub.”
2. Click
 
 New application
 
 (Fig. 1). This opens a window.
 




 Fig. 1 Add an app
 

![add_new_app_1.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/add_new_app_1.png)
3. Select a new app template based on your business goals (Fig. 2):
 


	* **Records & Business processes** 
	 . Contains Freedom UI section schemas. The Freedom UI section is displayed in a separate workplace.
	* **Dashboards** 
	 . Contains Home Page schemas of page type. The page is displayed in a separate workplace.
	* **Custom** 
	 . An empty template that contains a package with no configuration element schemas.
 For example, select “Records & Business processes” to add a list and form page to the app automatically.
 





 Note.
 
 If you want to install an existing app, select “
 [Install from file](https://academy.creatio.com/documents?id=2444&anchor=title-2304-2) 
 ” or “
 [Marketplace powered](https://academy.creatio.com/documents?id=2444&anchor=title-2304-1) 
 .” Also, you can select “Customer 360” and “Case Management” to install these apps quickly if you do not have them.
 





 Fig. 2 Select an app template
 

![choose_type_new_app_2.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/choose_type_new_app_2.png)
4. Click
 
 Select
 
 to confirm the template. This opens a window.
5. Specify the app parameters. This data will be stored as the app metadata. You can review or change it whenever you need. Learn more about the app metadata in a separate article:
 [Set up the app metadata](https://academy.creatio.com/documents?id=2405) 
 .
 


	1. Select the app icon by clicking the arrows or using the scroll wheel.
	2. Select the app icon color.
	3. Enter the app name in the
	 
	 PLEASE NAME YOUR APPLICATION
	 
	 field. The app name must be unique. This is a required field.
	4. Edit the app code if needed.
	 
	
	
	
	
	
	 Note.
	 
	 App content includes source code that contains macros. When you create an app, Creatio sets the macros to metadata values.
6. Select
 
 Link to an existing object
 
 to use an existing object in the app and transfer your previous customizations to Freedom UI. Otherwise Creatio adds a new object for the app.
7. Click
 
 Create
 
 (Fig. 3).
 




 Fig. 3 App parameters
 

![scr_populate_fields_new_app.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/scr_populate_fields_new_app.png)



 As a result, Creatio will add the app to the
 
 Application Hub
 
 section (Fig. 4). The app will contain the elements included in the template. For example, a list page and form page. You might need to add new sections to workplaces before users can start working with the app.
 




 Fig. 4 Configuration of the new app
 

![scr_new_app_advanced_settings.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/scr_new_app_advanced_settings.png)



 To view the results or test the app in operation, click
 
 Run app
 
 . You can also use this option to preview the improvements you make to the app.
 



 Create an app using AI
------------------------



 You can accelerate Creatio app development drastically using AI. Enter the app description and the AI will create an app, including objects, pages, sections, and columns.
 



 This functionality is available out of the box in
 **Creatio cloud** 
 . Take the following steps to be able to use the functionality in
 **Creatio on-site** 
 :
 


1. Update the database enrichment service. Instructions:
 [Database enrichment service](https://academy.creatio.com/documents?id=15066) 
 (developer documentation).
2. Turn on the “GenAIFeatures.Application” feature. Instructions:
 [Manage an existing additional feature](https://academy.creatio.com/documents?id=15631) 
 (developer documentation).



 To create a new app using AI:
 


1. Click
 ![btn_system_designer_8_shell.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “Application management” → “Application Hub”.
2. Click
 
 New application
 
 . This opens a window.
3. Select
 
 AI generated
 
 →
 
 Select
 
 . This opens a window (Fig. 5).
 

 Fig. 5 Create an app using AI
 

![scr_create_an_app_using_ai.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/scr_create_an_app_using_ai.png)
4. Specify the app parameters. This data will be stored as the app metadata. You can review or change it whenever you need. Learn more about the app metadata in a separate article:
 [Set up the app metadata](https://academy.creatio.com/documents?id=2405) 
 .
	1. Select the app icon by clicking the arrows or using the scroll wheel. OpenAI does not use the icon as part of the app generation.
	2. Select the app icon color. OpenAI does not use the color as part of the app generation.
	3. Enter the app name in the
	 
	 PLEASE NAME YOUR APPLICATION
	 
	 field. OpenAI uses this value as the name of the app and the main app section.
5. Describe the app structure in the
 
 DESCRIBE WHAT IT'S FOR
 
 field. OpenAI generates the app in the language of the prompt. Learn more about making the most effective prompts:
 [AI prompt guidelines](#title-2304-12) 
 .
6. Click
 
 Generate with AI
 
 .
7. Wait until OpenAI finishes generating the app.



 As a result, OpenAI will create a new app based on your prompts. You will be able to customize it further similarly to any other app.
 


### 
 AI prompt guidelines



 OpenAI generates apps based on any prompt, but the results might not always be close to your business vision. Follow these guidelines to ensure the result fulfills your business goals as much as possible:
 


1. Describe
 **only the app structure** 
 in the prompt, i. e., objects, lookup objects, sections, pages, and fields. Avoid marketing text, internal jargon, or functionality unrelated to the app structure, for example, Jira integration.
2. Describe the app structure
 **thoroughly and explicitly** 
 if you want to get precise results. AI can add details, for example, fields, to the app if your prompt is short or vague.
3. Describe the
 **data model** 
 if you want to have the most control over the results. For example: “Object Requests. Columns: status(lookup), name(text), description(text), owner(lookup), creation date(date).”



 Install an app from Marketplace
---------------------------------


1. Click
 ![btn_system_designer_8_shell.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “Application Management” → “Application Hub.”
2. Click
 
 New application
 
 (Fig. 7). This opens a window.
 




 Fig. 6 Add an app
 

![scr_app_hub_new_app.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/scr_app_hub_new_app.png)
3. Select
 
 Marketplace powered
 
 →
 
 Select
 
 . You will be redirected to the Creatio Marketplace website.
4. Log in under your credentials. If you do not have an account, sign up and log in to your account.
5. Select the app to install and look through its characteristics and support conditions. Click
 
 Install
 
 if the app requirements match your Creatio configuration. This opens a new page.
6. Specify the address of the website to install the app, accept the Public offer agreement and click
 
 Install
 
 (Fig. 7). You will be redirected to the page of the Creatio App Installation Wizard.
 




 Fig. 7 Installation page of a Creatio Marketplace app
 

![scr_chapter_marketplace_insert_web_address.png](/docs/sites/en/files/images/NoCode_Customization/marketplace_setup/scr_chapter_marketplace_insert_web_address.png)
7. Click
 
 Install
 
 on the Wizard page. The installation might take several minutes to finish. Wait for the process to complete before taking any further action.



 As a result, Creatio will add the app to the
 
 Application Hub
 
 section.
 




 Fig. 8 New app in the
 
 Application Hub
 
 section
 

![scr_appliication_hub_new_app_installed.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/scr_appliication_hub_new_app_installed.png)



 To view the results or test the app in operation, open the app and click
 
 Run app
 
 .
 



 If something goes wrong during the installation, you can always download the installation log and restore your Creatio configuration to the state before the app was installed in a single click.
 




 Fig. 9 App installation error
 

![scr_app_installation_error.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/scr_app_installation_error.png)



 Install an app from a file
----------------------------



 You can also install an app
 **from a \*.zip or \*.gz file** 
 . This method can be more convenient for Creatio on-site users who have limited access to external requests. To do this:
 


1. Open the needed app → the
 
 Packages
 
 tab → download the Marketplace app files.
2. Click
 ![btn_system_designer_8_shell.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “Application Management” → “Application Hub.”
3. Click
 
 New application
 
 . This opens a window.
4. Select
 
 Install from file
 
 →
 
 Select
 
 .
5. Click
 
 Select file
 
 on the page of the Marketplace App Installation Wizard and specify the app file path.
 



 Once you select the file, the installation will run automatically.



 Install an app into an environment that uses a balancer
---------------------------------------------------------



 If you use a load balancer to ensure fault tolerance of your Creatio application, the install process for apps differs. Install an app from a file into one Creatio instance, then transfer settings to other instances. Learn more in a separate article:
 [Compile an app on a web farm](https://academy.creatio.com/documents?id=2410) 
 .
 



 Deploy an app
---------------



 You can transfer apps between trial Creatio environments in the Application Hub without downloading apps. For example, this is useful for setting up demo websites and conducting presentations.
 



 To
 **transfer** 
 an app:
 


1. Click
 ![btn_system_designer_8_shell.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “Application Management” → “Application Hub.”
2. Click the
 ![scr_button_to_delete_app.png](/docs/sites/en/files/images/NoCodePlatform/ApplicationHub/scr_button_to_delete_app.png)
 button in the bottom right of the app icon → “Deploy” (Fig. 12).
 




 Fig. 10 Deploy the app
 

![scr_application_hub_deploy_app.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/scr_application_hub_deploy_app.png)
3. Select the target site →
 
 Deploy
 
 .
 




 Fig. 11 Deployment parameters
 

![scr_application_hub_deploy_app_parameters.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/scr_application_hub_deploy_app_parameters.png)



 As a result, Creatio will add the app to the
 
 Application Hub
 
 section of the target website.
 



 If something goes wrong during the installation, you can always download the installation log and restore your Creatio configuration in a single click.
 



 Download an app
-----------------



 You can download custom and Marketplace apps as archives to transfer them to different environments. To
 **download** 
 an app:
 


1. Click
 ![btn_system_designer_8_shell.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “Application Management” → “Application Hub.”
2. Click the
 ![scr_button_to_delete_app.png](/docs/sites/en/files/images/NoCodePlatform/ApplicationHub/scr_button_to_delete_app.png)
 button in the bottom right of the app icon → “Export” (Fig. 12) and wait for the process to complete.
 




 Fig. 12 Download an app
 

![app_hub_download_app.png](/docs/sites/en/files/images/NoCodePlatform/ApplicationHub/app_hub_download_app.png)



 As a result, the browser will download the \*.zip archive that contains all the app files to your machine.
 



 When you download an app, Creatio saves any data you entered into the app as well as the following metadata:
 


* icon
* color
* name
* description



 Creatio applies this data when you install the app into a different environment. If you install an app from an archive, Creatio creates an app automatically. An app name and code are based on the \*.zip or \*.gz archive name, the date specified in the app name is the archive downloading date an
 



 Delete an app
---------------



 You can delete custom and Marketplace apps. To
 **delete** 
 an app:
 


1. Click
 ![btn_system_designer_8_shell.png](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “Application Management” → “Application Hub.”
2. Click the
 ![scr_button_to_delete_app.png](/docs/sites/en/files/images/NoCodePlatform/ApplicationHub/scr_button_to_delete_app.png)
 button in the bottom right of the app icon → “Delete” (Fig. 13) and wait for the process to complete.
 




 Fig. 13 Delete an app
 

![app_hub_delete_app.png](/docs/sites/en/files/images/NoCodePlatform/ApplicationHub/app_hub_delete_app.png)




