


 OAuth is an open authentication standard for restricted access delegation. OAuth provides third parties with secure delegated access to protected user resources without saving user login and password in the application. Set up OAuth authentication for Microsoft 365 by registering your OAuth application.
 



 To do this:
 


1. Register your application using the administrator role in the Azure Active Directory identity and access management service (Azure AD). Learn more in the
 
[Microsoft documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app) 

 .
 





 Note.
 
 Specify redirection parameters in the
 
 Redirect URI
 
 field. Use this template:
   

 https://<your\_website>.creatio.com/0/rest/Office365OAuthAuthenticator/ProcessAuthenticationCode.
 




 Azure AD will assign a unique ID to the application after the registration is complete. The ID will display in the
 
 Application (client) ID
 
 field on the Overview page of the application. Creatio will request this parameter as the client secret key.
2. Add permissions to provide application access to users. Learn more about adding web-API permissions in the
 
[Microsoft documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis#add-permissions-to-access-web-apis) 

 .
 


	1. Select “Office 365 Exchange Online” in the list of supported APIs. Specify the “Delegated permissions” permission type and select the
	 
	 EWS.AccessAsUser.All
	 
	 checkbox.
	2. Select “Microsoft Graph” in the list of supported APIs. Specify the “Delegated permissions” permission type and select the
	 
	 User.Read
	 
	 checkbox.
3. Click the
 
 Grant admin consent for Tenant
 
 button to grant admin consent to the permissions configured for the application. Read more about the Admin consent button in the
 
[Microsoft documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis#understanding-api-permissions-and-admin-consent-ui) 

 .
4. Create a client secret for Creatio to use. Learn more in the
 
[Microsoft documentation](https://docs.microsoft.com/en-us/azure/storage/common/storage-auth-aad-app?tabs=dotnet#create-a-client-secret?) 

 .
5. Copy the key for later use by Creatio.
 



 As a result, you will get the values for the “Client ID” and “Client Secret” parameters required by Creatio to finish the integration. The Creatio application itself will be specified in the redirection parameters.




