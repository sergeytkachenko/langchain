


 The
 
 Agent desktop
 
 section is designed to facilitate the work of contact centers and helpdesk agents. Use the agent desktop to manage cases in a single window with the help of out-of-the-box best practice processes, get instant access to customer's profile, and improve customer experience.
 



 Using the
 
 agent desktop
 
 an agent can quickly process tickets in the omnichannel mode, manage incoming and outgoing calls, and work with other queue items. In the
 
 agent desktop,
 
 the employee can read the messages posted on the feed and analytical KPI dashboards of a single employee or the whole team are available.
 





 Note.
 
 To allow the employees to receive incoming calls from the agent desktop, set up a connection between Creatio and your phone provider.
 




 The
 
 Agent desktop
 
 (
 [Fig. 1](#XREF_52095_205)
 ) section consists of the following areas:
 


* [The working area](#HT_section_agent_desktop_workspace) 


 of the agent
 
 (1) displays the list of records for processing.
* [The feed area](#HT_section_agent_desktop_channel) 

 (2) displays posts from your enterprise social network.
* [The analytics area](#HT_section_agent_desktop_analytics) 

 (3) displays aggregate data on agent performance.





 Fig. 1
 

 The
 
 Agent desktop
 
 section
 

![scr_section_agent_desktop_overview.png](/sites/default/files/documents/docs_en/product/bpm'online service enterprise/service enterprise/7.16.0/BPMonlineHelp/section_agent_desktop/scr_section_agent_desktop_overview.png)




 The working area of the agent
--------------------------------



 The working area of the contact center agent or helpdesk agent on the agent desktop is a number of tabs with the records that are displayed in the agent desktop according to the conditions of pre-configured queues.
 



 The agent desktop tabs are created automatically, based on the queue teams of which the current agent is a member. Each agent desktop tab corresponds to a system object regardless of the number of the configured queues. For example, all records coming from the “Case” type will be displayed in the
 
 Cases
 
 tab of the agent desktop.
 



 By default, the
 
 Cases
 
 tab displays incidents, service requests, claims, and complaints, that come from the
 
 Cases to be processed
 
 queue. These are unresolved requests.
 





 Note.
 
 You can set up custom agent desktop queues in the
 [Queues
 
 section](https://academy.creatio.com/documents?product=base&ver=7&id=1073) 
 .
 






 Note.
 
 Use the
 
 Agent desktop queues upload interval
 
 system setting to change the update cycle for agent desktop records.
 





 Agent desktop feed channel
-----------------------------



 Use the feed channel for prompt notification of the helpdesk agents or agents about noteworthy events of the company. The agent desktop feed displays posts and comments from a specific feed channel. Use the
 
 Agent desktop - Channel
 
 system setting to select this channel.
 




 Agent desktop dashboards
---------------------------



 The agent
 [desktop dashboard displays](https://academy.creatio.com/documents?product=base&ver=7&id=1236) 
 .  The agent desktop analytics consists of two tabs. One tab displays the agent’s personal achievements and the other tab displays the team's achievements. These dashboards display summary data for the current day.
 



 Manage records in the Agent Desktop
-------------------------------------



 The list of records displayed on the agent desktop tabs depends on the queue type, which can be "regular" or "blind."
 


### 
 Display records in regular queues



**Regular queues** 
 display lists of records and the agent can select which record to process. The order of the records depends on the sorting rules of the
 
 agent desktop
 
 records.
 


### 
 Display records in blind queues



**Blind queues** 
 display:
 


* The
 
 Next record
 
 button initiates the processing of the next record in the queue. The processing order depends on the sorting rules of the
 
 agent desktop
 
 records.
* The list of records for which the processing started, but has not been completed yet.



 Use the
 
 Maximum number of records in progress for a blind queue
 
 system setting to limit the maximum number of records that can be displayed in the list of a blind queue. By using this system setting, you can limit the number of cases in progress shown to the agent in order to increase the case resolution efficiency.
 



 By default, the
 
 Maximum number of records in progress for a blind queue
 
 system setting is set to “1”. Thus, the agent desktop working area shows either the
 
 Next record
 
 button or a single record if the processing of this record has not been completed.
 



 If you increase the value of this system setting, the agent will be able to continue working with the record in progress or take the next record in the queue for processing as long as the number of displayed records is not at maximum. When the number of displayed records reaches the maximum, the
 
 Next record
 
 button becomes unavailable.
 



 For example, the value of the
 
 Maximum number of records in progress for a blind queue
 
 system setting has been set to “3”.
 



 The agent who has started processing one or two cases on the agent desktop will see both the list of his cases in progress and the
 
 Next record
 
 button (
 [Fig. 1](#XREF_89594_85)
 ). The agent can choose to continue processing the cases in the list or take a new record.
 



 If the agent takes a third case, it will be added to the list in the agent desktop working area and the
 
 Next record
 
 button will be unavailable, so in order to be able to take another new case for processing, the agent must resolve at least one of the currently open cases.
 





 Fig. 1
 

 Blind queue example
 

![scr_section_agent_desktop_closed_queue.png](/sites/default/files/documents/docs_en/product/bpm'online service enterprise/service enterprise/7.16.0/BPMonlineHelp/section_agent_desktop/scr_section_agent_desktop_closed_queue.png)


### 



 Sort records on the agent desktop



 The records on the agent desktop tabs are sorted based on certain rules. These sorting rules are identical for both regular and blind queues.
 


* The records whose due date has been reached are displayed at the top of the list.
* These records are followed by more records from the existing queues.
 



 If multiple queues have been created for an object, then the records from a higher priority queue will be closer to the top of the list.
 



 If multiple queues with the same priority have been created for an object, their records will be sorted based on the internal sorting settings of the corresponding queues. Therefore, the records from multiple queues may take turns on the agent desktop. If the records which are coming from different queues should not be mixed in the list, create additional priorities in the
 
 Agent desktop queue priority
 
 and assign a separate priority for each queue specified for the object.
* The records in the queues are sorted based on the object columns first, and then – by the number of calls connected to each record (the less repeated calls there are, the higher the record's position in the list will be).





 Note.
 
 More information on how to sort queue records by object columns is available in a
 
[separate article](https://academy.creatio.com/documents?product=studio&ver=7&id=813) 

 .
 





