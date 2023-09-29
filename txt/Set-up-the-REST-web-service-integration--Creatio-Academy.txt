


 Integrate the custom REST services with low-code tools. Creatio will generate and send a request to the web service, receive the response and extract the relevant data. Use the data received from the web service to create or update Creatio records, as well as to set up custom business logic or automation.
 



 Although the general integration setup procedure is the same for all REST services, the details largely depend on the web service specifics.
 



 To
 **set up** 
 an integration with a new web service:
 


1. [Add the web service and configure](/docs/7-18/user/customization_tools/web_services/rest/set_up_the_rest_web_service_integration#title-311-22) 
 its properties and methods.
2. Set up the web service authentication (optional step).
 [The authentication setup](/docs/8-0/user/customization_tools/web_services/authentication/web_service_authentication) 
 is similar for both REST and SOAP services.
3. [Test the integration](/docs/7-18/user/customization_tools/web_services/rest/set_up_the_rest_web_service_integration#title-311-42) 
 .



 You can start using the integration in custom business processes after that. For instance, you can set up an integration with the “Fixer” web service to update the
 
 Currency
 
 lookup data via a business process. Read more about this example in the
 [Update currency exchange rates with web service integration](/docs/7-18/user/bpm_tools/bpm_process_examples/end_to_end_use_cases#title-1612-7) 
 article.
 





 Example.
 
 Set up an integration with the “Fixer” (
 [https://fixer.io/](https://fixer.io) 
 ) REST service to receive the most up-to-date currency exchange rates.
 




 Make sure these parameters are supported:
 


* “
 **endpoint** 
 ” – method address parameter. Returns the actual currency exchange rates in real time.
* **“access\_key”** 
 – request parameter. Use it to pass the service access key.
* **“symbols”** 
 – request parameter. Use it to pass the currency codes. You can specify several comma-separated currency codes.
* “
 **$.base** 
 ” – response parameter. Contains the base currency value used to calculate the currency exchange rates. Euro is the default base currency.
* “
 **$.date** 
 ” – response parameter. Contains the currency exchange rate relevancy date.
* “
 **rates** 
 ” – response parameter. Contains a collection of exchange rates, calculated relative to the base currency. Each exchange rate is a separate nested parameter named after the currency code.



 Set up the web service properties and methods
-----------------------------------------------



 To be able to work with the “Fixer” REST service, sign up on
 <https://fixer.io/>
 and get the API access key.
 



 Creatio lets you set up web service properties and methods
 [automatically](#title-311-8) 
 or
 [manually](#title-311-9) 
 .
 


### 
 Set up the web service properties and methods automatically


1. Go to the
 
 Studio
 
 workplace and open the
 
 Web services
 
 section.
2. Click
 
 New web service
 
 →
 
 REST service
 
 .
3. Specify the web service address and click
 
 OK
 
 (Fig. 1).
 

 Fig. 1 Setting up the web service methods automatically
 

![scr_add_rest_web_service.gif](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_add_rest_web_service.gif)


### 
 Set up the web service properties and methods manually


1. Go to the
 
 Studio
 
 workplace and open the
 
 Web services
 
 section.
2. Click
 
 New web service
 
 →
 
 REST service
 
 .
3. Fill out the fields on the web service
 **properties page** 
 (Fig. 2).
 


| 
 Field
  | 
 Comment
  | 
 Example
  |
| --- | --- | --- |
| 
 Name
  | 
 Enter the name that will be displayed in the
 
 Which method to call?
 
 field of the
 
 Call web service
 
 business process element.
  | 
 Currency exchange rates (Fixer)
  |
| 
 Code
  | 
 Used to interact with this web service in Creatio source code. In this case, it consists of the method name and the “Usr” prefix.
  | 
 Usr
 
 Fixer
  |
| 
 Web service URI
  | 
 The complete web service call address will consist of this URI and the settings specified on the method setup page.
 
 Use the same protocol (HTTP/HTTPS) as your Creatio application.
 
 If the web service is located in an unmodifiable package, you can still edit its URI.
  | 
 http://
 
 data.fixer.io
  |
| 
 Retries on call failure
  | 
 If the web service response returns an error code or times out, Creatio will repeat the request the specified number of times. Keep in mind the response timeout you are going to specify for web service methods when filling out this field.
  | 
 10
  |
| 
 Type
  | 
 Web service type.
  | 
 Default value – REST
  |
| 
 Package
  | 
 The package where Creatio will save this web service integration. The list displays the packages the current user can modify.
  | 
 RestWeb
 
 ServicePackage
  |





 Fig. 2 Filling out the web service properties page
 

![scr_rest_web_service.gif](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_rest_web_service.gif)





 Note.
 
 Creatio saves the web service integrations as configuration items. If a web service configuration item is located in an unmodifiable package, you will only be able to edit its URI. To make other changes to such web service integrations, copy the relevant configuration items to custom packages.
 




 Set up method calling for each web service integration. You can set up several methods per web service.
 





 Note.
 
 You can call any number of web service methods within a single process flow by using multiple
 [Call web service
 
 business process elements](https://academy.creatio.com/documents?product=BPMS&ver=7&id=7141) 
 and passing incoming and outgoing parameters between them.
4. Click
 ![scr_add_button.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_add_button.png)
 to add methods to the
 
 Methods
 
 tab of the web service integration setup page.
5. Study the
 [web service documentation](https://fixer.io/documentation#latestrates) 
 and fill out the
 **method properties** 
 (Fig. 3).
 


| 
 Field
  | 
 Comment
  | 
 Example
  |
| --- | --- | --- |
| 
 Name
  | 
 Enter the name that will be displayed in the
 
 Which method to call?
 
 field for the
 
 Call web service
 
 business process elements.
  | 
 Retrieve the exchange rates
  |
| 
 Code
  | 
 Used to interact with this web service in Creatio source code. In this case, it consists of the method name and the “Usr” prefix.
  | 
 UsrLatest
  |
| 
 Method address
  | 
 Use the value specified in the web service documentation.
 

 You can specify a static value use the method address parameters as “variables” to generate a dynamic method address that will depend on the
 
 Call web service
 
 process element properties. For instance, the “Fixer” web service has a “latest” endpoint that returns the up-to-date currency exchange rates.
 

 If you need more flexibility, pass the endpoint as a method address parameter by specifying the parameter name in curly braces. In this example, we use the “{endpoint}” parameter. You can pass several method address parameters, for example: “{parameter1}/
 
 {parameter2}.”
  | 
 /{endpoint}?
 
 access\_key=
 
 d3\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*4b
 
 &symbols=
 
 USD,GBP,AUD,CAD
  |
| 
 Complete address
  | 
 Creatio automatically generates the complete address. It consists of the web service URI and the method address along with specified parameters and parameter values. The following format is used: “?paramCode1=
 
 value1&
 
 paramCode2=
 
 value2.”
 

 This address is displayed for reference.
 

 The complete address structure is as follows: “Web service URI” + “Method address” + “?” + "A set of request parameters separated by &." For instance: http://
 
 data.fixer.io/
 
 latest?
 
 access\_key=
 
 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*&
 
 symbols=
 
 GBP.
 

 Specify the web service access key in the “access\_key” parameter.
 

 The service will return the exchange rates for the currencies you specify in the “symbols” parameter. For example, use the following request to retrieve the exchange rates for the US dollar and British pound: https://data.fixer.io/latest?symbols=USD,GBP. If you do not pass the “symbols” parameter in the request, the service will return the exchange rates for all supported currencies.
  | 
 http://
 
 data.fixer.io/
 
 api/
 
 {endpoint}?
 
 access\_key=
 
 d3\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*4b
 
 &symbols=
 
 USD,GBP,AUD,CAD
  |
| 
 Request type
  | 
 The request HTTP method. The standard HTTP methods are supported. The request type you have to use is usually listed in the web service documentation.
 

 For example, use the “GET” method to retrieve the currency exchange rates.
  | 
 GET
  |
| 
 Content type
  | 
 Supports the following types: XML (as of version 8.0.1) and JSON.
  | 
 JSON
  |
| 
 Response timeout, ms
  | 
 The time frame before Creatio considers a web service request timed out. If the service returns no response or responds with an error message, Creatio will retry the request after this time frame so long as there are retries available for this service call.
  | 
 By default, “5000”
  |
| 
 Use authentication
  | 
 Use the authentication to access the web service. To enable authentication, set it up on the
 
 Authentication
 
 detail of the web service integration setup page. Learn more:
 [Web service authentication](/docs/8-0/user/customization_tools/web_services/authentication/web_service_authentication) 
 .
  | 
 By default, “false”
  |





 Fig. 3 Web service method properties
 

![scr_web_service_method_properties.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_method_properties.png)



 Set up the request parameters
-------------------------------



 You can add the request parameters manually or import them from the request example by clicking
 
 Quick setup
 
 and selecting the example type (cURL, RAW or JSON) in the menu. Also, you can add request parameters from the “Method address” field. For this example, use a GET request to the “/latest” endpoint to get the most up-to-date currency exchange rates.
 



 Creatio uses the method request parameters to generate the endpoint URL for calling the web service.
 



 The number and type of request parameters depend on the web service specifics. You can
 [import](#title-311-22) 
 the request parameters from the examples or add them
 [manually](#title-311-3) 
 .
 



 The following
 **request parameter types** 
 are available:
 





|  |  |
| --- | --- |
| 
 Method address parameter
  | 
 Use these parameters as variables to generate the request method address.
 

 Enclose the parameter names in curly braces in the
 
 Method address
 
 field to add them to the method address. For instance: {parameterName1}/{parameterName2}, etc.
 

 Upon a web service call, Creatio will replace these variables with the actual method address parameter values specified in the corresponding
 [Call web service](https://academy.creatio.com/documents?product=bpms&ver=7&id=7141)
 business process element. For instance: http://web.service.uri/parameterValue1/parameterValue2.
 

 If you do not specify the parameter value in the element properties yet fill out the
 
 Default value
 
 field, Creatio will use the default value.
 

 The
 
 Required
 
 checkbox is selected and non-editable for this parameter type.
  |
| 
 Body parameter
  | 
 Creatio uses this parameter type to send data of any type (including
 [collections](#HT_chapter_web_service_integration_collection) 
 ) in the request body. Learn more about the POST request method in
 [Wikipedia](https://en.wikipedia.org/wiki/POST_(HTTP)) 
 .
 

 The parameter is not available for the GET method
  |
| 
 Query parameter
  | 
 Creatio will add this parameter type to the request after the method address and the “?” character. Learn more about this parameter in
 [Wikipedia](https://en.wikipedia.org/wiki/Query_string) 
 .
  |
| 
 Header parameter
  | 
 Creatio uses this parameter type to generate request headers. Learn more about HTTP headers in
 [Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields) 
 .
  |
| 
 Cookies parameter
  | 
 Creatio uses this parameter type to pass cookie files in the requests. For example, you can pass a previously-received authentication cookie. Learn more about cookies in
 [Wikipedia](https://en.wikipedia.org/wiki/HTTP_cookie) 
 .
  |



### 
 Set up the request parameters automatically


1. Click the
 ![icn_magic_wand.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/icn_magic_wand.png)
 quick setup button to the right of the
 
 Method address
 
 field. Alternatively, click
 
 Quick setup
 
 at the top of the method setup window and select
 
 From field “Method address”
 
 (Fig. 4):
 

 Fig. 4 Adding parameters from the “Method address” field
 

![scr_web_service_add_method_address.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_add_method_address.png)
2. Select the parameters you need to add to the request in the newly-opened list and click
 
 Save
 
 (Fig. 5):
 

 Fig. 5 The method address parameter list
 

![scr_web_service_method_address_parameters.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_method_address_parameters.png)



 This will add the selected parameters to the request. You can modify the parameter settings to adjust them for further use in the
 
 Call web service
 
 business process element. For example, select the
 
 Required
 
 checkbox for the “Access\_key” parameter.
 


### 
 Set up the request parameters manually


1. Study the
 [web service documentation](https://fixer.io/documentation#latestrates) 
 .
2. Add the
 **request parameters** 
 :
	1. Click
	 
	 Add parameter
	 
	 on the
	 
	 Request parameters
	 
	 tab.
	2. Add the “Endpoint” parameter and fill out its properties (Fig. 6).
	 
	
	
	| 
	 Field
	  | 
	 Comment
	  | 
	 Example
	  |
	| --- | --- | --- |
	| 
	 Name
	  | 
	 The service parameter name.
	  | 
	 Endpoint
	  |
	| 
	 Parameter type
	  | 
	 The service parameter type.
	  | 
	 Method address parameter
	  |
	| 
	 Request code
	  | 
	 The code used in the request.
	  | 
	 endpoint
	  |
	| 
	 Code in Creatio
	  | 
	 Used to interact with this web service in Creatio source code. In this case, it consists of the method name and the “Usr” prefix.
	  | 
	 UsrEndpoint
	  |
	| 
	 Default value
	  | 
	 The default parameter value.
	  | 
	 A constant. Value – “latest”
	  |
	
	
	
	
	
	 Fig. 6 Setting up the “Endpoint” parameter
	 
	
	![scr_web_service_add_method_request_parameter_endpoint.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_add_method_request_parameter_endpoint.png)
	
	
	
	
	
	 Note.
	 
	 Creatio will bind the system settings used during the method parameter setup to the web service package. This streamlines transferring the web service to a different
	 
	 environment
	 
	 .
	3. Add the “API key” parameter and fill out its properties (Fig. 7).
	 
	
	
	| 
	 Field
	  | 
	 Comment
	  | 
	 Example
	  |
	| --- | --- | --- |
	| 
	 Name
	  | 
	 The service parameter name.
	  | 
	 API key
	  |
	| 
	 Parameter type
	  | 
	 The service parameter type.
	  | 
	 Query parameter
	  |
	| 
	 Request code
	  | 
	 The code used in the request.
	  | 
	 access\_key
	  |
	| 
	 Code in Creatio
	  | 
	 Used to interact with this web service in Creatio source code. In this case, it consists of the method name and the “Usr” prefix.
	  | 
	 Usr
	 
	 Access
	 
	 Key
	  |
	| 
	 Required
	  | 
	 If selected, the parameter will be required in the Process Designer. If you specify a default parameter value, this checkbox will become unmodifiable.
	  | 
	 Selected
	  |
	| 
	 Default value
	  | 
	 The default parameter value.
	  | 
	 Constant
	  |
	
	
	
	
	
	 Fig. 7 Setting up the “API key” parameter
	 
	
	![scr_web_service_add_method_request_parameter_api_key.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_add_method_request_parameter_api_key.png)
	4. Add the “Currencies” parameter and fill out its properties (Fig. 8).
	 
	
	
	| 
	 Field
	  | 
	 Comment
	  | 
	 Example
	  |
	| --- | --- | --- |
	| 
	 Name
	  | 
	 The service parameter name.
	  | 
	 Currencies
	  |
	| 
	 Parameter type
	  | 
	 The service parameter type.
	  | 
	 Query parameter
	  |
	| 
	 Request code
	  | 
	 The code used in the request.
	  | 
	 symbols
	  |
	| 
	 Code in Creatio
	  | 
	 Used to interact with this web service in Creatio source code. In this case, it consists of the method name and the “Usr” prefix.
	  | 
	 Usr
	 
	 Symbols
	  |
	| 
	 Required
	  | 
	 If checked, the parameter will be required in the Process Designer. If you specify a default parameter value, this checkbox will become unmodifiable.
	  | 
	 Cleared by default
	  |
	| 
	 Default value
	  | 
	 The default parameter value.
	  | 
	 Constant
	  |
	
	
	
	
	
	 Fig. 8 Setting up the “Currencies” parameter
	 
	
	![scr_web_service_add_method_request_parameter_symbols.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_add_method_request_parameter_symbols.png)



 This will allow Creatio to call the web service via automatically-generated requests. Business processes generate the requests based on the following template:
 






```

http://data.fixer.io/latest?access_key={value}&symbols={value}
```





 The values in curly braces are set to the values of the request parameters. For example:
 






```

http://data.fixer.io/latest?access_key=d3****************************4b&symbols=USD
```






 Set up the response parameters
---------------------------------



 The web service can send cURL, RAW, and JSON responses. To use the data retrieved from the web service, set up the response parameters. Creatio will parse the response and pass the data to these parameters. You can add the response parameters
 [automatically](#title-311-5) 
 or
 [manually](#title-311-6) 
 .
 


### 
 Set up the response parameters automatically



 If the server returns a JSON or RAW response, you can add the response parameters automatically by clicking the
 
 Quick setup
 
 button.
 


1. Click
 
 Quick setup
 
 and select
 
 Example in JSON
 
 from the “From response example” menu block (Fig. 9).
 

 Fig. 9 Setting up the response parameters from a JSON example
 

![scr_web_service_response_json.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_response_json.png)
2. Enter the server’s JSON response (Fig. 10). This code will display in the browser if you go to the URL that calls the web service.
 

 Fig. 10 A JSON response
 

![scr_web_service_json_code.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_json_code.png)



 Click
 
 Next
 
 .
3. This will open a parameter list:
	* “
	 **Success** 
	 ” – indicates whether the request was successful.
	* “
	 **Timestamp** 
	 ” – an object with a UNIX time stamp that indicates the time when the service collected this data.
	* “
	 **Base** 
	 ” – specifies the base currency relative to which the service calculated the exchange rates. For example,
	 **"base":"EUR"** 
	 indicates that the service calculated the exchange rates relative to euro.
	* “
	 **Date** 
	 ” – specifies the exchange rate relevancy date. For example,
	 **“date”:”2021-05-26”** 
	 indicates that the service calculated the exchange rates for May 26, 2021.
	* “
	 **Rates** 
	 ” – contains an array of nested parameters. Each nested parameter contains the exchange rate between the base currency and one of the supported currencies.
	 
	 For example,
	 **"rates":{"USD":1.222845,"GBP":0.862279,"AUD":0.635032,"CAD":0.676577}** 
	 in the response indicates that the service returned the exchange rates for US dollar (
	 **"USD": 1.222845** 
	 ), British pound (
	 **"GBP": 0.862279** 
	 ), Australian dollar (
	 **"AUD":0.635032** 
	 ), and Canadian dollar (
	 **"CAD":0.676577** 
	 ).
 Specify the parameters you need to add to the response and click
 
 Save
 
 (Fig. 11):
 




 Fig. 11 List of parameters from the JSON example
 

![scr_web_service_response_parameters.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_response_parameters.png)



 This will add all the selected parameters to the response. You can modify the parameter settings. For example, change the data type of the currency rate to “Decimal” to adjust it for further use.
 


### 
 Set up the response parameters manually


1. Study the
 [web service documentation](https://fixer.io/documentation#latestrates) 
 .
2. Add the
 **response parameters** 
 :
	1. Go to the
	 
	 Response parameters
	 
	 tab and click
	 
	 Add parameter
	 
	 .
	2. Add the “Base currency” parameter and fill out its properties (Fig. 12).
	 
	
	
	| 
	 Field
	  | 
	 Comment
	  | 
	 Example
	  |
	| --- | --- | --- |
	| 
	 Name
	  | 
	 The service parameter name.
	  | 
	 Base currency
	  |
	| 
	 Parameter type
	  | 
	 The service parameter type.
	  | 
	 Body parameter
	  |
	| 
	 Path to element (JSONPath)
	  | 
	 The value must be in JSON format. For example, JSONPath “$.base” receives the “base” parameter value in the web service response.
	  | 
	 $.base
	  |
	| 
	 Code in Creatio
	  | 
	 Used to interact with this web service in Creatio source code. In this case, it consists of the method name and the “Usr” prefix.
	  | 
	 Usr
	 
	 Base
	 
	 Currency
	  |
	| 
	 Data type
	  | 
	 The service parameter data type. A parameter with nested elements must have an “Object” data type.
	  | 
	 Text
	  |
	| 
	 Is array
	  | 
	 An array parameter value cannot be set in the process designer’s “Call web service” element. Use the “Script task” element instead. The parameter with an “Object” data type must be an array.
	  | 
	 Cleared by default
	  |
	| 
	 Default value
	  | 
	 The default parameter value.
	  | 
	 A constant. Value – EUR
	  |
	
	
	
	
	
	 Fig. 12 Setting up the “Base currency” request parameter
	 
	
	![scr_web_service_add_method_response_parameter_base_currency.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_add_method_response_parameter_base_currency.png)
	3. Add the “Date” parameter and fill out its properties (Fig. 13).
	 
	
	
	| 
	 Field
	  | 
	 Comment
	  | 
	 Example
	  |
	| --- | --- | --- |
	| 
	 Name
	  | 
	 The service parameter name.
	  | 
	 Date
	  |
	| 
	 Parameter type
	  | 
	 The service parameter type.
	  | 
	 Body parameter
	  |
	| 
	 Path to element (JSONPath)
	  | 
	 The value must be in JSON format. For example,
	 **JSONPath** 
	 “$.date” receives the “date” parameter value in the web service response.
	  | 
	 $.date
	  |
	| 
	 Code in Creatio
	  | 
	 Used to interact with this web service in Creatio source code. In this case, it consists of the method name and the “Usr” prefix.
	  | 
	 Usr
	 
	 Date
	  |
	| 
	 Data type
	  | 
	 The service parameter data type A parameter with nested elements must have an “Object” data type.
	  | 
	 Date
	  |
	| 
	 Is array
	  | 
	 An array parameter value cannot be set in the process designer’s “Call web service” element. Use the “Script task” element instead. The parameter with an “Object” data type must be an array.
	  | 
	 Cleared by default
	  |
	| 
	 Default value
	  | 
	 The default parameter value.
	  | 
	 Constant
	  |
	
	
	
	
	
	 Fig. 13 Setting up the “Date” parameter
	 
	
	![scr_web_service_add_method_response_parameter_date.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_add_method_response_parameter_date.png)
	4. Add the “RatesAUD” parameter and fill out its properties (Fig. 14).
	 
	
	
	| 
	 Field
	  | 
	 Comment
	  | 
	 Example
	  |
	| --- | --- | --- |
	| 
	 Name
	  | 
	 The service parameter name.
	  | 
	 Rates AUD
	  |
	| 
	 Parameter type
	  | 
	 The service parameter type.
	  | 
	 Body parameter
	  |
	| 
	 Path to element (JSONPath)
	  | 
	 The value must be in JSON format. For example, JSONPath “$.rates.AUD” receives the “AUD” parameter value in the web service’s response.
	  | 
	 $.rates.AUD
	  |
	| 
	 Code in Creatio
	  | 
	 Used to interact with this web service in Creatio source code. In this case, it consists of the method name and the “Usr” prefix.
	  | 
	 Usr
	 
	 Rates
	 
	 AUD
	  |
	| 
	 Data type
	  | 
	 The service parameter data type A parameter with nested elements must have an “Object” data type.
	  | 
	 Decimal
	  |
	| 
	 Is array
	  | 
	 An array parameter value cannot be set in the process designer’s “Call web service” element. Use the “Script task” element instead. The parameter with an “Object” data type must be an array.
	  | 
	 Cleared by default
	  |
	| 
	 Default value
	  | 
	 The default parameter value.
	  | 
	 Constant
	  |
	
	
	
	
	
	 Fig. 14 Setting the “Rates AUD” parameter
	 
	
	![scr_web_service_add_method_request_parameter_rate_usd.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_add_method_request_parameter_rate_usd.png)
	
	
	
	
	
	 Note.
	 
	 JSONpath “$.rates.USD” receives the “AUD” parameter value. “AUD” is a nested parameter of the “rates” parameter in the web service response.
	5. Set up the response parameters for the other necessary exchange rates in a similar way (Fig. 15).
	 
	
	 Fig. 15 Setting up the web service response parameters
	 
	
	![scr_web_service_add_method_response_parameter.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_add_method_response_parameter.png)
3. Click
 
 OK
 
 to save the settings.




 Set up the “collection” type response and request parameters
---------------------------------------------------------------



 A collection (or an array) is a set of elements. Creatio can pass collections to the web service and parse the service responses that contain collections. You can set up both request and response “collection” parameters, provided the web service can receive and/or send arrays.
 



**Collection parameter types** 
 :
 


* **Simple collection** 
 . You can make any parameter a collection by selecting the “Is array” checkbox in the parameter properties. Simple collections are arrays with data of a single type. Each value is a separate collection element. For example, “1, 2, 3” is a simple array of integer values, “Boston, New York, Chicago” is a simple array of string values, etc.
* **Object collection** 
 . A root parameter (or an object) that contains nested parameters. Each item in an object collection can have a different parameter type. These collection item parameters are nested within the root parameter. For example, a contact collection can have nested parameters for contact name, date of birth, and age (Fig. 16).




 Fig. 16 An example of a contact collection
 

![scr_web_service_object_collection_example.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_object_collection_example.png)



 The collection with such a structure would look like this:
 





| 
 Contact name
  | 
 Birth date
  | 
 Age
  |
| --- | --- | --- |
| 
 John Best
  | 
 04/12/1991
  | 
 30
  |
| 
 Andrew Barber
  | 
 04/10/1985
  | 
 36
  |
| 
 Alice Phillips
  | 
 05/12/1989
  | 
 31
  |




 Creatio can pass collections in web service requests and parse web service responses that contain collections. You can set up both request and response “collection” parameters, provided the web service can receive and/or send arrays.
 





 Note.
 
 You can only select the “collection” data type for the “Body parameter” type parameters. This parameter type is not available for GET requests. However, it is available for GET responses.
 




 To set up a collection:
 


1. Study the
 [web service documentation](https://fixer.io/documentation#latestrates) 
 .
2. Add the “Receive contacts” method.
3. To set up a collection request parameter, specify “Object” in the
 
 Data type
 
 field. Creatio will select the
 
 Is array
 
 checkbox automatically (Fig. 17).




 Fig. 17 Adding a parameter to a collection
 

![scr_web_service_object.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_object.png)



 That way, the web service “collection” response parameter that receives the contact records from the server will look like this (Fig. 18):
 




 Fig. 18 Setting up the request parameters
 

![scr_web_service_object_parameters.png](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_web_service_object_parameters.png)





 Note.
 
 The value of the nested parameter’s JSONPath is a suffix of the root parameter’s JSONPath. For example, if the root parameter has the “$.records” value in the JSONPath field and the “$.records.name” value should be specified for the “Name” nested parameter, you need to specify only “$.records” in the “Path to element” field.
 




 You can use the web service response parameters of the collection type as incoming parameters in the “Call web service” business process element. Learn more:
 [Call web service
 
 process element](https://academy.creatio.com/documents?product=BPMS&ver=7&id=7141) 
 .
 



 Test the REST service integration
-----------------------------------



 Test the integration setup before using the data received from the web service with custom business logic.
 



 Since Creatio version 7.18.0, you can test a REST integration in the UI without creating a
 [test business process](/docs/8-0/user/customization_tools/web_services/soap/set_up_the_soap_web_service_integration#title-2003-7) 
 .
 



 To
 **test the REST web service integration** 
 :
 


1. Go to the
 
 Studio
 
 workplace and open the
 
 Web services
 
 section.
2. Open the page of the web service whose integration you want to test. For example, “Currency exchange rates (Fixer).”
3. Open the “Retrieve the exchange rates” method on the
 
 Methods
 
 detail of the web service integration setup page.
4. Click
 
 Send a test request
 
 on the method setup page.
5. Specify the values for the method call parameters.
 


| 
 Parameter
  | 
 Value
  |
| --- | --- |
| 
 Endpoint
  | 
 latest
  |
| 
 API key
  | 
 d3\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*4b
  |
| 
 Currencies
  | 
 USD,GBP,AUD,CAD
  |
6. Click
 
 Send request
 
 (Fig. 19).



 As a result of the test request, the web service will send a response. The values of the response parameters are displayed on the
 
 Response parameters
 
 tab in the corresponding fields (Fig. 19). View the request and response formatted as JSON or raw HTTP on other tabs.
 




 Fig. 19 Testing the REST service integration
 

![scr_send_test_request.gif](/docs/sites/en/files/images/NoCode_Customization/web_rest_service/7.18/scr_send_test_request.gif)



 If the web service integration is configured with an error, the test request will result in a response with empty parameter values. In this case, check all of the web service’s settings and try again.
 



 Once you test the web service integration, you can start using the service in custom business processes. Read more about this example in the
 [Update currency exchange rates with web service integration](/docs/7-18/user/bpm_tools/bpm_process_examples/end_to_end_use_cases#title-1612-7) 
 article.
 



 Depending on the web service specifics, you may need to authenticate the service before it becomes available. Read more:
 [Set up the web service authentication](/docs/8-0/user/customization_tools/web_services/authentication/web_service_authentication) 
 .
 




