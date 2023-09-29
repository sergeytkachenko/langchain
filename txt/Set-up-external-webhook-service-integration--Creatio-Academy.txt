



 This functionality is available for Creatio 8.0.5 and later.
 




**Webhook** 
 is an extension of a web app functionality via callbacks. Third-party users and developers can maintain, change, and manage the callbacks. Webhooks let you track events of any third-party app that can send webhooks to Creatio without coding or managing Creatio infrastructure. You can integrate any third-party app that can send webhooks with Creatio (Fig. 1), including certain landing page builders that support webhook functionality, for example, Landingi. Learn more in a separate article:
 [Integrate with landing pages and web forms](https://academy.creatio.com/documents?id=2414) 
 .
 



 You can use webhooks functionality to integrate Creatio and any tools and products. Previously, you needed to write source code and create your own app infrastructure to work with webhooks. Now webhook functionality lets you track the event in any third-party app that can send webhooks to Creatio with no need to write source code or manage an app infrastructure.
 




 Fig. 1 Mechanism that integrates a third-party app that can send webhooks with Creatio
 

![](/sites/default/files/documentation/sdk/ru/BPMonlineWebSDK/Screenshots/Webhooks/8.0/scr_IntegrationSchema.png)



 To
 **integrate an external webhook service with Creatio** 
 :
 


1. Connect the external webhook service.
 [Read more >>>](#title-2501-1)
2. Set up field mapping (optional).
 [Read more >>>](#title-2501-2)



 Before you start integrating an external webhook service with Creatio, set up the third-party app. Learn more about the setup in the official vendor documentation.
 



 Step 1. Connect the external webhook service
----------------------------------------------



 If you use Creatio
 **on-site** 
 , set up OAuth authentication to enable secure connection for webhook service. To do this follow the instructions in a separate article:
 [Set up OAuth 2.0 authorization for integrated applications](https://academy.creatio.com/documents?id=2396) 
 . Use the following parameters for article and create the record in the
 
 OAuth 2.0 integrated applications
 
 section:
 


* Name
 
 : Webhook Account Service Identity
* Application URL
 
 : https://webhooks.creatio.com



 These parameters are not localizable.
 



 This is a one-time procedure.
 



 The general procedure to connect the external webhook service includes the following steps:
 


1. **Get your API key** 
 . Creatio identifies an external webhook service via API key. This step differs based on your Creatio version.
 




 For Creatio version 8.0.7 and later
 




	1. Open the
	 
	 Contacts
	 
	 section or any Freedom UI section that uses the “Records and business processes” template.
	2. Click
	 
	 Data import
	 
	 →
	 
	 Web forms and pages
	 
	 in the top right.
	3. Click
	 
	 Click to get your API key
	 
	 (Fig. 2).


 Fig. 2 Get an API key for external webhook service integration
 

![](/sites/default/files/documentation/sdk/ru/BPMonlineWebSDK/Screenshots/Webhooks/8.0/scr_GetYourApiKey.png)






 For Creatio version 8.0.5-8.0.6
 




 Contact Creatio support (
 <support@creatio.com>
 ) to receive the API key. Creatio support generates and binds the API key to your Creatio instance.
 







 Attention.
 
 We recommend receiving a unique API key for each webhook service you use. For example, use different API keys for Landingi and Instapage landing page builders.
 




 Get another API key if you want to receive webhooks in another Creatio instance.
2. **Add the API key to URL** 
 for receiving webhooks from an external webhook service. The URL format is as follows:
 






```

https://webhooks.creatio.com/webhooks/[API_KEY]

```





 where
 


	* https://webhooks.creatio.com/webhooks/
	 
	 is the Creatio service URL to receive webhooks. Unmodifiable.
	* [API\_KEY]
	 
	 is a personal API key that identifies the external webhook service in your Creatio instance.
3. **Add the URL to the external webhook service** 
 . Take this step only for services that support this feature.
 



 Keep in mind the following webhook
 **limitations** 
 when configuring them in an external service:
 


	* Only
	 
	 POST
	 
	 request method is supported.
	* Only
	 
	 JSON
	 
	 and
	 
	 FormData
	 
	 data types of the request are supported.
	* Any webhook sending frequency is supported.



 Step 2. Set up field mapping (optional)
-----------------------------------------



 Set up field mapping to add a Creatio record based on the webhook. By default, the
 
 Create object records based on incoming webhook
 
 business process (
 
 Webhooks to entity
 
 business process in Creatio 8.0.5-8.0.6) attempts to parse the webhook and add a Creatio record. If the webhook parameters match the object code and field names, Creatio adds a record based on the webhook. Otherwise, Creatio receives a webhook without adding a record. If you want to receive a webhook in Creatio without adding a record, deactivate or customize the business process. Learn more in a separate article:
 [Process webhooks in Creatio](https://academy.creatio.com/documents?id=2411) 
 .
 



 View an example of the webhook that the
 
 Create object records based on incoming webhook
 
 business process can parse below.
 






```

{
    "Contact":"New user",
    "Email":"new_user@gmail.com",
    "MobilePhone":"+1 617 221 5187",
    "CountryId": "f8af0e88-f36b-1410-fa98-00155d043204"
    "EntityName":"Lead"
}

```





 where
 


* Contact
 
 is the code of the object column.
* New user
 
 is the value of the object column.
* EntityName
 
 is the name of the required parameter.
* Lead
 
 is the code of the Creatio object.



 You can set up field mapping automatically or manually. The exact procedure depends on the webhook service that you use.
 


### 
 Set up field mapping automatically



 The general procedure to set up field mapping automatically includes the following steps:
 


1. Retrieve the index of Creatio objects and their columns.
 [Read more >>>](#title-2501-4)
2. Specify the Creatio object to add based on the webhook.
 [Read more >>>](#title-2501-5)
3. Map the webhook form parameters to Creatio object fields.
 [Read more >>>](#title-2501-6)


#### 
 1. Retrieve the index of Creatio objects and their columns



 Creatio implements a service that lets you receive a real-time index of Creatio objects and their column names. This streamlines the field mapping of the external service to Creatio objects.
 



 To retrieve the index of Creatio objects and their columns, use the following
 **endpoints** 
 :
 


* /get\_entities/[API\_KEY]
 
 . Retrieves the index of mappable Creatio objects.
 







```

POST https://webhooks.creatio.com/get_entities/[API_KEY]

{
    "apiKey": "string"
}

```




```

{
    "entities": [
        {
            "name": "Contact",
            "caption": "Contact",
            "formId": "6e05fd0c-7212-45bf-8b6e-f263423e97b1"
        },
        {
            "name": "Lead",
            "caption": "Lead",
            "formId": "2b755431-dd89-4f4c-b97b-9a15ebe9cea9"
        },
        {
            "name": "Order",
            "caption": "Order",
            "formId": "4b1f24dd-95ee-4049-b611-dfd701f0cab1"
        }
    ]
}

```
* /get\_entity\_description/[API\_KEY]/[SOME\_OBJECT\_NAME]
 
 . Retrieves the column index of the Creatio object.
 







```

POST https://webhooks.creatio.com/get_entity_description/[API_KEY]/[SOME_OBJECT_NAME]

{
    "apiKey": "string",
    "entityName": "string"
}


```




```

// Response for the [Contact] object.
{
    "value": {
        "entityModel": {
            "fields": [
                {
                    "required": true,
                    "name": "Id",
                    "net_type": "System.Guid",
                    "caption": "Id"
                },
                {
                    "required": true,
                    "name": "Name",
                    "net_type": "System.String",
                    "caption": "Full name"
                },
                {
                    "required": false,
                    "name": "BirthDate",
                    "net_type": "System.DateTime",
                    "caption": "Birth date"
                },
                {
                    "required": false,
                    "name": "Age",
                    "net_type": "System.Int32",
                    "caption": "Age"
                },
                {
                    "required": false,
                    "name": "IsEmailConfirmed",
                    "net_type": "System.Boolean",
                    "caption": "IsEmailConfirmed"
                }
            ],
            "name": "Contact"
        },
        "isSuccess": true,
        "status": "ok",
        "code": 0
    },
    "statusCode": 200
}

```



 You can use endpoints to work with base Creatio objects listed in the
 
 Webhook entities
 
 lookup. View the codes of base Creatio objects listed in the
 
 Webhook entities
 
 lookup by default in the table below.
 




 Codes of base Creatio objects listed in the
 
 Webhook entities
 
 lookup by default
 


| 
 Object
  | 
 Object code
  |
| --- | --- |
| 

 Contact
 
 | 

 Contact
 
 |
| 

 Lead
 
 | 

 Lead
 
 |
| 

 Order
 
 | 

 Order
 
 |
| 

 Form Submit
 
 | 

 FormSubmit
 
 |




 To
 **map another Creatio object** 
 , add it to the
 
 Webhook entities
 
 lookup.
 


#### 
 2. Specify the Creatio object



 By default, Creatio lets you add any object based on the webhook. To do this, set the
 
 EntityName
 
 webhook parameter to the code of the needed object. The way to set the parameter depends on the webhook service. By default, you can use Creatio objects listed in the
 
 Webhook entities
 
 lookup as the
 
 EntityName
 
 parameter value. Learn more about the index of Creatio objects listed in the
 
 Webhook entities
 
 lookup in the table above.
 





 Note.
 
 Use the Creatio object code, not the name, as the
 
 EntityName
 
 parameter value. Learn more about the object code in a separate article:
 [Object](https://academy.creatio.com/documents?id=15107&anchor=title-3028-6) 
 .
 



#### 
 3. Map the webhook form parameters to Creatio object fields



 To map the webhook form parameters to Creatio object fields, select the needed fields. Make sure the values match the field codes of the Creatio object.
 




 Follow these
 **recommendations** 
 when mapping the webhook form parameters to Creatio object fields:
 


* Ensure the field type in the form matches the Creatio field type. For example, if you need to transfer the contact birth date, use the
 
 Date
 
 field type.
* Use the field code of the Creatio object with the
 
 Id
 
 suffix in the form as the name of the parameter that has the
 
 Lookup
 
 field type. For example,
 
 CountryId
 
 .
* Use the record ID of the Creatio lookup in the form as the value of the parameter that has the
 
 Lookup
 
 field type. For example, to set the value of the
 
 Country
 
 field in the
 
 Lead
 
 object to
 
 Canada
 
 , the webhook must look as follows:
 






```

"CountryId": "f8af0e88-f36b-1410-fa98-00155d043204"

```





 where
 
 f8af0e88-f36b-1410-fa98-00155d043204
 
 is the
 
 Canada
 
 record ID in the
 
 Countries
 
 lookup.
* If the webhook service cannot set the
 
 Dropdown
 
 field type to a specific value, pass the value via a separate text field, for example,
 
 Notes
 
 . Do not pass the value via the
 
 Lookup
 
 field type.



 Creatio lets you set up custom processing conditions for different field types. To do this, customize the base logic of the
 
 Create object records based on incoming webhook
 
 business process. Learn more in a separate article:
 [Process webhooks in Creatio](https://academy.creatio.com/documents?id=2411) 
 .
 


### 
 Set up field mapping manually



 The general procedure to set up field mapping manually includes the following steps:
 


1. Specify the Creatio object to add based on the webhook.
 [Read more >>>](#title-2501-8)
2. Map the webhook form parameters to Creatio object fields.
 [Read more >>>](#title-2501-9)


#### 
 1. Specify the Creatio object



 By default, Creatio lets you add any object based on the webhook. To do this, set the
 
 EntityName
 
 webhook parameter to the code of the needed object. The way to set the parameter depends on the webhook service.
 





 Note.
 
 Use the code, not the Creatio object name, as the
 
 EntityName
 
 parameter value. Learn more about the object code in a separate article:
 [Object](https://academy.creatio.com/documents?id=15107&anchor=title-3028-6) 
 .
 



#### 
 2. Map the webhook form parameters to Creatio object fields



 To map the webhook form parameters to Creatio object fields, add the needed Creatio object fields manually. Make sure the values match the field codes of the Creatio object.
 



 Follow the
 **recommendations** 
 for mapping the webhook form parameters to Creatio object fields in a different section:
 [Map the webhook form parameters to Creatio object fields](#recommendations) 
 .
 




