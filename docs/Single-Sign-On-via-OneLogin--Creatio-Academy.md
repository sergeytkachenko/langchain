


 You can use OneLogin SSO portal as a single sign-on point for all your services, including Creatio. For this, you need to configure a number of settings both on the OneLogin and Creatio's end.
 





 Attention.
 
 In the setup example below, we use https://site01.creatio.com/ as Creatio site address and “appid” as application id in OneLogin. During the actual setup process, replace these values with your site address and the id of the corresponding application in OneLogin.
 




 Settings on OneLogin's end
----------------------------


1. Start the procedure by logging in to OneLogin using an administrator account.
2. Click
 
 Apps
 
 and select
 
 Add Apps
 
 . Enter “Creatio” in the search bar and select the Creatio application.
3. If needed, change the value in the
 
 Display name
 
 field, modify the application icons, or clear the
 
 Visible in portal
 
 checkbox. These settings affect the way the website is displayed on the OneLogin site.
4. Click
 
 Save
 
 .
5. Go to the
 
 Configuration
 
 tab and enter your website domain name in the
 
 Creatio site
 
 field (Fig. 1). For example, “site01.”
 





 Fig. 1
 
 The website configuration page
 

![scr_chapter_single_sign_on_onelogin_step3_set_site.png](/docs/sites/en/files/images/Setup_and_Administration/onelogin_integration/scr_chapter_single_sign_on_onelogin_step3_set_site.png)



 Settings on Creatio's end
---------------------------



 If you use
 **Creatio cloud** 
 , prepare the setup information according to the instructions below and contact
 [Creatio support](mailto: support@bpmonline.com) 
 to apply the settings.
 



 The single sign-on setup instructions below are intended for
 **on-site** 
 customers. We strongly recommend granting Creatio support temporary access to Creatio configuration or performing setup under the guidance of a Creatio support specialist.
 



 Follow these steps to set up single sign-on on Creatio's end:
 


1. Enter the SAML provider settings.
2. Set up the SSO authentication parameters.
3. Test the basic SSO scenarios.
4. Set up Just-In-Time User Provisioning (JIT).
5. Set SSO as the default option.



 To do this:
 


1. **Fill out the SAML provider settings** 
 by specifying the data of the SAML identification provider in the saml.config file.
	1. Specify your website's FQDN in the Name parameter.
	 
	
	
	
	
	
	 Attention.
	 
	 The value of the ServiceProvider Name parameter must be identical to the Identifier value specified on the ADFS identity provider's end. This is how it verifies that the SAML Assertion was issued specifically for your application. We recommend using the FQDN of your website. For example, https://site01.creatio.com/Demo\_161215/. The URL must match verbatim, including the “/” at the end.
	2. Specify the IdP settings in the Partner Identity Provider section. You can view these settings in the metadata file.
		* **WantAssertionSigned** 
		 – specify “false” if an encryption certificate will not be used during SAML Assertion data exchange.
		 
		
		
		
		```
		
		WantAssertionSigned="false"
		```
		* **SingleSignOnServiceUrl** 
		 – URL of the identity provider's single sign-on. You can retrieve it from the SAML 2.0 Endpoint (HTTP) on the trusted application page.
		 
		
		
		
		```
		
		SingleSignOnServiceUrl="https://ts-dev.onelogin.com/trust/saml2/http-post/sso/appid"
		```
		* **SingleLogoutServiceUrl** 
		 – URL of the identity provider's single sign-off. You can retrieve it from the SLO Endpoint (HTTP) on the trusted application page.
		 
		
		
		
		```
		
		SingleLogoutServiceUrl="https://ts-dev.onelogin.com/trust/saml2/http-redirect/slo/appid"
		```
2. **Enable the SSO provider in Creatio** 
 . To do this, modify the web.config file in the website root folder:
 


	1. Enable using the SSO Auth providers on login:
	 
	
	
		* **SsoAuthProvider** 
		 – identity provider for the main application.
		* **SSPSsoAuthProvider** 
		 – identity provider for the customer portal.
		 
		
		
		
		 You can enable one or both providers.
		 
		
		
		
		
		
		
		```
		
		<terrasoft>
		<auth providerNames="InternalUserPassword,SSPUserPassword,SsoAuthProvider,SSPSsoAuthProvider" autoLoginProviderNames="" defLanguage="en-US" defWorkspaceName="Default" useIPRestriction="false" loginTimeout="30000">
		<providers>
		```
	2. Specify which identification provider from the saml.config file to use in Service Provider initiated SSO scenarios by default. In the web.config App Loader, specify the PartnerIdP parameter value from the Issuer URL string in the saml.config file, such as:
	 
	
	
	
	
	
	
	```
	
	<appSettings> ... <add key="PartnerIdP" value="https://app.onelogin.com/saml/metadata/appid"/> ... </appSettings>
	```
	3. Set SSO as the default option upon login. To do this, specify the Login/NuiLogin.aspx?use\_sso=true resource in the web.config App Loader.
	 
	
	
	 Note.
	 
	 Users will still be able to log in with Creatio credentials via a direct link: https://site01.creatio.com/NuiLogin.aspx?. Use the following link to test the SSO before setting it as the default option: https://site01.creatio.com/NuiLogin.aspx?use\_sso=true.
	4. Enable redirection to the identity provider when going to the website root:
	 
	
	
	
	```
	
	<defaultDocument> <files> <add value="Login/NuiLogin.aspx?use_sso=true" /> </files> </defaultDocument>
	```
	5. Enable redirection to the identity provider if no user session is available:
	 
	
	
	
	```
	
	<authentication mode="Forms">
	<forms loginUrl="~/Login/NuiLogin.aspx?use_sso=true" protection="All" timeout="60" name=".ASPXAUTH" path="/" requireSSL="false" slidingExpiration="true" defaultUrl="ViewPage.aspx?Id=4e342d5e-bd89-4b79-98e2-22e433122403" cookieless="UseDeviceProfile" enableCrossAppRedirects="true" />
	</authentication>
	```
3. Test the
 **Identity Provider (IdP) initiated SSO basic scenario** 
 to make sure the settings are correct:
 


	1. Navigate to the trusted IdP applications page. The default link is https://sts.contoso.com/adfs/ls/idpinitiatedsignon.aspx.
	2. Authorize.
	3. Navigate to Creatio with the IdP authorization results.
	 
	
	
	
	 Test the settings in the IdP initiated scenario before setting SSO as the default option on Creatio's end. Make sure Creatio has an active user account whose login matches the NameId passed by the Identity Provider before starting the test. If there is no such account, the SSO setup process will not finish since it will be impossible to match the domain user to a Creatio user. After you successfully log in via SSO, proceed to further setup.
4. **Set up Just-In-Time User Provisioning (JIT)** 
 . The Just-In-Time User Provisioning functionality complements the single sign-on technology. It enables not only creating a user on the first login to Creatio but also updating the contact page data with the data received from the identification provider on every login. Learn more:
 [Just-In-Time User Provisioning](/docs/7-18/user/setup_and_administration/user_and_access_management/authentication/set_up_jit_provisioning/just-in-time_user_provisioning) 
 .
	1. Add the JIT settings to web.config file in the Creatio root folder:
	 
	
	
	
	```
	
	<add name="UseJit" value="true" />
	
	```
	
	
	
	
	
	 The user type is defined by the page they use to log in. If the
	 **Identity initiated** 
	 scenario is used to log in, specify the DefUserType value:
	 
	
	
		* General – general user.
		* SSP – portal user.
	2. Map the SAML Assertion fields to Creatio columns using the
	 
	 SAML field name converter to contact field name
	 
	 lookup. You need this to ensure Creatio populates the contact fields correctly when creating new users via Just-In-Time User Provisioning. If the field is empty or disabled in the identity provider data, you can fill it out with the value specified in the
	 
	 Default value
	 
	 field of the lookup. Upon the next login, Creatio will populate the contact fields specified in the lookup with either the values received from the provider or with the current default values.
	 
	
	
	
	
	
	 Note.
	 
	 If the lookup is missing from the lookup list, register it.
5. **Set SSO as the default option** 
 upon login. We recommend following this step only after you finished the previous steps successfully and made sure the SSO works correctly. This step will enable the Service Provider (SP) initiated SSO. The standard Service Provider (SP) initiated scenario is as follows:
 


	1. The user navigates to Creatio, they have no active sessions on the site.
	2. They are redirected to the IdP where they authorize.
	3. They are redirected back to Creatio with the IdP authorization results.
 To set the SSO provider as the default option:
 


	1. Enable Single Log Out in the web.config file in the Terrasoft.WebApp folder:
	 
	
	
	
	
	
	
	```
	
	<add key="UseSlo" value="true" />
	```
	2. Select the
	 
	 Default value
	 
	 checkbox in the “SSO in mobile application” (“MobileUseSSO”) system setting to use the Single Sign-On in the mobile application.




