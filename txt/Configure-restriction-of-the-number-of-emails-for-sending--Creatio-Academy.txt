


 Adjust the email restriction settings and your customers will not receive an excessive number of emails from your company. It helps to reduce spam complaints. For example, you can configure sending of no more than 2 emails per day and no more than 10 emails per month.
 



 Note that the configuration is based on the email category – you need to set up separate email sending restrictions for bulk and trigger emails. If you want to configure the same restrictions for all email types, create two identical rules of
 
 Bulk email
 
 and
 
 Trigger email
 
 categories (the
 
 Email category
 
 column).
 



 To set up:
 


1. Open the system designer by clicking the
 ![system_designer.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_emails_limit/system_designer.png)
 button.
2. Go to the
 
 System setup
 
 block → click
 **Lookups** 
 .
3. Open the
 **Email restriction rules** 
 lookup.
4. Click the
 **New** 
 button to create a rule.
   

 A new string appears in the editable list.
5. Specify the values of the new record in the new string (Fig. 1):
 


	1. **Name** 
	 – specify the name of the rule. For example, “10 emails per week”.
	2. **Time period, days** 
	 – specify the period (days) for the email restriction.
	3. **Maximum sending** 
	 – specify the maximum number of emails that can be sent to the contact during a specified time.
	4. **Email category** 
	 – specify the category that the restriction applies to: “Bulk email” or “Trigger email”.
	5. **Email type** 
	 – select the type of emails that the restriction applies to. This column displays values from the
	 
	 Email type
	 
	 lookup.
	 
	
	
	
	
	
	 Fig. 1
	 
	
	 Configure restriction of the number of emails for sending
	 
	
	![scr_section_email_lookup_bulk_emai_restriction_rules.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_emails_limit/scr_section_email_lookup_bulk_emai_restriction_rules.png)
6. Click the
 ![btn_com_apply.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_emails_limit/btn_com_apply.png)
 button to save the added record.
7. Repeat these steps for each new rule.
 



 You can create an unlimited number of rules. All rules added to the lookup are considered to be active.
 



 Creatio checks whether marketing communication has been reached for each recipient, whenever a new marketing email is sent. If at least one of the thresholds is reached for a recipient, the system will not send another email to this recipient and set "Communication limit" as their response.




