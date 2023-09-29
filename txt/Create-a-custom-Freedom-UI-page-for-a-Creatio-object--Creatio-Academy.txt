



 This functionality is available for Creatio 8.0.3 and later.
 




 You can set up a custom Freedom UI record page for any out-of-the-box or custom Creatio object in an editable app using no-code tools. This can be done in several ways:
 


* Set up a page in an app data model.
 [Read more >>>](#title-2371-1)
* Set up a page while setting up
 
 Button
 
 or
 
 List
 
 Freedom UI components.
 [Read more >>>](#title-2371-4)





 Attention.
 
 Creatio supports one record page per object. We do not recommend setting up custom record pages for the same object in multiple apps as this can cause hierarchy issues.
 



 For Creatio 8.0.6 and later objects can have both a Freedom UI and Classic UI form page. Learn more in a separate article:
 [Manage the form pages in the Freedom UI and Classic UI shell](https://academy.creatio.com/documents?id=2413) 
 .
 




 Creatio stores the custom Freedom UI record page in the app where you created it. The page is bound to the object via the
 
 Addon
 
 type configuration element stored in the app where you bound the page to the object. The app, page, and configuration element must be present in the environment for the functionality to operate as intended.
 



 Set up a custom Freedom UI record page in an app data model
-------------------------------------------------------------



 You can set up a custom record page in a data model of an editable app. For example, this is useful if you need to create a custom record page for an out-of-the-box Creatio object and the page is the only Freedom UI functionality required.
 


### 
 Set up a custom Freedom UI record page for an out-of-the-box Creatio object


1. Click
 ![btn_system_designer.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/btn_system_designer.png)
 in the top right →
 
 Application Hub
 
 .
2. Create an app based on a
 
 Custom
 
 template.
3. Open the
 
 Data models
 
 tab.
4. Click
 
 New data model
 
 →
 
 Replacing object
 
 .
5. Go to the
 
 Inheritance
 
 block and select the relevant object in the
 
 Parent object
 
 field. For example, “Account.”
6. Open the
 
 Pages
 
 tab.
7. Select an existing Freedom UI page in the
 
 Default page
 
 field or click
 ![btn_add_data_model.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/btn_add_data_model.png)
 to the right of the field to create and set up a new page (Fig. 1).
 

 Fig. 1 Create a custom record page
 

![create_a_record_page.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/create_a_record_page.png)
8. Click
 
 Save
 
 .



 As a result, Creatio will use the page to display individual records of the parent object everywhere in Creatio, including existing sections.
 





 Note.
 
 In Creatio version 8.0.6 and later you can also add a Freedom UI page for an object that has only classic UI section via Object designer. To do this you will also need to add the new page to the
 
 Edit pages in UIs by object
 
 lookup. Learn more in a separate article:
 [Manage the form pages in the Freedom UI and Classic UI shell](https://academy.creatio.com/documents?id=2413&anchor=title-2514-2) 
 .
 



### 
 Set up a custom Freedom UI record page for an existing app data model


1. Click
 ![btn_system_designer.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/btn_system_designer.png)
 in the top right →
 
 Application Hub
 
 .
2. Open the relevant app.
3. Open the
 
 Data models
 
 tab.
4. Open the needed data model.
5. Take steps 6-8 of the instructions in the previous section.



 As a result, Creatio will use the page to display individual records of the data model everywhere in Creatio, including existing sections.
 



 Set up a custom Freedom UI record page while setting up Freedom UI components
-------------------------------------------------------------------------------



 You can also set up a custom Freedom UI record page while setting up the
 [Button](https://academy.creatio.com/documents?id=2376&anchor=title-2230-17)
 or
 [List](https://academy.creatio.com/documents?id=2376&anchor=title-2230-77)
 Freedom UI components. For example, this is useful if you need to bind the custom record page to additional Freedom UI functionality.
 


### 
 Use a [Button] component


1. Click
 ![btn_system_designer.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/btn_system_designer.png)
 in the top right →
 
 Application Hub
 
 .
2. Open the relevant app.
3. Open the page to bind to the custom Freedom UI record page.
4. Drag a
 
 Button
 
 component to the canvas. Alternatively, select an existing button and click
 ![btn_properties.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/btn_properties.png)
 .
5. Go to the
 
 Action
 
 block in the setup area and select
 
 Open new record
 
 or
 
 Open existing record
 
 in the
 
 Action
 
 field depending on your business goals.
6. Select the data model whose record page to set up in the
 
 Which record to create?
 
 or
 
 Which object to open record of?
 
 field (Fig. 2). For example, “Account.” The field name is based on the selected action.
 

 Fig. 2 Select a data model
 

![select_an_object.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/select_an_object.png)
7. Click
 ![btn_page_setup.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/btn_page_setup.png)
 to the right of the field that contains the selected data model. This opens a dialog.
8. Select an existing Freedom UI page in the
 
 Default page
 
 field or click
 ![btn_add.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/btn_add.png)
 to the right of the field to create and set up a new page.
9. Click
 
 Save
 
 .



 As a result, Creatio will use the page to display individual records of the data model everywhere in Creatio, including existing sections.
 


### 
 Use a [List] component


1. Click
 ![btn_system_designer.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/btn_system_designer.png)
 in the top right →
 
 Application Hub
 
 .
2. Open the relevant app.
3. Open the page to bind to the custom Freedom UI record page.
4. Drag a
 
 List
 
 component to the canvas. Alternatively, select an existing list and click
 ![btn_properties.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/btn_properties.png)
 .
5. Select the data model whose record page to set up in the
 
 Object
 
 field of the setup area. For example, “Account.”
6. Click
 ![btn_page_setup.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/btn_page_setup.png)
 to the right of the
 
 Object
7. field. This opens a dialog.
8. Select an existing Freedom UI page in the
 
 Default page
 
 field of the dialog or click
 ![btn_add.png](/docs/sites/en/files/images/NoCodePlatform/custom_record_pages/btn_add.png)
 to the right of the field to create and set up a new page.
9. Click
 
 Save
 
 .



 As a result, Creatio will use the page to display individual records of the data model everywhere in Creatio, including existing sections.
 




