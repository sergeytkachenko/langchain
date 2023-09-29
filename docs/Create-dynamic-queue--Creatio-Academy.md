


 Dynamic queues are populated automatically. The queue will be populated with records that match a specific filter condition. For example, dynamic queues can be used to process new cases that have not yet been assigned a responsible.
 



 Let's take a closer look at how to create and populate dynamic case queues. To create a dynamic queue for cases where the resolution deadline is today or falls within the nearest three days: To do this:
 


1. Go to the
 
 Queues
 
 section.
2. Open the
 
 Queues setup
 
 view and add a new element.
3. Specify the name of the queue in the opened window.
4. Select the priority for the queue. The queue priority influences the display order of the queue elements on the agent desktop.
 





 Note.
 
 Learn more about elements sorting order on the agent desktop from a
 [separate article](https://academy.creatio.com/documents?product=studio&ver=7&id=804)
 .
5. Select a system object in the
 
 Queue type
 
 field. In our case, it is “Case”. You can customize queue objects in the
 
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
7. Select a business process in the
 
 Process
 
 field. The selected business process will be run each time an agent takes an element from the queue. Select the “Agent desktop: Queue cases processing” business process for cases.
 





 Note.
 
 To be able to use a process in a queue, add two global parameters to it: “queueelementId” and “entityRecordId” with the "Unique identifier” type. The record ID from the (
 
 Queue element
 
 object) is passed to the “queueelementId” parameter, and the contact/case/application record ID is passed to the “entityRecordId” parameter.
8. Select the
 
 Automatically by filter conditions
 
 option in the
 
 Queue population type
 
 field group on the
 
 Queue population
 
 tab.
9. Specify the filter conditions in the filter area.
 


	1. Click the
	 
	 Add condition
	 
	 link and select the
	 
	 Resolution time
	 
	 column in the opened window. Select the value of the condition: "Day → Today”(
	 [Fig. 1](#XREF_16900_156)
	 ).
	 
	
	
	
	
	
	 Fig. 1
	 
	
	 Setting up the "Resolution time = Today” filter condition
	 
	
	![scr_section_supervisor_filter_today.png](/sites/default/files/documents/docs_en/product/bpm'online service enterprise/service enterprise/7.16.0/BPMonlineHelp/section_supervisor/scr_section_supervisor_filter_today.png)
	2. Add another filter condition: "Resolution time = Following 3 days" (
	 [Fig. 2](#XREF_60106_157_3) 
	 ).
	 
	
	
	
	
	
	 Fig. 2
	 
	
	 Setting up the "Resolution time =Following 3 days” filter condition
	 
	
	![scr_section_supervisor_filter_3_days.png](/sites/default/files/documents/docs_en/product/bpm'online service enterprise/service enterprise/7.16.0/BPMonlineHelp/section_supervisor/scr_section_supervisor_filter_3_days.png)
	3. Select the "OR" logical operator (
	 [Fig. 3](#XREF_79774_158)
	 ).
	 
	
	
	
	
	
	 Fig. 3
	 
	
	 Selecting the "OR" logical operator
	 
	
	![scr_section_supervisor_filter_set_or.png](/sites/default/files/documents/docs_en/product/bpm'online service enterprise/service enterprise/7.16.0/BPMonlineHelp/section_supervisor/scr_section_supervisor_filter_set_or.png)


 Attention.
 
 If you do not specify the filter condition for a dynamic queue, the queue elements will not be displayed on the agent desktop.
10. To form a list of agents to process objects from the queue, go to the
 
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
11. Save and close the page.
 



 To view the content of the queue, select the
 
 Fill queues
 
 action from the action menu of the
 
 Queues
 
 section. Open the queue record. All applications in the current queue will be displayed on the
 
 Queue population
 
 detail (
 [Fig. 4](#XREF_94879_159)
 ). The data is available in read-only mode.
 





 Fig. 4
 

 Dynamic queue page
 

![scr_section_supervisor_dynamic_page_fill.png](/sites/default/files/documents/docs_en/product/bpm'online service enterprise/service enterprise/7.16.0/BPMonlineHelp/section_supervisor/scr_section_supervisor_dynamic_page_fill.png)




