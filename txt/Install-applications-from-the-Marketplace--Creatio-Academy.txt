


 Use the
 
 Installed applications
 
 section to manage Creatio marketplace applications and add-ons.
 



 The section lets you:
 


* install applications for permanent or trial use
* view the list of installed applications
* purchase and distribute licenses
* delete applications



 Install an application from Marketplace
-----------------------------------------


1. Click the
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/apps_and_extensions/BPMonlineHelp/apps_and_extensions/btn_system_designer.png)
 button to open the System Designer.
2. Click “Installed applications” in the “Applications” block.
3. Click the
 
 Add application
 
 button.
4. Select
 
 Choose from Marketplace
 
 from the dropdown list. You will be redirected to the Creatio Marketplace web site.
5. Log in under your credentials. If you do not have an account, sign up and log in to your account.
6. Select the application to install and review its features and the support conditions. Click
 
 Install
 
 If the application requirements match your Creatio configuration. This will open a new page.
7. Specify the web site address to install the application and click
 
 Install
 
 (Fig. 1). You will be redirected to the page of the Creatio application Installation Wizard.
 

 Fig. 1 The installation page of a Creatio Marketplace application
 

![scr_chapter_marketplace_insert_web_address.png](/guides/sites/en/files/documentation/user/en/apps_and_extensions/BPMonlineHelp/apps_and_extensions/scr_chapter_marketplace_insert_web_address.png)
8. Click
 
 Install
 
 on the page of the Creatio application Installation Wizard. The installation may take several minutes to finish. Wait for the process to complete before taking any further action.



 Install an application from a file
------------------------------------



 You can also install an application
 **from a \*.zip or \*.gz file** 
 . This method may be more convenient for Creatio on-site users who have limited access to external requests. To do this:
 


1. Open the needed application → the
 
 Packages
 
 tab → download the Markeplace application files.
2. Click
 
 Add application
 
 in the
 
 Installed applications
 
 section →
 
 Install from file
 
 .
3. Click
 
 Select file
 
 on the page of the Marketplace application Installation Wizard and specify the path to the application files.
   

 Once you select the file, the installation will run automatically.



 As a result, Creatio will add the new application to the
 
 Installed applications
 
 section. You may need to add new sections in workplaces before you start working with the application.
 



 Install an application into an environment that uses a balancer
-----------------------------------------------------------------



 If you use a load balancer to ensure fault tolerance of your Creatio application, the install process for Marketplace applications will differ.
 





 Note.
 
 Install packages that contain changes created and tested on other environments into a production environment in a similar way.
 




 We recommend performing the setup outside of business hours since Creatio will be unavailable. View the general package installation procedure below. The specifics may vary based on the load balancer you use with your Creatio application.
 


### 
 The general installation procedure


1. **Set up a redirect** 
 to the placeholder page that explains the reasons for the downtime on the load balancer’s end. Learn more about setting up redirects in the vendor documentation. For example,
 [HAProxy Enterprise](https://www.haproxy.com/documentation/hapee/latest/traffic-routing/redirects/) 
 .
2. **Stop all Creatio instances** 
 except one. Learn more in the Update guide:
 [Stopping the site](/docs/release/update-guide/update-guide#title-143-13) 
 .
3. **Back up** 
 the database. Learn more in the Update guide:
 [Creating database backup](/docs/release/update-guide/update-guide#title-143-2) 
 .
4. Open the needed application → the
 
 Packages
 
 tab →
 **download the Marketplace application files** 
 .
5. Go to the active Creatio instance and
 **install the Marketplace application** 
 . Learn more:
 [Install an application from a file](https://academy.creatio.com/documents?id=1836&anchor=title-188-2) 
 .
 



 Creatio will run the compilation automatically after the installation finishes.
 



 Proceed to the next step upon successful compilation. If an error occurs, download the application logs and view the detailed error description.
 


	* If the error is on Creatio’s end, roll back to the previous configuration state (Fig. 2) and perform the installation once more.
	 
	
	
	
	
	 Fig. 2 Restore the configuration after the installation error of a Creatio Marketplace application
	 
	
	![scr_marketplace_failed_setup.png](/docs/sites/en/files/images/NoCode_Customization/marketplace_setup/scr_marketplace_failed_setup.png)
	
	
	
	 If the configuration rollback does not resolve the issue, restore the database from a backup and try again. Learn more:
	 [Deploy Microsoft SQL database for Creatio](https://academy.creatio.com/documents?product=administration&ver=7&id=2132) 
	 ,
	 [Deploy Oracle Database for Creatio](https://academy.creatio.com/documents?product=administration&ver=7&id=2133) 
	 ,
	 [Deploy PostgreSQL database (Linux)](https://academy.creatio.com/documents?product=administration&ver=7&id=2121) 
	 ,
	 [Deploy PostgreSQL database (Windows)](https://academy.creatio.com/documents?product=administration&ver=7&id=2134) 
	 .
	* If the error is on Marketplace application’s end, contact the application developer support.
6. **Apply the changes** 
 on the web farm level. To do this, copy the contents of the following folders to every Creatio instance:
	* WebApp/conf/ and WebApp/Terrasoft.Configuration/Pkg for Creatio
	 **NET Framework**
	* Creatio root folder for Creatio
	 **.NET Core**
7. **Flush** 
 Redis.
8. **Start** 
 the stopped Creatio instances. Learn more in the Update guide:
 [Website starting, compilation and verification](/docs/release/update-guide/update-guide#title-143-14) 
 .
9. **Disable the redirect** 
 on the load balancer’s end.



 Manage applications
---------------------



 After the installation, you can
 **purchase licenses** 
 to continue using the application after the trial period or delete it.
 



 To go to the License Manager, select the needed application in the
 
 Installed applications
 
 section and click the
 
 Licenses
 
 button.
 



 To
 **delete** 
 the installed application, click
 
 Delete
 
 and wait for the process to finish.
 




