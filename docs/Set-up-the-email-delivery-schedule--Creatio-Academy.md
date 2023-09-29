


 Creatio lets you customize the email send time and delivery schedule. The values specified in the
 [email send time](/docs/8-0/user/marketing_tools/email_marketing/bulk_email/create_an_email/add_a_bulk_email#title-1551-1) 
 settings determine the time when Creatio passes the emails to the cloud service. The email delivery schedule determines when the cloud service passes emails to the email provider. This lets you schedule when the end recipients get the emails. This is useful for things like limited-time offers.
 



 You can set up the email delivery schedule before Creatio starts to send the email.
 



 Delivery schedule settings are identical for bulk emails and trigger emails.
 





 Note.
 
 These features are available since Creatio version 7.17.4. Toggle on the “BulkEmailThrottlingQueue” system setting to enable them in beta testing mode. Learn more:
 [Add, enable, and disable functions](/docs/7-18/developer/interface_elements/interface_control_tools/existing_feature/overview#title-1655-2) 
 .
 



 These features are available out-of-the-box in Creatio 7.18.0.
 




 To set up the delivery schedule:
 


1. Go to the
 
 Email
 
 section and open the needed record.
 



 Click the
 
 Parameters
 
 tab and go to the
 
 Delivery schedule
 
 detail. By default, the cloud service passes the emails to the email provider “Every day” from 12:00 AM to 11:59 PM. The recipients get the emails 24/7. You can specify other parameters:
 


	1. Select “Every day” or “Days of week” in the
	 
	 Delivery schedule
	 
	 field. If you select “Days of week,” a widget for selecting delivery days will appear. For example, you can select weekdays only (Fig. 1)
	2. Fill out the
	 
	 Delivery time range
	 
	 field to specify the email delivery period. If you do not specify the time frame or keep the default value, the email delivery will start as soon as the cloud service processes the emails. For example, if you start the email at 8:00 AM and set up the delivery time frame between 9:00 AM and 7:00 PM, none of the emails will be delivered before 9:00 AM. If you keep the default value (from 12:00 AM to 11:59 PM), the delivery will start at approximately 8:05 AM (the average email processing time is 5 minutes).
	3. Fill out the
	 
	 Time zone
	 
	 field to set the reference time zone for the delivery time range. The time zone of the user who created the email is used by default. You can change this value. For example, if you are in Los Angeles (GMT -08:00) and plan to send emails based on New York’s time zone (GMT -05:00), specify GMT -05:00, as displayed in Fig. 1.
	 
	
	
	
	
	 Fig. 1 Setting up the delivery time range
	 
	
	![email_additional_settings_delivery_time.png](/docs/sites/en/files/images/Marketing_Tools/email_additional_settings_delivery_time/email_additional_settings_delivery_time.png)
	
	
	 Hover over the icon to the right of the
	 
	 Time range
	 
	 field to check the time zone settings. The tooltip will display the delivery time frame based on the time zone of the current user (Fig. 2).
	 
	
	 Fig. 2 The delivery time frame based on the time zone of the current user
	 
	
	![email_additional_settings_delivery_time_hint.png](/docs/sites/en/files/images/Marketing_Tools/email_additional_settings_delivery_time/email_additional_settings_delivery_time_hint.png)



 As a result, the recipients will get the emails within the specified time frame according to their time zone.
 





 Attention.
 
 Creatio starts to send emails based on the user’s time zone. Time zone settings only apply to the
 
 Delivery time range
 
 field group and affect the time when the cloud service passes the emails to the recipients.
 





