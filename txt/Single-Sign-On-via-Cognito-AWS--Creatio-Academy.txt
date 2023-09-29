



 This functionality is available for Creatio 8.0.8 and later.
 




 Creatio can be integrated with any identity provider that supports the Open ID protocol. You can use Cognito AWS portal as a single sign-on point for all your services, including Creatio. To do this, perform he setup both in Cognito AWS and Creatio.
 



 In general, the following
 **steps** 
 are required to set up Single Sign-On in Creatio:
 


1. Sign up for
 [Cognito AWS](https://aws.amazon.com/cognito/) 
 .
2. Perform the setup in Cognito AWS.
 [Read more >>>](#title-2660-2)
3. Perform the setup in Creatio.
 [Read more >>>](#title-2660-3)



 Perform the setup in Cognito AWS
----------------------------------


1. Sign in to Aws.Amazon as root user.
2. Click
 
 App client list
 
 →
 
 Create app client
 
 .
3. Enter “Creatio” in the
 
 App client list
 
 field.
4. Click
 
 Client secret
 
 →
 
 Generate a client secret
 
 .
5. Enter
 
 [creatioURL]/ServiceModel/AuthService.svc/OpenIdCallback
 
 in
 
 Allowed callback URLs
 
 where [creatioURL] is the URL of your Creatio instance.
6. Enter
 
 [creatioUrl]/ServiceModel/AuthService.svc/OpenIdLogoutCallback
 
 in
 
 Allowed sign-out URLs
 
 where [creatioURL] is the URL of your Creatio instance.
7. Select
 
 Email
 
 ,
 
 OpenId
 
 ,
 
 Phone
 
 ,
 
 Profile
 
 in the
 
 OpenID Connect scopes
 
 block.
 




 Fig. 1
 
 OpenID Connect scopes
 
 block
 

![scr_chapter_single_sign_on_Cognito_step3_set_site.png](/docs/sites/en/files/images/Setup_and_Administration/Cognito_integration/scr_chapter_single_sign_on_Cognito_step3_set_site.png)
8. Click
 
 Create app client
 
 .
9. Save the following data from Cognito AWS console to your machine:
 


	1. **Client ID** 
	 . Consists of 26 letters and digits. To find this value open the
	 
	 App integration
	 
	 section →
	 
	 App client list
	 
	 .
	2. **Client secret** 
	 . Consists of 52 letters and digits. To find this value open the
	 
	 App integration
	 
	 section →
	 
	 App clients and analytics
	 
	 block → click the name of your application.
	3. **User pool ID** 
	 . View the value in the settings of a specific user pool.
	4. **Region** 
	 . Matches the “Region” parameter in the “User pool ID” value. For example,
	 
	 User pool ID = cognito-idp.us-east-1.amazonaws.com/us-east-1\_123456789
	 
	 , where us-east-1 is the required region. Learn more in
	 [Cognito documentation](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-integrating-user-pools-with-identity-pools.html) 
	 .



 Perform the setup in Creatio
------------------------------



 Follow these steps to configure single sign-on in Creatio:
 


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
	1. Enter the client ID retrieved from Cognito AWS in the
	 
	 Client ID
	 
	 parameter.
	2. Enter the client secret retrieved from Cognito AWS in the
	 
	 Client secret
	 
	 parameter.
	3. Enter your provider’s website in the
	 
	 URL
	 
	 parameter. The URL template is as follows
	 
	 https://[userPoolId].auth.[Region].amazoncognito.com
	 
	 . [Region] and [UserPoolId] are “Region” and “User pool ID” values retrieved from Cognito AWS console, respectively.
	4. Enter the URL of the identity provider’s single sign-on in the
	 
	 Discovery URL
	 
	 parameter. The URL template looks like
	 
	 https://cognito-idp.[region].amazonaws.com/[userPoolId]/.well-known/openid-configuration
	 
	 . [Region] and [UserPoolId] are “Region” and “User pool ID” values retrieved from Cognito AWS console, respectively.
	5. Enter the URL of the identity provider’s single sign-off in the
	 
	 End session endpoint
	 
	 parameter. The URL template is as follows
	 
	 https://[userPoolId].auth.[region].amazoncognito.com/logout?client\_id={client\_id}&logout\_uri={redirect\_uri}&state={state}
	 
	 . [Region] and [UserPoolId] are “Region” and “User pool ID” values retrieved from Cognito AWS console, respectively.
6. Fill out the provider name to display on the Creatio login page in the
 
 Display name
 
 field.
7. Save the changes.
8. Turn on Just-In-Time Provisioning (optional). This mechanism automatically creates the corresponding Creatio user account that contains data from the identity provider, such as user group, employee name, contact information, etc. To do this, select the
 
 Create and update users data when log in (Just-In-Time Provisioning)
 
 checkbox and map the fields.
 

 Fig. 2 Set up Just-In-Time Provisioning
 

![scr_set_up_JIT_cognito.png](/docs/sites/en/files/images/Setup_and_Administration/Cognito_integration/scr_set_up_JIT_cognito.png)




