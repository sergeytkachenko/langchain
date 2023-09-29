


 The content of static queues is formed manually and is not updated automatically. The static queues can be used for cold calls to a predefined group of contacts to inform them about events.
 



 Let's look closer at an example of creating and populating the static queues for the cold calls to the new customers. To do this:
 


1. Go to the
 
 Queues
 
 section.
2. Open the
 
 Queues setup
 
 view and add a new element.
3. Specify the name of the queue on the new page, for example, “New customers”.
4. Select the priority for the queue. The queue priority influences the display order of the queue elements on the agent desktop.
 





 Note.
 
 Learn more about elements sorting order on the agent desktop from a
 
[separate article](/docs/7-17/user/service_tools/contact_center_tools/agent_desktop_setup/overview/general_agent_desktop_settings) 

 .
5. Select a system object in the
 
 Queue type
 
 field. In our case, it is “Contact”. You can customize queue objects in the
 
 Queue objects
 
 lookup by clicking the
 
 Queue sorting setup
 
 action in the
 
 Queues
 
 section. After saving the queue you cannot change its type.
 





 Note.
 
 The selected object defines the queue type - regular or blind.
6. Select the "In progress" queue status.
 





 Note.
 
 The agent desktop displays only active queues. The status of active queues is “In progress”. By default, the status is "Active".
7. Specify a pre-configured business process in the
 
 Process
 
 field.  The selected business process will be run each time an agent takes an element from the queue.
 





 Note.
 
 For queues by the “Contact” object, it is necessary to create a business process in Creatio on the agent desktop. To be able to use a process in a queue, add two global parameters to it: “queueelementId” and “entityRecordId” with the "Unique identifier” type. The record ID from the (
 
 Queue element
 
 object) is passed to the “queueelementId” parameter, and the contact/case/application record ID is passed to the “entityRecordId” parameter.
8. Select the
 
 Fill in manually
 
 option on the
 
 Queue population
 
 tab in the
 
 Queue population type
 
 fields group.
9. Go to the
 
 Queue population
 
 detail, to populate the queue. From the
 
 New
 
 button menu, select the
 
 New folder
 
 option and specify the pre-configured folder in the
 
 Contacts
 
 section for example, ”New customers”. As a result, the contacts, who are included in the selected folder will be added to the queue content. You can edit the content of the static queue by adding or deleting the elements manually. The agent desktop will display the queue content on the
 
 Contacts
 
 tab.
10. To form a list of agents to process the queue, go to the
 
 Team
 
 tab. Click the
 
 New
 
 button and select the required employees. The selected contacts can process the content of the queue from the agent desktop.
 





 Attention.
 
 Only those agents who have the
 
 Active
 
 checkbox selected on the
 
 Team
 
 tab can process the queues. By default, this checkbox is selected for all contacts on the detail. You can clear the checkbox for certain agents. In this case, the queue elements of the queue will not be displayed on the agent desktop for these agents.




