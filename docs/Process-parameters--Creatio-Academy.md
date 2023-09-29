


 Every process task requires some form of input, e. g, the date and time of a meeting, task assignee, customer’s contact, etc. Also, it is often necessary to exchange data between elements within the same business process (e. g., sending an email to the same contact that was specified in the meeting), as well as between different processes (e. g., branching a process depending on the result of its sub-process).
 



 The following table outlines common business tasks from the standpoint of process execution mechanisms in Creatio:
 





| 
 Business task
  | 
 Creatio task
  | 
 Process task
  |
| --- | --- | --- |
| 
 Schedule a task and make it easily identifiable in the calendar
  | 
 Create a new record in the
 
 Activities
 
 section with a certain value in the
 
 Subject
 
 field
  | 
 Manually enter the title of the task that must be created as the value of the
 
 What should be done?
 
 parameter of the
 [Perform task
 
 element](/docs/7-17/user/bpm_tools/process_elements_reference/user_actions/perform_task/task_process_element) 
 .
  |
| 
 Assign a task to the user who started the process
  | 
 The
 
 Owner
 
 field of the record in the
 
 Activities
 
 section should be populated with the current user contact
  | 
 Set the “Current user contact” variable as the value of the
 
 Who performs the task?
 
 parameter of the
 
 Perform task
 
 element.
  |
| 
 Email the meeting contact immediately after the meeting has ended
  | 
 Create a new email whose
 
 To
 
 field will contain the email address of a contact who was specified in the
 
 Contact
 
 field of the meeting activity
  | 
 The
 
 To
 
 parameter of the
 [Send email
 
 element](/docs/7-17/user/bpm_tools/process_elements_reference/user_actions/send_email/send_email_process_element) 
 must have the same value as the
 
 Contact
 
 parameter of the
 
 Perform task
 
 element.
  |






 Example.
 
 Check Creatio marketplace for free business process templates (Fig. 1, Fig. 2, Fig. 3, Fig. 4, Fig. 5) illustrating the examples of using process parameters.
 [Download the template](https://marketplace.creatio.com/template/business-processes-parameters) 
 .
 



 After you
 [install the template](/docs/7-18/user/customization_tools/marketplace_applications/install_applications_from_the_marketplace) 
 , two new processes will appear in the
 
 Process library
 
 section: “
 **Call a client** 
 ” and “
 **CEO review** 
 ” processes. Select a process and click
 
 Open
 
 to view its diagram. The business process examples mentioned in this article will be available in these two processes.
 






 Fig. 1
 
 Obtain the parameter value from another parameter
 

![chapter_process_principles_template_parameters_map_from_signal.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_parameters/chapter_process_principles_template_parameters_map_from_signal.png)





 Fig. 2
 
 Specify a system variable (current user contact) as the parameter value
 

![chapter_process_principles_template_parameters_current_user.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_parameters/chapter_process_principles_template_parameters_current_user.png)





 Fig. 3
 
 Obtain the parameter value from a record created as part of the process
 

![chapter_process_principles_template_parameters_created_record.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_parameters/chapter_process_principles_template_parameters_created_record.png)





 Fig. 4
 
 Exchange parameter values between the sub-process and the parent process
 

![chapter_process_principles_template_parameters_of_subprocess.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_parameters/chapter_process_principles_template_parameters_of_subprocess.png)





 Fig. 5
 
 Diagram of the “CEO review” sub-process
 

![chapter_process_principles_template_parameters_subprocess_diagram.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_parameters/chapter_process_principles_template_parameters_subprocess_diagram.png)



 Creatio uses
 **parameters** 
 to solve the aforementioned process tasks.
 



 Parameters
------------



 Parameters are similar to fields on Creatio record pages: they can be populated with values of different data types (text, numerical, lookup, etc.). In Creatio, business process parameters serve two functions:
 


* Provide specifics (or “
 **input** 
 ”) about how the process elements are executed (e. g., what will be the name and duration of an activity created as part of a business process, who will be assigned as its owner, etc.).
* Act as a
 **medium for exchanging information** 
 between the
 [elements within a business process](/docs/8-0/user/bpm_tools/process_element_use_cases/parameters/use_process_parameters#title-2784-6) 
 (e. g., what the task result was, who its owner was, etc.) or between a
 [sub-process and its parent process](/docs/8-0/user/bpm_tools/process_element_use_cases/parameters/use_process_parameters#title-2784-7) 
 .



 Since parameters represent the state of a process element or a process after its execution is complete, their values can be used for branching processes using
 [gateways](/docs/8-0/user/bpm_tools/process_elements_reference/gateways/exclusive_gateway_or/exclusive_gateway_or_process_element) 
 and
 [conditional flows](/docs/8-0/user/bpm_tools/process_elements_reference/flows/conditional_flow_shortcut/conditional_flow) 
 .
 



 Parameters are available in both business processes and process elements.
 



 Element parameters are displayed on the element setup area. For example, the
 
 To
 
 field in the
 
 Send Email
 
 process element (Fig. 6) is a text parameter whose value represents the recipient’s email address.
 





 Fig. 6
 
 Element parameters
 

![chapter_process_principles_element_parameters.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_parameters/chapter_process_principles_element_parameters.png)



 Important element parameters are available on the element’s setup area by default, whenever you select an element on the diagram. If the element setup area is closed, simply double-click the element to open it. To access all parameters of an element, switch to the advanced mode (Fig. 7).
 




 Fig. 7 Switching an element setup area to the advanced mode
 

![chapter_process_principles_advanced_mode.GIF](/docs/sites/en/files/inline-images/chapter_process_principles_advanced_mode.GIF)





 Note.
 
 The names of parameters in the regular and advanced modes may be different. To locate which parameter is being populated, type in a random value for the necessary parameter in the “regular” mode, switch to the “advanced” mode and locate the value in the list of parameters.
 




 Process parameters are available on the
 
 Parameters
 
 tab in the process setup area (Fig. 8), which you can access by clicking
 ![icn_process_properties.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_parameters/icn_process_properties.png)
 or empty space on the
 [Process Designer](/docs/8-0/user/bpm_tools/business_process_setup/overview/process_designer) 
 working area (if the element setup area is open).
 





 Fig. 8
 
 The
 
 Parameters
 
 tab of the Process Designer setup area
 

![chapter_process_principles_parameters_tab_process.png](/docs/sites/en/files/images/BPM_Tools/process_parameters/chapter_process_principles_parameters_tab_process.png)



 Parameter types
-----------------



 The type of parameter depends on the data type of its value. The types of parameters are roughly similar to types of Creatio section and lookup columns, which in turn correspond to columns in the Creatio database.
 



 The following parameter types are available in Creatio:
 





| 
 Parameter type
  | 
 Description
  |
| --- | --- |
| 
chapter_process_principles_text.png
 Text
  | 
 A parameter whose value is a text string that can represent a constant value or a value generated during the process flow. For example, the
 
 What should be done?
 
 parameter of the
 
 Perform task
 
 element.
  |
| 
chapter_process_principles_decimal.png
 Decimal
  | 
 Stores and exchanges decimal numeric values. For example, the
 
 Function result
 
 parameter of the
 [Read data
 
 element](/docs/8-0/user/bpm_tools/process_elements_reference/system_actions/read_data/read_data_process_element) 
 .
  |
| 
chapter_process_principles_integer.png
 Integer
  | 
 Stores and exchanges integer numeric values. For example, the
 
 Start executing in
 
 parameter of the
 
 Perform task
 
 element.
  |
| 
chapter_process_principles_boolean.png
 Boolean
  | 
 Stores logical values (true or false). For example, the
 
 Answer required
 
 parameter in the
 [User dialog
 
 element](/docs/7-17/user/bpm_tools/process_elements_reference/user_actions/user_dialog/user_dialog_process_element) 
 .
  |
| 
chapter_process_principles_lookup.png
 Lookup
  | 
 A parameter that stores a value from a lookup (i.e., a link to a lookup record). For example, the
 
 Who fills in the page?
 
 parameter of the
 [Open edit page
 
 element](/docs/7-17/user/bpm_tools/process_elements_reference/user_actions/open_edit_page/open_edit_page_process_element) 
 can be populated with values from the
 
 Contact
 
 lookup.
  |
| 
chapter_process_principles_date_time.png
 Date/Time
  | 
 Stores certain date/time values. For example, the
 
 Start date and time
 
 parameter of the
 [Start timer
 
 event](/docs/8-0/user/bpm_tools/process_elements_reference/events/start_timer/start_timer_event_process_element) 
 .
  |
| 
chapter_process_principles_decimal00001.png
 Currency
  | 
 Stores values of currency fields. Learn more:
 [Work with currencies](/docs/8-0/user/platform_basics/user_interface/currencies/working_with_currencies) 
 .
  |
| 
chapter_process_principles_date_object.png
 Collection of records
  | 
[Collection parameter](/docs/7-17/user/bpm_tools/business_process_setup/collections/process_collections) 
 contains complex values, each representing several entries, such as several contacts with name, address, and a phone number specified for each contact. For example, developers can use this parameter in the
 [Pre-configured page
 
 element](/docs/8-0/user/bpm_tools/process_elements_reference/user_actions/pre_configured_page/pre_configured_page_process_element) 
 .
  |
| 
chapter_process_principles_date_Id.png
 Id
  | 
 Stores a
 [unique record identifier](/docs/8-0/user/bpm_tools/business_process_setup/data/process_data) 
 . For example, the
 
 Id
 
 parameter of the
 [Signal
 
 start event](/docs/8-0/user/bpm_tools/process_elements_reference/events/signal/signal_start_event) 
 .
  |




 Depending on when and how a parameter value is populated, it can be either
 **input** 
 or
 **output** 
 .
 


* **Input values** 
 are populated before the element or process is executed. Input parameters affect the process element execution.
* **Output values** 
 are populated during the process/element execution and usually represent its result, or the state the process or element is in after it has been completed.



 An input value can be replaced with an output value in some parameters, e. g., a task was connected to a specific contact but needs to be replaced with a different contact during process execution.
 



 Populate parameter values
---------------------------



 You can populate
 **input parameter values ​​** 
 in one of the following ways:
 


* Enter a static parameter value manually. In this case, parameter values are specified directly, when the process is designed and are always the same in all process instances. For example, the name of the task (the
 
 What should be done?
 
 parameter) was created with the help of the
 
 Perform task
 
 element.
* Select a
 [system setting](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/manage_system_settings_shortcut/manage_system_settings) 
 (e. g., “Test email recipient”) or a system variable (e. g., current date and time, current user contact, current user account, etc.) whose value will be passed to the parameter. In this case, parameter values will be the same as the values of corresponding system settings or system variables at the time of process execution. For example, if you select the current user contact as the
 
 Who performs the task?
 
 parameter value in the
 
 Perform task
 
 element, the task will be created for the user who started the process.
* Use a formula. Multiple parameters can be combined or converted to other types using formula syntax, e. g., combining a text string with a parameter value.
* By obtaining a value from another parameter. This method enables you to get a parameter value from a different parameter in the process. For example, you can get the contact with whom the meeting had been previously scheduled (the
 
 Contact
 
 parameter of the
 
 Perform task
 
 element) and pass this value to the
 
 To
 
 parameter of the
 
 Send Email
 
 element.



 Learn more:
 [Use process parameters](/docs/8-0/user/bpm_tools/process_element_use_cases/parameters/use_process_parameters#title-2784-1) 
 .
 



 Obtain parameter values from another parameter
------------------------------------------------



 A parameter can be configured to obtain its input value from another parameter with the same data type.
 



 For example, a new contact is added via an
 
 Open edit page
 
 element, and later in the process flow, a meeting must be scheduled with that same contact. In this case, the value of the
 **source** 

 Record Id
 
 parameter (where the record Id of the contact is stored) of the
 
 Open edit page
 
 element must be passed to the
 **target** 

 Contact
 
 parameter of the
 
 Perform task
 
 element.
 





 Note.
 
 Make sure that the source parameter is properly populated at the time when the target parameter obtains its value.
 




 Most of the time, parameters can only receive values from other parameters of the same type. However, certain parameters can receive values of other parameter types, namely:
 


* Date/time parameters can store interchangeable values: you can specify a date value in the time parameter and vice versa.
* Integer and decimal parameters can store interchangeable values, i.e. you can specify a decimal value in the integer parameter and vice versa. Integer and decimal values will be converted depending on the parameter they are passed to.
* Lookup parameters can store a record’s unique identifier (Id). For example, specify the Id of a contact in a lookup parameter whose values can be selected from the
 
 Contacts
 
 lookup.



 To obtain a parameter value from a different parameter:
 


1. Click the
 ![btn_process_element_settings_lookup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_parameters/btn_process_element_settings_lookup.png)
 button next to the field of the “target” parameter (the one, which must be populated).
2. Select
 
 Process parameter
 
 from the menu (Fig. 9). The parameter selection window (Fig. 10) will open.
 





 Fig. 9
 
 Open the process parameter selection window
 

![chapter_process_parameters_call_select_parameter_contact_field_2.png](/guides/sites/en/files/images/BPM_Tools/process_parameters/chapter_process_parameters_call_select_parameter_contact_field_2.png)



 Select a source process or element parameter (the one, whose value must be passed to the current parameter) in the
 **parameter selection window** 
 .
3. The
 
 Process elements
 
 tab (Fig. 10) of the parameter selection window displays a list of elements in the current process (1). Select an element on the left-hand side of the window and the list of its parameters will be displayed to the right (2). This list only displays parameters whose type corresponds to the
 **target** 
 parameter. Double-click a parameter in the list to populate the
 **target** 
 parameter with its value.
 





 Fig. 10
 
 The element parameter selection tab
 

![chapter_process_principles_parameters_element_param.png](/guides/sites/en/files/images/BPM_Tools/process_parameters/chapter_process_principles_parameters_element_param.png)



 The
 
 Process parameters
 
 tab (Fig. 11) displays all available process parameters. This list only displays parameters whose type corresponds to the target parameter. Double-click a parameter in the list to populate the target parameter with its value.





 Fig. 11
 
 The process parameter selection tab
 

![chapter_process_principles_parameters_process_param.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_parameters/chapter_process_principles_parameters_process_param.png)




