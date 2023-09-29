


 Creatio can be integrated with any identity provider that supports the SAML 2.0 protocol. You can use OneLogin SSO portal as a single sign-on point for all your services, including Creatio. To do this, perform he setup both in OneLogin and Creatio.
 





 Attention.
 
 The example uses https://site01.creatio.com/ Creatio URL and “appid” application id in OneLogin. Replace these values with your website URL and the id of the corresponding application in OneLogin when you perform the actual setup.
 




 In general, the following
 **steps** 
 are required to set up Single Sign-On in Creatio:
 


1. Download the file that contains the integration metadata.
 [Read more >>>](#title-2452-1)
2. Perform the setup in your provider.
 [Read more >>>](#title-2452-2)
3. Perform the setup in Creatio.
 [Read more >>>](#title-2452-3)



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
4. Select “Custom SAML.” This opens the setup page.
5. Click
 
 Get metadata
 
 .
6. Save the file to your local machine.



 Perform the setup in OneLogin
-------------------------------


1. Log in to OneLogin using an administrator account.
2. Click
 
 Apps
 
 and select
 
 Add Apps
 
 . Enter “Creatio” in the search bar and select the Creatio application.
3. If needed, change the value in the
 
 Display name
 
 field, modify the application icons, or clear the
 
 Visible in portal
 
 checkbox. These settings affect the way the website is displayed on the OneLogin website.
4. Click
 
 Save
 
 .
5. Go to the
 
 Configuration
 
 tab and enter your website domain name in the
 
 Creatio site
 
 field (Fig. 1). For example, “site01.”
 





 Fig. 1
 
 Website configuration page
 

![scr_chapter_single_sign_on_onelogin_step3_set_site.png](/docs/sites/en/files/images/Setup_and_Administration/onelogin_integration/scr_chapter_single_sign_on_onelogin_step3_set_site.png)



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
4. Select “Custom SAML.” This opens the setup page.
5. Fill out the following parameters:
	1. Enter your provider’s website in the
	 
	 Entity ID
	 
	 parameter. For example, httpsw://app.onelogin.com/saml/metadata/appid for OneLogin.
	2. Enter the URL of the identity provider’s single sign-on in the
	 
	 Single Sign On URL
	 
	 parameter. You can retrieve the URL from the SAML 2.0 Endpoint (HTTP) on the trusted application page.
	3. Enter the URL of the identity provider’s single sign-off in the
	 
	 Single Logout URL
	 
	 parameter. You can retrieve the URL from the SLO Endpoint (HTTP) on the trusted application page.
6. Fill out the provider's name to display on the Creatio login page in the
 
 Display name
 
 field.
7. Save the changes.
8. Turn on Just-In-Time Provisioning (optional). This mechanism automatically creates the corresponding Creatio user account with proper data from the identity provider, such as user group, employee name, contact information, etc. To do this, select the
 
 Create and update users data when log in (Just-In-Time Provisioning)
 
 checkbox and map the fields.
 

 Fig. 2 Set up Just-In-Time Provisioning
 

![scr_set_up_JIT_custom_807.png](/docs/sites/en/files/images/Setup_and_Administration/onelogin_integration/8_0/scr_set_up_JIT_custom_807.png)
9. Define your provider.
 




 For Creatio version 8.0.7 and later
 




 Specify the provider in the “Default SSO provider” system setting (“DefaultSsoProvider” code) and save the changes.
 





 For Creatio version 8.0.3 – 8.0.6
 




 Select your provider in the
 
 SSO identity provider
 
 field and save the changes.
10. Test whether the provider is working correctly (optional).
 




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




