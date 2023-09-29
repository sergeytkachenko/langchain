


 You can use the inclusive gateway to create alternative flows in the process that can be executed concurrently. When diverging, an inclusive gateway activates the
 [conditional flows](/docs/8-0/user/bpm_tools/process_elements_reference/flows/conditional_flow_shortcut/conditional_flow) 
 whose conditions are met. Both one or several outgoing flows can be activated.
 



 For example, if the account annual revenue is 100,000 or more, it is considered a large customer, and if its annual revenue is more than 200,000, then this customer is considered VIP (Fig. 1).
 




 Fig. 1 Diverging inclusive gateway
 

![scr_process_designer_inclusive_gateway_branching.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_inclusive_gateway_branching.png)



 If the customer's annual revenue is 150,000, it will be classified as a large customer. If the customer annual revenue is more than 200,000, it will be added to the large customers group and also have VIP status. In case the annual revenue is less than 100,000, the
 [default flow](/docs/8-0/user/bpm_tools/process_elements_reference/flows/default_flow_shortcut/default_flow) 
 is used.
 



 The diverging inclusive gateway element requires an outgoing default flow. The default flow is activated when it is impossible to activate at least one of the conditional flows.
 



 A converging inclusive gateway works in the same way as a converging
 [exclusive gateway](/docs/8-0/user/bpm_tools/process_elements_reference/gateways/exclusive_gateway_or/exclusive_gateway_or_process_element) 
 .
 




