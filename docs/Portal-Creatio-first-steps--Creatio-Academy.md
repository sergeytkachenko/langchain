



 Creatio portal is available for both on-site and cloud deployment options. The portal is ready for use out of the box. We recommend having a look at what the portal functions have to offer.
 



 Log in to the portal
----------------------



 You need a portal user account to access the portal. Users can access the portal via an invitation email or sign up by themselves if you enable self-registration. If you need to create a single account, you can do it manually in the primary application:
 


1. Click
 ![btn_system_designer_2.png](/docs/sites/default/files/inline-images/btn_system_designer_2.png)
 → “System users.”
2. Click
 
 Add
 
 → “Portal user.”
3. Select a contact, fill out the
 
 Username
 
 and
 
 Password
 
 fields.
4. Save the changes.
 



 As a result, Creatio will create a new portal user, add them to the “All portal users” role and assign them a
 **portal license** 
 .
 





 Note.
 
 The name of the portal license consists of the portal configuration and the Creatio deployment method, e. g., “Creatio self-service portal cloud” or “Creatio Customer Portal on-site”.



 The main application and the portal have two different login pages. To
 **log in to the portal** 
 :
 


1. Log out of the primary application (Fig. 1).
 




 Fig. 1 Log out of the primary application
 

![scr_chapter_portal_setup_application_logout.png](/docs/sites/en/files/images/More_Apps/portal/portal_first_steps/scr_chapter_portal_setup_application_logout.png)
2. Add /login/SSPLogin.aspx to the URL inyou’re the address bar. Example of a link:
 **mysite.creatio.com/login/SSPLogin.aspx** 
 . As a result, you will be redirected to the portal home page.
3. Enter your login credentials and click
 
 Login
 
 .
   

 Study the portal functionality and move on to further setup.



 Portal customization overview
-------------------------------



 You can tailor the portal’s functionality to your company’s business goals.
 


1. **Set up sections** 
 available on the portal. You can add up to 3 custom sections on the portal. Note that you can only add custom sections in the “customer portal” configuration. Learn more:
 [Creatio portal overview](/docs/8-0/user/more_apps/portal/overview/portal_overview) 
 ,
 [Customize Portal Creatio](/docs/8-0/user/more_apps/portal/customize_portal/classic_ui_portal_setup/customize_portal_creatio#title-2088-26) 
 .
2. **Customize the portal** 
 . Personalize the portal to reflect your brand:
 


	* Upload your logo. The logo is displayed on the portal main page and the login page.
	* Add the customer support contact options to the portal login page.
	* Add charts and other analytics to the portal main page.
	 
	
	
	
	 Learn more:
	 [Customize the portal](/docs/8-0/user/more_apps/portal/customize_portal/classic_ui_portal_setup/customize_portal_creatio) 
	 .
3. **Set up roles and access permissions** 
 . You can group multiple portal users into portal organizations, and assign administrators for these organizations from among the portal users. Additionally, you can set up different access permissions for the data available on the portal for these organizations. Learn more:
 [Manage users and access permissions on the portal](/docs/7-18/user/more_apps/portal/manage_portal_in_the_main_application/manage_portal_in_main_application#title-2085-7) 
 .
 





 Note.
 
 Since Creatio version 8.0.9 “Portal user” user type and “All portal users” root role were renamed to “External user” and “All external users,” respectively.
4. **Set up user authentication** 
 . There are multiple ways to add new portal users to Creatio: manually, by importing from Excel, by synchronizing with LDAP, via SSO (Single-Sign-On), via an invitation email, via self-registration. Learn more:
 [Manage users and access permissions on the portal](/docs/7-18/user/more_apps/portal/manage_portal_in_the_main_application/manage_portal_in_main_application#title-2085-2) 
 .
5. **Create** 
**partner programs** 
 and display partner metrics in the “Partner portal” configuration. You can also process leads and opportunities in collaboration with your partners using lead and corporate sales management processes. Learn more:
 [Channel sales](https://academy.creatio.com/docs/user/sales_tools/channel_sales) 
 .




