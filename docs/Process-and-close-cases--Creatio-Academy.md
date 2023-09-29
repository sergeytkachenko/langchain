


 Process Creatio cases in the
 
 Cases
 
 section or in the
 [agent desktop](/docs/8-0/user/service_tools/contact_center_tools/agent_desktop_setup/overview/general_agent_desktop_settings) 
 .
 



 Cases are processed according to a predefined business process. You can set up a custom business process and use it for processing cases from separate queues.
 



 Start processing a case
-------------------------



 To begin working on a case, select a case in the
 
 Cases
 
 or
 
 Agent desktop
 
 section list. After you open the case, select the “In progress” status on the workflow bar (Fig. 1).
 




 Fig. 1 Start processing a case
 

![scr_section_service_requests_change_case_ctage.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_processing/scr_section_service_requests_change_case_ctage.png)



 As a result, Creatio will change the case status to “In progress” and specify the current user in the
 
 Assignee
 
 field. The customer will be notified that you started processing the case and given the resolution deadline by email.
 



 After you resolve the case, transfer it to the following stage using the workflow bar.
 





 Note.
 
 If you want to return to the
 
 Cases
 
 section list automatically after saving the case, select the
 
 Close on save
 
 checkbox in the “Case statuses” lookup. Learn more:
 [Set up case statuses](/docs/8-0/user/service_tools/service_cases/case_settings/case_statuses/set_up_case_statuses) 
 .
 



### 
 Notify the assignee/assignee group about the case



 If a case with
 
 Assignee
 
 and/or
 
 Assignee group
 
 case fields filled out becomes active, Creatio will notify the assignee/assignee group. Creatio will also notify the assignee/assignee group if the assignee/assignee group is specified for an active case.
 





 Note.
 
 The case is considered active if its status is “New,” “In progress,” “Reopened.”
 




 If the
 
 Assignee
 
 field is filled out, Creatio will notify the assignee. The
 
 Assignees group
 
 field can be either empty or filled out.
 



 If the
 
 Assignees group
 
 field is filled out and the
 
 Assignee
 
 field is not, Creatio will notify the assignee group. In this case, the
 
 To
 
 field will be populated with emails of every group member.
 



 Set up the content of the notification sent to the assignee/assignee group in the
 
 Message templates
 
 lookup. By default, the notification uses the “Specifying case assignee” template.
 


### 
 Diagnose and resolve an incident



 Service Creatio, enterprise edition includes the “Creating and processing tasks for case diagnostic and resolution” process that runs if the following conditions are met:
 


1. A customer support agent was assigned to an incident. The incident status is “New” or “In progress.”
2. The status of an inactive incident changes to “New,” “In progress,” “Reopened.” The
 
 Assignee
 
 field is filled out.
3. An incident is escalated to a support agent.



 Creatio adds a task for the responsible agent as part of the resolution process. When an agent modifies the incident, Creatio closes the task according to the following rules:
 


1. If the agent resolves the incident, Creatio will close the task with the “Solution found” result.
2. If the agent cancels an incident, Creatio will change its status to “Canceled.” The task status will also be changed to “Canceled” with the identical result.
3. If the agent postpones the resolution, Creatio will change the task status to “Closed” with the “Additional information required” result.
 



 If the values in the assignee/assignee group fields change, Creatio will change the status of the connected task to “Closed” with the “Escalation required” result. In this case, Creatio may run a new sub-process instance and create a new task for the new assignee.


### 
 Escalate a case



 Case escalation is available in Service Creatio, enterprise edition out-of-the-box. To escalate a case to a higher support level, select the
 
 Escalate
 
 action from the
 
 Actions
 
 menu on the case page.
 



 This will open the escalation page. Specify the new support level, as well as the assignee or assignee group, on the page.
 





 Note.
 
 Creatio will close the incident processing task created when transferring a case to the previous status with the “Escalation required” result.
 




 A new assignee or an agent from the assignee group will continue processing the case.
 


#### 
 Reassign a case



 You can reassign a case in Service Creatio, customer center edition. To do this, change the value in the
 
 Assignee
 
 or
 
 Assignee group
 
 field of the case page.
 



 A new assignee or an agent from the assignee group will continue processing the case.
 


### 
 Reclassify the case



 Case reclassification is available in Service Creatio, enterprise edition out-of-the-box. To change the service agreement, open the case page and click
 
 Actions
 
 →
 
 Reclassify
 
 .
 



 As a result, Creatio will update the terms, category, and other case parameters that are determined automatically.
 


### 
 Search for case solution



 Case solution search is available in Service Creatio, enterprise edition out-of-the-box. To do this, select the
 
 Search for similar cases
 
 action from the
 
 Actions
 
 menu when processing an incident or a service request.
 



 This will open a list showing cases connected to the same service, same configuration item, or marked by the same tags.
 



 If the list contains any resolved cases, the knowledge base articles linked to these cases are likely to contain the solution for the current case. To access these articles, use the
 
 Knowledge base articles
 
 detail in the
 
 Closure and feedback
 
 tab of the similar resolved cases.
 



 If the list contains an identical case, select it. As a result, Creatio will specify the selected case in the
 
 Parent case
 
 field of the current case.
 



 Use the
 
 Internal note
 
 button in the
 
 Processing
 
 tab to consult with other employees regarding the case resolution.
 



 Communicate with the customer
-------------------------------



 Use the
 ![btn_com_workflow_card_email.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_processing/btn_com_workflow_card_email.png)

 Email
 
 and
 ![btn_com_workflow_card_portal_message.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_processing/btn_com_workflow_card_portal_message.png)

 Portal message
 
 buttons on the action panel to send replies to the customer (Fig. 2).
 




 Fig. 2 Add a message to display on the customer portal
 

![section_service_requests_publish_portal.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_processing/section_service_requests_publish_portal.png)



 Click the
 ![btn_service_requests_attachment.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_processing/btn_service_requests_attachment.png)
 button to attach a file to an email or portal message.
 



 If you send a portal message, Creatio will notify the customer by email.
 



 After you finish processing the case, for example, ask the customer for more information, change the case status to “Waiting for response” (Fig. 3), which indicates that the case is waiting for a customer's reply.
 




 Fig. 3 Change the case status to “Waiting for response”
 

![scr_section_service_requests_change_case_ctage00001.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_processing/scr_section_service_requests_change_case_ctage00001.png)



 The customer can reply by email or by posting a message on the customer portal. The reply will appear in the
 
 History
 
 block (Fig. 4). Creatio will reopen the case automatically. The
 
 Assignee
 
 field will be cleared and the case will be returned to the processing queue.
 




 Fig. 4 The customer communication history
 

![section_service_requests_publish_portal_history.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_processing/section_service_requests_publish_portal_history.png)



 To call the customer quickly, hover over the contact name in the case profile. This will open a mini page. If the contact has phone communication options, dialing options will be available on the mini page (Fig. 5).
 




 Fig. 5 Dial the customer
 

![section_service_requests_mini_card.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_processing/section_service_requests_mini_card.png)



 You can also
 [dial](/docs/7-18/user/platform_basics/communications/calls/managing_calls) 
 the customer via the
 [communication panel](/docs/8-0/user/platform_basics/communications/notifications/check_notifications_and_process_tasks) 
 .
 


### 
 Notify the contact about a message in the “Portal” feed



 A portal user receives a notification about a message in the “Portal” feed if they have an active email.
 



 Configure the content of the notification in the
 
 Email templates
 
 lookup.
 



 Resolution and feedback
-------------------------



 After you provide the customer with the resolution, move the case to the resolved status.
 




 Fig. 6 Resolve the case
 

![section_service_requests_resolve.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_processing/section_service_requests_resolve.png)



 Creatio will notify the customer about the case resolution by email. The email will also contain the user satisfaction scale. The customer can use it to grade the contact center or support service performance. Learn more:
 [Set up case resolution notification](/docs/8-0/user/service_tools/service_cases/case_settings/email_notifications/set_up_email_notifications#title-198-4) 
 .
 



 Case status will change depending on the customer satisfaction level. For example:
 


* If the satisfaction level is “1” or “2,” Creatio will reopen the case, change its status to “Reopened,” and clear the
 
 Assignee
 
 field.
* If the satisfaction level is “3,” “4,” or “5,” Creatio will change the case status to “Closed.”





 Note.
 
 Configure the relationship between customer satisfaction levels and case statuses in the
 
 Satisfaction levels
 
 lookup.
 




 To expedite the resolution of similar cases in the future, link the knowledge base articles that contain the resolution to the case. If there are no such articles in the knowledge base, Creatio will suggest creating a new article automatically. By default, the article creation process is deactivated. To activate this process, go to the
 
 Process library
 
 section → select the needed process record → click
 
 Activate
 
 .
 



 If you change the status of the case that contains incomplete tasks in
 **Service Creatio, enterprise edition** 
 to “Resolved”, Creatio will ask you what to do with the tasks. You can mark all tasks as completed, cancel them, or leave them unchanged.
 


### 
 Create a knowledge base article after resolving a case



 After you resolve the case, you can create a corresponding knowledge base article that helps to resolve similar cases. Creatio includes a sub-process that automates the article creation.
 



 By default, the subprocess is inactive. To activate the sub-process:
 


1. Open the System Designer by clicking the
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_processing/btn_system_designer.png)
 button.
2. Go to
 
 Processes
 
 →
 **Process library** 
 .
3. Clear the
 
 Active
 
 checkbox to display all business processes available in Creatio.
4. Select the “Create a new article after case resolution” business process in the list and click
 **Activate** 
 (Fig. 7).




 Fig. 7 Activate the “Create a new article after case resolution” sub-process
 

![btn_service_requests_activate.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_processing/btn_service_requests_activate.png)



 The “Create a new article after case resolution” sub-process runs as follows:
 


1. When you resolve a case, the process checks the case for linked knowledge base articles.
2. If there are none, the process will ask you if you want to create a new article. Select “Yes” to create a new article.
3. After you save the article, the process will link it to the case automatically.


### 
 Reopen the case automatically when receiving an email or a comment on the portal



 Creatio reopens the case automatically and clears the
 
 Assignee
 
 field if the following conditions are met:
 


1. The case status is paused or resolved yet not final.
 





 Note.
 
 Configure incident and service request statuses in the
 
 Case statuses
 
 lookup. In this case, the status must have the
 
 Pause status
 
 or
 
 Resolved status
 
 checkbox selected yet the
 
 Final status
 
 checkbox cleared. By default, “Resolved” and “Waiting for response” statuses meet these criteria.
2. The customer sent a case email or left a comment on the portal.
 



 If Creatio receives an email or a portal comment, the case status will be changed to “Reopened” automatically. Creatio will also clear the
 
 Assignee
 
 field. This is done to enable other employees to work with the reopened case.
 





 Note.
 
 If the
 
 Assignee group
 
 field is not cleared, every group member will receive a case notification on their agent desktop.


### 
 Close cases automatically



 Creatio closes cases automatically if the following conditions are met:
 


1. The case status is “Resolved.”
2. The case's actual resolution time is filled in.
3. The waiting period for the evaluation of the case ended.





 Note.
 
 Specify the waiting period for case evaluation in the “Number of waiting days to reevaluate resolved case” (“FirstReevaluationWaitingDays” code) and “Number of waiting days after second reminder of resolved case” (“SecondReevaluationWaitingDays” code)
 [system settings](/docs/8-0/user/service_tools/service_cases/case_settings/case_statuses/set_up_case_statuses3#title-1880-25) 
 .
 




 Creatio checks for cases that meet these conditions once a day. The status of every case that meets the conditions is changed to “Closed.” The automatic case closure procedure remains the same whether case evaluation is on or off.
 



 You can disable the automatic case closure. To do this, clear the “Default value” checkbox in the “Automatically close resolved cases” (“CloseResolvedCases” code)
 [system setting](/docs/8-0/user/service_tools/service_cases/case_settings/case_statuses/set_up_case_statuses3#title-1880-25) 
 .
 



 Cancel a case
---------------



 If you created a case by mistake or the case no longer needs a response (for example, the customer resolved the issue on their own or the question is no longer relevant), select the
 
 Canceled
 
 stage on the workflow bar to cancel the case.
 




 Fig. 8 Cancel the case
 

![section_service_requests_cancel_select.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_processing/section_service_requests_cancel_select.png)



 Creatio will change the case status to “Canceled” and notify the customer by email.
 




