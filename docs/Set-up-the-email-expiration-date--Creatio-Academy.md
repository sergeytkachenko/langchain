


 Specify the date and time when Creatio will stop sending the email regardless of its completion state. This is important for time-sensitive offers or event invitations.
 



 You can set up the expiration date before Creatio starts to send the email.
 



 The expiration date settings are identical for bulk emails and trigger emails.
 





 Note.
 
 Toggle on the “BulkEmailThrottlingQueue” system setting to enable them in beta testing mode. Learn more:
 [Add, enable, and disable functions](/docs/7-18/developer/interface_elements/interface_control_tools/existing_feature/overview#title-1655-2) 
 . The “Bulk email expiration period (minutes)” (the “BulkEmailExpirationPeriod” code) was deprecated and retired. Follow the steps below to set up the email expiration date.
 




 To set up the expiration date:
 


1. Go to the
 
 Email
 
 section and open the needed record.
2. Specify when to stop sending the email in the
 
 Expiration date
 
 field on the
 
 Parameters
 
 tab (Fig. 1).
3. Click
 
 Save
 
 .
 

 Fig. 1 Setting up the expiration date
 

![email_additional_settings_expire.png](/docs/sites/en/files/images/Marketing_Tools/email_additional_settings_expire_time/email_additional_settings_expire.png)



 As a result, Creatio will stop sending the email on the date and time specified in the
 
 Expiration date
 
 field. Creatio will change the bulk email status to
 
 Expired
 
 . It will not be possible to resend the email to the remaining contacts. Creatio will mark the remaining contacts with “Stopped (time to send expired)”
 [personal response](/docs/7-18/user/marketing_tools/email_marketing/email_analytics/personal_responses_shortcut/personal_responses) 
 .
 



 If the campaign connected to trigger emails remains active, Creatio will keep adding participants to the audience. These participants will be marked with “Stopped (time to send expired)” personal response. You can use this to set up further conditional flows. For example, send another email to all contacts with “Stopped (time to send expired)” personal response.
 






 Note.
 
 If a campaign
 **trigger email** 
 expired but the campaign is still ongoing, the responses of new campaign participants will also be set to “Stopped (time to send expired).” In such cases, we recommend to
 [set up the campaign diagram](/docs/7-17/user/marketing_tools/marketing_campaings/campaign_diagram/set_up_campaign_diagram) 
 so that the
 [Email
 
 element](/docs/8-0/user/marketing_tools/marketing_campaings/campaign_elements/campaign_element_reference#title-347-8) 
 has a separate outgoing flow for participants with the “Stopped (time to send expired)” personal response
 





 If you leave the
 
 Expiration date
 
 field empty, Creatio will not stop sending the email.
 




