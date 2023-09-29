


 When diverging, a parallel gateway is used to create several parallel flows in a process. For example, after a contract draft has been prepared, it must be agreed upon by both the company lawyer and CEO (Fig. 1).
 




 Fig. 1 Diverging parallel gateway
 

![scr_process_designer_parallel_gateway_branching.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_parallel_gateway_branching.png)



 In this case, after the “Prepare contract” user task, the “Agree with lawyer” and “Agree with CEO” user tasks will begin simultaneously.
 



 You can also use the
 
 Parallel gateway (AND)
 
 for converging several parallel flows in one, if the execution of all parallel flows is necessary for continuing the process. For example, the contract can be signed only after it has been agreed with the lawyer and company CEO (Fig. 2).
 




 Fig. 2 Converging parallel gateway
 

![scr_process_designer_parallel_gateway_synchronization.png](https://academy.creatio.com/docs/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_designer/scr_process_designer_parallel_gateway_synchronization.png)



 In this case, the “Sign contract” user task will start only after both the “Agree with lawyer” and “Agree with CEO” user tasks are completed. The process will not continue unless both tasks are completed.
 



 When converging, a parallel gateway is used with the
 [sequence flows](/docs/8-0/user/bpm_tools/process_elements_reference/flows/sequence_flow_shortcut/sequence_flow) 
 .
 




