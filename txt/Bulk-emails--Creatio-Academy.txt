


 The functionality is available in
 **Creatio marketing** 
 and CRM bundles.
 



 Set up your email service integration with Creatio for sending bulk emails. All cloud email service settings for bulk emails are consolidated on the bulk email setup page in the
 
 Email
 
 section. You can use it to edit general settings of sending bulk emails and receiving responses, sender domains as well as to monitor the connection status.
 



 Integration with Creatio cloud email service (for on-site users)
------------------------------------------------------------------



 To check integration with cloud email service:
 


1. Go to the
 
 Email
 
 section. Open the
 
 Actions
 
 menu and select
 **Bulk email settings** 
 (Fig. 1).
 




 Fig. 1 Open the bulk email settings page
 

![section_email_setup_page_access.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/bulk_emails/section_email_setup_page_access.png)
2. Fill out the
 
 General settings
 
 tab fields.
 





 Attention.
 
 Contact Creatio support to change your bulk email service provider.
 



	1. In the
	 **Domain to receive responses** 
	 field, specify the domain address of your Creatio application in the following format: http://www.yourdomain.com.
	 
	
	
	
	
	
	 Important.
	 
	 POST requests are always over port 443 regardless of the port on which Creatio is available. We recommend checking the connection to port 443 after you complete the setup. To do this, open the Creatio cloud services connection URL in the “https://url\_address.com” format in the browser.
	 
	
	
	
	 As a result, a blank page should open. If the page will not open, check whether the port is opened correctly.
	2. In the
	 **API key** 
	 field, specify your personal access key to the bulk email service.
	3. In the
	 **Creatio cloud services connection URL** 
	 field, specify the bulk email cloud service address in the “https://url\_address.com” format.
	4. In the
	 **Auth key** 
	 field, specify the authentication key for receiving responses.
	 
	
	
	
	 To obtain the API key and the Auth key, as well as the URL to bulk email cloud services after installing product licenses, please contact our support at support@creatio.com.
	5. Creatio will populate the
	 **Email provider** 
	 field with the name of your email service provider after you fill out the
	 
	 API key
	 
	 and
	 
	 Creatio cloud services connection URL
	 
	 fields.



 Sender domain list
--------------------



 For the sender name to be displayed correctly in the bulk email and to avoid unauthorized bulk email sent on your behalf, perform the following settings:
 


* Specify the list of your domains on the bulk email settings page.
* Verify each domain by using specific text SPF-, DKIM- and DMARK-records.
* Save the changes.





 Note.
 
 Only custom email domains can be verified. Public domains (for example, gmail.com, yahoo.com, etc.) cannot be verified. We do not recommend using public domains for bulk emails. Such emails have a high risk of being marked as spam and ruining the reputation of the sender IP address.
 




 To do this:
 


1. Add the list of your domains by clicking the
 ![btn_com_add_tab.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/bulk_emails/btn_com_add_tab.png)
 button on the
 
 Sender domains
 
 tab.
 





 Note.
 
 All added domains, including those that are no longer in use, are displayed in the list. Domains cannot be deleted from the list.
2. Select a domain from the list for verification. A DKIM/SPF setup manual for the selected domain will be displayed on the right side of the screen. The manual text will contain correct SPF and DKIM records generated for your domains.
 





 Note.
 
 DKIM/SPF manuals are different for each domain. To view a specific manual, select the required domain from the list.
3. Set up domain verification. Learn more:
 [Recommendations on setting up the popular DNS providers](/docs/7-16/user/setup_and_administration/email_domain_verification/recommendations_for_dns/recommendations_on_setting_up_the_popular_dns_providers) 
 .
 



 As a result, the bulk email settings
 
 Connection status
 
 field will display the
 ![chapter_setup_additional_connection__status_indicator.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/bulk_emails/chapter_setup_additional_%D1%81onnection__status_indicator.png)
 “Connection active” message.



 Additional settings for integration with bulk email service
-------------------------------------------------------------



**Set up one of the Creatio access options** 
 for Creatio Cloud Email Service for the correct operation of bulk email functions:
 


1. In the server firewall, permit receiving POST requests from the Internet to the domain where Creatio is deployed: http://www.yourdomain.com.
2. In the server firewall, permit receiving POST requests from a specific web service. For example, if the application is deployed on http://www.yourdomain.com, then the following address must be accessible: http://www.yourdomain.com/0/ServiceModel/CESWebhooksService.svc/HandleWebHooks.
 





 Note.
 
 There is no need to set up processing of unsubscribe requests and to check if the Creatio application server is able to receive GET-requests. Creatio will process unsubscribe queries automatically.
 






 Attention.
 
 If the HTTPS protocol is used to access Creatio, the application server must have an active certificate installed. In case the data transfer protocol or application address is changed, make the appropriate changes on the bulk email setup page.
 




 It is not recommended to use IP address whitelists to limit access to open ports because the Creatio Cloud Email Service may send analytical information about responses from different IP addresses. If the whitelist does not contain the IP address that the analytical information is sent from, the data will be lost.
 



 When using blacklists, we recommend checking that the received IP addresses are not on this list.



 Bulk email monitoring on-site
-------------------------------



 We recommend that you set up monitoring of your bulk email status by the support service before you start working with bulk emails. If you do this, Creatio support will be able to resolve any potential bulk email issues faster. Support service employees will have access to aggregated bulk email metrics that do not contain personalized email message texts, email templates, etc.
 





 Note.
 
 The procedure is different for Creatio cloud and on-site. Learn more about the setup procedure for Creatio cloud:
 [Permit monitoring the email status by Creatio support](/docs/7-16/user/marketing_tools/email_marketing/additional_setup/monitoring_for_creatio_support/permit_monitoring_email_status_by_creatio_support) 
 .
 




 The setup procedure is as follows:
 


1. Go to the system designer by clicking the
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/on_site_deployment/BPMonlineHelp/bulk_emails/btn_system_designer.png)
 button in the top right corner of the application window and click
 
 System settings
 
 .
2. Open the
 
 Enable monitoring of the email troubleshooting indicators
 
 system setting and select the
 
 Default value
 
 checkbox. Save the changes.
3. In the application server firewall, permit access from the Internet to the web service:
 



 /0/ServiceModel/CESTroubleshootingService.svc/emailstate.
 



 For example, if the application is deployed on http://www.yourdomain.com, then the following address must be accessible:
 



 http://www.yourdomain.com/0/ServiceModel/CESTroubleshootingService.svc/emailstate.
 



 As a result, the support service employees will be able to identify and eliminate potential bulk email issues.




