


 Customizable HTTP response headers are required to send headers of
 **content security policy** 
 (CSP). Creatio automatically generates an HTTP header in every server response to prevent the connection of external resources that violate its security policies.
 





 Attention.
 
 We strongly recommend managing HTTP response headers using the
 
 HTTP response headers
 
 lookup instead of the Creatio configuration file. Learn more about transferring existing headers from the configuration file to the
 
 HTTP response headers
 
 lookup below.
 




 Set up HTTP response headers
------------------------------


1. Click
 ![btn_system_designer00001.png](/guides/sites/en/files/documentation/user/en/sys_settings_lookups/BPMonlineHelp/add_lookups/btn_system_designer00001.png)
 in the top right to open the System Designer.
2. Go to the
 
 System setup
 
 block →
 
 Lookups
 
 .
3. Open the
 
 HTTP response headers
 
 lookup.
4. Create an HTTP header. To do this, click
 
 New
 
 and fill out the required fields:
 
 Header name
 
 ,
 
 Header value
 
 .
 




 Fig. 1 Create an HTTP header
 

![scr_chapter_google_synchronization_administrator_workplace.png](/docs/sites/en/files/images/Setup_and_Administration/http_response_headers/scr_chapter_new_http_response.png)



 If the Creatio configuration file and lookup contain HTTP header responses whose names match, headers from the configuration file take priority.
 



 You cannot
 **change or delete** 
 headers added to the lookup. If you attempt to change the header, you will receive a corresponding notification.
 




 Fig. 2 Error when deleting an HTTP header
 

![scr_chapter_google_synchronization_administrator_workplace.png](/docs/sites/en/files/images/Setup_and_Administration/http_response_headers/scr_chapter_error_message.png)



 By default, Creatio uses the header for all requests and request methods (“\*”). You can redefine the following optional fields if needed:
 


* Endpoint
 
 . Relative URL path.
* Request Method
 
 . Request method. Available values: GET, OPTIONS, POST, PUT, DELETE, or PATCH.



 View the setup results of custom HTTP headers in an HTTP response.
 




 Fig. 3 Custom HTTP header
 

![scr_chapter_google_synchronization_administrator_workplace.png](/docs/sites/en/files/images/Setup_and_Administration/http_response_headers/scr_chapter_http_response_header_result.png)



 If the lookup contains headers that have matching names, the header selection priority is as follows:
 





| 
 Endpoint
  | 
 Response Method
  | 
 Priority
  |
| --- | --- | --- |
| 
 /api/HealthCheck/Ping
  | 
 GET
  | 
 1
  |
| 
 /api/HealthCheck/Ping
  | 
 \*
  | 
 2
  |
| 
 \*
  | 
 POST
  | 
 3
  |
| 
 \*
  | 
 \*
  | 
 4
  |




 If the database contains headers that have matching names, the header selection priority for requests sent from a specific endpoint and with a specific method is as follows:
 


1. Header whose endpoint and request method match verbatim.
2. Header whose endpoint matches verbatim and the request method is “\*.”
3. Header whose endpoint is “\*” and the request method matches verbatim.
4. Header whose endpoint is “\*” endpoint and the requeest method is “\*.”



 To enable and disable headers in HTTP responses, use the
 
 UseHttpHeaderProvider
 
 flag in the
 
 web.config
 
 configuration file of the Creatio root directory.
 






```
<add key="UseHttpHeaderProvider" value="true" />
```





 Transfer headers from the Creatio configuration file to the lookup
--------------------------------------------------------------------



 To transfer custom HTTP headers from the
 
 web.config
 
 configuration file of the Creatio root directory to the lookup, take the following steps:
 


1. Go to the
 
 <customHeaders>
 
 section of the configuration file. The section contains headers in the following format:
 






```
<add name="SomeHeaderName" value="SomeHeaderValue" />
```





 where:
 


	* name
	 
	 is the header name.
	* value
	 
	 is the header value.
2. Transfer the headers from the section to the
 
 HTTP response headers
 
 lookup. Specify the
 
 name
 
 attribute value in the
 
 Header name
 
 field and
 
 value
 
 attribute value in the
 
 Header value
 
 field. Leave default values (“\*”) in the
 
 Endpoint
 
 and
 
 Request Method
 
 fields.



 For example, the configuration file contains the following header:
 






```
<add name="X-Frame-Options" value="SAMEORIGIN" />
```





 Transfer it to the lookup as follows:
 




 Fig. 4 Add an HTTP header to the lookup
 

![scr_chapter_google_synchronization_administrator_workplace.png](/docs/sites/en/files/images/Setup_and_Administration/http_response_headers/scr_chapter_http_response_moving.png)




