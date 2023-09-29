


 In order for a campaign to function correctly, its elements must be properly connected by
 **flows** 
 . Some elements can function without flows, for example
 
 Exit from campaign
 
 .
 



 Flows can work unconditionally. For example, all contacts added on a trigger in Fig. 1 will advance to the next element and receive a congratulatory email. Flow can also advance campaign participants to the next element only when certain conditions are met. For example, only those participants who clicked the link in the email on the previous step will advance to the event step (Fig. 2). Set up conditions for advancing to the next element to fork the campaign into multiple branches with differing sets of steps.
 



 To add flows, select the needed campaign element on the diagram and click the arrow that appears (Fig. 1).
 




 Fig. 1 Set up the transition between elements
 

![scr_section_campaigns_flow_0.png](/docs/sites/en/files/images/Marketing_Tools/campaign_flows/scr_section_campaigns_flow_0.png)



 Conditional flows transfer participants to the next step only when the specified conditions are met. For example, a specific response was received from the participant, a certain amount of time has passed, etc. The following types of conditions are available:
 


* [delay](#title-1706-8) 
 before executing the next element
* [transition depending on participant response](#title-1706-9)
* [transition depending on configured filters](#title-1706-3) 
 .



 You can configure several conditions for a single condition flow. If several conditions are configured for a single condition flow, only those campaign participants who match all conditions as follows will be able to advance to the next campaign step:
 


* **Transition depending on participant response** 
 . The response of the participant matches any of the values specified in the condition.
* **Transition depending on configured filters** 
 . The participant matches the filter specified in the condition.



 Flows that have unspecified conditions will immediately advance participants to the next campaign step regardless of their response or filter conditions.
 



 Delay before executing the next element
-----------------------------------------



 A delay suspends the transition of the campaign participants to the next step for a specified period of time. For example, campaign participants (Fig. 2) who opened the webinar invitation and clicked the link will receive a reminder email three days later.
 



 Conditional flows have two options in the
 
 Enable delay before executing an element?
 
 field:
 


* “
 **No, execute after the previous one** 
 .” Select this option to advance the participants to the next step according to the default campaign execution frequency.
* “
 **Yes, for specified time period** 
 .” Select this option to advance the participants to the next step after a certain number of days (hours) at the specified time (Fig. 2).




 Fig. 2 Transition delay
 

![scr_section_campaigns_flow_time_delay_0.png](/docs/sites/en/files/images/Marketing_Tools/campaign_flows/scr_section_campaigns_flow_time_delay_0.png)



 The campaign element with the configured transition delay is executed every day at the time indicated in the flow properties. Select a delay unit (days or hours) specify the number of days/hours in the
 
 Quantity
 
 field.
 



 Wherein:
 


* A 1-day delay equals a 24-hour delay. Delays are always recalculated to hours on the back end.
* If the delay unit is “days” and the quantity is “1”, the element will be executed next day at the time specified in the
 
 Execution time
 
 field.
* If the delay unit is “days” and the value is more than “1”, the element will be executed after the specified number of days, at the time selected in the
 
 Execution time
 
 field.



 Use the
 
 Exact time
 
 checkbox to specify the exact time when the transition occurs.
 



 Transitions depending on participant response
-----------------------------------------------



 The
 
 Marketing email
 
 and
 
 Add to event
 
 elements can process participants’ responses. Responses enable custom interaction with the participants depending on their actions on the previous step.
 



 For example, the outgoing flows of the
 
 Marketing email
 
 element provide the following responses:
 


1. “
 **Email delivered** 
 ”
 **:** 
	* “Email opened”.
	* “Email clicked”.
	* “Spam complaint”.
	* “Recipient unsubscribed”.
2. “
 **Email undelivered** 
 ”
 **:** 
	* “Delivery error”.
	* “Soft Bounce”.
	   
	
	 is received as a result of a temporary problem with the recipient's address, for example, if the recipient's mailbox is full or any other temporary problem occurred.
	* “Hard Bounce”.
	   
	
	 A hard bounce response is received as a result of a permanent delivery error, such as an invalid email address domain.
3. “
 **Email canceled:** 
	* “Email limit reached”.
	* “Rejected”.
	* “Canceled (unsubscribed from all emails)”.
	* “Canceled (sender's name not valid)”.
	* “Canceled (sender's domain not verified)”.
	* “Canceled (duplicated email)”.
	* “Canceled (email not provided)”.
	* “Invalid email address”.
	* “Canceled (incorrect email)”.
	* “Canceled (invalid email)”.
	* “Canceled (template not found)”.
	* “Canceled (unsubscribed by email type)”.



 On Fig. 3, the next campaign steps for those participants who opened the email and those who clicked the link will be different.
 




 Fig. 3 Transitions depending on participant response
 

![section_campaigns_new_designer_condition_flow_2.png](/docs/sites/en/files/images/Marketing_Tools/campaign_flows/section_campaigns_new_designer_condition_flow_2.png)



 Transition by filter conditions
---------------------------------



 Use filtering to advance only those of the participants who match the filter conditions (Fig. 4).
 



 Select “Filtering conditions” in the
 
 Which conditions must the contacts meet to transition to the next step?
 
 field to display the filter, and specify the required conditions.
 



 You can configure any filtering conditions for the contact and its connected objects. For example, on Fig. 4, a participant is added on a trigger after event registration and immediately receives an invitation email. Subsequent transition depends on the filtering conditions: newsletters are only sent to those contacts who participated in the event, and only if the “Status” connected object is “Completed.”
 




 Fig. 4 Transition depending on the configured filters
 

![scr_section_campaigns_filter.png](/docs/sites/en/files/images/Marketing_Tools/campaign_flows/scr_section_campaigns_filter.png)





 Attention.
 
 Filtering based on connected objects may cause errors due to discrepancies between the campaign and the object of the marketing email. For example, adding a lead as a connected object when passing information about an event participant to the marketing email will trigger an error. That is because the event participant is the connected entity of the campaign, and the lead is not.
 





