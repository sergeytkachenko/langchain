



 This article is relevant to Creatio version 8.0.3 and later.
 




 You can integrate Creatio with Okta to manage single sign-on for all Creatio users that work in the corporate network.
 





 Attention.
 
 The example uses the https://site01.creatio.com/Demo\_161215/ Creatio URL. Replace this URL with the corresponding URL of your website when you perform the actual setup.
 




 In general, the following
 **steps** 
 are required to set up Single Sign-On in Creatio:
 


1. Download the file that contains the integration metadata.
 [Read more >>>](#title-2451-1)
2. Perform the setup in Okta.
 [Read more >>>](#title-2451-2)
3. Perform the setup in Creatio.
 [Read more >>>](#title-2451-3)



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
4. Select “Okta.” This opens the setup page.
5. Click
 
 Get metadata
 
 .
6. Save the file to your local machine.



 Perform the setup in Okta
---------------------------


1. Add a new SAML 2.0 app.
 

 Fig. 1 New SAML 2.0 app
 

![scr_Okta_add_saml20.png](/docs/sites/en/files/images/Setup_and_Administration/okta_sso/scr_Okta_add_saml20.png)
2. Fill out the general parameters: app name, logo, and description. These parameters will be displayed to all users. Click
 
 Next
 
 .
 

 Fig. 2 The general parameters
 

![scr_okta_general_settings.png](/docs/sites/en/files/images/Setup_and_Administration/okta_sso/scr_okta_general_settings.png)
3. Fill out the SSO parameters:
 


	1. Enter the URL of your Creatio website SSO in the
	 
	 Single sign on URL
	 
	 parameter. Use the following pattern: https://yoursite.com/ServiceModel/AuthService.svc/SsoLogin.
	2. Enter the URL of your Creatio website in the
	 
	 Audience URI (SP Entity ID)
	 
	 parameter. For example, https://site01.creatio.com/Demo\_161215/.
	3. Select “Unspecified” in the
	 
	 Name ID Format
	 
	 parameter. This specifies the data type required to log in to your website.
	4. Select “Email” in the
	 
	 Application username
	 
	 parameter. This specifies the parameter required for Just-In-Time Provisioning to work correctly.
	 
	
	 Fig. 3 The SSO parameters
	 
	
	![scr_Okta_sso_settings.png](/docs/sites/en/files/images/Setup_and_Administration/okta_sso/scr_Okta_sso_settings.png)
4. Fill out the advanced settings:
 


	1. Specify whether to sign queries for safe data transfer in the
	 
	 Response
	 
	 parameter. Select “Signed” for the production environment or “Unsigned” for the testing environment.
	2. Specify the security configuration type in the
	 
	 Assertion Signature
	 
	 parameter. Select “Signed” for the production environment or “Unsigned” for the testing environment.
	3. Set
	 
	 Enable Single Logout
	 
	 to turn on single sign-out for your Creatio website.
	 
	
	 Fig. 4 The advanced settings
	 
	
	![scr_Okta_advanced_settings.png](/docs/sites/en/files/images/Setup_and_Administration/okta_sso/scr_Okta_advanced_settings.png)
5. Map the following fields for JIT Provisioning:
 


	1. Map
	 
	 Name
	 
	 to “name.”
	2. Map
	 
	 Name format
	 
	 to “Basic.”
	3. Map
	 
	 Value
	 
	 to “user.email.”
	 
	
	 Fig. 5 Mapping fields
	 
	
	![scr_Okta_attribute_statement.png](/docs/sites/en/files/images/Setup_and_Administration/okta_sso/scr_Okta_attribute_statement.png)
6. Download the Okta Certificate if you are going to use Signed Response, Assertion Signature, and Single Logout.
 

 Fig. 6 The Okta certificate download
 

![scr_Okta_certificate.png](/docs/sites/en/files/images/Setup_and_Administration/okta_sso/scr_Okta_certificate.png)



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
	1. Enter the unique identifier you got while setting up Okta in the
	 
	 IdP Issuer
	 
	 parameter.
	2. Enter the URL of the identity provider’s single sign-on in the
	 
	 SingleSignOnServiceUrl
	 
	 parameter. For Okta, this is usually https://okta.com/qmBNBnkAkopZXwJpjpu5/sso/saml.
	3. Enter the URL of the identity provider’s single sign-off in the
	 
	 SingleLogoutServiceUrl
	 
	 parameter. For Okta, this is usually https://test-site.okta.com/app/test-site\_creatio\_1/qmBNBnkAkopZXwJpjpu5/sso/saml.
6. Fill out the provider's name to display on the Creatio login page in the
 
 Display name
 
 field.
7. Save the changes.
8. Turn on Just-In-Time Provisioning (optional). This mechanism automatically creates the corresponding Creatio user account with proper data from the identity provider, such as user group, employee name, contact information, etc. To do this, select the
 
 Create and update users data when log in (Just-In-Time Provisioning)
 
 checkbox and map the fields.
 

 Fig. 7 Set up Just-In-Time Provisioning
 

![scr_set_up_JIT_okta_807.png](/docs/sites/en/files/images/Setup_and_Administration/okta_sso/scr_set_up_JIT_okta_807.png)
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
 
 (Fig. 8).
 




 Fig. 8 Test the provider
 

![scr_test_sso_provider.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/8_0/scr_test_sso_provider.png)




