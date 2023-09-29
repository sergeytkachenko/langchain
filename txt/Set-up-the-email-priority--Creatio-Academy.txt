


 You can specify the priority of an email record in Creatio. Use this feature to manage the mailing order. Creatio sends emails with higher priority sooner. For example, you can set up the priority so that Creatio sends confirmation emails before newsletters.
 



 You can set up the email priority before Creatio starts to send the email.
 



 Priority settings are identical for bulk emails and trigger emails.
 





 Note.
 
 These features are available since Creatio version 7.17.4. Toggle on the “BulkEmailThrottlingQueue” system setting to enable them in beta testing mode. Learn more:
 [Add, enable, and disable functions](/docs/7-18/developer/interface_elements/interface_control_tools/existing_feature/overview#title-1655-2) 
 .
 



 These features are available out-of-the-box in Creatio 7.18.0.
 




 To set up the email priority:
 


1. Go to the
 
 Email
 
 section and open the needed record.
 



 Select the required value in the
 
 Priority
 
 field on the
 
 Parameters
 
 tab (Fig. 1). The value is “Normal” by default.
 



 Click
 
 Save
 
 .
 




 Fig. 1 Setting up the bulk email priority
 

![email_additional_settings_priority.png](/docs/sites/en/files/images/Marketing_Tools/email_additional_settings_priority/email_additional_settings_priority.png)



 As a result, Creatio will use the value in the
 
 Priority
 
 field to calculate the sending order. Creatio sends the higher priority emails before lower priority emails.
 



 If the user sends multiple bulk emails with the same priority simultaneously, the email that reached the cloud email service sooner will be sent first.
 



 You can select one of the pre-configured priorities or
 **add custom priority values** 
 and use them in the future. To do so:
 


1. Open the system designer by clicking
 ![system_designer00001.png](https://academy.creatio.com/sites/default/files/documents/docs/product/bpm'online%20marketing/marketing/7.16.0/BPMonlineHelp/section_employees/system_designer00001.png)
 in the top right.
2. Click
 
 Lookups
 
 in the
 
 System setup
 
 block.
3. Open the
 
 Bulk email priorities
 
 lookup.
4. Click
 
 New
 
 .
5. Enter the priority name, for example, “Critical.” Fill out the
 
 Description
 
 column if necessary.
6. Specify the needed value in the
 
 Priority
 
 field. The lower the value, the higher the email priority (Fig. 2).
 




 Fig. 2 Adding a new value to the
 
 Bulk email priorities
 
 lookup
 

![email_additional_settings_priority_lookup.png](/docs/sites/en/files/images/Marketing_Tools/email_additional_settings_priority/email_additional_settings_priority_lookup.png)





 Attention.
 
 We recommend against changing or deleting the pre-configured values since this can affect the sending order of active bulk emails. Add a new lookup entry with a different priority value instead.




