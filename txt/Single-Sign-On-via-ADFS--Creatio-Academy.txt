


 You can integrate your Active Directory Federation Services (ADFS) instance to help manage seamless single sign-on for your members. For this, you need to configure a number of settings both in ADFS and Creatio.
 





 Attention.
 
 In the setup example below, https://site01.creatio.com/Demo\_161215/ is the Creatio website and http://adfs01.mysite.com/adfs/ is the ADFS site. Replace these addresses with the corresponding addresses of your sites when you perform the actual setup.
 




 Settings in ADFS
------------------


1. Add a new Relying Party Trust to ADFS (Fig. 1).
 




 Fig. 1 The Relying Party Trust menu
 

![scr_chapter_single_sign_on_adfs_step1_add_party.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step1_add_party.png)
2. Select the “Enter data about the relying party manually” option, as shown on the Fig. 2.
 




 Fig. 2 The “Enter data about the relying party manually” option
 

![scr_chapter_single_sign_on_adfs_step2_enter_data_manually.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step2_enter_data_manually.png)
3. Enter the name of the Relying Party in the
 
 Display name
 
 field. This name is needed to make it easier to navigate the list of trusted applications in ADFS and does not affect the actual setup.
4. Keep the default ADFS profile. Click the
 
 Next
 
 button.
5. Click
 
 Next
 
 on the “Configure Certificate” step.
6. Enable SAML 2.0 protocol support. Specify the site address and add “/ServiceModel/AuthService.svc/SsoLogin” to it (Fig. 3).
 




 Fig. 3 The SAML 2.0 protocol support option
 

![scr_chapter_single_sign_on_adfs_step6_enable_saml.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step6_enable_saml.png)
7. Specify the full site address in the identifier settings and click the
 
 Add
 
 button, as shown on the Fig. 4.
 




 Fig. 4 The identifier
 

![scr_chapter_single_sign_on_adfs_step7_set_identifier.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step7_set_identifier.png)





 Attention.
 
 The identifier is used when verifying the authenticity of a source that requests authentication. The URL must match verbatim, including the “/” at the end.
8. Set up the rest of the parameters according to your security requirements. You can leave default values for test purposes.
9. Click
 
 Finish
 
 . Click
 
 Add Rule
 
 and add a new SAML Assertion to SAML Response rule (Fig. 5) in the newly-opened window.
 




 Fig. 5 The “Add rule” button
 


![scr_chapter_single_sign_on_adfs_step9_add_rule.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step9_add_rule.png)




 Note.
 
 Creatio will use the data generated according to the new rule to search for users, as well as to update their profiles and roles.
10. Keep the default settings and click
 
 Next
 
 on the first step of the Rule Wizard. Set up a set of parameters that will be received from the user’s data (Fig. 6). In this example, the user’s name and a list of domain groups will be passed via SAML Assertion.
 




 Fig. 6 The rule parameters
 

![scr_chapter_single_sign_on_adfs_step10_rule_parameters.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step10_rule_parameters.png)
11. Click the
 
 Save
 
 button.
12. Open the Trusted Relay settings, go to the
 
 Advanced
 
 tab, and specify SHA-1 encryption according to the website certificate algorithm.
13. Add the public certificate key on the
 
 Encryption
 
 tab to set up the SAML encryption (Fig. 7).
 





 Note.
 
 If you are using Creatio cloud, get the public certificate key from the Creatio support service.
 





 Fig. 7 The
 
 Encryption
 
 tab
 

![scr_chapter_single_sign_on_adfs_step13_add_public_key.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step13_add_public_key.png)
14. Add the logout endpoint and set the following parameters (Fig. 8) on the
 
 Endpoints
 
 tab:
 


	* **Endpoint type** 
	 : SAML Logout.
	* **Binding** 
	 : Redirect.
	* **Trusted URL** 
	 : https://site01.creatio.com/Demo\_161215/ServiceModel/AuthService.svc/SsoLogout
	 
	
	
	
	
	 Fig. 8 The Endpoint parameters
	 
	
	![scr_chapter_single_sign_on_adfs_step13_add_endpoint.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step13_add_endpoint.png)
15. Add the Logout Request certificate on the
 
 Signature
 
 tab, as specified on the Fig. 9.
 




 Fig. 9 The Logout Request certificate
 

![scr_chapter_single_sign_on_adfs_step14_add_certificate.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_step14_add_certificate.png)





 Attention.
 
 Single Sign-Out does not work without a certificate.
 




 Settings in Creatio
---------------------



 If you use
 **Creatio cloud** 
 , prepare the setup information according to the instructions below and contact
 [Creatio support](mailto:%20support@bpmonline.com) 
 to apply the settings.
 



 The single sign-on setup instructions below are intended for
 **Creatio on-site** 
 customers. We strongly recommend granting Creatio support temporary access to Creatio configuration or performing setup under the guidance of a Creatio support specialist.
 



 Follow these steps to set up single sign-on in Creatio:
 


1. Enter the SAML provider settings.
2. Set up the SSO authentication parameters.
3. Test the basic SSO scenarios.
4. Set up Just-In-Time User Provisioning (JIT).
5. Set SSO as the default option.



 Certain settings are different for Creatio .NET Framework and Creatio .NET Core. This guide provides instructions for both platforms.
 



### 
 .NET Framework



1. **Fill out the SAML provider settings** 
 by specifying the data of the SAML identification provider in the
 **saml.config** 
 file.
	1. Specify your website’s FQDN in the Name parameter.
	 
	
	
	
	
	
	 Attention.
	 
	 The value of the ServiceProvider Name parameter must be identical to the Identifier value specified in the ADFS identity provider. This is how it verifies that the SAML Assertion was issued specifically for your application. We recommend using the FQDN of your website. For example, https://site01.creatio.com/Demo\_161215/. The URL must match verbatim, including the “/” at the end.
	2. Specify the IdP settings in the Partner Identity Provider section. You can view these settings in the metadata file.
		* **WantAssertionSigned="false"** 
		 : if no encryption certificate will be used for SAML Assertion.
		* **SingleSignOnServiceUrl** 
		 : URL of the identity provider’s single sign-on. For ADFS, this is usually https://adfs01.mysite.com/adfs/ls.
		* **SingleLogoutServiceUrl** 
		 : URL of the identity provider’s single sign-off. For ADFS, this is usually https://adfs01.mysite.com/adfs/ls.
		* **PartnerCertificateFile** 
		 : path to the \*.cer security certificate in the server file system relative to the Creatio application root. Specify this parameter if WantAssertionSigned="true."
		* **SignLogoutRequest="true"** 
		 : specify for ADFS, since the LogoutRequest must be signed. If set to “true,” specify the certificate for signature generation in the LocalCertificateFile parameter.
		* **SignLogoutResponse="true"** 
		 : specify for ADFS, since the LogoutResponse must be signed. If set to “true,” specify the certificate for signature generation in the LocalCertificateFile parameter.
		* **OverridePendingAuthnRequest="true"** 
		 : if enabled, Creatio does not check whether the IdP response matches the earlier Auth Request.
		 
		**Example of the saml.config file for ADFS:** 
		
		
		
		
		
		
		
		```
		
		    <ServiceProvider Name="https://site01.creatio.com/Demo_161215/"
		             
		                Description="Example Creatio Service Provider"
		                AssertionConsumerServiceUrl="~/ServiceModel/AuthService.svc/SsoLogin"
		                LocalCertificateFile="sp.pfx"
		                LocalCertificatePassword="password"
		            />
		    <PartnerIdentityProviders>
		         
		<!-- ADFS Creatio -->
		        <PartnerIdentityProvider Name="http://adfs01.mysite.com/adfs/services/trust"
		                            OverridePendingAuthnRequest="true"
		                                 Description="MVC Example Identity Provider"
		                                 SignAuthnRequest="false"
		                                 SignLogoutRequest="true"
		                                 SignLogoutResponse="true"
		                                 WantSAMLResponseSigned="false"
		                                 WantAssertionSigned="false"
		                                 WantAssertionEncrypted="false"
		                                 SingleSignOnServiceUrl="https://adfs01.mysite.com/adfs/ls"
		                                 SingleLogoutServiceUrl="https://adfs01.mysite.com/adfs/ls"
		                                 PartnerCertificateFile="Certificates\idp.cer"/>
		
		
		```
	 If you enable the SignLogoutRequest or SignLogoutResponse flags, add the \*.pfx private encryption certificate key to the same file system as your Creatio application. Specify the file path and the password in the saml.config configuration files and make sure that the user who runs the application has permission to read the file. Make sure that the certificate file is available in the Terrasoft.WebApp directory and the website root directory.
	 
	
	
	
	
	
	
	```
	
	LocalCertificateFile="sp.pfx"
	LocalCertificatePassword="password"
	
	```
	
	
	
	
	
	
	 Fig. 10 The SAML packet encryption settings
	 
	
	![scr_chapter_single_sign_on_adfs_add_private_key.png](/docs/sites/en/files/images/Setup_and_Administration/adfs_integration/scr_chapter_single_sign_on_adfs_add_private_key.png)
2. **Enable the SSO provider in Creatio** 
 . Enable the SAML SSO in Creatio after specifying the SAML provider settings. Modify the
 **web.config** 
 file in the website root directory:
	1. Enable using the SSO Auth providers on login:
		* **SsoAuthProvider** 
		 for the main application.
		* **SSPSsoAuthProvider** 
		 for the customer portal.
		 
		 You can enable one or both of the providers.
		 
		
		
		
		
		
		
		```
		
		<terrasoft> <authproviderNames="InternalUserPassword,SSPUserPassword,SsoAuthProvider,SSPSsoAuthProvider" autoLoginProviderNames="" defLanguage="en-US" defWorkspaceName="Default" useIPRestriction="false" loginTimeout="30000"> <providers>
		
		```
	2. Specify which identification provider from the saml.config file to use in Service Provider initiated SSO scenarios by default. In the web.config App Loader, specify the PartnerIdP parameter value from the Issuer URL string in the saml.config file, such as:
	 
	
	
	
	
	
	
	```
	
	<appSettings>  
	
	... 
	
	<add key="PartnerIdP" value="http://adfs01.mysite.com/adfs/services/trust"/>  
	
	...  
	
	</appSettings>
	
	```
3. Test the
 **Identity Provider (IdP) initiated SSO basic scenario** 
 to make sure the settings are correct:
 


	* Go to the trusted IdP applications page. The default link is https://sts.contoso.com/adfs/ls/idpinitiatedsignon.aspx.
	* Authorize.
	* Go to Creatio with the IdP authorization results.
	 
	
	
	
	 Test the settings in the IdP initiated scenario before setting SSO as the default option in Creatio. Make sure Creatio has an active user account whose login matches the NameId passed by the Identity Provider before starting the test. If such account does not exist, the SSO setup process will not finish since it will be impossible to match the domain user to a Creatio user. After you successfully log in via SSO, proceed to further setup.
4. **Set up Just-In-Time User Provisioning (JIT)** 
 . The Just-In-Time User Provisioning functionality complements the single sign-on technology. It enables not only creating a user on the first login to Creatio, but also updating the contact page data with the data received from the identification provider on every login. Learn more in a separate article:
 [Just-In-Time User Provisioning](https://academy.creatio.com/documents?id=1759) 
 .
	1. Add the JIT settings to the web.config file in the Creatio root directory.
	 
	
	
	
	```
	
	<add name="UseJit" value="true" />
	
	```
	
	
	
	
	
	 The user type is defined by the page that they use to log in. If the “Identity initiated” scenario is used to log in, specify the DefUserType value:
	 
	
	
		* **General** 
		 for general users.
		* **SSP** 
		 for portal users.
	2. Map the SAML Assertion fields to Creatio columns using the
	 
	 SAML field name converter to contact field name
	 
	 lookup. You need this to ensure Creatio populates the contact fields correctly when creating new users via Just-In-Time User Provisioning. If the field is empty or disabled in the identity provider data, you can fill it out with the value specified in the
	 
	 Default value
	 
	 field of the lookup. Upon the next login, Creatio will populate the contact fields specified in the lookup with either the values received from the provider or with the current default values.
	 
	
	
	 Note.
	 
	 If the lookup is missing from the lookup list, register it.
5. **Set SSO as the default option** 
 upon login. We recommend following this step only after you finished the previous steps successfully and made sure the SSO works correctly. This step enables the Service Provider (SP) initiated SSO.
 



 The standard Service Provider (SP) initiated scenario is as follows:
 


	* The user goes to Creatio, they have no active sessions on the site.
	* They are redirected to the IdP where they authorize.
	* They are redirected back to Creatio with the IdP authorization results.
 To set the SSO provider as the default option:
 


	1. Specify the NuiLogin.aspx?use\_sso=true default resource in the root web.config file.
	 
	
	
	 Note.
	 
	 Users will still be able to log in with Creatio credentials via a direct link: https://site01.creatio.com/Login/NuiLogin.aspx?
	 
	
	
	
	 Use the following link to test the SSO operation before it is enabled by default: https://site01.creatio.com/NuiLogin.aspx?use\_sso=true\
	2. Enable redirection to the identity provider when going to the website root in the root web.config file:
	 
	
	
	
	```
	
	<defaultDocument> <files> <add value="Login/NuiLogin.aspx?use_sso=true" /> </files> </defaultDocument> 
	
	<authentication mode="Forms">
	        <forms loginUrl="~/Login/NuiLogin.aspx?use_sso=true ...
	</authentication>
	```
	3. Enable Single Log Out in the web.config file in the Terrasoft.WebApp directory:
	 
	
	
	
	```
	
	<add key="UseSlo" value="true" />
	```
	4. Specify where to redirect the user when the active session expires in the web.config file in the Terrasoft.WebApp directory
	 
	
	
	
	```
	
	<authentication mode="Forms">
	        <forms loginUrl="~/../Login/NuiLogin.aspx?use_sso=true...
	</authentication>
	```
	5. Select the
	 
	 Default value
	 
	 checkbox in the “Use SSO in the mobile app” (“MobileUseSSO” code) system setting to use the Single Sign-On in the mobile application.





### 
 .Net Core



1. **Fill out the SAML provider settings** 
 by specifying the data of the SAML identification provider in the
 **saml.json** 
 file.
	1. Specify your website’s FQDN in the Name parameter.
	 
	
	
	
	
	
	 Attention.
	 
	 The value of the ServiceProvider Name parameter must be identical to the Identifier value specified in the ADFS identity provider. This is how it verifies that the SAML Assertion was issued specifically for your application. We recommend using the FQDN of your website. For example, https://site01.creatio.com/Demo\_161215/. The URL must match verbatim, including the “/” at the end.
	2. Specify the IdP settings in the Partner Identity Provider section. You can view these settings in the metadata file.
		* **WantAssertionSigned** 
		 : specify “false” if no encryption certificate will be used for SAML Assertion.
		 
		
		
		
		```
		
		"WantLogoutRequestSigned":false
		```
		* **SingleSignOnServiceUrl** 
		 : URL of the identity provider’s single sign-on. For ADFS, this is usually https://adfs01.mysite.com/adfs/ls.
		 
		
		
		
		```
		
		"SingleSignOnServiceUrl":"https://adfs01.mysite.com/adfs/ls"
		```
		* **SingleLogoutServiceUrl** 
		 : URL of the identity provider’s single sign-off. For ADFS, this is usually https://adfs01.mysite.com/adfs/ls.
		 
		
		
		
		```
		
		"SingleLogoutServiceUrl":"https://adfs01.mysite.com/adfs/ls"
		```
		* **PartnerCertificateFile** 
		 : path to the \*.cer security certificate in the server file system relative to the Creatio application root. Specify this parameter if WantAssertionSigned="true."
		 
		
		
		
		```
		
		"PartnerCertificates":[
		   {
		      "FileName":"adfs_sandbox.cer"
		   }
		
		```
		* **SignLogoutRequest** 
		 : specify “true” for ADFS since the LogoutRequest must be signed. If set to “true,” specify the certificate for signature generation in the LocalCertificateFile parameter.
		 
		
		
		
		```
		
		"SignLogoutRequest":true
		```
		* **SignLogoutResponse** 
		 : specify “true” for ADFS since the LogoutResponse must be signed. If set to “true,” specify the certificate for signature generation in the LocalCertificateFile parameter.
		 
		
		
		
		```
		
		"SignLogoutResponse":true
		```
2. If you enable the SignLogoutRequest or SignLogoutResponse flags, add the \*.pfx private encryption certificate key to the same file system as your Creatio application. Specify the file path and the password in the saml.json configuration file and make sure that the user who runs the application has permission to read the file. Make sure that the certificate file is available in the Terrasoft.WebApp directory and the website root directory.
 



```

"...""LocalCertificates":[
   {
"FileName":"sp.pfx",
"Password":"password"}
]"..."
```
3. **Enable the SSO provider in Creatio** 
 . Enable the SAML SSO in Creatio after specifying the SAML provider settings. To do this, edit the
 **Terrasoft.WebHost.dll.config** 
 file in the website root directory:
	1. Enable using the SSO Auth providers on login:
		* **SsoAuthProvider** 
		 for the main application.
		* **SSPSsoAuthProvider** 
		 for the customer portal.
		 
		 You can enable one or both of the providers.
		 
		
		
		
		
		
		
		```
		
		"...
		
		<auth providerNames=""LdapProvider,InternalUserPassword,SSPUserPassword,SsoAuthProvider,SSPSsoAuthProvider""autoLoginProviderNames=""""defLanguage=""en-US""defWorkspaceName=""Default""useIPRestriction=""false""loginTimeout=""30000"">
		
		..."
		```
	2. Specify which identification provider from the saml.json file to use in Service Provider initiated SSO scenarios by default. In
	 **Terrasoft.WebHost.dll.config** 
	 , specify the PartnerIdP parameter value from the Issuer URL string in the saml.json file, such as:
	 
	
	
	
	
	
	
	```
	
	"...""PartnerName":"http://adfs.sandbox.local/adfs/services/trust",
	"..."
	```
4. Test the
 **Identity Provider (IdP) initiated SSO basic scenario** 
 to make sure the settings are correct:
 


	* Go to the trusted IdP applications page. The default link is https://sts.contoso.com/adfs/ls/idpinitiatedsignon.aspx.
	* Authorize.
	* Go to Creatio with the IdP authorization results.
	 
	
	
	
	 Test the settings in the IdP initiated scenario before setting SSO as the default option in Creatio. Make sure Creatio has an active user account whose login matches the NameId passed by the Identity Provider before starting the test. If such account does not exist, the SSO setup process will not finish since it will be impossible to match the domain user to a Creatio user. After you successfully log in via SSO, proceed to further setup.
5. **Set up Just-In-Time User Provisioning (JIT)** 
 . The Just-In-Time User Provisioning functionality complements the single sign-on technology. It enables not only creating a user on the first login to Creatio, but also updating the contact page data with the data received from the identification provider on every login. Learn more in a separate article:
 [Just-In-Time User Provisioning](https://academy.creatio.com/documents?id=1759) 
 .
	1. Add the JIT settings to the
	 **Terrasoft.WebHost.dll.config** 
	 file in the Creatio root directory. Enable JIT for general users in the SsoAuthProvider settings and for portal users in the SSPSsoAuthProvider settings:
	 
	
	
	
	 ...
	 
	
	
	
	 <provider name="
	 **SsoAuthProvider** 
	 " type="Terrasoft.Authentication.Core.SSO.BaseSsoAuthProvider, Terrasoft.Authentication">
	   
	
	 <parameters>
	   
	
	 <add name="UserType" value="General" />
	   
	
	 <add name="
	 **UseJit** 
	 " value="
	 **true** 
	 " />
	   
	
	 </parameters>
	   
	
	 </provider>
	   
	
	 <provider name="
	 **SSPSsoAuthProvider** 
	 " type="Terrasoft.Authentication.Core.SSO.BaseSsoAuthProvider, Terrasoft.Authentication">
	   
	
	 <parameters>
	   
	
	 <add name="UserType" value="SSP" />
	   
	
	 <add name="
	 **UseJit** 
	 " value="
	 **true** 
	 " />
	   
	
	 </parameters>
	 
	
	
	
	 ...
	 
	
	
	
	
	
	
	 The user type is defined by the page they use to log in. If the “Identity initiated” scenario is used to log in, specify the DefUserType value:
	 
	
	
		* **General** 
		 for general users.
		* **SSP** 
		 for portal users.
	2. Map the SAML Assertion fields to Creatio columns using the
	 
	 SAML field name converter to contact field name
	 
	 lookup. You need this to ensure Creatio populates the contact fields correctly when creating new users via Just-In-Time User Provisioning. If the field is empty or disabled in the identity provider data, you can fill it out with the value specified in the
	 
	 Default value
	 
	 field of the lookup. Upon the next login, Creatio will populate the contact fields specified in the lookup with either the values received from the provider or with the current default values.
	 
	
	
	 Note.
	 
	 If the lookup is missing in the lookup list, it needs to be registered.
6. **Set SSO as the default option** 
 upon login. We recommend following this step only after you finished the previous steps successfully and made sure the SSO works correctly. This step will enable the Service Provider (SP) initiated SSO.
 



 The standard Service Provider (SP) initiated scenario is as follows:
 


	* The user goes to Creatio, they have no active sessions on the site.
	* They are redirected to the IdP where they authorize.
	* They are redirected back to Creatio with the IdP authorization results.
 To set the SSO provider as the default option:
 


	1. Specify UseSsoByDefault": "true" in the saml.json file.
	 
	
	
	 Note.
	 
	 Users will still be able to log in with Creatio credentials via a direct link: https://site01.creatio.com/Login/NuiLogin.aspx?
	 
	
	
	
	 Use the following link to test the SSO operation before it is enabled by default: https://site01.creatio.com/NuiLogin.aspx?use\_sso=true\
	2. Enable redirection to the identity provider when going to the website root in the
	 **Terrasoft.WebHost.dll.config** 
	 file:
	 
	
	
	
	```
	
	<defaultDocument> <files> <add value="Login/NuiLogin.aspx?use_sso=true" /> </files> </defaultDocument> 
	
		<authentication mode="Forms">
	        <forms loginUrl="~/Login/NuiLogin.aspx?use_sso=true ...
		</authentication>
	```
	3. Enable Single Log Out in
	 **Terrasoft.WebHost.dll.config** 
	 :
	 
	
	
	
	```
	
	<add key="UseSlo" value="true" />
	```
	4. Specify where to redirect the user the active session expires in the
	 **Terrasoft.WebHost.dll.config** 
	 file:
	 
	
	
	
	```
	
	<authentication mode="Forms">
		<forms loginUrl="~/../Login/NuiLogin.aspx?use_sso=true...
	</authentication>
	```
	5. Select the
	 
	 Default value
	 
	 checkbox in the “Use SSO in the mobile app” (“MobileUseSSO” code) system setting to use the Single Sign-On in the mobile application.






