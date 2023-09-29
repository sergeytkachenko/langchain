



 This article is relevant to Creatio version 8.0.3 and later. If you need to set up integration with Creatio version 8.0.2 and earlier for testing purposes or to look for errors, follow the instructions for Creatio version 7.18.
 




 You can integrate Creatio with Azure Active Directory (Azure AD) to manage single sign-on for all Creatio users that work in the corporate network.
 





 Attention.
 
 The example uses the https://site01.creatio.com/Demo\_161215/ Creatio URL. Replace these URLs with the corresponding URLs of your sites when you perform the actual setup.
 




 In general, the following
 **steps** 
 are required to set up Single Sign -On in Creatio:
 


1. Download the file that contains the integration metadata.
 [Read more >>>](#title-2449-1)
2. Perform the setup in Azure AD.
 [Read more >>>](#title-2449-2)
3. Perform the setup in Creatio.
 [Read more >>>](#title-2449-3)



 Download the metadata
-----------------------


1. Click the
 ![](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/8_0/btn_system_designer_8_shell.png)
 button to open the
 **System Designer** 
 .
2. Click
 
 Single Sign On configuration
 
 .
3. Click
 ![](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/8_0/btn_add_record.png)
 . This opens a drop-down menu.
4. Select “Azure AD.” This opens the setup page.
5. Click
 
 Get metadata
 
 .
6. Save the file to your local machine.



 Perform the setup in Azure AD
-------------------------------



 To configure the settings below, register Creatio in the administrator account of the enterprise identity service of Azure Active Directory (Azure AD). Learn more in the
 [Microsoft documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app) 
 .
 


1. Add a new SSO application (Trusted Relaying Party) to Azure AD:
	1. Open the
	 
	 Enterprise applications
	 
	 section →
	 
	 All Applications
	 
	 .
	2. Click
	 
	 New application
	 
	 .
	3. Select “Creatio” in the
	 
	 Add from the gallery
	 
	 section and add the application. Learn more in the Microsoft documentation:
	 [Add Creatio from the gallery](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/bpmonline-tutorial#add-creatio-from-the-gallery) 
	 .
2. Open the
 
 Single sign-on
 
 section and specify the following parameters:
	1. Select “SAML” in the
	 
	 Single Sign-on Mode
	 
	 parameter.
	2. Enter the full website name, for example, “https://site01.creatio.com/Demo\_161215/,” in the
	 
	 Identifier
	 
	 parameter.
	3. Enter the full website name and ““/ServiceModel/AuthService.service.svc/SsoLogin” address, for example, “https://site01.creatio.com/Demo\_161215/ServiceModel/AuthService.service.svc/SsoLogin,” in the
	 
	 Reply URL
	 
	 parameter.
3. Save the following data to perform the setup in Creatio (Fig. 1):
	* Azure AD Identifier
	* Login URL
	* Logout URL




 Fig. 1 Data required to perform the setup in Creatio
 

![creatio_azure_settings.png](/docs/sites/en/files/images/Setup_and_Administration/azure_ad/creatio_azure_settings.png)





 Note.
 
 By default, Azure AD passes the following fields to Creatio:
 
 Given name
 
 ,
 
 Surname
 
 ,
 
 Email address
 
 ,
 
 Name
 
 . The email address serves as the username.
 




 Perform the setup in Creatio
------------------------------



 Follow these steps to set up single sign-on in Creatio:
 


1. Click the
 ![](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/8_0/btn_system_designer_8_shell.png)
 button to open the
 **System Designer** 
 .
2. Click
 
 Single Sign On configuration
 
 .
3. Click
 ![](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/8_0/btn_add_record.png)
 . This opens a drop-down menu.
4. Select “Azure AD.” This opens the setup page.
5. Fill out the following parameters:
	1. Enter the unique identifier you got while setting up Azure AD in the
	 
	 Azure AD identifier
	 
	 parameter.
	2. Enter the URL of the identity provider’s single sign-on in the
	 
	 SingleSignOnServiceUrl
	 
	 parameter. For Azure AD, this is usually https://login.microsoftonline.com/<azure account="" id="">/saml2. Find out the settings of the added connector in the Azure account.
	3. Enter the URL of the identity provider’s single sign-off in the
	 
	 SingleLogoutServiceUrl
	 
	 parameter. For Azure AD, this is usually https://logout.microsoftonline.com/<azure account="" id="">/saml2. Find out the settings of the added connector in the Azure account.
6. Fill out the provider's name to display on the Creatio login page in the
 
 Display name
 
 field.
7. Turn on Just-In-Time Provisioning (optional). This mechanism automatically creates the corresponding Creatio user account with proper data from the identity provider, such as user group, employee name, contact information, etc. To do this, select the
 
 Create and update users data when log in (Just-In-Time Provisioning)
 
 checkbox and map the fields.
 

 Fig. 2 Set up Just-In-Time Provisioning
 

![scr_set_up_JIT_azure_807.png](/docs/sites/en/files/images/Setup_and_Administration/azure_ad/8_0/scr_set_up_JIT_azure_807.png)
8. Define your provider.
 




 For Creatio version 8.0.7 and later
 




 Specify the provider in the “Default SSO provider” system setting (“DefaultSsoProvider” code) and save the changes.
 





 For Creatio version 8.0.3 – 8.0.6
 




 Select your provider in the
 
 SSO identity provider
 
 field and save the changes.
9. Test whether the provider is working correctly (optional).
 




 For Creatio version 8.0.7 and later
 




 Open the provider page and click
 
 Test Sign In
 
 .
 






 For Creatio version 8.0.3 – 8.0.6
 




 Click
 
 Test
 
 (Fig. 3).
 




 Fig. 3 Test the provider
 

![scr_test_sso_provider.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/8_0/scr_test_sso_provider.png)




