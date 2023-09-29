


 Creatio uses the “Customer SATisfaction” (CSAT) scale, for grading the quality of service by the case customers. You can set up automatic email notifications, asking a case customer to evaluate the quality of service after the case has been resolved. Creatio can automatically reopen or close cases, based on the customer feedback. If the customer does not provide feedback within a set time frame, a reminder email notification will be sent.
 



 General procedure for setting up case feedback evaluation
-----------------------------------------------------------


1. Issue the “self-service portal creatio on-site/cloud”
 **Portal license** 
 to the SysPortalConnection user.
 [Read more >>>](https://academy.creatio.com/documents?id=1472)
2. Configure the satisfaction scale and specify the rules for closing or reopening cases depending on the actual evaluation score in the
 **Satisfaction levels** 
 lookup.
 [Read more >>>](#title-202-2) 






 Note.
 
 If a case is reopened as a result of a low score point, its
 
 Assignee
 
 field will be cleared automatically and the case will be queued for processing. To disable clearing of the
 
 Assignee
 
 field, clear the
 
 Default value
 
 checkbox in the “Remove case assignee after case reopening” (“ClearAssigneeOnCaseReopening” code) system setting.
3. Go to the
 
 Studio
 
 workplace →
 
 Email templates
 
 and edit the contents of the “Case feedback request notification” email template. Localize the template content to different languages if needed.
 [Read more >>>](https://academy.creatio.com/documents?id=1787#title-198-3)
4. Specify the usage rule (“Send immediate” or “Send after a delay”) in the
 
 Case notification rule
 
 lookup.
 [Read more >>>](https://academy.creatio.com/documents?id=1787#title-198-2)
5. Configure sending a second evaluation request if the customer did not rate the work of the support service after the first notification. Use the “Number of waiting days to reevaluate resolved case” (“FirstReevaluationWaitingDays” code) and “Number of waiting days after second reminder of resolved case” (“SecondReevaluationWaitingDays” code) system settings.
 



 If the customer does not provide a score after the reminder, Creatio will automatically close the case after the time specified in the corresponding system setting.



 User satisfaction scale setup
-------------------------------



 You can customize the scale that is displayed in the case resolution message in the
 
 User satisfaction levels
 
 lookup.
 



 By default, the lookup contains a 5-point scale: “Extremely poor,” “Poor,” “Neutral,” “Good,” “Excellent.” Case status in the
 
 Satisfaction levels
 
 lookup is determined according to the score given by the customer.
 



 You can set up a scale with an optional number of points, for example, 3 or 7, and customize the color schema. To add a new level to the scale:
 


1. Click
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_csat_settings/btn_system_designer.png)
 to open the System Designer.
2. Go to the
 
 System setup
 
 block →
 
 Lookups
 
 .
3. Select the
 
 Satisfaction levels
 
 lookup in the list.
4. Add a new record and populate the fields:
 


	1. Fill out the name of the satisfaction level that is going to be displayed in the
	 
	 Rating
	 
	 field on the
	 
	 Closure and feedback
	 
	 tab of the case page.
	2. Specify the rating for the level. This rating will be used in the system for statistical calculations and customer satisfaction analysis in different sections.
	3. Select a status that will be automatically assigned to cases that receive this satisfaction score.
	4. Select the
	 
	 Is used
	 
	 checkbox to add the score to the email notification template.
5. Click
 ![btn_edit.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_csat_settings/btn_edit.png)
 . On the edit page of the satisfaction level, add an image that will display corresponding satisfaction level in the email. To do this, click the
 ![btn_add_userpic.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_csat_settings/btn_add_userpic.png)
 button and upload the image (Fig. 1).
 




 Fig. 1 Upload the satisfaction level image
 

![scr_section_service_requests_satisfaction_level_edit_page.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_csat_settings/scr_section_service_requests_satisfaction_level_edit_page.png)





 Attention.
 
 Deleting base lookup values is not recommended, since this might lead to incorrect operation of preconfigured business processes. Deselect the
 
 Is used
 
 checkbox to remove the score from the scale.
 




 As a result, the case resolution notification will contain the customized scale for evaluating the work of the service team (Fig. 2).
 




 Fig. 2 User satisfaction scale in the email
 

![scr_cases_email_send_satisfaction_levels_letter.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_csat_settings/scr_cases_email_send_satisfaction_levels_letter.png)



 After selecting a score the case will change its status automatically. For example, the score is “Poor,” the case will be reopened automatically.
 



 Upon clicking a grade in the email, the case customer's browser will open a page that will let them add a comment to their evaluation grade. The page displays a corporate logo according to the value of the “Logo - Thank you for your feedback” (“ImageThanksForRaiting” code) system setting. Learn more about setting up the corporate logo in a separate article:
 [Add corporate logo](https://academy.creatio.com/documents?id=1249) 
 .
 



 Both the customer’s grade and comments will be added to the
 
 Feedback
 
 field block on the
 
 Closure and feedback
 
 tab automatically.
 


##### 
 View case feedback grades



 The CSAT score and the comment that the customer leaves on the thank you page are displayed on the
 
 Closure and feedback
 
 tab of the case page. General CSAT indicators are available on the
 
 Feedback
 
 tab in the
 
 Dashboards
 
 section.
 



 Use the “Ability to change case satisfaction level” (“CanChangeCaseSatisfactionLevel” code) system operation to manage permissions for modifying information on the
 
 Closure and feedback
 
 tab.
 





 Note.
 
 By default, employee users do not have permission to edit the case feedback, while the portal users have such permission.
 



 We recommend granting permission to the
 
 Ability to change case satisfaction level
 
 system operation only to senior managers of customer support department.
 





