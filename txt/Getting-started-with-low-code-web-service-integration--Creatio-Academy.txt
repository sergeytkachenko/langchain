


 Creatio supports custom REST and SOAP service integration with low-code tools. Creatio will generate and send the request to the web service, receive the response, and extract the needed data using the custom business logic. Use the data received from the web service to create or update Creatio database records, as well as to set up custom business logic or automation.
 



 The general web service integration setup procedure
-----------------------------------------------------



 Set up the basic web service connection parameters in the
 
 Web services
 
 section of the
 
 Studio
 
 workplace. Configure the web service integration parameters there, including:
 


* How Creatio connects to the web service and authenticates in it.
* How Creatio forms requests to the web service.
* How Creatio reads the web service responses.





 Note.
 
 The complexity of the setup procedure largely depends on how the specific web service is implemented and documented. The most common web service integrations do not require a development background.
 




 The general web service integration setup procedure is as follows:
 


1. Add the web service and configure its properties and methods. The settings are different for
 [REST](/docs/7-18/user/customization_tools/web_services/rest/set_up_the_rest_web_service_integration#title-311-22) 
 and
 [SOAP](/docs/8-0/user/customization_tools/web_services/soap/set_up_the_soap_web_service_integration#title-2003-1) 
 services.
2. Set up the web service authentication. This step is optional. The authentication setup is identical for both REST and SOAP services and is available in the
 [Web service authentication](/docs/8-0/user/customization_tools/web_services/authentication/web_service_authentication) 
 article.
3. Test the integration. The settings are different for
 [REST](/docs/7-18/user/customization_tools/web_services/rest/set_up_the_rest_web_service_integration#title-311-42) 
 and
 [SOAP](/docs/8-0/user/customization_tools/web_services/soap/set_up_the_soap_web_service_integration#title-2003-7) 
 services.



 You can start using the integration in custom business processes after that. Learn more about setting up these processes in the
 [Update currency exchange rates with web service integration](https://academy.creatio.com/documents?id=2364) 
 article.
 



 Read more about the
 [REST](/docs/7-18/user/customization_tools/web_services/rest/set_up_the_rest_web_service_integration) 
 and
 [SOAP](/docs/8-0/user/customization_tools/web_services/soap/set_up_the_soap_web_service_integration) 
 setup procedures in the respective articles.
 



 Studying the web service documentation
----------------------------------------



 Before you start setting up the service integration, you need to learn how to call this web service and what kind of response it will return. This information is usually available in the web service documentation.
 



 For example, according to
 
<http://fixer.io/>

 , to call the Fixer web service, you can use these GET requests:
 


* **https://data.fixer.io/api/latest** 
 — to retrieve the latest exchange rates.
* **https://data.fixer.io/api/2000-01-03** 
 — to retrieve the exchange rates for a specific date (in this case, January 3, 2000).




