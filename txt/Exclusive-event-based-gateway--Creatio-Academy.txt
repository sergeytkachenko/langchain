


 An exclusive event-based gateway is used to branch a process when alternative paths are determined by events (
 [Throw message](/docs/8-0/user/bpm_tools/process_elements_reference/events/throw_message/throw_message_intermediate_event_process_element)
 ,
 [Throw signal](/docs/8-0/user/bpm_tools/process_elements_reference/events/throw_signal/throw_signal_intermediate_event)
 , and
 [Wait for timer](/docs/8-0/user/bpm_tools/process_elements_reference/events/wait_for_timer/wait_for_timer_intermediate_event_process_element)
 ) rather than by
 [conditional flows](/docs/8-0/user/bpm_tools/process_elements_reference/flows/conditional_flow_shortcut/conditional_flow) 
 .
 



 This can happen when the decision about one of the alternative paths is taken by someone out of the process. For example, a signing contract process expects a signal regarding a client's decision during the negotiation process. Further development of the process depends on this decision (Fig. 1).
 




 Fig. 1 Exclusive event-based gateway
 

![scr_process_designer_event_gateway_branching.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_event_gateway_branching.png)



 Depending on which event occurs first, the process will take the corresponding path. In the mentioned example, if the customer agreed to the conditions, the process will proceed with the “Sign contract” user task, and if the customer refuses – the process will end. In any case, only the expected event that occurs first will be processed, and all subsequent events will be considered no longer valid.
 



 Outgoing flows for the exclusive event-based gateway are
 [sequence flows](/docs/8-0/user/bpm_tools/process_elements_reference/flows/sequence_flow_shortcut/sequence_flow) 
 . The gateway is used in conjunction with intermediate catching events:
 [Wait for message](/docs/8-0/user/bpm_tools/process_elements_reference/events/wait_for_message/wait_for_message_intermediate_event_process_element)
 ,
 [Wait for signal](/docs/8-0/user/bpm_tools/process_elements_reference/events/wait_for_signal/wait_for_signal_intermediate_event)
 , or
 [Wait for timer](/docs/8-0/user/bpm_tools/process_elements_reference/events/wait_for_timer/wait_for_timer_intermediate_event_process_element)
 .
 



 As soon as the first catching event is triggered, the gateway activates the corresponding outgoing flow and then ignores any other events.
 




