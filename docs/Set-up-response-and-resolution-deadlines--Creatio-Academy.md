


 Creatio enables you to calculate case response and resolution time. You can select the time calculation rule that suits you most and set it up according to your business specifics. Response and resolution deadlines can take the following factors into account:
 


* Case priority
* Case service
* Service in the applicable service agreement (available in Service Creatio, enterprise edition).



 You can set up response and resolution deadlines in two steps:
 


* Set up calendars.
* Select a deadline calculation rule.


#### 
 Set up time values for deadline calculation rules



 The response and resolution deadline calculation accounts for holidays, weekends and work hours specified in the calendar used for the customer service. Set up calendars for correct deadline calculation. By default, one standard calendar with the following characteristics is available:
 


* Time zone GMT 0, without daylight saving time.
* 5-day workweek (from Monday till Friday).
* 8-hour work day (from 9:00 AM to 6:00 PM), without lunch break.
* Reduced work days and holidays are not included.



 This calendar is specified as default in the
 
 Base calendar
 
 system setting. The
 
 Base calendar
 
 system setting must be populated for the correct work of calendars. You can modify the standard calendar according to the support service schedule of your company, or create a new one and add it to the system setting as the default one. You can also create additional calendars that take into account additional scheduling of services provision. For example, calendars of services provision with different work hours or different time zones.
 



 The service calendar is the calendar the system used to calculate case response and resolution deadlines. Creatio will select the firs available calendar, by checking the availability in the following order:
 


1. **The calendar of the service in the applicable service agreement** 
 (available in Service Creatio, enterprise edition). When service provision schedule differs from the general calendar of the service agreement, you can specify separate calendars on the service page in the service agreement. If the corresponding calendar is not specified, the system will use the calendar in the service contract.
2. **The calendar of the applicable service agreement** 
 (available in Service Creatio, enterprise edition). You can set up specific calendars of service provision for customers located in different time zone. This calendar is specified in the customer service agreement. One calendar can be specified in several service agreements. If the service contract calendar is not available, the system will use the base calendar.
3. **The service calendar** 
 is the service provision calendar specified on the service page. If the calendar is not available on the service page, the system will use the base calendar.
4. **Base calendar** 
 is the calendar specified in the
 
 Base calendar
 
 system setting. The system uses this calendar if no custom calendar is specified.
 





 Case.
 
 Create a new calendar for a service that is provided six days a week. Saturday has shorter working hours. Fixed one-hour technical break.
5. Open the System Designer.
6. Go to the
 
 System setup
 
 block → click
 **Lookups** 
 .
7. Open the
 **Calendars** 
 lookup.
8. Click
 
 New
 
 . Specify the new calendar name and time zone.
9. Click the
 ![btn_edit.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_response_and_resolution_time_settings/btn_edit.png)
 button and edit the workweek settings. The default week parameters match the parameters of the base calendar.
10. Set up workweek. Set the day type as “Work” for all days from Monday to Friday, “Reduced” for Saturday and “Day off” for Sunday.
11. Set up work time. Set the technical break by separating the work time into two intervals, before and after the break: 9:00AM–1:00PM and 2:00PM–6:00PM.
12. Specify all holidays on the
 
 Days off
 
 tab.
 



 The created calendar can be set as the base calendar or specified on a service page. Additionally, Service Creatio, enterprise edition enables specifying this calendar in a service agreement page or the page of service in a service agreement.



 To specify the service calendar in the service agreement:
 


1. Open the service agreement page
2. Select the service for which you want to specify a separate calendar.
3. Click the
 ![btn_com_roles_actions_menu.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_response_and_resolution_time_settings/btn_com_roles_actions_menu.png)
 button and select the
 
 Edit
 
 command in the menu.
4. On the service page, in the
 
 Calendar
 
 field, select the calendar you just created.


#### 
 Select a case deadline calculation rule



 The
 
 Case deadline calculation rules
 
 lookup contains a list of
 
[rules](https://academy.creatio.com/documents?product=service%20enterprise&ver=7&id=1653) 

 that can be used for calculating response and resolution deadlines for cases.
 



 General procedure for selecting a deadline calculation rule:
 


* When calculating response and resolution time, the system will use the rule set by default.
* If there is not enough data in the default schema, Creatio will use the alternative rule. If an alternative rule is not specified, the deadlines will not be calculated. If an alternative rule is specified, but also cannot be applied, its own alternative strategy will be used, and so on.
* If none of the rules can be used, the deadlines will not be calculated.



 The response time and resolution time are calculated independently from one another. If the data in the case is sufficient for calculation based on the base resolution time calculation rule, but not sufficient for calculation of the response time, then the resolution time will be calculated based on the base rule, and the response time - based on the alternative rule.
 





 Case.
 
 Set up the calculation of deadlines by case priority with an alternative calculation by service.
 



1. Open the system designer by clicking the
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_response_and_resolution_time_settings/btn_system_designer.png)
 button.
2. Go to the
 
 System setup
 
 block → click
 **Lookups** 
 .
3. In the
 
 Lookups
 
 section, open the
 **Case deadline calculation rules** 
 lookup content (Fig. 1).
 





 Fig. 1
 

 The
 
 Case deadline calculation rules
 
 lookup
 

![scr_section_service_requests_dedline_calculation_rules_lookup.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_response_and_resolution_time_settings/scr_section_service_requests_dedline_calculation_rules_lookup.png)
4. Select the “By priority” rule.
5. Select the
 
 By default
 
 checkbox.
 





 Note.
 
 The
 
 By default
 
 checkbox can be selected only for one strategy. If you try to select a checkbox for two rules simultaneously, only the last selected checkbox will be saved.
6. Specify “By service” in the
 
 Alternative schema
 
 field of the default rule.
 



 We recommend setting up an alternative rule for each rule. Therefore, when calculating response and resolution time, all possible case parameters will be taken into account.







 Set up case response and resolution deadlines
---------------------------------------------------



 The response and resolution deadlines are calculated based on the case, service, and service contract data as well as the corresponding calendar. In Service Creatio, enterprise edition, the service agreement will also be taken into account.
 



 The deadlines are calculated based on the following strategies:
 


* Service
* Case priority
* Service in the applicable service agreement (available in Service Creatio, enterprise edition).
* Case priority based on the service in the applicable service agreement (available in Service Creatio, enterprise edition).
* SLA priority (available in Service Creatio, enterprise edition).



 One of the rules is used by default, while others can be alternative rules. If Creatio is unable to calculate deadline using the default rule, it will automatically attempt its alternative rule. If the alternative rule cannot be used, and if it has its own alternative rule, Creatio will use that rule. If an alternative rule is not specified, the deadlines will not be calculated. Use the
 
 Case deadline calculation rules
 
 lookup to set the default and alternative rules.
 





 Note.
 
 New rules are created with development tools in the Creatio platform
 



#### 
 By service



 This deadline calculation strategy is based on the service page data and the calendar of the service (Fig. 1) or the service agreement (in
 **Service Creatio, enterprise edition** 
 ).
 **Service Creatio, customer center edition** 
 use this rule as the primary one.
 





 Fig. 1
 

 Data used for calculating deadlines by service
 

![by_service_strategy_CC.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_response_and_resolution_time_settings/by_service_strategy_CC.png)


#### 
 By priority



 Creatio uses the
 
 Case priorities
 
 lookup data (Fig. 2). This strategy is based on the response and resolution deadlines set for different case priorities.
 





 Fig. 2
 

 Data used for calculating case deadlines by priority
 

![cases_priority.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_response_and_resolution_time_settings/cases_priority.png)


#### 
 By service in SLA



 This strategy is based on the values in the
 
 Response time
 
 and
 
 Resolution time
 
 fields on the
 
 Services
 
 detail of the service contract page (Fig. 3). If the service calendar is different from the service agreement calendar, specify the service calendar on the same detail. This is the default rule for calculating deadlines in
 **Service Creatio, enterprise edition** 
 . Its alternative rule is “By service”.
 





 Fig. 3
 

 Data used for calculating deadlines by service in SLA
 

![by_service_in_service_agreement_strategy_se.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_response_and_resolution_time_settings/by_service_in_service_agreement_strategy_se.png)





 Note.
 
 In this case, the specified calendar will be used when calculating the response and resolution time. Otherwise, the response time will be calculated according to the base agreement calendar.
 



#### 
 By service priority in SLA



 This strategy uses the values on the
 
 Time to prioritize
 
 detail on the page of the service in SLA (Fig. 4). If the service calendar is different from the service agreement calendar, specify the service calendar on the same detail.
 





 Fig. 4
 

 Data used for calculating deadlines by service priority in SLA
 

![by_case_priority_considering_service_in_service_agreement_strategy.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_response_and_resolution_time_settings/by_case_priority_considering_service_in_service_agreement_strategy.png)


#### 
 By priority in SLA level



 The calculation is based on the data from the
 
 Priority in Support level
 
 detail of the
 
 Support levels
 
 lookup pages (Fig. 5). This strategy requires that a support level and a calendar is specified in service contracts.
 





 Fig. 5
 

 Data used for calculating deadlines by priority in SLA level
 

![by_sla_priority_strategy.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_response_and_resolution_time_settings/by_sla_priority_strategy.png)



 The setup procedure is as follows:
 


1. Open the contents of the
 **Support levels** 
 lookup.
2. Select a support package to configure and click
 ![btn_edit00001.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_response_and_resolution_time_settings/btn_edit00001.png)
 .
3. Response and resolution deadline values by case priority in the Service package are sown on the
 
 Priority in Support level
 
 detail. To do so:
 


	1. Click
	 ![btn_com_add_tab.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_response_and_resolution_time_settings/btn_com_add_tab.png)
	 .
	2. Populate the
	 
	 Priority
	 
	 field.
	3. Populate the
	 
	 Response time unit
	 
	 field.
	 
	
	
	
	
	
	 Note.
	 
	 The “Working days” time unit  is not converted in working hours. If 1 working day is set as response deadline and the case was registered before the working day started, then the end of this working day will be the actual response deadline. If the case was registered during the working day, then the response deadline will be the end of the next working day.
	 
	
	
	
		* Specify the response deadline in the
		 
		 Response time value
		 
		 field.
	 Populate the
	 
	 Resolution time unit
	 
	 and
	 
	 Resolution time value
	 
	 fields.



 These values are used in the calculation of the response and resolution deadlines according the “By priority in SLA level” strategy in the
 
 Case deadline calculation rules
 
 lookup.
 




