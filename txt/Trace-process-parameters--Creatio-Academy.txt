


 Process element
 parameters
 determine the behavior of the element in each particular process instance. Tracing the actual parameter values that were used in a specific process instance is a great way to test and debug business processes in Creatio.
 



 You can enable tracing for a particular process by selecting the
 
 Trace enabled
 
 checkbox on the process properties page of the
 
 Process library
 
 section. Trace data becomes available on the
 
 Process elements
 
 detail of the process log page for all process instances that have been run while the checkbox is selected.
 





 Attention.
 
 Parameter data can be traced for the following process elements: all elements in the “User actions” group, as well as the
 
 Read data
 
 ,
 
 Add data
 
 ,
 
 Modify data
 
 ,
 
 Delete data
 
 ,
 
 Change access rights
 
 ,
 
 Call web service
 
 , and
 
 Subprocess elements
 
 .
 




 Attention.
 
 Process tracing should only be enabled for a short period of time to avoid negative impact to performance.
 




 To trace process parameter values:
 


1. Enable parameter value tracing for that process:
 


	1. Open the
	 
	 Process library
	 
	 section.
	2. Select the needed process and click
	 
	 Properties
	 
	 .
	3. Select the
	 
	 Trace enabled
	 
	 checkbox on the process properties page.
	4. Save changes made to the process properties page.
2. Run the process.
3. Go to the
 
 Process log
 
 section.
4. Open the process log entry for the process instance that you just run.
5. On the
 
 Process elements
 
 detail, select a process element whose parameter values you need to check.
6. Click the
 
 Show trace data
 
 button (Fig. 1).
 





 Fig. 1
 
 – Viewing parameter information of a process element
 


![Show trace data](/docs/sites/en/files/2020-12/scr_chapter_process_monitoring_show_trace_data.png)



 As a result, a parameter trace dialog will open, showing values for all parameters of the process element, before and after element execution (Fig. 2). The trace data are shown in the JSON format. The trace log displays both the element parameters and the process parameters before and after element execution.
 




 Fig. 2 – Parameter trace data of a process element
 


![Show trace dtaa window](/docs/sites/en/files/2020-12/scr_chapter_process_monitoring_show_trace_data_window.png)




 For example, according to the text on the figure, the value of the “Approval objective” parameter has changed from empty to “Approve contract specification,” the value of the “Delegation permitted” parameter changed from “False” to “True,” etc.
 




