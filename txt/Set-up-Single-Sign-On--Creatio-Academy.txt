


 The Single Sign-On technology in Creatio enables users to log in to multiple services using a single account. After a user signs in once via an identity provider, they can access their applications and services without the need to enter their login credentials. When a user signs out of any of the applications, sessions of all other connected applications end as well.
 



**Prerequisites** 
 :
 


1. A Creatio website available over HTTPS.
2. Administrator privileges on the website.
3. Administrator privileges in the identity provider.
4. Users in the corporate domain.



 In general, the following
 **steps** 
 are required to set up Single Sign-On:
 


1. Download the file that contains the integration metadata.
2. Set up the identity provider by adding Creatio to trusted websites.
3. Set up the trusted identity provider in Creatio.



 You can expedite the setup by using one of the following pre-configured providers:
 


* AD FS
* Azure AD
* Okta



 Also, you can integrate Creatio with any identity provider that supports the SAML 2.0 protocol.
 




