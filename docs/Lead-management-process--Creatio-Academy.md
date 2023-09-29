


 Use the best practices and increase your chances to hand-off the lead to sales by following the
 **lead management process** 
 steps.
 



 Lead management implies handling a lead by stages, starting with qualification. This may lead to creating activities and opening additional pages in Creatio. As these activities are completed, their results influence the process flow.
 



 Process specifics:
 


* If the lead management business process is active, Creatio automatically adds linked activities and suggests steps that the user should take on each stage of lead processing.
* Use the
 **workflow bar** 
 and
 **action panel** 
 at the top of the lead page (Fig. 1) to manage a lead stages.
* With the workflow bar, you can switch to any stage, skip a stage or return to any previous one.
* Using the action panel, you can manage activities created when managing a lead.
* Customer need details, lead management history and other information are available on the tab dashboard.
* Check tips for each stage by hovering the cursor over the
 ![btn_info.png](/guides/sites/en/files/documentation/user/en/leads/BPMonlineHelp/leads_process/btn_info.png)
 icon.



 You can view detailed information on the process steps in the process library.
 





 Fig. 1
 
 The lead management process
 

![specs_leads_dashboard_actionsboard.png](/guides/sites/en/files/documentation/user/en/leads/BPMonlineHelp/leads_process/specs_leads_dashboard_actionsboard.png)



 To run the lead management process, click the
 
 Qualify
 
 button, which is displayed in the list when selecting a lead record or on the new lead page.
 



 Qualification
---------------



 The qualification stage is used to check completeness of information about a contact or an account to which the lead is linked. This stage starts after the
 [lead information has been saved](/docs/8-0/user/marketing_tools/leads/create_a_lead/new_lead) 
 .
 


* If the available information is sufficient for further work on the lead, qualify the lead without opening the record page. To do this, select the record in the list and click
 
 Qualify
 
 .
* If information about a contact or account needs to be checked and updated, select a lead in the record list, click
 
 Open
 
 , and populate the information blocks – contact and account profiles. You can add a new contact and account or select existing ones. For example, update the record information by adding a mobile phone or website address. After checking and entering the required data on the qualification page, click
 
 Qualify
 
 .
 



 If you enter a contact or account in the
 
 Lead Info
 
 tab on the
 
 Qualification
 
 stage, Creatio will automatically create a new contact or account record.
* If the lead information is insufficient to contact the customer, disqualify the lead by clicking
 
 Actions
 
 →
 
 Disqualify
 
 →
 
 Incorrect data
 
 .



 Nurturing
-----------



 On this stage, the
 [owner](/docs/8-0/user/marketing_tools/leads/faq/leads_faq#title-314-1) 
 and the nurturing strategy are determined. Since the owner is appointed at the qualification stage, after qualification, the lead is transferred to the “Handoff to sales” stage, and the "Nurturing" stage is skipped.
 



 If necessary, you can return to this stage and specify the employees responsible for the handoff to sales, and determine the further strategy of working with the lead. To move to the nurturing stage, click
 
 Nurturing
 
 on the workflow bar at the top of the lead page. When a lead is being transferred to this stage, the “Lead management: Distribution” page is created in the action panel. Click
 
 Execute
 
 and go to the lead distribution page.
 


* If the customer's interest is confirmed, advance the lead to the next stage to specify the need. To do this, in the
 
 Distribute
 
 button menu select the
 
 Start proceeding to handoff
 
 command. As a result, the lead proceeds to the “Handoff to sales” stage. If the
 
 Remind owner
 
 checkbox is selected on the distribution page, a notification will be sent to the user responsible for proceeding the lead to handoff.
* If there is no point in communicating at the moment, but the customer has a postponed interest, select the
 
 Continue nurturing
 
 command in the
 
 Distribute
 
 button menu. As a result, the lead remains at the nurturing stage, and you can continue working on it later.
* If the customer is no longer interested in your products or services, select the
 
 Not interested
 
 result. The lead will advance to the “Not interested” stage.



 Proceed to handoff
--------------------



 The lead is transferred to this stage automatically after the qualification. Contact the customer and find out more about the potential opportunity. After estimating the customer's potential, you can hand the customer over to a particular sales manager taking into consideration the manager qualification and profile. As a result, you can run the handoff or proceed to order for this customer. If the customer has a postponed interest, you can return the lead to the previous stage and carry on nurturing them.
 


### 
 Specify the lead's parameters



 On this stage, Creatio will create a task titled ”Contact the customer and specify the availability and actuality of the need, budget, parameters as well as their role in decision-making,” available on the workflow bar.
 



 Execute the task by clicking the title or the
 
 Complete
 
 button.
 



 After you complete the task on the
 
 General information
 
 tab of the task page, select the required result and click
 
 Save
 
 .
 



 The process depends on the activity results. For example, if you use Sales Creatio, commerce edition, or Sales Creatio, enterprise edition, and the customer is ready to make an order, specify the task result as “
 **Proceed to order** 
 .” On the lead page, the “
 **Sales-ready** 
 ” need maturity will be set.
 


### 
 Handoff to sales



 If you are ready for handoff, select the “
 **Proceed to handoff** 
 ” task result. Creatio will ask you to enter additional notes for the handoff. After that, a new task will be created to enter information required to hand-off the lead to sales.
 



 While executing it, populate the following fields on the task page:
 


1. Budget, base currency
 
 – specify expected opportunity budget in the base currency.
2. Sales division
 
 – division that will handle the opportunity, for example, direct sales department or affiliate sales department.
3. Meeting date and time
 
 – specify date and time of the first meeting with the customer.
4. Decision date
 
 – date and time when the customer is ready to make a decision about the opportunity.
 



 The
 
 Need type
 
 ,
 
 Assignee
 
 , and
 
 Notes
 
 will populated automatically. Information specified in the
 
 Result details
 
 field of the lead proceed to handoff page will be displayed in the
 
 Notes
 
 field. Once the page is saved, you can see the specified note in the lead feed.
 



 The data entered will be displayed in the
 
 Proceed to handoff
 
 field group on the
 
 History
 
 tab of the lead page. You can edit it later.
 



 Once the page is saved, the note about the handoff will be added to the lead feed. The lead then proceeds to the “Awaiting sale” stage. On the lead page, the “
 **Sales-ready** 
 ” need maturity will be set.


### 
 Back to distribution



 If the customer is not interested at the moment, but communication with the customer is still available and the possibility to close the opportunity still exists, complete the task and select “
 **Back to distribution** 
 ” in the
 
 Select results
 
 field of the task completion mini page. In this case, the lead will return to the “Nurturing” stage, and the “Discovered” need maturity is set on the lead page.
 


### 
 Postpone lead processing



 If you need to postpone the task for some defined period, complete it and select “
 **Rescheduled** 
 ” in the
 
 Select results
 
 field of the task completion mini page. The lead will remain at the “Handoff to sales” stage. A new task for proceeding lead to handoff will be created.
 



 If the customer need is not confirmed, complete the task and select the “
 **Not interested** 
 ” in the
 
 Select results
 
 field of the task completion mini page. In this case, the “Not interested” need maturity will be set on the lead page. The lead will remain at the “Handoff to sales” stage. Later on, after the customer's need is renewed, you can continue working according to the process.
 



 Awaiting sale
---------------



 All lead management stages are complete. If you use Sales Creatio, team edition, or Sales Creatio, enterprise edition, Creatio will add an
 
 Opportunities
 
 section record based on the lead.
 [Corporate sale process](/docs/8-0/user/sales_tools/long_sales/corporate_sale_process_shortcut/corporate_sale_process) 
 will start for the new opportunity. If the corporate sales process is completed successfully, the lead will then proceed to the final “
 **Need satisfied** 
 ” stage.
 




