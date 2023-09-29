


 The
 
 Call web service
 
 process element is a means of sending web service method requests and processing the response as part of a business process flow. Before using this element, you need to set up
 [web service integration](https://academy.bpmonline.com/documents?product=studio&ver=7&id=1862) 
 in the
 
 Web services
 
 section of the system designer.
 



 The function of the
 
 Call web service
 
 element largely depends on the integrated web service. For example, you can use this element to obtain latest exchange rates as part of a process flow (Fig. 1), by calling a web service, which returns currency exchange rates in its response.
 




 Fig. 1 Calling a web service as part of a business process and displaying results
 




[![scr_chapter_process_designer_call_web_servce_example.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_call_web_servce_example.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_call_web_servce_example.png)






 Attention.
 
 Detailed instructions on
 [setting up integration](https://academy.creatio.com/documents?id=1862) 
 with the “http://fixer.io/” web service are available in a separate article.
 




 When its incoming flows are activated, the
 
 Call web service
 
 element:
 


1. Executes the needed web service method request with the specified request parameters.
2. Waits for a response from the web service, according to integration settings.
3. Records results to its outgoing parameters.
4. Activates own outgoing flows.



 Set up [Call web service] element properties
----------------------------------------------



 To integrate a web service into your business process, add the
 
 Call web service
 
 element to the Process Designer working area, select a web service and method to call, then specify the parameter values on the
 
 Call web service
 
 element setup area (Fig. 2).
 




 Fig. 2
 
 The
 
 Call web service
 
 element setup area
 




[![scr_chapter_process_designer_web_service_properties.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_web_service_properties.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_web_service_properties.png)





 Which service to call?
 
 – select one of previously set up web service integrations For example, if you previously set up integration with the “Fixer” currency exchange rate service, you will be able to select it here. Click the
 ![btn_basis_filters_add_condition.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/btn_basis_filters_add_condition.png)
 button to open a new web service integration page. You can set up integration with a new web service on this page. If a web service is already selected, click
 ![icn_open_desiner.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/icn_open_desiner.png)
 to open its setup area.
 




 Which method to call?
 
 – select a web service method to call when executing the web service request. The available values of this parameter depend on web service integration specifics.
 




 Maximum execution time, in seconds
 
 – Limit total time for calling the web service by this element. The limit includes retries. When the execution time is exceeded and there have been responses with error status (400, etc.), the outgoing parameters will be populated according to the last received response from the web service.
 




 Request parameters
 
 – If the selected method has request parameters, they will become available here, once a method is selected. Business processes treat them as “incoming” parameters for the corresponding
 
 Call web service
 
 process element.
 



 For example, according to the web service information available at
 <http://fixer.io/>
 , we have set up integration with this web service using the following request parameters:
 


* Base currency
 
 – the base currency for exchange rates to retrieve.
* API key
 
 – the web service API key. You will need to register on
 <https://fixer.io/>
 . to obtain your API key.
* Endpoint
 
 – the web service endpoint (will be added right after URI and before the query parameters). In the case of
 <http://fixer.io/>
 it can be either “latest” – to request latest available exchange rates, or a specific date in the text format (such as “2000-01-03”) – to request rates for that date. All required parameters should be populated. If left empty, the query parameters will still be part of request, but will not have values. For example: “?parameter-With-Value-1=Value-1&parameter-With-No-Value-1&parameter-With-No-Value-2”.





 Note.
 
 You can enter request parameter values manually or map them to other process parameters. Working with parameter values is covered in a separate article.
 [Read more >>>](https://academy.creatio.com/documents?id=7054) 






 Work with request parameters of the collection type
------------------------------------------------------



 If the request parameter is a collection (the “Is array” checkbox is selected in the properties of the parameter at the web service record), the nested collection parameters will be displayed under the collection name in the process element parameters (Fig. 3). For example, Creatio “batch query” service can insert several records (e.g. contacts) to Creatio. To do this, the service would require information to write into the fields of each inserted record (e.g. contact names and types). In this case, you can pass the values as a request parameter of an array type, where “Name” and “Type” will be nested parameters and each instance of the collection would represent data for a separate contact record.
 




 Fig. 3
 
 An example of request parameters, one of which is a collection
 




[![chapter_process_designer_collection_params.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/chapter_process_designer_collection_params.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/chapter_process_designer_collection_params.png)




 The values of collection parameters of one
 
 Call web service
 
 process element can be mapped to the nested parameters of another collection of a
 
 Read data
 
 or
 
 Call web service
 
 process element(Fig. 4, Fig. 5).
 




 Fig. 4
 
 Mapping values for collection parameters
 




[![chapter_process_designer_collection_select_value.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/chapter_process_designer_collection_select_value.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/chapter_process_designer_collection_select_value.png)





 Fig. 5
 
 Selecting a nested parameter of another collection to map
 




[![chapter_process_designer_collection_select_parameter.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/chapter_process_designer_collection_select_parameter.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/chapter_process_designer_collection_select_parameter.png)




 The parameters of the collection of process elements can be mapped to the process parameter of the “Collection of values” data type (Fig. 6).
 




 Fig. 6
 
 Adding a collection process parameter
 




[![chapter_process_designer_collection_process_parameter.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/chapter_process_designer_collection_process_parameter.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/chapter_process_designer_collection_process_parameter.png)




 Process web service call errors
---------------------------------



 When the
 
 Call web service
 
 element is activated, it executes a web service request, obtains and parses the response, and populates its outgoing parameters. Each
 
 Call web service
 
 element has the two outgoing parameters for processing errors –
 
 Success
 
 ,
 
 Http status code
 
 :
 


* If the call is successful (response code is <400) the
 
 Success
 
 parameter will be set to “true”.
* If the call resulted in an error (response code is 400 and up), the
 
 Success
 
 outgoing parameter will be set to “false” and the
 
 Http status code
 
 parameter will be populated. Use these parameters to process errors of the web service call in the business process. You can call the web service later automatically, use other call parameters or terminate the process.



 Work with web service response
--------------------------------



 Each response parameter that you set up for a web service method will be added as an additional outgoing parameter to the
 
 Call web service
 
 element, where this method is selected in the
 
 Which method to call
 
 property.
 



 To use this information in your business processes, map process, and process element parameters to the outgoing parameters of the
 
 Call web service
 
 element.
 



 EXAMPLE
 



 In the current “Fixer” web service integration, the following outgoing parameters will be available in addition to the error processing parameters: “Base currency” (“string” parameter), “Date” (“date” parameter), and a separate decimal parameter for each currency rate, i.e., “RatesAUD”, “RatesEUR”, etc. You can display the received data via the
 [pre-configured page](https://academy.creatio.com/documents?id=7008) 
 by setting up its field connection with the corresponding outgoing parameters of the
 
 Call web service
 
 element (Fig. 7, Fig. 8). As a result, the page fields will contain the data received from the web service response.
 





 Note.
 
 The list of actions to display the web service data is described in the “Testing the web service integration” article. More information about setting up the parameters can be found in the “
 [Process parameters](https://academy.creatio.com/documents?id=7054) 
 ” article.
 





 Fig. 7 Setting up page parameters on the pre-configured page element setup area
 




[![scr_chapter_process_designer_preset_page_currency_map.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_preset_page_currency_map.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/scr_chapter_process_designer_preset_page_currency_map.png)





 Fig. 8 Mapping parameters of the pre-configured page to the
 
 Call web service
 
 element
 




[![scr_process_designer_map_web_service_params.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/scr_process_designer_map_web_service_params.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/scr_process_designer_map_web_service_params.png)






 Work with response parameters of the collection type
-------------------------------------------------------




 Response parameters of a web service can also be collections. The Response parameters are available on the
 
 Parameters
 
 tab of the
 
 Call web service
 
 element in the advanced mode (Fig. 9). The nested collection parameters will be displayed under the collection name.
 




 Fig. 9
 
 Collection in response parameters
 




[![chapter_process_designer_collection_response.png](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/chapter_process_designer_collection_response.png)](https://academy.creatio.com/sites/default/files/documents/docs_en/technic/BPMS/7.16.0/BPMonlineHelp/chapter_process_designer/chapter_process_designer_collection_response.png)




 The values of collection parameters of a
 
 Call web service
 
 process element can be mapped to the nested parameters of another collection of a
 
 Read data
 
 or
 
 Call web service
 
 process element (Fig. 4, Fig. 5).Additionally, each item of the collection can be mapped to an individual subprocess instance in the
 
 Subprocess
 
 element, Read more about using data collections in the “
 [Process collections](https://academy.creatio.com/documents?id=2316) 
 ” article.
 



 Attention
 



 The
 
 Call web service
 
 may produce a tree-like data collection. The
 
 Subprocess
 
 element can only parse flat structures fully. When dealing with a multi-level data collection, the
 
 Subprocess
 
 element will only extract and make available for mapping top-level parameters and none of the deeply nested structures.
 




