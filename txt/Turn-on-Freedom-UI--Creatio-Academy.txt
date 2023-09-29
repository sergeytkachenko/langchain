


 As part of transition to new architecture, the application UI was revamped in Creatio version 8.0.6. Freedom UI encompasses the latest and greatest UX best practices to streamline the user workflow all while providing extensive personalization capabilities. Learn more in a separate article:
 [Get started with Creatio Freedom UI](https://academy.creatio.com/documents?id=2445) 
 .
 



 Freedom UI is fully compatible with out-of-the-box pages that use Classic UI. They continue to operate as intended regardless of the UI type. Most pages customized using code are compatible as well.
 



 General procedure to turn on Freedom UI
-----------------------------------------



 Freedom UI is turned on for
 **new** 
 Creatio instances by default.
 



 To turn on Freedom UI for
 **existing** 
 instances:
 


1. Make sure you have the permission to run the “Can show the system designer icon” (CanOpenSystemDesigner code) system operation.
2. Click
 ![](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “System setup” → “System settings.”
3. Open the “Use Freedom UI interface” (“UseNewShell” code) system setting that determines the user host.
4. Select the
 
 Default value
 
 checkbox. Otherwise, a user works in Classic UI.
5. Clear the
 
 Save value for current user
 
 checkbox to turn on Freedom UI for all existing users. Otherwise, Freedom UI will be turned on only for the current user.
6. Save the changes.
7. Log out of and log back in to Creatio to apply the changes.



 As a result, Freedom UI will be turned on for your Creatio users. The Creatio URL will be changed from [Creatio URL]/0/Nui/ViewModule.aspx to [Creatio URL]/0/shell/. We recommend turning on Freedom UI for all users only after you check whether the existing customizations are compatible with Freedom UI. You can manage the form pages to display in Freedom UI. Learn more in a separate article:
 [Manage the form pages in Freedom UI and Classic UI](https://academy.creatio.com/documents?id=2413) 
 .
 



 Turn on Freedom UI for external users in Portal Creatio
---------------------------------------------------------



 Freedom UI is turned on for external users in
 **new** 
 Creatio instances by default.
 



 We recommend turning on Freedom UI for external users in
 **existing** 
 instances only after you check whether the existing portal customizations are compatible with Freedom UI. To turn on Freedom UI for external users:
 


1. Turn on Freedom UI in the main Creatio application at least for some users. To do this, follow the steps in a different section:
 [General procedure to turn on Freedom UI](https://academy.creatio.com/documents?id=2446#title-2605-1) 
 .
2. Click
 ![](/docs/sites/en/files/images/NoCodePlatform/Manage_Apps/btn_system_designer_8_shell.png)
 in the top right → “System setup” → “System settings.”
3. Open the “Use Freedom UI interface for external users” (“UseNewShellForExternalUsers” code) system setting that determines the user host in Portal Creatio.
4. Select the
 
 Default value
 
 checkbox. Otherwise, external users work in Classic UI.
5. Save the changes.



 As a result, Freedom UI will be turned on for external users. You can manage the form pages to display in portal sections similarly to section pages of the main Creatio application. Learn more in a separate article:
 [Manage the form pages in the Freedom UI and Classic UI](https://academy.creatio.com/documents?id=2413) 
 .
 




