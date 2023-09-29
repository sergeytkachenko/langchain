


 You can monitor the flow of your campaigns using campaign log. To open the log, click the
 
 Campaign log
 
 action in the
 
 Campaigns
 
 section (Fig. 1).
 





 Fig. 1
 
 The
 
 Campaign log
 
 action
 

![section_campaigns_log_action.png](/sites/en/files/documentation/user/en/marketing_campaigns/BPMonlineHelp/monitor_campaigns/section_campaigns_log_action.png)



 You can also open the campaign log from the campaign page. Click
 
 Actions
 
 →
 
 Go to campaign log
 
 . The log will be automatically filtered by the current campaign.
 



 The list view of the campaign log (Fig. 2) displays information on campaign element execution. Aggregate metrics are available in the analytics view.
 





 Fig. 2
 
 Campaign log list
 

![section_campaigns_log.png](/sites/en/files/documentation/user/en/marketing_campaigns/BPMonlineHelp/monitor_campaigns/section_campaigns_log.png)



 The log contains information on elements from all campaigns. After you start a campaign, its events will start appearing in the campaign log. The campaign log is activated automatically and does not require additional setup.
 



 Campaign log list
-------------------



 Each record in the list is a separate log event. Log data is displayed as a list of records with the following columns:
 





|  |  |
| --- | --- |
| 
 Campaign
  | 
 The name of the campaign where the log event has occurred. Click the campaign name to open the corresponding record in the
 
 Campaigns
 
 section.
  |
| 
 Action
  | 
 The name of the
 
[logged action type](#title-2062-2) 

 .
  |
| 
 Step
  | 
 The name of the
 
[campaign element](/docs/7-16/user/marketing_tools/marketing_campaings/campaign_elements/campaign_element_reference) 

 in the Campaign Designer that triggered the logged action.
  |
| 
 Number of participants
  | 
 Number of participants involved in the logged action.
  |
| 
 Status
  | 
 Status of the campaign execution step (“Success” or “Error”).
  |
| 
 Start
  | 
 Start and end dates of the actual campaign execution step. Depending on the action type, it can be: start or end of the campaign (for “Campaign execution” actions), start/end dates of a campaign element execution (for “Element execution: <Campaign element type>” actions) or date of adding and removing campaign participants manually (for “Participant adding (manually)” action).
  |
| 
 End date
  |
| 
 Duration, m (sec)
  | 
 Duration of the execution step in minutes or seconds.
  |
| 
 Scheduled date
  | 
 The date on which the campaign was planned to start if the campaign start was scheduled to a specific date in conditional flows.
  |
| 
 Error details
  | 
 If the status is “Error”, the field displays the error message that can help with diagnosing and resolving the campaign errors.
  |




 Types of logged campaign actions
----------------------------------



 Creatio logs three types of campaign actions:
 





|  |  |
| --- | --- |
| 
 Campaign execution
  | 
 Indicates the start of a campaign. The first action logged for any campaign.
  |
| 
 Element execution: <Campaign element type>
  | 
 Indicates execution of a campaign element or flow on the campaign diagram.
  |
| 
 Participant adding (manually)
  | 
 Indicates manual adding of a participant to the campaign.
  |




 Monitoring counters on the
 
 Campaign flow
 
 tab
----------------------------------------------------



 Once you create a campaign flow in the Campaign Designer, the
 
 Campaign flow
 
 tab of the campaign page will display the campaign diagram with participant counters for every campaign element, as well as a set of checkboxes that enable different types of counters (Fig. 3). The color of the checkbox is the same as the color of the respective counter.
 





 Fig. 3
 
 Participant counter filters in the
 
 Campaign flow
 
 tab
 

![new_counters.png](/docs/sites/en/files/images/Marketing_Tools/monitor_campaigns/new_counters.png)


* **All** 
 – select to view the number of participants on all steps.
* **Step complete** 
 – select to view the number of participants on a step that completed successfully. These participants are queued to transfer to subsequent campaign step(s).
* **Step incomplete** 
 – select to view the number of participants on a step they reached but are yet to complete. These participants are usually delayed by a
 
 conditional flow
 
 .
* **Step in progress** 
 – select to view the number of participants on the step which is being executed at the moment.
* **Executed with error** 
 – select to view the number of participants on a step in which the error occurred.
* **Participating suspended** 
 – select to view the number of participants on a step in which their participation was suspended. These participants are likely set to re-enter the campaign.
* **History** 
 – displays the total number of participants who reached this step since the start of the campaign.



 If you add new participants to a campaign at different time, use the
 **filter by date** 
 to find out how many participants were added to the campaign at a specified period and what their current step is. The filters by date are available when the counters are enabled. The counters display only the contacts added during the specified period: “today” (
 ![btn_com_filter_day.png](/guides/sites/default/files/documentation/user/ru/marketing_campaigns/BPMonlineHelp/monitor_campaigns/btn_com_filter_day.png)
 ), “current week” (
 ![btn_com_filter_week.png](/guides/sites/default/files/documentation/user/ru/marketing_campaigns/BPMonlineHelp/monitor_campaigns/btn_com_filter_week.png)
 ) or custom period (
 ![btn_com_menu_period.png](/guides/sites/default/files/documentation/user/ru/marketing_campaigns/BPMonlineHelp/monitor_campaigns/btn_com_menu_period.png)
 ).
 



 To edit the campaign diagram, click
 
 Edit
 
 .
 



 Monitoring participants on the
 
 Audience
 
 tab
---------------------------------------------------



 The tab displays all campaign participants (contacts), their current steps on the campaign diagram and status (Fig. 5).
 





 Fig. 5
 
 The
 
 Audience
 
 tab
 

![section_campaigns_audience.png](/sites/en/files/documentation/user/en/marketing_campaigns/BPMonlineHelp/monitor_campaigns/section_campaigns_audience.png)



 The period when the list of participants is available on the
 
 Audience[ tab is configured in the [Start mode
 
 field on the campaign page. If “manual” is selected, the list will be displayed as soon as the campaign starts. If the campaign has the “at the specified time” selected, the list of participants on the
 
 Participants
 
 tab will be displayed at the first launch of the campaign according to the schedule. The list will not be displayed until the campaign starts.
 



 The
 
 Audience
 
 tab primary columns are available in the table:
 





|  |  |
| --- | --- |
| 
 Contact
  | 
 Full name of the campaign participant.
  |
| 
 Status
  | 
 The status of the campaign participant: “Participating” or “Exited”.
 

 The “Participating” status indicates that the contact continues to advance through the steps of the campaign. The “Exited the campaign” status indicates that the contact no longer participates in the campaign.
  |
| 
 Current step
  | 
 Campaign step (campaign element) the participant is currently on.
  |
| 
 Step completed
  | 
 “Yes” or “No”, depending on the participant’s execution of the corresponding step of the campaign. For example, clicked the email link or filled out the web-form.
  |
| 
 Step modified on
  | 
 The date and time when the participant advanced to the step, specified in the
 
 Current step
 
 column.
  |
| 
 Step completed on
  | 
 Date and time when the participant completed the step.
  |





