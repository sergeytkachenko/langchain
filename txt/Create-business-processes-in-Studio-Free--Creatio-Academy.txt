


 You design a business process by adding elements to the working area, arranging them, connecting, and adding their descriptions.
 





 Note.
 
 The development of business processes in Creatio is based on the BPMN 2.0 notation developed by the Object Management Group consortium. Learn more about the BPMN notation on the OMG consortium’s
 
[website](https://www.omg.org/spec/BPMN/About-BPMN/) 

 .
 





 Create a new process
-----------------------



 Add a new business process in the following ways:
 


* Click
 ![add_icon.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/add_icon.png)
 in the Studio toolbar and select
 
 Process
 
 . A new process will be added to the currently selected process library folder.




![New process A](/docs/sites/en/files/2020-12/new_process_a.gif)


* Select a process library folder and click
 
 New process
 
 .




![New process B](/docs/sites/en/files/2020-12/new_process_b.gif)


* In a process library folder menu, click
 ![process_library_folder_menu.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/process_library_folder_menu.png)
 and select
 
 New process
 
 .




![New process C](/docs/sites/en/files/2020-12/new_process_c.gif)



 Add elements to a business process
------------------------------------



 There are two ways of adding process elements in Creatio:
 


* Drag&drop an element from the element toolbar.




![Add start event](/docs/sites/en/files/2020-12/add_start_event.gif)


* Drag an element from any element on the diagram. This will add the corresponding new element, connected to the previously selected element with a sequence flow.




![Drag elements from previous](/docs/sites/en/files/2020-12/drag_elements_from_previous_elements.gif)



 Add flows
-----------



 To connect two elements on the diagram with a
 **flow** 
 , click the first element, click
 ![flow_button.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/flow_button.png)
**flow** 
 in the element context menu, then drag the flow to the second element. After the new flow has been added, you can change its position on the diagram, and the flow type (conditional or default).
 




![Add flow](/docs/sites/en/files/2020-12/add_flow.gif)



 Change the element type
-------------------------



 The
 **process element toolbar** 
 and
 **process element context menu** 
 contain general categories of elements: action, start/intermediate/end event, gateway, flow.
 



 To add a specific process element first add an element of the corresponding category (e.g., “action”), and then set its type (e.g., “User action”).
 



 To change an element type:
 


1. Select the element.
2. Click
 ![optins_gear_button.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/optins_gear_button.png)
 in its context menu.
3. Select the needed type from the menu that appears.




![Change element type](/docs/sites/en/files/2020-12/change_element_type.gif)



 Similarly, you can change types of other elements:
 


* To add a
 **loop** 
 ,
 ![parallel_marker.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/parallel_marker.png)
**parallel** 
 ,
 ![sequential_marker.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/sequential_marker.png)
**sequential,** 
 or
 ![compensation_marker.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/compensation_marker.png)
**compensation marker** 
 to an activity – select it, click
 ![optins_gear_button00001.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/optins_gear_button00001.png)
 in its context menu, and select the needed marker.




![Set marker](/docs/sites/en/files/2020-12/set_marker.gif)


* To add a
 ![conditional_flow.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/conditional_flow.png)
**conditional flow** 
 or
 ![default_flow.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/default_flow.png)
**default flow** 
 , add a
 ![flow_button00002.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/flow_button00002.png)
**sequence flow** 
 , select it, click
 ![optins_gear_button00003.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/optins_gear_button00003.png)
 in its context menu, and change its type to the needed one.




![Set flow type](/docs/sites/en/files/2020-12/set_flow_type.gif)



 Add description
-----------------



 Use the
 **setup area** 
 of the Process Designer to change the process or element
 **name** 
 and add a
 **description** 
 , which is vital for
 
[documenting business processes](/docs/node/1632/%26#9;) 

 .
 




![Adding descriptions](/docs/sites/en/files/2020-12/adding_descriptions.gif)



 Make sure that you
 **populate a description for the process and each of its elements** 
 . Description normally explains what happens when the element is executed as part of the process flow.
 



 You can open the settings toolbar in the following ways:
 


* Double-click an element to open its
 **setup area** 
 . If you double-click the empty process designer
 **working area** 
 , the
 **process setup area** 
 will open.
* Click on the top right side of the Process Designer window to open the
 **setup area of the currently selected element** 
 . If no elements are selected, the process setup area will open.



 Add lanes
-----------



 Swimlanes are a means of organizing elements on the diagram. They usually denote different process participants, as well as organize and categorize activities. You can add swimlanes at any time, but it is generally recommended to map them first and add other elements on the needed pool/lane, to exclude rearranging existing process steps.
 


* To add a
 ![pool.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/pool.png)
**pool** 
 , drag it to the designer working area from the
 **element toolbar** 
 .




![Add pool](/docs/sites/en/files/2020-12/add_pool.gif)


* To add a lane, select a
 **pool** 
 on the diagram and click
 ![lane_up.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/lane_up.png)
 or
 ![lane_down.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/lane_down.png)
 . A lane will be added to the selected pool in the corresponding position.




![Add lane](/docs/sites/en/files/2020-12/add_lane.gif)


* To split a
 **lane** 
 in two, select the lane and click
 ![split_lane.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio_cases/split_lane.png)
 .




![Split lane](/docs/sites/en/files/2020-12/split_lane.gif)




 Select and move elements
---------------------------



 Use the
 ![lasso_tool.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio/lasso_tool.png)

 Lasso
 
 tool to select several elements at once. Selected elements can be moved, copied (
 **Ctrl** 
 +
 **C** 
 ), or deleted (
 **Del** 
 ).
 



![lasso-tool.gif](/docs/sites/en/files/images/lasso-tool.gif)




 Use
 ![space_tool.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio/space_tool.png)

 Space
 
 tool to shift all elements on the diagram left/right or up/down. This tool applies to all elements to the right or left from the cursor – when shifting elements horizontally. Likewise, when shifting elements vertically, the tool will apply to all elements above the cursor (when shifting upwards) and all elements below the cursor (when shifting the elements downward).
 



![space_tool.gif](/docs/sites/en/files/images/space_tool.gif)




 The
 ![arrow_tool.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_designer_studio/arrow_tool.png)

 Arrow
 
 tool is the default mode in which you work with the elements on the working area. Use the toolbar to switch the cursor back to
 
 Arrow
 
 after using
 
 Lasso
 
 or
 
 Space
 
 tool.
 



![activate_arrow_tool.gif](/docs/sites/en/files/images/activate_arrow_tool.gif)





 Drag&drop the working area canvas to
 **navigate large diagrams** 
 . Use the
 **mouse wheel** 
 while holding down the
 **Ctrl** 
 key to zoom. Use the
 **zoom menu** 
 to restore default zoom and alignment.
 




![Navigation](/docs/sites/en/files/2020-12/navigation.gif)



 Use the
 **mini-map** 
 for fast diagram navigation.
 




![Mini map](/docs/sites/en/files/2020-12/mini_map.gif)














