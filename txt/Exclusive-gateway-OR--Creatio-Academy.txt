


 The
 
 Exclusive gateway (OR)
 
 is used when only one of the parallel flows in the process can be selected, for example, you can offer a discount or standard price to a customer (Fig. 1).
 




 Fig. 1 Diverging exclusive gateway
 

![scr_process_designer_exclusive_gateway_branching.png](/docs/sites/en/files/images/BPM_Tools/exclusive_gateway_or_process_element/scr_process_designer_exclusive_gateway_branching.png)



 In this case, only one of the two actions can be executed.
 



 When diverging, an exclusive gateway usually requires an outgoing
 [default flow](/docs/8-0/user/bpm_tools/process_elements_reference/flows/default_flow_shortcut/default_flow) 
 . Default flow is activated when it is impossible to activate at least one of the
 [conditional flows](/docs/8-0/user/bpm_tools/process_elements_reference/flows/conditional_flow_shortcut/conditional_flow) 
 .
 



 The converging exclusive gateway is used to merge several parallel flows. In this case, every incoming sequence flow is routed to a single outgoing flow.
 



 For example, after delivery conditions were offered to the customer (either with or without a discount), the quotation must be prepared (Fig. 2).
 




 Fig. 2 Converging exclusive gateway
 

![scr_process_designer_exclusive_gateway_merging.png](/docs/sites/en/files/images/BPM_Tools/exclusive_gateway_or_process_element/scr_process_designer_exclusive_gateway_merging.png)



 When the converging
 
 Exclusive gateway (OR)
 
 is used, the process will continue after either of the incoming flows is activated.
 




