







 Use events for branching processes
-----------------------------------------



 To branch processes depending on an activated event, the
 
 Event-based gateway
 
 operator is used. Events used for process branching are placed on the gateway outgoing flows (Fig. 1).
 





 Fig. 1
 

 Using the event-based gateway
 



![scr_process_creation_designer_event_gateway_example.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_process_creation_designer_event_gateway_example.png)







 Example.
 
 After creating a contract, you need to send it for approval. The execution of a business process will depend on the approval results. Upon receiving the approval, the contract must be signed. If a contract wasn't approved, it must be sent back for revision.
 




 To create a contract, use the
 
 Open edit page
 
 element. Settings here are identical to the settings used when creating a new document.
 



 To send a contract for approval, you must use the
 
 Auto-generated page
 
 element. Working with the
 
 Read data
 
 element is covered in the
 [Auto-generated page
 
 process element](/docs/7-17/user/bpm_tools/process_elements_reference/user_actions/auto_generated_page/auto_generated_page_process_element)
 article. After the contract has been sent to approval, add the approval to the contract page. Use the
 
 Add data
 
 element to automatically add new system records.
 



 A schema with branching is displayed on Fig. 2.
 





 Fig. 2
 

 The contract approval process
 



![scr_process_creation_designer_process_with_events_contracts.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_process_creation_designer_process_with_events_contracts.png)





 To build a process branching, the outgoing flow of each branch has to be activated depending on the result:
 


1. Place the
 
 Event-based gateway
 
 operator after the "Add approval" action and connect them with a sequence flow.
2. Place the
 
 Wait for signal
 
 element after the gateway and connect them with a sequence flow.
3. Populate the
 
 Wait for signal
 
 element settings page if the contract has been approved (Fig. 3):
 





 Fig. 3
 

 Setting up the
 
 Wait for signal
 
 element for a contract to be approved
 



![scr_process_creation_designer_signal_for_visa.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_process_creation_designer_signal_for_visa.png)
4. In the
 
 Which type of signal is received?
 
 field, select “Object signal”.
5. Click the
 
 Record ID
 
 field to open the parameters window.
 


	1. Select the
	 
	 Add approval
	 
	 element on the
	 
	 Process elements
	 
	 tab.
	2. Double-click the
	 
	 Record ID
	 
	 parameter. The corresponding value will be added to the text field at the top of the parameter value window.
6. Click
 
 Save
 
 .
7. Specify the object to receive a signal from. For example, "Contract approval".
8. In the
 
 Which event should trigger the signal?
 
 field, set "Record modified".
9. Select the column whose event must activate the signal. For example, the "Status" column.
10. Specify the filter conditions that the modified record must meet. For the signal to activate after the approval and the previously created contract page to open, the contract status has to be "Approved".
11. Place one more
 
 Wait for signal
 
 element after the gateway and connect them with a sequence flow. This signal should activate when a contract has not been approved.
12. Populate the
 
 Wait for signal
 
 element setup area (Fig. 4): Settings are identical to the signal which is triggered after obtaining an approval, however you must specify “Status=Negative” in the filtering criteria.
 





 Fig. 4
 

 Setting up the
 
 Wait for signal
 
 element for a contract to be approved
 



![scr_process_creation_designer_signal_for_visa_cancel.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_process_creation_designer_signal_for_visa_cancel.png)
13. Add the
 
 Open edit page
 
 element after the “Contract approved” and “Send for revision” elements. If a contract has been approved, the previously created contract opens in which you must change the status to "Approved". If a contract was rejected, the previously created contract page will open for revision.
14. Save the process.
 





 Attention.
 
 The
 
 Event-based gateway
 
 operator requires the process to be published. All created processes are checked during the publication.








 Run a process automatically upon changes in Creatio
----------------------------------------------------------



 Business processes can start automatically, whenever a Creatio record is added, modified or deleted. To set up such a process, use the
 
 Signal
 
 element as the process start event. More information is available in the
 
[Signal
 
 start event](/docs/7-16/user/bpm_tools/process_elements_reference/events/signal/signal_start_event) 

 article.
 



 For example, a customer onboarding process can start automatically, each time a new customer account is added in Creatio.
 


1. To run a process automatically, based on changes in Creatio, add the
 
 Signal
 
 element as the process initial event (Fig. 5) and populate the
 
 Signal
 
 element setup area (
 
 Fig. 6
 
 ):
 


 Fig. 5
 

 A process with the
 
 Signal
 
 start event
 



![scr_chapter_process_designer_start_main_process_with_signal.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_start_main_process_with_signal.png)







 Fig. 6
 

 Configuring the
 
 Start
 
 signal parameters
 



![scr_chapter_process_designer_start_signal_param_main_process.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_start_signal_param_main_process.png)




	1. In the
	 
	 Which type of signal is received?
	 
	 field, select “Object signal”.
	2. In the
	 
	 Object
	 
	 field, select the object (section, detail or lookup), whose changes will automatically initiate the process. For example, to run a process in response to changes in the
	 
	 Accounts
	 
	 section, select the “Account” object.
	3. In the
	 
	 Which event should trigger the signal?
	 
	 field, select the type of event (adding, editing or deleting a record) in the chosen object that will automatically run the process. For example, to run the process each time a new account is added, select “Record added”.
	4. Specify any additional requirements to the record that must initiate the signal. For instance, to activate the signal only when adding an account of the “Customer” type, set the “Type = Customer” filter.
2. Save the process diagram.
 



 As a result, the process will launch automatically each time the corresponding changes occur in Creatio records. For example, a customer onboarding process can start automatically whenever a new account of the “Customer” type is added.








 Run a process from another process using signals
-------------------------------------------------------



 To run a process from another process using signals, add intermediate
 
[Throw signal](/docs/7-16/user/bpm_tools/process_elements_reference/events/throw_signal/throw_signal_intermediate_event)

 event to the parent process and have the triggered process start with a custom
 
[Signal](/docs/7-16/user/bpm_tools/process_elements_reference/events/signal/signal_start_event)

 event.
 



 For example, a “Preparation for webinar” business process must initiate a number of parallel independent business processes, such as sending reminders, collecting feedback, etc.
 


1. Add the
 
 Throw signal
 
 intermediate event element on the diagram of the business process that must trigger the associated processes. For example, associated processes must run after the “Confirm the webinar date” task is complete. Thus, a
 
 Throw signal
 
 event, (e.g.,“Webinar date confirmed”), must be added to the process flow after this task (Fig. 7).
 





 Fig. 7
 

 Placing the
 
 Throw signal
 
 event on the diagram of the parent business process
 



![scr_chapter_process_designer_prepare_for_webinar.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_prepare_for_webinar.png)
2. Populate the
 
 Which signal is generated?
 
 field of the
 
 Throw signal
 
 setup area with the name of the custom signal which will be generated. Make sure that different custom signals do not have matching texts. You can use any custom text, for example, use the “WebinarDateConfirmed” signal name (Fig. 8).
 





 Fig. 8
 


 Throw signal
 
 element setup area
 



![scr_chapter_process_designer_throw_signal_setup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_throw_signal_setup.png)
3. Add the start
 
 Signal
 
 event on the diagram of the triggered process (Fig. 9)
 





 Fig. 9
 

 Starting element of the process triggered by a custom signal
 



![scr_chapter_process_designer_email_reminder.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_email_reminder.png)
4. Set up the
 
 Signal
 
 element properties (Fig. 10):
 





 Fig. 10
 


 Signal
 
 element setup area
 



![scr_chapter_process_designer_start_signal_setup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_start_signal_setup.png)




	1. In the
	 
	 Which type of signal is received?
	 
	 , select “Custom signal”.
	2. In the
	 
	 Signal
	 
	 field, copy the name from the
	 
	 Throw signal
	 
	 element of the main process, e.g. “WebinarDateConfirmed”.
5. Save the process diagram.
 



 As a result, the associated processes will be run automatically upon generating a corresponding signal in another process.




 Run a process on a schedule
------------------------------



 You can run a business process once, on a specific date, using the
 
 Start timer
 
 element. More information is available in the
 
[Start timer
 
 event](/docs/7-16/user/bpm_tools/process_elements_reference/events/start_timer/start_timer_event_process_element) 

 article.
 



 For example, you can schedule preparation of a customer presentation for specific date and time.
 



 To set up a process that runs on specific date:
 


1. Add the
 
 Start timer
 
 event element on the process diagram as the initial event (Fig. 11) and populate the
 
 Start timer
 
 element setup area (Fig. 12):
 


 Fig. 11
 

 Running a business process on specific date
 



![scr_chapter_process_designer_running_process_once.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_running_process_once.png)







 Fig. 12
 


 Start timer
 
 element setup area for running the process on specific date
 



![scr_chapter_process_designer_running_process_once_setup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_running_process_once_setup.png)




	1. In the
	 
	 Frequency of process start
	 
	 field, select “Once”.
	2. In the
	 
	 Start date time
	 
	 field, select the date and time when the process should run.
	3. Select the
	 
	 Repeat on misfire
	 
	 checkbox in the
	 
	 Additional settings
	 
	 section to ensure that the business process launches even if the
	 
	 Start timer
	 
	 element cannot be triggered at the intended time, e.g., due to a server downtime. In this case, the process will run automatically at the nearest time available after the intended time has passed.
	4. Select the needed time zone in the
	 
	 Time zone
	 
	 field. The process will run according to the time in that time zone.
2. Save the process diagram.
 



 As a result, the process will run automatically at the time specified in the parameters of the
 
 Start timer
 
 element.








 Run a process weekly
---------------------------



 You can set up a process that starts automatically, on a regular weekly basis, on the specified day and at the specified time.
 



 For example, a business process can send reminders about a weekly webinar held regularly on Fridays in October.
 



 To set up a process that runs automatically on a weekly basis:
 


1. Add the
 
[Start timer](/docs/7-16/user/bpm_tools/process_elements_reference/events/start_timer/start_timer_event_process_element)

 event element on the process diagram as the initial event
 [(Fig. 13)](#XREF_14360_Fig_25_Running_a)
 and populate the
 
 Start timer
 
 element setup area (
 
 Fig. 14
 
 ):
 


 Fig. 13
 

 Run a business process weekly
 



![scr_chapter_process_designer_run_weekly_timer.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_run_weekly_timer.png)







 Fig. 14
 


 Start timer
 
 element setup area for running the process weekly
 



![scr_chapter_process_designer_run_weekly_timer_setup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_run_weekly_timer_setup.png)




	1. In the
	 
	 Frequency of process start
	 
	 field, select “Week”.
	2. In the
	 
	 Process start time
	 
	 field, select the time when the process should run.
	3. In the
	 
	 Which days of the week to run?
	 
	 field, select the days of the week on which the process should run.
	4. In the
	 
	 Timer validity
	 
	 fields, specify the period of time during which the process run schedule will repeat. For example, if you need to run your process during October, select 10/1/2018 in the
	 
	 Start date and time
	 
	 field and 10/31/2018 in the
	 
	 End date and time
	 
	 field.
	5. Select the
	 
	 Repeat on misfire
	 
	 checkbox in the
	 
	 Additional settings
	 
	 section to ensure your business process launches even if the
	 
	 Start timer
	 
	 element cannot be triggered at the intended time, e.g., due to a server downtime. In this case, the process will run automatically at the nearest time available after the intended time has passed.
	6. Select the needed time zone in the
	 
	 Time zone
	 
	 field. The process will repeat according to date and time in that time zone.
2. Save the process diagram.
 



 As a result, the process will run automatically, according to the specified custom schedule within the specified period. For example, the process will run every Friday in October, at 9:45 AM, Central Time.








 Run a process on a custom schedule (using cron expressions)
------------------------------------------------------------------



 You can set up custom schedules for running business processes using cron-expressions in Creatio. Cron-expressions support flexible long and short-term schedules and use the cron syntax (digits, words, and/or special characters in a specific order). Learn more about syntax of cron-expressions in
 
[QUARTZ documentation](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-06.html) 

 .
 



 For example, a business process must run at a certain time on the 15th day of every month during October, November and December.
 



 To run a process on a custom schedule:
 


1. Add the
 
[Start timer](/docs/7-16/user/bpm_tools/process_elements_reference/events/start_timer/start_timer_event_process_element)

 on the process diagram (Fig. 15). Set up the element properties (Fig. 16):
 


 Fig. 15
 
 Run a business process on a custom schedule
 



![scr_chapter_process_designer_run_custom_schedule.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_run_custom_schedule.png)







 Fig. 16
 

 Start timer
 
 element setup area for running the process according to custom schedule
 



![scr_chapter_process_designer_start_timer_other_frequency.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_start_timer_other_frequency.png)




	1. In the
	 
	 Frequency of process start
	 
	 field, select “Other frequency”.
	2. In the
	 
	 Cron expression
	 
	 field, type in the cron-expression implementing your custom schedule. If the cron-expression is correct, you will see the time/date of the process launch in the traditional format under the
	 
	 Cron-expression
	 
	 field. For example, use the “0 15 10 15 \* ?” expression to run the process at 10:15am on the 15th day of every month. Learn more about using cron expressions in
	 
	[QUARTZ documentation.](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/tutorial-lesson-06.html)
	3. In the
	 
	 Timer validity
	 
	 fields, specify the period of time during which the process run schedule will repeat. For example, if you need to run your process October through December 2018, select 10/1/2018 in the
	 
	 Start date and time
	 
	 field and 10/31/2018 in the
	 
	 End date and time
	 
	 field.
	4. Select the
	 
	 Repeat on misfire
	 
	 checkbox in the
	 
	 Additional settings
	 
	 section to ensure your business process launches even if the
	 
	 Start timer
	 
	 element cannot be triggered at the intended time, e.g., due to a server downtime. In this case, the process will run automatically at the nearest time available after the intended time has passed.
	5. Select the needed time zone in the
	 
	 Time zone
	 
	 field. The process will run according to the time in that time zone.
2. Save the process diagram.
 



 As a result, the process will run automatically, according to the specified custom schedule within the specified period. For example, the process will run on the 15th day of every month, October through December 2018, at 10:15 AM, Central Time.








 Run a process using a message
------------------------------------



 Use intermediate messages to synchronize independent flows within one process. You can set up a business process that stops at a certain point and waits for the corresponding message before activating its next element.
 



 For example, a business process must wait until invoice payment has been received before initiating a task to dispatch the goods.
 



 To set up a process that resumes using a message:
 


1. Add the two intermediate message events on the diagram (Fig. 17).
 


	1. Add
	 
	[Throw message
	 
	 event](/docs/7-16/user/bpm_tools/process_elements_reference/events/throw_message/throw_message_intermediate_event_process_element) 
	
	 after the process task which is supposed to trigger the event.
	2. Add
	 
	[Wait for message
	 
	 event](/docs/7-16/user/bpm_tools/process_elements_reference/events/wait_for_message/wait_for_message_intermediate_event_process_element) 
	
	 before the process task which is supposed to be executed after the event.
	 
	
	
	
	
	
	 Fig. 17
	 
	 Resuming a process using a message
	 
	
	
	
	![scr_chapter_process_designer_resume_using_message.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_resume_using_message.png)
2. In the
 
 Throw message
 
 element setup area (Fig. 18), specify the custom message in the
 
 Which message to generate?
 
 field. You can use any custom text, for example, “InvoicePaid”.
 





 Fig. 18
 


 Throw message
 
 element setup area
 



![scr_chapter_process_designer_throw-message-setup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_throw-message-setup.png)
3. Populate the
 
 Wait for message
 
 element setup area (Fig. 19):
 





 Fig. 19
 


 Wait for message
 
 element setup area
 



![scr_chapter_process_designer_wait_for_message_setup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_events/scr_chapter_process_designer_wait_for_message_setup.png)




	1. In the
	 
	 Which message should be received?
	 
	 field, copy the message from the
	 
	 Throw message
	 
	 element.
	2. If you select the
	 
	 Run following elements in the background
	 
	 checkbox, all the following system operations of the process will be performed in the background, without displaying the loading mask.
4. Save the process diagram.
 



 As a result, the process will stop at the
 
 Wait for message
 
 element and will be resumed only after the message specified in the
 
 Throw message
 
 element is caught




