


 Creatio implements the “Service catalog management” ITSM process in the
 
 Services
 
 section. This section is designed to manage the list of services you provide. Here, you can set the parameters of services, assign employees to process the related cases, as well as view the history of services provided.
 








 Add services
-------------------



 To add a new service in Creatio:
 


1. Open the
 
 Services
 
 section and click
 
 New service
 
 in the section list.
2. Populate the service page:
 





|  |  |
| --- | --- |
| 
 Name
  | 
 Service name.
  |
| 
 Status
  | 
 Current service status. For example, “Active” or “Under testing.”
  |
| 
 Response time unit
  | 
 The time units used to measure the case response time, e.g., “Working days,” “Calendar days,” etc.
  |
| 
 Resolution time unit
  | 
 Time units used to measure the case resolution time, e.g., “Working days,” “Calendar days,” etc.
  |
| 
 Owner
  | 
 The employee responsible for the quality of the provided service. The field is only available for
 **Service Creatio, enterprise edition** 
 .
  |
| 
 Category
  | 
 The service category, for example, “Hardware” or “Internal support.” The field is only available for
 **Service Creatio, enterprise edition** 
 .
  |
| 
 Case category
  | 
 The category that will be assigned to the cases based on this service: “Incident,” “Complaint,”“Claim,” “Consultation” (available for The
 **Financial Services Creatio, customer journey edition** 
 ), “Service request.” When you create a new case and populate the
 
 Service
 
 field, Creatio will specify the selected category in the
 
 Category
 
 field of the
 
[case page](https://academy.creatio.com/documents?product=service%20enterprise&ver=7&id=1550) 

 .
  |
| 
 Calendar
  | 
 The calendar that defines the work of the support team. Creatio calculates the response and resolution time for the service-related cases based on the selected calendar. By default, the field is populated with the value specified in the “Base calendar” (BaseCalendar) system setting. Custom calendars can be set up in the corresponding lookup
  |
3. On the
 
 Service profile
 
 tab →
 
 Service team
 
 detail, click
 ![btn_com_add_tab.png](/guides/sites/en/files/documentation/user/en/itsm_tools/BPMonlineHelp/manage_service_catalog/btn_com_add_tab.png)
 and populate information about the service team providing support within the service. The detail is only available for
 **Service Creatio, enterprise edition** 
 .
 





 Note.
 
 The
 
 Service team
 
 detail contains information about the employees or employee groups responsible for resolving cases related to a service, e.g., “Contact center agents,” “System administrators” or “2nd line of support.”
 



 Information on this detail is used to select assignees and assigned teams on the
 
[case page.](https://academy.creatio.com/documents?product=service%20enterprise&ver=7&id=1550) 






 Populate the record data directly in the detail list.
 





|  |  |
| --- | --- |
| 
 Member/team
  | 
 Employees or employee groups that can resolve the service-related case. The field lookup contains the list of administration objects: system users and user groups.
  |
| 
 Support line
  | 
 Support line whose employee is assigned to provide service-related support.
  |
4. Populate information about the service-related agreements on the
 
 Users
 
 tab. The tab is only available for
 **Service Creatio, enterprise edition** 
 .
 





 Note.
 
 The
 
 Service agreements
 
 tab displays a list of service contracts from the
 
[Service agreements
 
 section](https://academy.creatio.com/documents?product=service%20enterprise&ver=7&id=1062) 

 that include the service. To connect a service to a service contract, populate the
 
 Services
 
 detail of the service agreement page. The information on the detail is available in the “read-only” mode.
5. On the
 
 Attachments and notes
 
 tab, add attachments and links to the web resources related to the service.
 
 Read more >>>
6. Click
 
 Save
 
 to save the service record.
 



 As a result, the new service record with the specified parameters will appear in the list of the
 
 Services
 
 section.








 Create a service model
-----------------------------



 A
 **service model** 
 is a diagram that displays connections and dependencies between various IT infrastructure items. The model is generated based on the connections between the services and the configuration items.
 





 Note.
 
 The service models are only available in Service Creatio, enterprise edition.
 




 To add a service to the service model:
 


1. In the
 
 Services
 
 section, open the record to specify the connected services and configuration items.
2. Click the
 
 Connected to
 
 tab.
3. Click
 ![btn_com_add_tab00001.png](/guides/sites/en/files/documentation/user/en/itsm_tools/BPMonlineHelp/manage_service_catalog/btn_com_add_tab00001.png)
 on the
 
 Configuration items
 
 detail. A new record with blank fields will appear on the detail.
4. Select the connection category with the configuration item in the
 
 Category
 
 field (
 [Fig. 1](#XREF_79270_96)
 ).
 





 Fig. 1
 

 Selecting the connection category
 

![scr_specs_services_connected_category.png](/guides/sites/en/files/documentation/user/en/itsm_tools/BPMonlineHelp/manage_service_catalog/scr_specs_services_connected_category.png)


1. Select the "Influencer" connection category to add a link to a configuration item that affects the current service delivery.
2. Select the "Dependent" connection category to add a link to a configuration item whose operation depends on the current service.
3. In the
 
 Configuration item
 
 field, select the linked configuration item. For example, the "WiFi access" service depends on the "Router" configuration item (
 [Fig. 2](#XREF_13770_97)
 ).
 





 Fig. 2
 

 Selecting the connected configuration item
 

![scr_specs_services_connected_ci.png](/guides/sites/en/files/documentation/user/en/itsm_tools/BPMonlineHelp/manage_service_catalog/scr_specs_services_connected_ci.png)
4. In the
 
 Type
 
 field, select a short description of connections between the current service and the selected configuration item. For example, the "Required for" connection type can be specified for the "WiFi access" service and the "Router" configuration item (
 [Fig. 3](#XREF_46967_98)
 ).
 





 Fig. 3
 

 Selecting the connection type
 

![scr_specs_services_connected_type.png](/guides/sites/en/files/documentation/user/en/itsm_tools/BPMonlineHelp/manage_service_catalog/scr_specs_services_connected_type.png)



 As a result, a
 **connection** 
 between the service and the configuration item will be specified. If the “Influencer” category was selected upon specifying the connection, the configuration item, whose connection has been specified will contain
 **inverse relation** 
 with the “Dependent” category on the
 
 Connected to
 
 tab of the
 
 Services
 
 detail. The
 
 Type
 
 field of the inverse relationship will be automatically populated with the inverse connection type according to the “
 **Object dependency type** 
 ” lookup content. For example, if the type of the connection is “Required for,” the inverse relation is “Installed on.”
5. Specify other connections to the configuration items.
6. Add connections to the relevant services by clicking
 ![btn_com_add_tab00002.png](/guides/sites/en/files/documentation/user/en/itsm_tools/BPMonlineHelp/manage_service_catalog/btn_com_add_tab00002.png)
 on the
 
 Related services
 
 detail. The procedure for linking services is similar to that of linking configuration items (see steps 3-6).
7. If required, open the
 
 Configurations
 
 section and add the missing connections between the configuration items.
 



 As a result, Creatio will add connections between the services and configuration items which make the visual display of the service model possible when handling the cases or planning the changes.




