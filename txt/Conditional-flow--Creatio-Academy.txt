


 Moving down the conditional flow is done upon fulfilling the condition specified for a flow. For example, if a customer is interested in your products or services, the relevant information must be forwarded to them (Fig. 1)
 




 Fig. 1 Conditional flow
 

![scr_process_designer_conditional_sequence_flow_connection.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_conditional_sequence_flow_connection.png)



 Conditions for gateways are set in the same manner. If a process element (for example, “Perform task”) is connected to a
 [gateway](https://academy.creatio.com/docs/user/bpm_tools/process_elements_reference/gateways) 
 with a sequence flow, then when you add conditional flows between this gateway and subsequent process elements, it is necessary to specify the conditions for moving down these flows.
 



 Depending on the element they originate from, the conditional flows can be assigned conditions by selecting a preset condition in the element setup window of a conditional flow, or specifying a custom condition using a formula.
 



 Selecting a condition from the list
-------------------------------------



 When you add an outbound conditional flow to an action, such as
 [Perform task](/docs/7-18/user/bpm_tools/process_elements_reference/user_actions/perform_task/task_process_element)
 , you can select task results as a condition for activating this conditional flow (Fig. 2).
 




 Fig. 2 Select a condition for a conditional flow
 

![chapter_process_designer_conditional_flow.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/chapter_process_designer_conditional_flow.png)





 Note.
 
 Possible results of the
 
 Perform task
 
 element are stored in the
 
 Activity results
 
 lookup. The list of possible options depends on the type of activity. In this case, only one of the outgoing conditional flows can be activated, as with an
 [exclusive gateway](/docs/7-18/user/bpm_tools/process_elements_reference/gateways/exclusive_gateway_or/exclusive_gateway_or_process_element) 
 .
 




 Using a formula to create a condition
---------------------------------------



 If a conditional flow originates from any process element whose results cannot be determined by the value in a certain column, you need to specify the condition using the parameter value window. Formulas are also used for conditional flows outgoing from gateways. When you add such a conditional flow, the
 
 Formula
 
 element card is opened. Use it to set conditions for moving down this flow.
 



 When a formula is used to set conditions for conditional flows, the result of the formula is treated as a Boolean value. The logic is the same as that of the standard
 
 Formula
 
 item whose value is passed to a parameter with the boolean data type.
 




