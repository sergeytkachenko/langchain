




 Example.
 
 Create the following business process: an email is sent to an employee that was added to the list of participants in the activity.
 




 Business process diagram (Fig. 1) elements:
 


1. Incoming signal for adding an activity participant - when a new participant is added to the activity, the signal is activated and the business process is started.
2. Reading the Id of the added activity participant record – getting about the new activity participant information for later use in the process.
3. Reading the activity header – retrieving activity data that will be used in the preconfigured template.
4. Sending email – notifying the contact that they were added to the activity.
 





 Fig. 1
 
 The "Employees added as activity participants notification" business process
 

![scr_process_creation_designer_case_activity_participant.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_case_activity_participant.png)



 To do this:
 


1. Place the
 
 Signal
 
 element of the
 
 Initial events
 
 group on the schema — "Participant added". The element will be activated when a contact is added on the
 
 Participants
 
 detail of the activity.
2. Set up the signal parameters:
	1. In the
	 
	 Object
	 
	 field, set "Activity participant".
	2. In the
	 
	 What event should happen?
	 
	 field, select "Add record".
3. Add two
 
 Read data
 
 elements of the
 
 System actions
 
 group.
4. Set up the "Read activity participant" element parameters to read data from the activity participant added record (Fig. 2):
	1. In the
	 
	 Which data read mode to use?
	 
	 field, select “Read the first record in the selection”.
	2. In the
	 
	 Which object to read data from?
	 
	 field, select “Activity participant”.
	3. In the
	 
	 How to filter records?
	 
	 area, set the filter “Id = Participant added.Record ID". To do this, click <Add condition>, select the “Id” column, then in the appeared menu, select
	 
	 Compare with parameter
	 
	 . In the opened window, select the
	 
	 Record ID
	 
	 parameter of the "Participant added" element.
	 
	
	
	
	
	
	 Fig. 2
	 
	 The "Read activity participant" element properties
	 
	
	![scr_process_creation_designer_case_activityparticipant_read_participant.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_case_activityparticipant_read_participant.png)
5. Set up the "Read activity title" element parameters to read the activity title, to which a participant has been added (Fig. 3):
 


 Fig. 3
 
 The "Read activity title" element properties
 

![scr_process_creation_designer_case_activityparticipant_read_activity_title.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_case_activityparticipant_read_activity_title.png)


	1. In the
	 
	 Which data read mode to use?
	 
	 field, select “Read the first record in the selection”.
	2. In the
	 
	 Which object to rad data from?
	 
	 field, select “Activity”.
	3. In the
	 
	 How to filter records
	 
	 area, set up filter "id = Read activity participant.First element of the resulting collection.Activity". To do this, click <Add condition>, select the “Id” column, then in the appeared menu, select
	 
	 Compare with parameter
	 
	 . In the opened window, select the "Activity" parameter of the "Read activity participant" element.
	4. In the
	 
	 Which column values should be read?
	 
	 field, select “Only selected columns" and select the “Title” column.
6. Add the “Send e-mail” element of the
 
 System actions
 
 group and set the following parameters (Fig. 4):
	1. In the
	 
	 From
	 
	 field, specify the return address in the message. To do this, select
	 
	 Select from lookup
	 
	 in the parameter value menu, then in the
	 
	 Synchronization with mailbox settings
	 
	 lookup, select one of the configured email accounts.
	2. In the
	 
	 To
	 
	 field, specify the email of the recipient. In the parameter value menu, click the
	 
	 Process element
	 
	 , select the
	 
	 Read contact data
	 
	 element, and the
	 
	 Email
	 
	 parameter.
	3. In the
	 
	 What is the message?
	 
	 field, select “Template message”.
7. Select the existing template in the
 
 Template message
 
 field. The
 
 Subject
 
 field is populated automatically.
8. Select “Send email automatically” in the
 
 How is the message sent?
 
 field.
 





 Fig. 4
 
 The "Send email" element properties
 

![scr_process_creation_designer_case_activityparticipant_send_email.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_case_activityparticipant_send_email.png)
9. After creating the process elements, connect each element with the next one by dragging the
 ![icn_process_elements_connection_straight00014.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/icn_process_elements_connection_straight00014.png)
 element in the upper right corner of the selected process element.
10. Save the created business process.
   

 As a result of the business process, an email is sent to an employee that was added to the list of participants in the activity.




