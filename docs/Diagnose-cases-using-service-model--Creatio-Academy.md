


 Use the service model to track the connections of a configuration item or service of the incident or service request.
 


#### 



 Open a service model of a case


1. Go to the
 **Cases** 
 section and open the required case record.
2. Click
 
 Actions
 
 →
 **Display service dependencies** 
 (
 [Fig. 1](#XREF_64985_117)
 ).
 





 Fig. 1
 

 The
 
 Display service dependencies
 
 action
 

![section_service_requests_act_show_service_connections.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_analyze_srm/section_service_requests_act_show_service_connections.png)



 As a result, the service connection diagram will open. The diagram displays dependencies of the service specified in the
 
 Service
 
 field of the case page (
 [Fig. 2](#XREF_56582_2)
 ).
 





 Fig. 2
 

 Service model diagram
 

![scr_section_service_requests_srm_display.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_analyze_srm/scr_section_service_requests_srm_display.png)



 The interconnections of a faulty (red) diagram element indicate possible causes (influencing elements) and consequences (dependent elements) of the failure. For example, the service model on
 

 (
 [Fig. 2](#XREF_56582_2)
 ) indicates that the correct operation of the “Diagnostics and adjustment of hardware” service depends on the “router” configuration item that is currently inactive.
 



 Click a diagram element to open the corresponding configuration item or service page.
 


#### 

 Open a service model of a case configuration item


1. Go to the
 
 Cases
 
 section and open the required case record.
2. Go to the
 
 Case information
 
 tab →
 
 Configuration items
 
 detail → Select the configuration item whose connections you want to display.
3. In the
 
 Configuration items
 
 menu, select
 
 Display dependencies
 
 (
 [Fig. 3](#XREF_31830_99)
 ).
 





 Fig. 3
 

 The
 
 Display dependencies
 
 action of a configuration item
 

![section_service_requests_ci_show_service_connections.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_analyze_srm/section_service_requests_ci_show_service_connections.png)



 As a result, the service model of the case configuration item will open.
 


#### 

 Filter the service model



 The diagram filtering area displays to the left of the connection schema. Use it to show/hide different types of influencing and dependent elements on the diagram.
 



 The following filter options are available:
 





|  |  |
| --- | --- |
| 
 Connection categories
  | 
 Display only influencing or dependent services and configuration items on the diagram.
  |
| 
 Property types
  | 
 Display only configuration items or services on the diagram.
  |
| 
 Object status
  | 
 Display only active or inactive configuration items and services on the diagram.
  |
| 
 CI statuses
  | 
 Display only configuration items of a specific status on the diagram.
  |
| 
 CI categories
  | 
 Display only configuration items of a specific category on the diagram.
  |
| 
 CI types
  | 
 Display only configuration items of a specific type on the diagram.
  |
| 
 CI models
  | 
 Display only configuration items of a specific model on the diagram.
  |








 To set up the filters:
 


1. Set the filters in the
 
 Connection categories
 
 ,
 
 Property types
 
 ,
 
 Object status
 
 blocks (
 [Fig. 4](#XREF_67262_355)
 ).
 





 Fig. 4
 

 Setting up filters
 

![scr_section_changes_srm_filter.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_analyze_srm/scr_section_changes_srm_filter.png)
2. Click
 ![btn_small_plus.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_analyze_srm/btn_small_plus.png)
 to set the conditions for the
 
 CI statuses
 
 ,
 
 CI categories
 
 ,
 
 CI types
 
 and
 
 CI models
 
 blocks.
 



 For example, to display only the configuration items of the "Equipment" category, go to the
 
 CI categories
 
 block, click
 
 New category
 
 and select "Equipment" in the lookup that opens (
 [Fig. 5](#XREF_40025_356)
 ).
 





 Fig. 5
 

 Adding filters
 

![section_service_requests_add_category.gif](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_analyze_srm/section_service_requests_add_category.gif)
3. Click
 
 Apply
 
 to save the changes.
 



 As a result, the diagram will only display the items that meet your filtering conditions and will contain services or configuration items used as the basis for building the diagram.




