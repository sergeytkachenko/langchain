


 You can set up automatic lead registration in Creatio when a customer fills in a form on Facebook or Instagram.
   

 The setting is available for users with a preconfigured Facebook Ads Manager account.
 



 Before you start setting up lead generation from social networks, make sure that the values of the following Creatio
 [system settings](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/manage_system_settings_shortcut/manage_system_settings) 
 are populated:
 


* “Identity server Url” (“IdentityServerUrl” code)
* “Identity server client id” (“IdentityServerClientId” code)
* “Identity server client secret” (“IdentityServerClientSecret” code)



 If the values of these settings are empty, contact Creatio support.
 





 Attention.
 
 If you use Safari, make sure to allow pop-up windows for your Creatio instance.
 




 To set up lead registration from social networks:
 


1. **Open** 
 the
 
 Landing pages and web forms
 
 section.
2. **Click** 

 New
 
 →
 
 Lead registration form
 
 .
3. **Populate** 
 the fields on the opened page:
	1. Name
	 
	 – the record title that will display in the section list and the connected records;
	2. Website domains
	 
	 – facebook.com.
4. **Save** 
 the record.
5. Open the created record and
 **activate** 
 the
 
 Facebook Lead Generation
 
 switcher.
 

 Enabling Facebook lead generation
 

![turn_on_leadgeneration_enu.png](/docs/sites/en/files/images/CRM_Tools/facebook_lead_generation/turn_on_leadgeneration_enu.png)
6. **Click** 
 the
 
 Creatio URL setting
 
 link.
7. **Specify** 
 your application URL in the
 
 Creatio URL
 
 field and click
 
 Next
 
 .
 

 Specifying Creatio URL
 

![fill_in_creatio_url_enu.png](/docs/sites/en/files/images/CRM_Tools/facebook_lead_generation/fill_in_creatio_url_enu.png)
8. Click
 
 Select a source
 
 .
9. If synchronization with social networks is
 **already configured** 
 in Creatio, proceed with step 10 of the current guide.
   

 If you are setting up lead registration from social networks
 **for the first time** 
 and Creatio is not synchronized with any Facebook account yet, click
 
 Manage pages
 
 .
	1. **Log in** 
	 to Facebook. To ensure the correct setup, log in to your user account with administrator permissions to your Facebook public page and the “Ads manager” role.
	 
	
	
	 Attention.
	 
	 After you set up the integration, do not degrade the administrator user permissions. This may cause issues with the functionality operation.
	2. **Select** 
	 one or several pages for setting up synchronization with Creatio. Click
	 
	 Next
	 
	 .
	 
	
	 Selecting a Facebook page to synchronize with Creatio
	 
	
	![synchronize_creatio_with_facebook_page_enu.png](/docs/sites/en/files/images/CRM_Tools/facebook_lead_generation/synchronize_creatio_with_facebook_page_enu.png)
	3. Permit Creatio to
	 **manage your public page** 
	 . This will enable passing the data from social networks to Creatio. If you restrict Creatio from managing the page, lead registration may not work properly.
	 
	
	 Setting up access to managing the page
	 
	
	![setup_facebook_access_rights_enu.png](/docs/sites/en/files/images/CRM_Tools/facebook_lead_generation/setup_facebook_access_rights_enu.png)
10. On the page of selecting a form, specify:
	1. The
	 **Facebook page** 
	 with a configured campaign;
	2. **Lead registration form** 
	 that has been created for this page in Ads Manager.
11. Click
 
 Save
 
 .
 

 Selecting a Facebook page and form to synchronize with Creatio
 

![select_facebook_page_and_form_enu.png](/docs/sites/en/files/images/CRM_Tools/facebook_lead_generation/select_facebook_page_and_form_enu.png)
12. Close the setup window and return to the
 **landing page in Creatio** 
 .
13. Refresh the page. As a result, the
 
 Facebook Lead Generation
 
 block will be populated with data from the synchronized Facebook page.
14. **Save** 
 the landing record.
   

 As a result, after the campaign is triggered in Facebook and Instagram, the ad record available for users will be connected to the form. Each time a form is submitted, a new lead will be added in Creatio.
 

 Displaying an ad record with a lead registration form in the Facebook feed
 

![facebook_web_form_enu.png](/docs/sites/en/files/images/CRM_Tools/facebook_lead_generation/facebook_web_form_enu.png)



 The following values can be passed to the leads added via social networks: email, phone number, address, city, region, country, postal code, full name, position, work phone, work email, account name. If you add other fields to the Facebook form, their values will be stored in the
 
 Notes
 
 detail. You can only pass text field values to Creatio due to restrictions on the Facebook side.
 





 Note.
 
 If you change the default captions of the Facebook Ads Manager fields in the form, the field values may not be passed to Creatio properly.
 





