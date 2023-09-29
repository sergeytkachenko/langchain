


 Let's take a look at the typical procedure to process cases via the agent desktop using a blind queue. When an employee takes a case from the queue, the “Processing order in Agent desktop queue” business process is run.
 





 Note.
 
 You can set up another business process to handle your cases.
 




 To start working on a case from a regular queue:
 


1. On the corresponding tab of the agent desktop, click the
 
 Next record
 
 button (
 [Fig. 1](#XREF_66041_88)
 ).
 
 When an agent takes a case, other agents will not be able to process the case on the agent desktop.
 





 Fig. 1
 

 Taking a case from a regular queue
 

![Agent desktop next record button](/docs/sites/en/files/2020-12/scr_section_agent_desktop_next_record_btn.png)



 As a result, the page of the case to process next will open. The algorithm used to select a case takes into account the queue priorities and inner sorting rules of a given queue. (
 [Fig. 2](#XREF_33507_138)
 ).
 





 Note.
 
 Learn more about elements sorting order on the agent desktop from a
 
separate article

 .
 




 On the opened case page:
 


	* The value in the
	 
	 Status
	 
	 field is changed to “In progress”
	* The agent who took the case is specified as the assignee
	* The
	 
	 Actual response time
	 
	 field is filled in with the current date.


 Fig. 2
 


 — Page of the case in progress
 

![Agent desktop case page](/docs/sites/en/files/2020-12/scr_section_agent_desktop_case_page.png)
2. Perform one of the following actions:
	* To process the case, change its status. For example, specify the “Resolved” status.
	 
	 After you save the page, the
	 
	 Agent desktop
	 
	 section will be displayed again. The processed case will be removed from the queue.
	* To postpone processing the case to another specific time, click the
	 
	 Postpone till
	 
	 button and enter the date and the time.
	 
	 Click the
	 
	 Submit
	 
	 button to return to the agent desktop. The case will not be displayed on the agent desktop until the specified processing time comes. At the scheduled time, the case will be displayed on the agent desktop tab only for the agent who has started handling the case. Along with this, the
	 
	 Next record
	 
	 button will be available or unavailable based on the maximum number of cases that can be assigned with the “In progress” status simultaneously for the blind queue. This value is specified in the
	 
	 Maximum number of records in progress for a closed queue
	 
	 system setting.
	* To put off processing the case, click the
	 
	 Re-queue
	 
	 button.
	 
	 The
	 
	 Agent desktop
	 
	 section will be displayed again. The case  will be placed at the end of the queue regardless of the record sorting rules of this queue. Time for processing such case will come after having processed the cases which are on the higher positions in the queue.
	* To cancel processing the case, click the
	 
	 Cancel
	 
	 button.
	 
	 The
	 
	 Agent desktop
	 
	 section will be displayed again showing the case which has been canceled. Along with this, the
	 
	 Next record
	 
	 button will be available or unavailable based on the maximum number of cases that can be assigned with the “In progress” status simultaneously for the blind queue. This value is specified in the
	 
	 Maximum number of records in progress for a closed queue
	 
	 system setting.


 Note.
 
 The way the records from a blind queue are displayed on the agent desktop is described in a
 
separate article

 .




