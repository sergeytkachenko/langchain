


 Creatio sends automatic emails with various notifications regarding cases. Users receive emails when their cases are registered, processed, resolved, canceled, or closed.
 



 The general setup procedure is as follows:
 


* Set up contact case notification rules.
 [Read more >>>](#title-198-2)
* Set up email notification templates.
 [Read more >>>](#title-198-3)
* Set up case resolution notifications.
 [Read more >>>](#title-198-4)



 If the case was registered by email, all recipients of the original letter will receive notifications. By default the
 
 From
 
 field will contain email of support service that received customer’s email. If the case was registered from another channel (portal, call, etc.), then the
 
 From
 
 field will contain email of the support service specified in the
 
 Customer service Email
 
 system setting. To send notifications only to the case contact, even if they did not send the original email, enable the “Send automatic notifications only to contact” system setting (“AutoNotifyOnlyContact” code).
 



 The logic for sending email notifications is set up in the “Send email to contact on case status change” business process.
 





 Note.
 
 You also have to set up a mailbox for sending email notifications in Creatio version 7.12.2 and earlier. Read more in the Creatio 7.16 documentation.
 




 Set up contact case notification rules
----------------------------------------



 The setup procedure is as follows:
 


1. Open the system designer by clicking the
 ![btn_system_designer00001.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_automatic_emailing_setup/btn_system_designer00001.png)
 button.
2. Go to the
 
 System setup
 
 block → click
 
 Lookups
 
 .
3. In the
 
 Lookups
 
 section, open the
 **Case notification rule** 
 lookup content (Fig. 1).
 





 Fig. 1
 
 The
 
 Case notification rules
 
 lookup content page
 

![scr_section_service_requests_rules.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_automatic_emailing_setup/scr_section_service_requests_rules.png)
4. Click
 **New** 
 and set the notification parameters:
 


	1. Case category
	2. Case status
	3. Email message template
	4. Usage rule – choose whether the notification immediately or after a delay. To configure sending delay of the selected notification rule, specify the “Send after a delay” usage rule and populate the
	 
	 Sending delay, minutes
	 
	 column.
	5. Sending delay, minutes Select the
	 
	 Quote original email
	 
	 checkbox to include the text of the email that originated the case.
5. Save the changes by clicking the
 ![btn_com_apply.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_automatic_emailing_setup/btn_com_apply.png)
 button.



 Set up the email notification templates
-----------------------------------------



 The email template used for each notification depends on the case status and category. For example, the
 
 Case closure notification
 
 template is used to notify the user that the case has been closed.
 



 Use the
 [Email templates
 
 lookup](https://academy.creatio.com/documents?product=administration&ver=7&id=1451) 
 to manage the notification templates.
 



 To set up an email template:
 


1. Open the system designer by clicking the
 ![btn_system_designer00002.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_automatic_emailing_setup/btn_system_designer00002.png)
 button.
2. Go to the
 
 System setup
 
 block → click
 **Lookups** 
 .
3. Open the
 **Email templates** 
 lookup.
4. Select a template and click
 **Edit** 
 .
5. In the displayed
 [content designer](https://academy.creatio.com/documents?product=base&ver=7&id=2080) 
 window, edit the text of the email.
6. If required, add macros to the template, for example, the #Number# macro to specify the incident number in the message. To do this, click the
 ![btn_chapter_content_designer_macros.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_automatic_emailing_setup/btn_chapter_content_designer_macros.png)
 button and select the
 
 Standard macros
 
 action. If there is no required macro in the list of pre-installed macros, use the
 
 Custom macro
 
 action and set up the required macro.
 



 Contents of the
 
 Email templates
 
 lookup



 Creatio uses the following templates for sending service notifications to the customers:
 


* **“Case registration notification“** 
 – notifies the customer that the case has been registered in Creatio and is about to be processed.
* **“Case processing notification“** 
 – notifies the customer that the helpdesk team has started processing the case.
* **“Case resolution notification“** 
 – notifies the customer that the case has been resolved.
* **“Case closure notification“** 
 – notifies the customer that the case has been closed.
* **“Confirmation of closing request”** 
 – notifies the customer that the case has been closed when the customer did not reply to the question of the support operator.
* **“Case canceling notification“** 
 – notifies the customer that the case has been canceled. This may occur if a case was created by mistake.
* **“Case feedback request notification”** 
 – notifies the customer that the case has been resolved and awaits customer feedback and evaluation of the helpdesk performance.
* **“Case update: new message received”** 
 – notifies the customer that the case has been updated with a new message on the customer portal.
* **“Empty case email template** 
 – used for specialized case notifications.
* **“Template - Portal user registration”** 
 – sends an account activation link to the new customer portal user.
* **“Link for password recovery”** 
 – sends a link to password recovery page to the customer portal user.



 Creatio uses the following templates for sending
 **notifications to helpdesk agents** 
 :
 


* **“Specifying case assignee”** 
 and
 **“Case assigned to group”** 
 templates are used to send internal notifications to employees about being appointed assignees on cases.
* **“Creating new email for case”** 
 – notifies the assignee that the case has been updated with a new email message.



 Set up case resolution notification
-------------------------------------



 When a case is assigned the “Resolved“ status, the user will receive an email asking to evaluate the quality of processing. If no evaluation is received, an additional evaluation request will be sent. You can manage the response waiting time before sending additional evaluation request using the
 **Number of waiting days to reevaluate resolved case** 
 system setting.
 



 To ensure a proper quality evaluation emailing, set up the link of Creatio website that will be used for gathering user feedback. Populate the
 
 Default value
 
 field of the
 **Website URL** 
 system setting with the site URL used for Creatio access, for example http://creatio.com.
 




