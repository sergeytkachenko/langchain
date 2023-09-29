


 The diagrams of the business processes configured in Creatio are saved to the
 
 Process library
 
 section.
 





 Note.
 
 The process library displays the list of BPMN processes whose
 
 Tag
 
 parameter value is “Business Process.” By default, the “Business Process” tag is set for all processes that the users configure in the process designer. You can view and modify the process tag text on the business process properties areas in the process designer.
 




 The
 
 Process library
 
 section contains the “Active” filter for displaying only business processes with the
 
 Active
 
 checkbox selected.
 



 View the process list
-----------------------



 To view the process list:
 


1. Click
 ![btn_system_designer.png](/docs/sites/default/files/2020-11/btn_system_designer.png)
 to open the System Designer.
2. Click
 
 Process library
 
 under
 
 Processes
 
 .





 Note.
 
 Business processes whose diagrams contain a
 [start timer](/docs/node/1682/%26#9;) 
 or a
 [signal](/docs/node/1680/%26#9;) 
 event are indicated with the corresponding icons in the list (Fig. 1). These icons match the process element icons for the start timer and start signal events, respectively. If a business process uses different types of start events, the corresponding record will contain several icons.
 





 Fig. 1 – Business processes initiated with starting signal events
 

![Start signal](/docs/sites/en/files/2020-12/src_process_library_start_signal_picture.png)



 Find a process using organizational trees
-------------------------------------------



 The folder tree is displayed in the
 
 Process library
 
 section b default (Fig. 2). In addition to standard folders, the tree contains folders that are generated automatically, based on the processes currently available in the library.
 





 Fig. 2
 

 – Folders in the
 
 Process library
 
 section
 

![List view](/docs/sites/en/files/2020-12/src_process_library_list_view.png)



 All standard folder functions are available in the
 
 Process library
 
 section.
 





 Note.
 
 More information about working with folders is available in the “
 [Folders](https://academy.creatio.com/documents?product=marketing&ver=7&id=1235) 
 ” article.
 




 By default, the folders in the
 
 Process library
 
 section contain folders that group the processes by the type of their starting event. These folders have unique icons to visually distinguish them from regular folders. These folders cannot be edited.
 



 The folders that group business processes by the type of their starting events are displayed only if corresponding processes exist in the library.
 



 These folders also have automatically generated subordinate folders that further group the processes by their starting event parameters:
 


* In the “Run by object signal” folder, the further grouping is done by objects that trigger processes (Fig. 3).
 

 Fig. 3 – Grouping of processes by objects in the “Run by object signal” folder
 

![List folders](/docs/sites/en/files/2020-12/src_process_library_list_folders.png)
* In the “Run by timer” folder, the further grouping is done by the timer settings (Fig. 4).
 


 Fig. 4
 
 – Grouping of processes by timer settings in the “Run by timer” folder
 

![List timer folders](/docs/sites/en/files/2020-12/src_process_library_list_timer_folders.png)




