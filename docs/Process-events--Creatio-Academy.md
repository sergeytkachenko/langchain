


 In Creatio, you can create business processes that launch automatically on specific conditions. There are several ways to implement this, depending on the business task:
 





| 
 Business task
  | 
 Automatic launch conditions
  | 
 Implementation in process designer
  |
| --- | --- | --- |
| 
 Automatically launch customer onboarding process
  | 
 The process runs automatically whenever a new customer account is added in Creatio
  | 
 The process initial event is
 [Signal](/docs/7-16/user/bpm_tools/process_elements_reference/events/signal/signal_start_event)
 in the “Object signal mode”. The signal initiates a new business process instance whenever a new record is added in the
 
 Accounts
 
 section.
  |
| 
 Automatically send a “Thank you” email to the customer when their invoice gets paid
  | 
 The process runs automatically whenever an invoice payment status changes
  | 
 The process initial event is
 [Signal](/docs/7-16/user/bpm_tools/process_elements_reference/events/signal/signal_start_event)
 in the “Object signal mode”. The signal initiates a new business process instance whenever a record in the
 
 Invoices
 
 section is modified and the value in its
 
 Payment status
 
 field changes to “Paid”.
  |
| 
 Automatically update the permissions when deleting an employee from a folder
  | 
 The process runs automatically whenever the connection between a folder and a corresponding contact is deleted
  | 
 The process initial event is
 [Signal](/docs/7-16/user/bpm_tools/process_elements_reference/events/signal/signal_start_event)
 in the “Object signal mode”. The signal initiates a new business process instance whenever a specific contact record is deleted from the “Employee in folder” object.
  |
| 
 Automatically begin preparing for an event on specific date
  | 
 The process runs automatically, on specific date at specific time
  | 
 The process initial event is
 [Start timer](/docs/7-16/user/bpm_tools/process_elements_reference/events/start_timer/start_timer_event_process_element)
 in the “Once” mode. The timer initiates a new business process instance on the specified date and time.
  |
| 
 Automatically send reminders about a regular (e.g., weekly) event
  | 
 The process runs automatically at regular intervals
  | 
 The process initial event is
 [Start timer](/docs/7-16/user/bpm_tools/process_elements_reference/events/start_timer/start_timer_event_process_element)
 in the “Week” mode. The timer initiates a new business process instance on the specified weekdays at specified time.
  |
| 
 Send notifications about an event (e.g., webinar) automatically, whenever preparations to it are complete in a different business process
  | 
 The process runs automatically, whenever a different process (e.g., “Preparation for webinar”) triggers it
  | 
 The “Sending reminder” process initial event is
 [Signal](/docs/7-16/user/bpm_tools/process_elements_reference/events/signal/signal_start_event)
 in the “Custom signal” mode. The process runs whenever the “Preparation for webinar” process generates the corresponding signal.
  |
| 
 Automatically start the “Meeting with customer” business process for the customer from the “Corporate sale” process
  | 
 The “Meeting with customer” process runs automatically as an action of the “Corporate sale” process
  | 
 The “Corporate sale” process contains a
 [Sub-process
 
 element](/docs/7-16/user/bpm_tools/process_elements_reference/sub_processes/sub_process/sub_process_element) 
 with the “Meeting with customer” process specified in the
 
 Which process to run?
 
 field.
  |
| 
 Automatically start the “Qualification” business process as part of the lead management case workflow
  | 
 The process runs automatically when a user advances to a specific case stage (e.g., “Qualification”)
  | 
 The “Qualification” stage of lead management
 [case](/docs/7-16/user/bpm_tools/dynamic_case_setup/case_designer_workflows/overview/case_designer#HT_chapter_case_designer) 
 includes a
 Sub-process
 
 case element
 . “Qualification” business process is specified in the
 
 Which process to run?
 
 field.
  |








 Check Creatio marketplace for free business process templates (Fig. 1, Fig. 2, Fig. 3, Fig. 4, Fig. 5) illustrating the examples of running processes using events. Click
 [here](https://marketplace.bpmonline.com/template/business-processes-start-events) 
 to download the template.
 



 After
 [installing the marketplace template](https://academy.bpmonline.com/documents?product=studio&ver=7&id=1835) 
 , go to the
 
 Process library
 
 section, select the “
 **Start events in business processes** 
 ” process and click
 
 Open
 
 to view its diagram. Select a start event on the diagram to check its settings.
 




 Fig. 1
 
 Example of a business process that runs automatically on adding a new record in Creatio
 

![chapter_process_principles_template_events_new_rec.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_events/chapter_process_principles_template_events_new_rec.png)




 Fig. 2
 
 Example of a business process that runs automatically on modifying a Creatio record
 

![chapter_process_principles_template_events_modified_rec.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_events/chapter_process_principles_template_events_modified_rec.png)




 Fig. 3
 
 Example of a business process that runs automatically, on the specific day
 

![chapter_process_principles_template_events_specific_date.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_events/chapter_process_principles_template_events_specific_date.png)




 Fig. 4
 
 Example of a business process that runs automatically, according to schedule
 

![chapter_process_principles_template_events_weekly.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_events/chapter_process_principles_template_events_weekly.png)




 Fig. 5
 
 Example of a business process that runs automatically, according to a CRON expression
 

![chapter_process_principles_template_events_cron.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_events/chapter_process_principles_template_events_cron.png)



 There are thus two general ways of setting up business processes that run automatically:
 


* using initial events, such as
 
 Signal
 
 and
 
 Start timer
* using the
 
 Sub-process
 
 element in dynamic cases and BPMN processes.





 Use start events to run business processes
----------------------------------------------



 An “initial event” is the first element on a business process diagram. These elements determine how the business process is launched. Before the initial event is triggered, the business process is inactive: it will not execute any logic or receive signals (except for the signals that activate the start event). Each time a start event is triggered, a new process instance is created in the
 
 Process Log
 
 .
 



 Using different types of events, you can set up business processes that will run automatically upon changes in Creatio records, when another process broadcasts a system-wide signal, or at the specified time.
 



 Run business processes on record changes
------------------------------------------



 Any change in Creatio data results in adding, modifying or deleting records. Use the
 [Signal
 
 start event](/docs/7-16/user/bpm_tools/process_elements_reference/events/signal/signal_start_event) 

 in the
 **“object signal”** 
 mode to run automatically when such changes occur in Creatio.
 



 The Id of the record that triggered the process will be passed to the parameters of the
 
 Signal
 
 start event. Read more about it in the
 [“Use events in a business process”](/docs/node/1613/%26#9;) 
 article.
 



 Run business processes on a system-wide signal
------------------------------------------------



 A business process can broadcast a system-wide signal via the
 [Throw signal
 
 intermediate event](/docs/7-16/user/bpm_tools/process_elements_reference/events/throw_signal/throw_signal_intermediate_event) 
 . Use the
 [Signal
 
 start event](/docs/7-16/user/bpm_tools/process_elements_reference/events/signal/signal_start_event) 
 in the
 **“custom signal”** 
 mode
 
 if you want your process to react to such signals.
 



 The process where the signal is generated is not otherwise connected with the processes that are triggered by that signal (e.g., these processes cannot exchange parameter values). When business processes are run from other processes or cases, the logic of the automatic launch is defined by the parent process or the case.
 



 Read more about using custom signals in the
 “How to run a process from another process using signals”
 article.
 



 Run business processes on timer
---------------------------------



 Use the
 
 Start timer
 
 event to run a business process automatically at the specified time.
 



 You can run business processes once, on certain date and time. Read more about configuring the timer for this case in the
 [“Use events in a business process”](/docs/node/1613/%26#9;) 
 article. You can run business processes regularly, according to schedule. Read more about configuring the timer for this case in the
 “How to run a process weekly”
 article.
 



 You can configure your custom logic for a schedule using cron expressions and run the business process accordingly. Read more about configuring the timer for this case in the
 “How to run a process according to custom schedule (cron expression)”
 article.
 





 Run sub-processes from a parent process
-------------------------------------------



 Business processes can be executed as part of other process or case via the
 [Sub-process
 
 element.](/docs/7-16/user/bpm_tools/process_elements_reference/sub_processes/sub_process/sub_process_element) 




 Running business processes automatically as sub-processes from other Creatio processes has the following specifics:
 


* Sub-processes run as separate instances, but are connected to the corresponding instance of the parent process or case. They can exchange parameter values, e.g., receive input from the parent process and return their execution result. Read more about exchanging parameter values between a sub-process and its parent process from the
 “How to obtain a sub-process execution result”
 article.
* When business processes are run from other processes or cases, the logic of the automatic launch is defined by the parent process or the case.
* Using sub-processes enables running processes automatically, with custom parameters that can be populated in the corresponding
 
 Process parameters
 
 block of the
 
 Sub-process
 
 element setup area.




