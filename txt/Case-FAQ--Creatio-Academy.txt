

#### 

 Why doesn’t the list display all cases even when you scroll all the way down?



 By default, the list displays only open cases with the “New”, “In progress”, “Pending”, “Resolved” or “Reopened” statuses. To display closed and canceled cases, select the
 
 Show closed cases
 
 checkbox.
 



 Also, the list may not display all cases due to the current custom filter settings (
 [Fig. 1](#XREF_83311_177)
 ). To remove the quick filter, click the  button on the right.
 





 Fig. 1
 

 Using the quick filter example
 

![scr_filters_quick_filter.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_faq/scr_filters_quick_filter.png)


#### 

 Why can’t I select a service in a case, though there are records in the [Services] section?



 Service in in a case can only be selected after the user’s service agreement has been specified. A user can only specify services that are a part of their service agreement. To specify a service in a case, one of the following conditions must be met:
 


* A valid service agreement exists with the case contact or their company, which includes services with the corresponding category, for example, "Incident";
* Customers without a service agreement can use a default service agreement.


#### 

 Why was the case reopened?



 Paused cases and cases being resolved (in the "Pending", "Resolved” status), will be automatically reopened in case a new message from the case customer is received on the self-service portal or an incoming email-message with the case number in its subject has been received. You can also reopen a case manually by selecting the “Reopened” status on the workflow bar (
 [Fig. 2](#XREF_89033_290)
 ).
 





 Fig. 2
 

 Reopening a case manually
 

![scr_section_service_requests_case_reopen.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_faq/scr_section_service_requests_case_reopen.png)


#### 

 Why after reopening a case, the [Assignee] field is cleared?



 After receiving a new email or message on the self-service portal for a paused and resolved case (in the "Pending", "Resolved” status), the case will be reopened. The
 
 Assignee
 
 field will be cleared, and the case will be transitioned to the queue for processing. This will ensure that the case customer receives a response to their case as soon as possible, regardless of the agent's workload, or their presence in the workplace at the time of receiving a case from the customer.
 


#### 

 Why can’t I attach an email or publish a message for a case in a final stage?



 A case in a final stage is a case that was fully processed. This case cannot be re-opened or resolve again. Incoming emails will not be attached to this case. If at any point a user asks an additional question about a closed or canceled case, you need to register a new case and specify the closed case as its parent case.
 



 Case feed is accessible for the support team regardless of its status. Service team member can manually connect any incoming and outgoing message to the case in the final stage or send the email from the case page.
 


#### 


 In what cases and why does the system send automatic notifications to contacts?



 By default, automatic notifications are sent to case contacts in 2 instances:
 


* when a new comment is posted on the self-service portal;
* when the case status is changed (registered, pending, resolved, canceled, etc).



 Read more in the “
 
[Set up automatic email notifications](/docs/8-0/user/service_tools/service_cases/case_settings/email_notifications/set_up_email_notifications#HT_specs_service_request_rules_notification) 

 ” article.
 



 Automatic notifications are not sent when:
 


* the case contact profile does not contain email address;
* the
 
mailbox for automatic notifications

 is not set up.


#### 

 How do I add new case notifications?



 To add new or change existing
 **case status change** 
 notification,
 
 do the following:
 


1. Set up an email template:
 
[Read more >>>](/docs/8-0/user/service_tools/service_cases/case_settings/email_notifications/set_up_email_notifications#HT_specs_service_requests_management_process_set_up_templates)
2. In the
 
 Case contact notification rules
 
 lookup, create new or edit an existing rule and connect it to the created email template.
 
[Read more >>>](/docs/8-0/user/service_tools/service_cases/case_settings/email_notifications/set_up_email_notifications#HT_specs_service_request_rules_notification) 





 For any
 **other notifications** 
 you need to create a business process by which emails will be sent and specify the email template.


#### 

 What happens to a case that was not evaluated?



 If customers do not assess the support service quality after receiving a message about case resolution, they will receive an additional evaluation request in a few days. If no evaluation is received after the additional request, the case will be closed automatically. The evaluation response waiting time is set in the
 **Number of waiting days to reevaluate resolved case** 
 and
 **Number of waiting days after second reminder of resolved case** 
 system settings.
 


#### 

 How do I disable case re-evaluation request?



 Case re-evaluation request is made, if the first request went unanswered. Reevaluation requests are made by the “Reevaluate case level request process” (the ReevaluateCaseLevelRequestProcess schema of the Case package) business process. Deactivate this business process, and the re-evaluation requests will not be sent anymore.
 


#### 

 How do I disable reopening cases by emails?



 To disable reopening cases by incoming emails, you must disable the following business processes:
 


* “Run process: Reopen case and notify assignee on receiving an answer regarding the case” (the RunSendNotificationCaseOwnerProcess schema of the CaseService package);
* “Reopen case and notify assignee on receiving an answer regarding the case” (the SendNotificationToCaseOwner schema of the CaseService package);
* “Send email to case contact after adding a portal message” (the CasePortalMessageHistoryNotificationProcess schema of the Portal package).


#### 

 Why can’t I escalate a case?



 The
 
 Escalate
 
 action is available only in the Service Creatio, enterprise edition. In the Creatio customer center, you can reassign the case. To do this click the
 ![btn_com_lookup.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_faq/btn_com_lookup.png)
 button in the
 
 Owner
 
 field and select an employee who will continue processing of the case.
 


#### 

 Why the searching for similar cases is disabled for me?



 The
 
 Search for similar cases
 
 action is available only in the Service Creatio, enterprise edition. In the Service Creatio, customer center edition, you can attach the knowledge base article to the case and assign a parent case.
 




