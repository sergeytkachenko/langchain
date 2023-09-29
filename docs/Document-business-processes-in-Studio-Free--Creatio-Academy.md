


 Understanding each step of a business process by every participant is crucial for successful implementation. You can export documentation on each process created in Studio Creatio, free edition, as a PDF file. The documentation will contain a detailed and meaningful digest of all process elements. This is an optimal format to present a business process to employees and run a training program.
 



 To generate the documentation:
 


1. Select the needed process in the library.
2. Click
 
![process_library_folder_menu.png](/guides/sites/default/files/documentation/user/ru/studio_free/BPMonlineHelp/chapter_process_documentation_studio/process_library_folder_menu.png)

 .
3. Select
 
 Download documentation
 
 in the window that opens.



 This action will download the generated file via your browser download UI.
 




![Export documentation](/docs/sites/en/files/2020-12/export_documentation.gif)



 Before exporting the documentation, make sure that you have provided a description of the process and its elements:
 


1. **Process title** 
 . Name the process to help the users understand its purpose. As a rule, the title of a process is descriptive, such as “Long sales,” “Shipment,” and so on.
2. **Process description** 
 . Describe the process. Aside from the purpose, cover all details that are not directly displayed in the diagram. Creatio uses this description as the intro when generating the process documentation.
3. **Process element names and descriptions** 
 . The name of each business process element must comply with the BPMN notation guidelines. Short and meaningful element names are good practice. Avoid pronouns, articles, unnecessary precisions, and ambiguity. For example, use “Conduct meeting” rather than “Conduct the scheduled meeting with the customer.”



 The general BPMN naming conventions are available below:
 





| 
 Process elements
  | 
 BPMN naming conventions and documentation guidelines
  |
| --- | --- |
| 
 Actions
  | 
 An
 **action name** 
 should start with a descriptive action verb. For example, “Call customer.”
 

 The
 **action description** 
 contains action details. For example, “The manager calls the customer and appoints a meeting.” The users need such descriptions to figure out what they should do to progress the business process.
  |
| 
 Events
  | 
 Construct
 **event names** 
 using an action object and a past participle of an active verb. For example, “Employee hired.” Use specific time-dates or specific conditions to name timer and conditional events. For example, use “Every morning at 10 AM” for a timer event or “Yes,” “Correct” and so on for a conditional event. Make sure that paired start and intermediate events share matching names.
 

 An
 **event description** 
 should include detailed information about the event: what, how, and when it occurs. Such descriptions help users to find out if the event has happened.
  |
| 
 Gateways
  | 
**Gateway names** 
 depend on the gateway type. Diverging exclusive gateways (OR) normally have interrogative names phrased as closed questions. The answers to the question are used to name the outgoing conditional flows. For example, “Does candidate qualify?” Names are optional for other gateway types.
 

 The
 **gateway description** 
 covers the process branching on the respective gateway. For example, “The process branches depending on the job qualifications of the candidate” (exclusive gateway (OR)).
  |
| 
 Flows
  | 
 A
 **conditional flow name** 
 includes the condition that triggers the flow. Sequence flows and default flows usually have no names.
 

**Flow descriptions** 
 will not be included in the documentation and are optional.
  |
| 
 Artifacts
  | 
 The
 **name of the data object** 
 includes the name of the business object. For example, “Organization profile.”
 

 The
 **comment** 
 contains additional information and can be filled in arbitrarily.
  |
| 
 Lanes
  | 
 The
 **lane name** 
 should match the role of the business process participant. In the process documentation, lanes are listed as process participants.
  |





