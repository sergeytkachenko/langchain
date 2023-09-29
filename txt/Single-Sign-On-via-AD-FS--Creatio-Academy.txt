



 This article is relevant to Creatio version 8.0.3 and later. If you need to set up integration with Creatio version 8.0.2 and earlier for testing purposes or to look for errors, follow the instructions for Creatio version 7.18.
 




 You can integrate your Active Directory Federation Services (AD FS) instance to manage single sign-on for your members. To do this, perform the setup both in AD FS and Creatio.
 





 Attention.
 
 This example uses the, https://site01.creatio.com/Demo\_161215/ Creatio website and http://ADFS01.mysite.com/ADFS/ AD FS website. Replace these URLs with the corresponding URLs of your websites when you perform the actual setup.
 




 In general, the following
 **steps** 
 are required to set up Single Sign -On in Creatio:
 


1. Download the file that contains the integration metadata.
 [Read more >>>](#title-2415-1)
2. Perform the setup in AD FS.
 [Read more >>>](#title-2415-2)
3. Perform the setup in Creatio.
 [Read more >>>](#title-2415-3)



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
4. Select “AD FS.” This opens the setup page.
5. Click
 
 Get metadata
 
 .
6. Save the file to your local machine.



 Perform the setup in AD FS
----------------------------


1. Add a new Relying Party Trust to ADFS (Fig. 1).
 




 Fig. 1 Relying Party Trust menu
 

![scr_chapter_single_sign_on_adfs_step1_add_party.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step1_add_party.png)
2. Select “Import data about the relying party from file,” as shown on the Fig. 2.
 




 Fig. 2 “Import data about the relying party from file” option
 

![scr_chapter_single_sign_on_adfs_step2_import_data.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/8_0/scr_chapter_single_sign_on_adfs_step2_import_data.png)
3. Specify the full website address in the identifier settings and click
 
 Add
 
 , as shown on the Fig. 3.
 




 Fig. 3 Identifier
 

![scr_chapter_single_sign_on_adfs_step7_set_identifier.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step7_set_identifier.png)





 Attention.
 
 The identifier is required to verify the authenticity of a source that requests authentication. The URL must match verbatim, including the “/” at the end.
4. Set up the rest of the parameters according to your security requirements. You can leave default values for test purposes.
5. Click
 
 Finish
 
 . This opens a window.
6. Click
 
 Add Rule
 
 and add a new SAML Assertion to SAML Response rule (Fig. 4)
 




 Fig. 4 “Add rule” button
 


![scr_chapter_single_sign_on_adfs_step9_add_rule.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step9_add_rule.png)




 Note.
 
 Creatio will use the data generated based on the new rule to search for users, as well as to update their profiles and roles.
7. Keep the default settings and click
 
 Next
 
 on the first step of the Rule Wizard. Set up a set of parameters to receive from the user’s data (Fig. 5). In this example, the user’s name and a list of domain groups will be passed via SAML Assertion.
 




 Fig. 5 Rule parameters
 

![scr_chapter_single_sign_on_adfs_step10_rule_parameters.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step10_rule_parameters.png)
8. Click
 
 Save
 
 .
9. Open the Trusted Relay settings, go to the
 
 Advanced
 
 tab, and specify SHA-1 encryption according to the website certificate algorithm.
10. Add the public certificate key on the
 
 Encryption
 
 tab to set up the SAML encryption (Fig. 6).
 





 Note.
 
 If you are using Creatio in the cloud, get the public certificate key from the Creatio support service.
 





 Fig. 6
 
 Encryption
 
 tab
 

![scr_chapter_single_sign_on_adfs_step13_add_public_key.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step13_add_public_key.png)
11. Add the logout endpoint and set the following parameters (Fig. 7) on the
 
 Endpoints
 
 tab:
 


	* Set
	 
	 Endpoint type
	 
	 to “SAML Logout”.
	* Set
	 
	 Binding
	 
	 to “Redirect”.
	* Enter https://site01.creatio.com/Demo\_161215/ServiceModel/AuthService.svc/SsoLogout in the
	 
	 Trusted URL
	 
	 parameter.
	 
	
	
	
	
	 Fig. 7 Endpoint parameters
	 
	
	![scr_chapter_single_sign_on_adfs_step13_add_endpoint.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step13_add_endpoint.png)
12. Add the Logout Request certificate to the
 
 Signature
 
 tab, as specified on the Fig. 8.
 




 Fig. 8 Logout Request certificate
 

![scr_chapter_single_sign_on_adfs_step14_add_certificate.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step14_add_certificate.png)





 Attention.
 
 Single Sign-Out does not work without a certificate.
 




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
4. Select “AD FS.” This opens the setup page.
5. Fill out the
 
 AD FS tenant URL
 
 parameter. Creatio will populate other parameters automatically.
6. Fill out the provider's name to display on the Creatio login page in the
 
 Display name
 
 field.
 




 Fig. 9 AD FS settings
 

![scr_ad_fs_settings_example_807.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/8_0/scr_ad_fs_settings_example_807.png)
7. Save the changes.
8. Turn on Just-In-Time Provisioning (optional). This mechanism automatically creates the corresponding Creatio user account with data from the identity provider, such as user group, employee name, contact information, etc. To do this, select the
 
 Create and update users data when log in (Just-In-Time Provisioning)
 
 checkbox and map the fields (Fig. 10).
 




 Fig. 10 Set up Just-In-Time Provisioning
 

![scr_set_up_JIT_807.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/8_0/scr_set_up_JIT_807.png)
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
 
 (Fig. 11).
 




 Fig. 11 Test the provider
 

![scr_test_sso_provider.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/8_0/scr_test_sso_provider.png)




