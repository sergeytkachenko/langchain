




 Example.
 
 Create the following business process: when adding a new comment to the message in the feed, an email is sent to the author of this message.
 




 Business process diagram (Fig. 1) elements:
 


1. Incoming signal for adding a message comment – when a new comment is added, the signal is activated and the business process is started.
2. Reading the Id of the added comment – reading the new comment data for use in the email template.
3. Reading the parent message - reading the data of the main message for use in the email template.
4. Sending email – an email to a contact with the selected text and new comment data.
 





 Fig. 1
 

 The "Comment to a message in the feed notification" business process
 

![scr_process_creation_designer_case_feed_comment.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_case_feed_comment.png)



 To do this:
 


1. Place on the schema the
 
 Signal
 
 element of the
 
 Initial events
 
 group — "Comment added". The element will be activated when a comment is added to the feed.
2. Set up the signal parameters (Fig. 2).
 


 Fig. 2
 
 The "Comment added" element properties
 

![scr_process_creation_designer_case_feedcomment_starting_signal_settings.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_case_feedcomment_starting_signal_settings.png)


	1. In the
	 
	 Object
	 
	 field, set "Message/comment".
	2. In the
	 
	 What event should happen?
	 
	 field, select "Add record".
	3. In the
	 
	 Added record must correspond to conditions
	 
	 field, select "Parent message populated.
3. Add two
 
 Read data
 
 elements of the
 
 System actions
 
 group.
	1. The "Read comment data" element will read data from the added record in the feed. Set up the element parameters (Fig. 3).
		* In the
		 
		 Which data read mode to use?
		 
		 field, select “Read the first record in the selection”.
		* In the
		 
		 Which object to read data from?
		 
		 field, select ”Message/comment”.
		* In the
		 
		 How to filter records?
		 
		 area, set the filter “Id = Comment added. Unique record Id”. To do this, click <Add condition>, select the “Id” column, then in the appeared menu, select
		 
		 Compare with parameter
		 
		 . In the opened window, select the
		 
		 Record ID
		 
		 parameter of the "Comment added" element.
		* In the
		 
		 Which column values to read?
		 
		 , select "All columns".
		 
		
		
		
		
		
		 Fig. 3
		 
		 The "Read comment title" element properties
		 
		
		![scr_process_creation_designer_case_feedcomment_read_comment.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_case_feedcomment_read_comment.png)
	2. The "Read primary message" element will read data of the message to which a comment has been left. Set up the element parameters (Fig. 4).
		* In the
		 
		 Which data read mode to use?
		 
		 field, select “Read the first record in the selection”.
		* In the
		 
		 Which object to read data from?
		 
		 field, select ”Message/comment”.
		* In the
		 
		 How to filter records
		 
		 area, set up filter "id = Read comment data.First element of the resulting collection.Parent message". To do this, click <Add condition>, select the “Id” column, then in the appeared menu, select
		 
		 Compare with parameter
		 
		 . In the opened window, select the
		 
		 Parent message
		 
		 parameter of the "read comment data" element.
		* In the
		 
		 Which column values to read?
		 
		 , select "All columns".
		 
		
		
		
		
		
		 Fig. 4
		 
		 The "Read primary message" element properties
		 
		
		![scr_process_creation_designer_case_feedcomment_read_mainpost.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_case_feedcomment_read_mainpost.png)
4. Add the “Send e-mail” element of the
 
 System actions
 
 group and set the following parameters (Fig. 5):
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
	 
	 Contact
	 
	 >
	 
	 Process parameter
	 
	 , select the
	 
	 Read contact data
	 
	 element, and the
	 
	 Email
	 
	 parameter.
	3. In the
	 
	 What is the message?
	 
	 field select “Template message”.
	4. Select the existing template in the
	 
	 Template message
	 
	 field. The
	 
	 Subject
	 
	 field is populated automatically.
	5. Select “Send email automatically” in the
	 
	 How is the message sent?
	 
	 field.
	 
	
	
	
	
	
	 Fig. 5
	 
	 The "Send email" element properties
	 
	
	![scr_process_creation_designer_case_feedcomment_send_email.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_case_feedcomment_send_email.png)
5. After creating the process elements, connect each element with the next one by dragging the
 ![icn_process_elements_connection_straight00020.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/icn_process_elements_connection_straight00020.png)
 element in the upper right corner of the selected process element.
6. Save the created business process.
   

 As a result of the new business process, when adding a new comment to the message in the feed, an email is sent to the author of this message.




