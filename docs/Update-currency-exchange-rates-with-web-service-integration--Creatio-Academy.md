


 Creatio uses a special business process element to call web services and parse their response.
 





 Example.
 
 Create a business process that will obtain currency exchange rates from the
 <http://api.fixer.io/>
 web service and update exchange rates on the
 
 Currency rate
 
 detail of the
 [Currencies](/docs/8-0/user/platform_basics/user_interface/currencies/working_with_currencies)
 lookup.
 






 Attention.
 
 Detailed instructions on setting up integration with the
 <http://fixer.io/>
 web service are available in a separate article.
 




 Business process diagram (Fig. 1) elements:
 




 Fig. 1 The “Update currency exchange rates” process
 

![scr_process_creation_designer_web_service_process_diagram.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_web_service_process_diagram.png)


1. Business process custom
 parameter
 : “Base currency”, which contains the current value of the
 
 Base currency
 
 system setting.
2. [Timer](/docs/8-0/user/bpm_tools/process_elements_reference/events/start_timer/start_timer_event_process_element) 
 start event: “Start every night” – the process starts daily, at the specified time.
3. [Read data](/docs/8-0/user/bpm_tools/process_elements_reference/system_actions/read_data/read_data_process_element) 
 system action: “Read base currency” – the process obtains the current base currency name.
4. [Call web service](/docs/8-0/user/bpm_tools/process_elements_reference/system_actions/call_web_service/call_web_service_process_element)
 system action: “Get currency exchange rate from the Fixer web service” – the process calls web service request method “latest” to obtain exchange rates for the current base currency. The element has 2 outgoing
 [conditional flows](/docs/8-0/user/bpm_tools/process_elements_reference/flows/sequence_flow_shortcut/sequence_flow) 
 :
 


	1. “Success”: the process proceeds to updating the exchange rates if response from the web service has been received.
	2. “Error”: the process will terminate if web service call resulted in error or timed out.
5. [Add data](/docs/8-0/user/bpm_tools/process_elements_reference/system_actions/add_data/add_data_process_element)
 system actions: add one for each currency whose rate must be modified. For example, “Add EUR exchange rate” – The process adds a record on the
 
 Currency rate
 
 detail for each currency whose rate must be updated. The
 
 Exchange rate
 
 field for each record contains the corresponding exchange rate received from the web service.
6. *[Parallel gateway AND](/docs/8-0/user/bpm_tools/process_elements_reference/gateways/parallel_gateway_and/parallel_gateway_and_process_element)*
 : this gateway will ensure that the process will end only after all currency rates have been updated.





 Attention.
 
 Before using the
 
 Call web service
 
 element, make sure that you set up integration with the needed web service, using the
 
 Web services
 
 section in the
 
 Studio
 
 workplace. Learn more about adding the
 <http://fixer.io/>
 web service integration in the
 [Getting started with low-code web service integration](https://academy.creatio.com/documents?id=1862) 
 article.
 





 To configure the process:
 


1. Use a custom parameter to pass the current “Base currency” system setting value to the business process.
	1. Click
	 ![icn_process_properties.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/icn_process_properties.png)
	 , then click
	 
	 Parameters
	 
	 tab and
	 
	 Add parameter
	 
	 button. Select “Lookup” parameter type (Fig. 2).
	 
	
	 Fig. 2
	 
	 Add a custom “Lookup” type process parameter
	 
	
	![scr_process_creation_designer_add_lookup_parameter.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_add_lookup_parameter.png)
	2. Populate parameter properties (Fig. 3):
	 
	
	
	
	
	 Fig. 3
	 
	 Mapping a custom process parameter to a system setting value
	 
	
	![scr_process_creation_designer_add_sys_setting_parameter_value.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_add_sys_setting_parameter_value.png)
	
	
		* Populate
		 
		 Title
		 
		 and
		 
		 Code
		 
		 properties.
		* In the
		 
		 Lookup
		 
		 field, select the
		 
		 Currency
		 
		 lookup.
		* In the
		 
		 Value
		 
		 field, click
		 ![btn_process_element_settings_lookup00008.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_process_element_settings_lookup00008.png)
		 >
		 
		 System setting
		 
		 and select the
		 
		 Base currency
		 
		 system setting.
2. Set up the “Start every night” element properties:
 

 Fig. 4 The “Start every night” timer event element
 

![scr_process_creation_designer_web_service_start_timer_event.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_web_service_start_timer_event.png)


	1. In the
	 
	 Frequency of process start
	 
	 field, select “Day”.
	2. In the
	 
	 Run every
	 
	 field block, specify “1 day in 1:30 AM”.
	3. Select your time zone and configure other optional properties, if needed.
3. Set up the “Read base currency” element properties (Fig. 5):
 

 Fig. 5
 
 The “Read base currency name” element properties
 

![scr_process_creation_designer_web_service_read_data.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_web_service_read_data.png)


	1. In the
	 
	 Which data read mode to use?
	 
	 field, select “Read the first record in the selection”.
	2. In the
	 
	 Which object to read data from?
	 
	 field, select the “Currency” object.
	3. Set up the following filter in the
	 
	 How to filter records?
	 
	 area: “Id = Base currency”. In this case, “Base currency” is the name of the custom process parameter that you added earlier.
	 
	
	
	
	
	
	 Note.
	 
	 To set the filter: click
	 
	 Add condition
	 
	 , select the
	 
	 Id
	 
	 column; click
	 
	 <?>
	 
	 and select
	 
	 Compare with parameter
	 
	 command; in the
	 
	 Select parameter
	 
	 window, click
	 
	 Process parameters
	 
	 tab and select the “Base currency” parameter that you added earlier.
	4. In the
	 
	 What record data should the process read?
	 
	 field, select “Read data from selected columns only”.
	5. Click
	 
	 Add column
	 
	 link and select the
	 
	 Short name
	 
	 column to have the process read the base currency short name (USD, EUR, etc.) from the lookup.
4. Set up the “Get currency exchange rate from the Fixer web service” element properties (Fig. 5):
 


 Fig. 6
 
 The “Get currency exchange rate from the Fixer web service” element properties
 



![scr_process_creation_designer_web_service_element_properties.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_web_service_element_properties.png)



	1. In the
	 
	 Which service to call?
	 
	 field, select “Currency exchange rate (Fixer)”.
	2. In the
	 
	 Which method to call?
	 
	 field, select the “Get latest exchange rates” method.
	 
	
	
	
	
	
	 Note.
	 
	 The
	 <http://fixer.io/>
	 web service does not require authentication, so you can use a single
	 
	 Call web service
	 
	 element to obtain the response with the required data. If web service requires authentication, then in addition to the request methods for obtaining the necessary data, you need to set up authentication methods. In a process diagram, you will need to add at least two
	 
	 Call web service
	 
	 elements: the first one calls the authentication method, and the second
	 
	 Call web service
	 
	 element calls the needed functional method, while passing authentication cookie, session Id, etc. as a request parameter.
	3. Populate the request parameter values:
	 
	
	
		* Map the
		 
		 Base Currency
		 
		 parameter to the base currency short name, obtained by the “Read base currency” element. To do this, click
		 ![btn_process_element_settings_lookup00009.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_process_element_settings_lookup00009.png)
		 >
		 
		 Process parameter
		 
		 and select the
		 
		 Read base currency
		 
		 element and its parameter
		 
		 Short name
		 
		 .
		* Specify the value of the
		 
		 Endpoint
		 
		 parameter. For the purposes of this process, using the “latest” endpoint will be enough. Enter “latest” value manually.
5. Add an outgoing conditional flow to the
 
 Parallel gateway (AND)
 
 . Set up the condition for moving down this flow only if the outgoing
 
 Success
 
 parameter of the “Get currency exchange rate from the Fixer web service” element is “true”:
 


	1. In the
	 
	 Condition to move down the flow
	 
	 field, click
	 ![btn_process_element_settings_lookup00010.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/btn_process_element_settings_lookup00010.png)
	 .
	2. In the opened
	 
	 Formula
	 
	 window, on the
	 
	 Process elements
	 
	 tab, select the
	 
	 Get currency exchange rate from the Fixer web service
	 
	 element.
	3. In the right side of the window, double-click the
	 
	 Success
	 
	 parameter.
	4. Add “==true” text after the parameter variable, so that the whole formula text looks like this:
	 
	 #Get currency exchange rate from the Fixer web service.Success#
	 
	 ==true
6. Add an outgoing condition flow to the
 
 Terminate
 
 signal. Set up the condition for moving down this flow only if the outgoing
 
 Success
 
 parameter of the “Get currency exchange rate from the Fixer web service” element is “false”. This way, if the web service call ends in error, the process will terminate (Fig. 6).
7. Add an
 
 Add data
 
 element for each exchange rate that must be updated. For example, to update Euro exchange rate, “Add EUR exchange rate” element properties (Fig. 7):
 

 Fig. 7 – The “Add EUR exchange rate” element properties
 

![scr_process_creation_designer_web_service_add_data.png](/guides/sites/en/files/documentation/user/en/bpms/BPMonlineHelp/chapter_process_creation_end/scr_process_creation_designer_web_service_add_data.png)



 As a result, the process will automatically start every day, at 1:30 AM, and:
 



 The process will terminate if the web service call results in an error.
 


	* check current base currency
	* call web service for exchange rates in relation to the base currency
	* write the updated rates for the selected currencies (in this particular case, Euro, Australian dollar and Ruble) on the
	 
	 Currency rates
	 
	 detail of the
	 
	 Currency
	 
	 lookup (Fig. 8).




