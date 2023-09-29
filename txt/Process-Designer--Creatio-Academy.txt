


 The Process Designer workspace is designed for creating and editing business processes. The workspace (Fig. 1) contains all elements required to create a process.
 




 Fig. 1 The Process Designer
 

![scr_chapter_process_designer_interface.png](/docs/sites/en/files/images/BPM_Tools/process_designer/scr_chapter_process_designer_interface.png)



 Toolbar (1)
-------------



 The area includes the following buttons:
 


* Save
 
 – saves the business process.
 





 Note.
 
 The business processes are automatically saved in Creatio. If a process diagram was closed without saving, it is possible to recover unsaved data.
* Run
 
 – runs the currently open business process.
* Cancel
 
 – discards unsaved changes.



 The
 
 Actions
 
 menu of the Process Designer includes the following commands:
 


* Source code
 
 – opens the source code of the business process.
* View Metadata
 
 – opens the metadata of the business process.
* Copy diagram
 
 – creates a copy of the business process in the
 
 Process library
 
 section.
* Export Metadata
 
 – downloads the metadata of the current process as an \*.md file.
* Process Log
 
 – opens the
 
 Process log
 
 section in a new browser tab.
* Save current version
 
 – saves the current version of the business process. For example, if you have several versions of a business process, this command will save the one with which you are working.
* Set as actual version
 
 – sets the current version of the business process as actual. Whenever you run a business process, you always run the “actual version” version of this process.
* Process parameters
 
 – opens the list of process parameters. Learn more about how to use the parameters:
 [Process parameters](/docs/7-17/user/bpm_tools/business_process_setup/parameters/process_parameters) 
 .



![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/btn_system_designer.png)
 – opens the process settings in the element setup area.
 



![btn_designer_documentation.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/btn_designer_documentation.png)
 – opens this help on the Academy.
 



![btn_designer_search.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/btn_designer_search.png)
 – searches the current diagram for process elements by name.
 


### 
 Search for elements in the Process Designer



 The search function in the Process Designer simplifies navigation and switching between the diagram elements during the business process setup and configuration. The search is done by the element name or code.
 



 To open the search field (Fig. 2), click the
 ![btn_designer_search00001.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/btn_designer_search00001.png)
 button or press Ctrl+F on your keyboard.
 




 Fig. 2 Search field in the Process Designer
 

![scr_chapter_process_designer_search_field.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/scr_chapter_process_designer_search_field.png)



 Enter the searched text in the search string and press Enter. The number of found process elements will be displayed on the right side of the field (Fig. 3).
 




 Fig. 3 Search for process elements and display search results
 

![scr_chapter_process_designer_search_start.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/scr_chapter_process_designer_search_start.png)



 Use the
 ![btn_designer_search_navigate.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/btn_designer_search_navigate.png)
 buttons to toggle between the found elements on the diagram. You can go to the next element by pressing the Enter or F3 keyboard keys. To go back to the previously found element, press Shift+F3 on your keyboard (Fig. 4).
 




 Fig. 4 Toggle between the found process elements
 

![scr_chapter_process_designer_search_next.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/scr_chapter_process_designer_search_next.png)



 All found process elements are highlighted with a frame. Additionally, the currently selected element will be highlighted in orange (Fig. 5).
 




 Fig. 5 Found elements highlighted on the process diagram
 

![scr_chapter_process_designer_search_highlight.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/scr_chapter_process_designer_search_highlight.png)



 The setup area will open for the currently selected element.
 



 Click “Hide search” or press Esc to hide the search field.
 



 Working area (2)
------------------



 The Process Designer working area is where you design the process diagram. You can add process elements to the working area in two ways:
 


1. Drag an element from the element area
2. Drag an element from any element on the diagram. This will add the corresponding new element, connected to the previously selected element with a sequence flow.



 Process element toolbar (3)
-----------------------------



 The process element toolbar contains:
 


* A list of tools for working with the diagram.
* A list of basic elements you can use to create a business process.


### 
 Tools



 Use the
 ![arrow_tool.png](/guides/sites/en/files/documentation/user/en/marketing_campaigns/BPMonlineHelp/setup_campaign_diagram/arrow_tool.png)
 “
 **Arrow** 
 ” tool to select and move an element on the designer's working area.
 



 Use the
 ![lasso_tool.png](/guides/sites/en/files/documentation/user/en/marketing_campaigns/BPMonlineHelp/setup_campaign_diagram/lasso_tool.png)
 “
 **Lasso** 
 ” tool to select several diagram elements at once (Fig. 6)
 




 Fig. 6 Using the “Lasso” tool while designing a diagram
 

![](/guides/sites/en/files/documentation/user/en/marketing_campaigns/BPMonlineHelp/setup_campaign_diagram/setup_campaign_diagram_lasso.gif)



 Use the
 ![space_tool.png](/guides/sites/default/files/documentation/user/ru/marketing_campaigns/BPMonlineHelp/setup_campaign_diagram/space_tool.png)
 “
 **Space** 
 ” tool (Fig. 7) to move parts of the diagram right/left or up/down. For example, drag down to move down all the elements below the cursor.
 




 Fig. 7 Using the “Space” tool while designing a diagram
 

![](/guides/sites/en/files/documentation/user/en/marketing_campaigns/BPMonlineHelp/setup_campaign_diagram/setup_campaign_diagram_space_tool.gif)


### 
 Process elements



 Drag process elements from the toolbar to the working area to add them to your business process.
 



 The process element area displays all process elements in groups:
 





|  |  |
| --- | --- |
| 
process_designer_task_palette.png
 | 
[User actions](https://academy.creatio.com/docs/user/bpm_tools/process_elements_reference/user_actions)
 . Adds user action elements to the diagram. Users must interact with them.
  |
| 
process_designer_system_action_palette.png
 | 
[System actions](https://academy.creatio.com/docs/user/bpm_tools/process_elements_reference/system_actions)
 . Adds system action elements and sub-processes to the diagram. Creatio executes system actions automatically.
  |
| 
process_designer_start_event_palette.png
 | 
[Simple](/docs/8-0/user/bpm_tools/process_elements_reference/events/simple/simple_start_event)
 . Adds the
 
 Simple
 
 start event to the diagram. Click the
 btn_com_folder_filter.png
 button to change the element to a different start event:
 
 Signal
 
 ,
 
 Message
 
 , or
 
 Start timer
 
 .
  |
| 
process_designer_intermediate_event_palette.png
 | 
[Throw signal](/docs/8-0/user/bpm_tools/process_elements_reference/events/throw_signal/throw_signal_intermediate_event)
 . Adds the
 
 Throw signal
 
 intermediate event elements to the diagram. Click the
 btn_com_folder_filter.png
 button to change the element to a different intermediate event:
 
 Throw message
 
 ,
 
 Wait for message
 
 ,
 
 Wait for signal
 
 , or
 
 Wait for timer
 
 .
  |
| 
process_designer_end_event_palette.png
 | 
[Terminate](/docs/8-0/user/bpm_tools/process_elements_reference/events/terminate/terminate_end_event_process_element)
 . Adds the
 
 Terminate
 
 end event to the diagram.
  |
| 
process_designer_gateway_palette.png
 | 
[Exclusive gateway (OR)](/docs/8-0/user/bpm_tools/process_elements_reference/gateways/exclusive_gateway_or/exclusive_gateway_or_process_element)
 . Adds the
 
 Exclusive gateway (OR)
 
 logical gateway to the diagram. Click the
 btn_com_folder_filter.png
 button to change the element to a different logical gateway:
 
 Inclusive gateway (OR)
 
 ,
 
 Parallel gateway (AND)
 
 , or
 
 Event-based gateway
 
 .
  |




 Element setup area (4)
------------------------



 Use the element setup area (4) to specify the values of process element parameters. Learn more about how to use the parameters:
 [Process parameters](/docs/7-17/user/bpm_tools/business_process_setup/parameters/process_parameters) 
 . The list of available parameters depends on the type of the currently selected element.
 


### 
 The base mode



 In the base mode, the element setup area contains the main element parameters and the fields for connecting them with other Creatio records. The list of fields in the base mode is different for different elements and is covered separately in each element description.
 


### 
 Advanced mode



 In the advanced mode, the element setup area contains additional parameters and connections with system records
 



 To access the advanced mode, click the
 ![btn_advanced_mode.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/btn_advanced_mode.png)
 button in the element setup area and select the
 
 Advanced mode
 
 command (Fig. 8).
 





 Note.
 
 The advanced mode is intended for use by developers. We recommend using the base mode of the element setup area to regular users.
 





 Fig. 8 The advanced mode menu
 

![chapter_process_designer_advanced_mode.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/chapter_process_designer_advanced_mode.png)



 The following parameters are available in the advanced mode:
 


* Code
 
 – the internal name of a business process element containing a combination of Latin letters and numbers. Creatio uses it to identify the business process element. The default code is generated automatically, but you can edit it. The code cannot contain any special characters.
* Enable logging
 
 – enables process execution in the
 
 Process log
 
 section.
* Serialize in DB
 
 – saves parameter values for the running process in the database. Serialization is used for long processes. For example, if a new activity is created in the process and should be completed only after a certain time, all process parameters will be saved and the process can be resumed any time, even when you log out of the system.
* Run following elements in the background
 
 – determines how the next elements in the process flow are performed - whether they pop up to the process user or wait until the user activates them. Learn more about the ways to execute process steps:
 [Execute process steps](/docs/7-17/user/platform_basics/running_business_processes/execute_a_process/execute_process_steps) 
 .
 


	+ If the
	 
	 Run following elements in the background
	 
	 checkbox is
	 **cleared** 
	 for a process element, any user actions that are connected to the element's outgoing flows will open their edit pages (e. g., edit page, pre-configured page, or user dialog page) immediately, when the corresponding element activates in the process flow. For example, if the
	 
	 Open edit page
	 
	 element follows an element with the
	 
	 Run following elements in the background
	 
	 checkbox cleared, the corresponding page will immediately open for the corresponding user.
	+ If the
	 
	 Run following elements in the background
	 
	 checkbox is
	 **selected** 
	 for a process element, any user actions that are connected to the element's outgoing flows will appear on the
	 
	 Business process tasks
	 
	 tab of the communication panel. Such tasks though will not actively perform any logic (such as opening pages, etc.) until the user clicks them on the
	 
	 Business process tasks
	 
	 tab. All system actions connected to the element will be executed in the background without displaying the loading mask, to avoid user waiting for the process to finish. For example, if the
	 
	 Open edit page
	 
	 element follows an element with the
	 
	 Run following elements in the background
	 
	 checkbox cleared, a new business process task will display on the user communication panel. If the
	 
	 Open edit page
	 
	 element is followed by the
	 
	 System actions
	 
	 group elements that require complicated calculation and a long time, all calculations will be performed in the background without displaying the loading mask. This may cause business process delay issues, for example, if the user responsible for performing the user action is not currently logged in to Creatio.
 The
 
 Run following elements in the background
 
 checkbox is available for the following elements:
 


	+ All elements in the
	 
	 User actions
	 
	 group
	+ All elements from the
	 
	 Start events
	 
	 group except for the
	 
	 Start timer
	 
	 element. By default, the checkbox is selected for the
	 
	 Signal
	 
	 start event.
	+ The checkbox is selected and greyed out for the
	 
	 Wait for signal
	 
	 and
	 
	 Wait for timer
	 
	 intermediate events.
* Consider time in filter
 
 – specify “true” to enable precise time values in filters by date.





 Note.
 
 The list of parameters in advanced mode can be different for various process elements.
 




 Process element context menu (5)
----------------------------------



 The process element context menu contains a list of elements that can be added to the diagram after the currently selected element.
 



![icon_tools_setup.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/icon_tools_setup.png)
 – change the current element’s type.
 



![icon_tools_del.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/icon_tools_del.png)
 – delete the current element.
 



![process_designer_context_icon_tools_arrow.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/process_designer_context_icon_tools_arrow.png)
 – connect the current element to another element with an outgoing flow.
 



 Zoom toolbar (6)
------------------



 The zoom toolbar enables users to zoom and pan the process diagram as well restore the default zoom level and alignment (Fig. 9).
 




 Fig. 9 Reset zoom
 


![resetting_zoom.gif](/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/resetting_zoom.gif)




 Process settings
------------------



 A business process has a number of properties available on the
 
 Settings
 
 tab of the process setup area (Fig. 10). To open the business process setup area, click anywhere on the working area of the Process Designer.
 




 Fig. 10 Business process properties area
 

![scr_process_creation_designer_process_settings.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/scr_process_creation_designer_process_settings.png)



 The area includes the following fields:
 


* Caption
 
 – the title of the business process displayed in the system interface. The
 
 Caption
 
 field is displayed at the top of the setup page and at the top of the working area.
* Code
 
 – the internal name of the business process used by Creatio to identify it. The default code is generated automatically, but you can edit it. The code can only contain Latin characters and numbers and cannot contain any special characters.
* Version
 
 – current version of the process. The field is grayed out. It will be populated automatically when a new process version is saved.
 





 Note.
 
 Creatio numbers the versions within a single package consecutively, i. e., the new process version is greater than the last saved version of any process in the package by 1.
* Tag
 
 – tags used to filter and identify processes. If the process is marked with the “Business Process” tag, it becomes available in the
 
 Process library
 
 section.
* Process description
 
 – additional information about the process.
* Package
 
 – the package that contains the process schema.
* Maximum number of repetitions
 
 – a limit for how many times an element can be repeatedly executed within a single process instance. The purpose of this setting is to avoid infinite process looping. If the limit is reached on any element, the process will automatically stop.
* Process instance caption
 
 – specify the title that instances of this process will have. The business process instance titles are displayed in the
 
 Business process tasks
 
 tab of the communication panel. By default, this property contains the
 
 #Process name#
 
 system variable. Consider adding the process parameter values and/or text generated via a
 
 Formula
 
 element to make the process notifications more informative. For example, an invoicing process instance can have the actual number of invoice in its title: "Processing of invoice No. " +
 
 #Read invoice data.First item of the resulting collection.Number#
 
 . As a result, business process notifications will show the actual number of the invoice in processing (Fig. 11).
 




 Fig. 11 A business process notification
 

![chapter_process_creation_designer_notification.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_principles/chapter_process_creation_designer_notification.png)
* Active
 
 – this property is always grayed out. Use the actions of the
 
 Process library
 
 section to
 [deactivate and activate processes](/docs/8-0/user/bpm_tools/business_process_administration/deactivate_a_process_shortcut/deactivate_a_process) 
 .
* Enable logging
 
 – enables process execution in the
 
 Process log
 
 section.
* Serialize in DB
 
 – saves parameter values for the running process in the database. Serialization is used for long processes. For example, if a new activity is created in the process and should be completed only after a certain period of time, all process parameters will be saved and the process can be resumed any time, even when you log out of the system.
 



 If you clear the
 
 Serialize in DB
 
 checkbox, the process parameters will be saved, but not in the database.
 





 Attention.
 
 If you add elements to the process that have the
 
 Serialize in DB
 
 checkbox selected, then this checkbox will automatically be selected for the whole process.
* Actual version
 
 – indicates whether the current process version is used for running new instances of this process. The checkbox is available on the process properties page.
* Use system security context
 
 – manages security context for executing business process logic implemented in the
 
 Script task
 
 process elements. If the checkbox is selected, the
 
 Script task
 
 element will be executed in the security context of the “system user” – user account specified in the “System operations user” (“SystemUser” code) system setting. The
 
 Use system security context
 
 checkbox is selected by default for all new business processes. This enables using the same code without any additional UserConnection operations for processes intended both for the regular Creatio users and for portal users.




