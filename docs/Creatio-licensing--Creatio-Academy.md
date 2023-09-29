


 Only licensed users have access to Creatio functionality.
 



 To
 **license Creatio** 
 :
 


1. Add licenses to Creatio.
 [Read more >>>](#HT_chapter_licensing_software)
2. Distribute the available licenses among the user accounts.
 [Read more >>>](#HT_chapter_licensing_distribute)



 Set up licensing in the
 
 License manager
 
 section (Fig. 1).
 




 Fig. 1 The
 
 License manager
 
 section
 

![scr_chapter_licensing.png](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_chapter_licensing.png)



 If the licenses expire, the license manager page will open for a user with the “System administrators” role automatically when they log in to Creatio.
 





 Note.
 
 Viewing, distributing, and recalling licenses requires permissions to the “Manage user licenses” (the “CanManageLicUsers” code) system operation. Read more:
 [Set up system operation permissions](/docs/7-18/user/setup_and_administration/user_and_access_management/access_management/system_operation_permissions_shortcut/system_operation_permissions) 
 .
 





 Add licenses to Creatio
--------------------------



 The licensing process is similar for all types of licenses used in Creatio.
 



 When purchasing licenses, extending available licenses, and updating Creatio on-site:
 


1. Generate a license request file and send it to the Creatio technical support team.
2. The support team will send a file for you to upload to Creatio.



 Starting from version 7.17.4, this procedure is also required when updating Creatio on-site.
 


### 

 Generate a license request


1. Click the
 ![btn_system_designer.png](/guides/sites/default/files/documentation/user/ru/licensing/BPMonlineHelp/licensing_creatio/btn_system_designer.png)
 button to open the System Designer.
2. Click “
 **License manager** 
 ” under “Users and administration”.
3. Click
 
 Actions
 
 →
 
 Request
 
 .
4. Enter the company Id for licensing. Creatio provides the Id after the purchase. Alternatively, request it from Creatio support.
5. Click
 
 Generate a license request file
 
 (Fig. 2).
 



 This will generate a \*.tlr license request file.
 




 Fig. 2 Generating a license request
 

![scr_chapter_licensing_wnd_license_request.gif](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_chapter_licensing_wnd_license_request.gif)
6. For version 7.17.4 and later: fill out the
 
 License Version
 
 field with the Creatio version to which you are planning to update.
7. Send the license request file to Creatio technical support team. In response, the team will send you a file with the information about purchased licenses.



 You can also request licenses from the
 
 System users
 
 section by clicking
 
 Request licenses
 
 in the
 
 Actions
 
 menu (Fig. 3).
 




 Fig. 3 Generating a license request
 

![scr_user_license_request.gif](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_user_license_request.gif)


### 

 Upload licenses to Creatio


1. Save the license file received from the technical support team.
2. Click the
 ![btn_system_designer00001.png](/guides/sites/default/files/documentation/user/ru/licensing/BPMonlineHelp/licensing_creatio/btn_system_designer00001.png)
 button to open the System Designer.
3. Click “
 **License manager** 
 ” under “Users and administration”.
4. Click
 
 Actions
 
 →
 
 Upload
 
 (Fig. 4).
 




 Fig. 4 Uploading a license file to Creatio
 

![scr_chapter_licensing00002.png](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_chapter_licensing00002.png)
5. Specify the path to the license file you saved earlier.



 You can also request licenses from the
 
 System users
 
 section by clicking
 
 Upload licenses
 
 in the
 
 Actions
 
 menu (Fig. 5).
 




 Fig. 5 Uploading a license file to Creatio
 

![scr_chapter_licensing00002_user.png](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_chapter_licensing00002_user.png)



 This will upload the new licenses to Creatio. The total license number may increase, and the available licenses will be extended.
 




 Distribute licenses among users
----------------------------------



 To allow the new employees to log in or use specific functions, their user accounts must be licensed. A system administrator can redistribute the available licenses at any time. The number of active and available licenses is displayed on the product licensing page and depends on the license type (Fig. 6 and 7).
 



 The following license types are available in Creatio:
 


* **Personal licenses** 
 provide access to the product for specific users. These licenses are linked to user accounts. When distributing personal licenses, make sure the number of provided licenses does not exceed the number of purchased licenses.
 

 Fig. 6 The number of personal licenses.
 

![scr_chapter_licensing_name_product.png](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_chapter_licensing_name_product.png)
* **Server licenses** 
 provide access to additional Creatio functionality, for example, phone integration, to all users on the server. Unlike personal licenses, server licenses are not limited by the number of users.
 

 Fig. 7 The number of server licenses
 

![scr_chapter_licensing_server_product.png](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_chapter_licensing_server_product.png)



 Distribute licenses in the
 
 License manager
 
 or
 
 System users
 
 sections. If you need to distribute licenses to several user accounts at once, use the
 
 License manager
 
 section:
 


1. Click the
 ![btn_system_designer00003.png](/guides/sites/default/files/documentation/user/ru/licensing/BPMonlineHelp/licensing_creatio/btn_system_designer00003.png)
 button to open the System Designer.
2. Click “
 **License manager** 
 ” under “Users and administration”.
3. Select a license from the list. Use the search field and list sorting by columns to quickly find the needed product by name.
4. Click the product name.
 



 The product licensing page will open. You can view the license type, the start and due dates, the status, the total number of available licenses, as well as distribute the available licenses among users on this page.
5. Click
 
 Add
 
 and select the users to whom you would like to issue licenses (Fig. 8).
 




 Fig. 8 Adding users in the license manager
 

![scr_chapter_licensing_wnd_licenses_select.png](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_chapter_licensing_wnd_licenses_select.png)



 Note that the number of licensed users should not exceed the number of available licenses. View the number of available/used licenses on the pie chart on the left (Fig. 8).
 



 You can recall licenses to redistribute them among other users if needed.
6. To recall licenses, select users from the list and click
 
 Recall
 
 (Fig. 9).
 




 Fig. 9 Recalling licenses
 

![scr_chapter_licensing_wnd_licenses_delete.png](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_chapter_licensing_wnd_licenses_delete.png)



 You can also hover over the names of users whose licenses you would like to recall and click the
 ![btn_delete.png](/guides/sites/default/files/documentation/user/ru/licensing/BPMonlineHelp/licensing_creatio/btn_delete.png)
 button (Fig. 10).
 




 Fig. 10 Recalling licenses
 

![scr_chapter_licensing_wnd_licenses_delete_button.png](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_chapter_licensing_wnd_licenses_delete_button.png)
7. Click
 
 Apply
 
 to save the changes.
8. Use the same procedure to distribute the available licenses for other purchased products.
9. Close the license manager window.



 As a result, Creatio will distribute/recall licenses for the specified user accounts.
 




 Delete licenses from Creatio
-------------------------------



 Sometimes, deleting licenses is required. For example, you need to switch Creatio to the demo mode.
 



 To
 **delete licenses from Creatio** 
 :
 


1. Click the
 ![btn_system_designer.png](/guides/sites/default/files/documentation/user/ru/licensing/BPMonlineHelp/licensing_creatio/btn_system_designer.png)
 button to open the System Designer.
2. Click “
 **License manager** 
 ” under “Users and administration”.
3. Click
 
 Actions
 
 →
 
 Delete
 
 (Fig. 11).
 




 Fig. 11 Deleting licenses
 

![scr_chapter_licensing_delete_license.gif](/docs/sites/en/files/images/Setup_and_Administration/creatio_licensing/scr_chapter_licensing_delete_license.gif)



 As a result, Creatio will delete all licenses.
 




