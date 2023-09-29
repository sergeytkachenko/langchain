


 Case pages display response and resolution deadlines as well as remaining time until the resolution or the overdue time if the scheduled date has already passed (
 [Fig. 1](#XREF_68236_200)
 ).
 





 Fig. 1
 

 The case page with response and resolution time calculated
 

![scr_section_service_requests_case_page.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_calculate_response_and_resolution_time/scr_section_service_requests_case_page.png)





 Calculate the response and resolution time for cases
--------------------------------------------------------



 Creatio calculates the response and resolution deadlines of a case based on several factors. To check how the deadlines of a particular case were calculated, open the case page →
 
 Case information
 
 tab → the
 
 Terms
 
 detail, then click
 ![btn_question.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_calculate_response_and_resolution_time/btn_question.png)
 next to the
 
 Response time
 
 or
 
 Resolution time
 
 fields (
 [Fig. 1](#XREF_82082_357)
 ).
 



 When a case moves to the next stage of its life cycle, Creatio recalculates the resolution deadline. You can also view the time already spent on the case resolution, as well as the time remaining till the resolution deadline. The response time does not update after the case changes its status (i.e., the actual “response” occurs).
 





 Fig. 1
 

 Opening information on the response/resolution time
 

![scr_service_requests_btn_terms_calculate.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_calculate_response_and_resolution_time/scr_service_requests_btn_terms_calculate.png)



 The information on the response/resolution deadline calculation will open in a new window (
 [Fig. 2](#XREF_25188_358)
 ) with four “cards”:
 


* **Case parameters** 
 : priority, service, registration date. Service Creatio, enterprise edition has an additional “service agreement” parameter.
   

 You can open the case parameters: service or the SLA by clicking the corresponding link.
* **Deadline calculation rule** 
 : the selected rule of calculation the deadlines, the calendar and the time zone, as well as the response and resolution time that were used for calculation. To open the
 
 Case deadline calculation schemas
 
 lookup with the strategy parameters, click the corresponding link. If Creatio cannot calculate the deadline using the main schema, an alternative schema is used.
* **Calculation of deadline** 
 : specifies the day of the week and the day type (working day or day off). Deadline is calculated based on the case registration date or the current date (if the deadlines are recalculated).
* **Calculated response time** 
 . Response time is calculated based on the selected deadline calculation rule.





 Fig. 2
 

 Information on calculating the response time for a case
 

![scr_service_requests_wnd_terms_calculate.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_calculate_response_and_resolution_time/scr_service_requests_wnd_terms_calculate.png)



 The date and time displayed in the information window and in the
 
 Response time
 
 and
 
 Resolution time
 
 fields can differ. This is caused by different calendars used for calculation: the information window uses the support service calendar, while the record page fields use the user’s calendar. If the user calendar is not available, the time calculation is based on the data from the user’s browser.
 









 Overdue/remaining time indicators
-----------------------------------------



 On the case page, there are special indicators that show the progress in processing the case. They are available next to the
 
 Scheduled response time
 
 and
 
 Scheduled resolution time
 
 fields (
 [Fig. 1](#XREF_21681_157)
 ).
 





 Fig. 1
 

 Overdue/remaining time indicators
 

![scr_section_service_requests_clocks.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_calculate_response_and_resolution_time/scr_section_service_requests_clocks.png)



 The indicator appearance depends on the current case status and its compliance with the deadlines. The time displayed by the indicators is always calculated in calendar units (minutes, hours, days).
 



 Depending on the timely resolution of the case:
 


* Prior to the deadline, the indicator is green and displays the remaining time.
* After the deadline, the indicator is red and displays the overdue time.
* If the time until deadline exceeds 14 days, the indicator appears as “> 14 d“.
* If the overdue time exceeds 14 days, the indicator appears as “> 14 d“.



 Depending on the case status:
 


* + If the actual time is filled in (for example, the case is resolved), there are two options:
	+ If the actual value is less than the planned value (the case has been processed within the planned time), the indicator is hidden.
	+ If the actual value exceeds the planned value (the case is overdue), the indicator is displayed yet the clock is stopped.
* + If the actual deadline is not filled in:
	+ The indicator is visible and the countdown is on for active cases (in the “open”, or “in progress” status).
	+ The indicator is not visible for paused cases (cases that are awaiting customer’s response). When the case processing resumes, the indicator is displayed and keeps counting.
	 
	
	
	
	
	
	 Note.
	 
	 The checkbox for the final status, as well as for the pause status, is selected in the
	 
	 Case statuses
	 
	 lookup.







 Response and resolution time calculation rules
----------------------------------------------------



 The response and resolution deadlines are calculated based on the case, service, and service contract data as well as the corresponding calendar. In Service Creatio, enterprise edition, the service agreement will also be taken into account.
 



 You can set up contingency plans for deadline calculation using several pre-defined calculation strategies: by service, by case priority, by case priority and service in the service contract, by priority on the SLA level. One of the rules is used by default, while others can be alternative rules. If Creatio is unable to calculate deadline using the default rule, it will automatically attempt its alternative rule. If the alternative rule cannot be used, and if it has its own alternative rule, Creatio will use that rule. If an alternative rule is not specified, the deadlines will not be calculated. Use the
 
 Case deadline calculation schemas
 
 lookup to set the default and alternative rules.
 





 Note.
 
 New rules are created with development tools in the Creatio platform
 



#### 
 By service



 This deadline calculation rule is based on the service page data and the calendar of the service (
 [Fig. 1](#XREF_45973_201)
 ) or the service agreement (in Service Creatio, enterprise edition).
 





 Fig. 1
 

 Data used for calculating deadlines by service
 

![by_service_strategy_CC.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_calculate_response_and_resolution_time/by_service_strategy_CC.png)


#### 
 By priority



 To calculate deadlines by this rule, Creatio uses the
 
 Case priorities
 
 lookup data. This rule is based on the response and resolution deadlines set for different case priorities (
 [Fig. 2](#XREF_53506_202)
 ).
 





 Fig. 2
 

 Data used for calculating deadlines by priority
 

![cases_priority.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_calculate_response_and_resolution_time/cases_priority.png)


#### 
 By service in SLA



 This rule is based on the values in the
 
 Response time
 
 and
 
 Resolution time
 
 fields on the
 
 Services
 
 detail of the service contract page (
 [Fig. 3](#XREF_77501_203)
 ). Here you can also select a specific service calendar if it is different from the calendar of the service agreement. This is the default rule for calculating deadlines in Service Creatio, enterprise edition. Its alternative strategy is “By service”.
 





 Fig. 3
 

 Data used for calculating deadlines by service in SLA
 

![by_service_in_service_agreement_strategy_se.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_calculate_response_and_resolution_time/by_service_in_service_agreement_strategy_se.png)





 Note.
 
 In this case, the specified calendar will be used when calculating the response and resolution time. Otherwise, the response time will be calculated according to the base agreement calendar.
 



#### 
 By service priority in SLA



 This rule uses the values on the
 
 Time to prioritize
 
 detail on the page of the service in SLA (
 [Fig. 4](#XREF_15442_7)
 ). Here you can also select a specific service calendar if it is different from the calendar of the service agreement.
 





 Fig. 4
 

 Data used for calculating deadlines by service priority in SLA
 

![by_case_priority_considering_service_in_service_agreement_strategy.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_calculate_response_and_resolution_time/by_case_priority_considering_service_in_service_agreement_strategy.png)


#### 
 By priority in SLA level



 The calculation is based on the data from the
 
 Priority in Support level
 
 detail of the
 
 Support levels
 
 lookup pages (
 [Fig. 5](#XREF_43584_204)
 ). This rule requires that a support level and a calendar is specified in service contracts.
 





 Fig. 5
 

 Data used for calculating deadlines by priority in SLA level
 

![by_sla_priority_strategy.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_calculate_response_and_resolution_time/by_sla_priority_strategy.png)






 Response and resolution time calculation rules
---------------------------------------------------



 Let's take a look at how response and resolution deadline calculation rules affect actual case deadlines. In our example, customer and support service are in one time zone.
 





 Note.
 
 If the response and resolution time is specified in “calendar time” (minutes, hours or days), the service calendar does not affect the deadline calculation. If the response and resolution time is specified in workhours or workdays, the response time will be calculated from the start of the next business period (next business day, etc.). For example, if a case was at 13.00, and the response time is 1 work day, the planned response time will be set to the end of the work interval of the next calendar day.
 



#### 
 Calculating response and resolution deadlines using the “By service” rule



 Only the parameters configured on the service page and the service calendar in the service agreement (in Service Creatio, enterprise edition) are taken into account when calculating response and resolution deadlines
 **by service** 
 . Case priority and support level are not taken into account.
 





 Case.
 
 The following settings are specified for the “Consultations on the software setting” service:
   

 Response time unit: 1 working hour
   

 Resolution time unit: 3 working hours
   

 Service calendar (service in the service agreement calendar for Service Creatio, enterprise edition): 5-day workweek (from Monday to Friday), business hours are from 9:00 AM to 6:00 PM, no lunch break.
 




 As a result, response and resolution deadlines for all cases connected with the “Consultations on the software setting” service will be calculated in the same way, regardless of all other case parameters.
 



 For cases received on Monday, 10:00 AM, the deadlines will be calculated in the following way:
 


* Response deadline: Monday. 11:00 AM (registration time + response time unit).
* Resolution deadline: Monday. 1:00 PM (registration time + resolution time unit).


#### 
 Calculate response and resolution deadlines using the “By service” rule



 Only the case priority and the service calendar are taken into account when calculating of response and resolution deadlines
 **by priority** 
 . Service and support level are not taken into account.
 





 Case.
 
 The following settings are specified for critical priority in the
 
 Case priorities
 
 lookup:
   

 Response time unit: 30 working minutes
   

 Resolution time unit: 2 working hours
   

 Service calendar: 5-day workweek (from Monday to Friday), business hours are from 10:00 AM to 6:00 PM, no lunch break.
 




 As a result, response and resolution deadlines for all cases of “Critical” priority will be calculated , service agreement and support level.
 



 For cases of “Critical” priority, received for this service on Monday, 10:00 AM the deadlines will be calculated in the following way:
 


* Response deadline: Monday. 10:30 AM (registration time + response time unit).
* Resolution deadline: Monday. 12:00 PM (registration time + resolution time unit).


#### 
 Calculate response and resolution deadlines using the “By service” rule



 Service Creatio, enterprise edition can calculate response and resolution deadlines using the “By service in SLA” rule. Only parameters configured for specific service in the service agreement are taken into account in the calculating of response and resolution deadlines By service in SLA. Case priority, service level and parameters on the service page are not taken into account.
 





 Case.
 
 Settings specified for  the “Consultations on the software setting” service in the “4 – Axiom” Service agreement:
   

 Response time unit: 4 work hour
   

 Resolution time unit: 1 working day.
   

 Service calendar: 5-day workweek (from Monday to Friday), business hours are from 9:00 AM till 5:00 PM, no lunch break.
 




 For the case received from the “Axiom” employee for the “Consultations on the software setting” service that is included in the “4 – Axiom” service agreement on Monday 10:00 AM the deadlines will be calculated in the following way:
 


* Response deadline: Monday. 14:00 AM (registration time + response time unit).
* Resolution deadline: Monday. 17:00 AM (registration time + resolution time unit).


#### 
 Calculate response and resolution deadlines using the “By service priority in SLA” strategy.



 Service Creatio, enterprise edition can calculate response and resolution deadlines using the “By service priority in SLA” rule. Only calendar and parameters configured for cases of different priorities on the service page in the service agreement are taken into account in the calculating of response and resolution deadlines
 **By service  priority in SLA** 
 . Service level and parameters on the service page are not taken into account.
 





 Case.
 
 Settings specified for cases of “Medium” priority of the “Consultations on the software setting” service in the “4 – Axiom” Service agreement:
   

 Response time unit: 2 work hour
   

 Resolution time unit: 4 working hours
   

 Service calendar: 5-day workweek (from Monday to Friday), business hours from 9:00 AM till 5:00 PM, no lunch break.
 




 For the case of “Medium” priority received from the “Axiom” employee for the “Consultations on the software setting” service on Monday 10:00 AM the deadlines will be calculated in the following way:
 


* Response deadline: Monday. 12:00 PM (registration time + response time unit).
* Resolution deadline: Monday. 2:00 PM (registration time + resolution time unit).


#### 
 Calculate response and resolution deadlines using the “By priority in SLA level” rule



 Service Creatio, enterprise edition can calculate response and resolution deadlines using the “By priority in SLA level” rule. Only parameters configured for specific priority in the
 
 Support levels
 
 lookup and service agreement are taken into account in the calculating of response and resolution deadlines By service in SLA. Parameters on the service page are not taken into account.
 





 Case.
 
 The “Axiom” company has a “Business” support level specified in the “4 – Axiom” service agreement. Settings specified for cases of “Business” support level in the
 
 Support levels
 
 lookup:
   

 Response time unit: 15 working minutes
   

 Resolution time unit: 1 work hour.
   

 Service calendar selected in the “4 – Axiom” service agreement: 5-day workweek (from Monday till Friday), business hours from 10:00 AM till 6:00 PM, no lunch break.
 




 For the case with critical priority received from the “Axiom” employee on Monday 10:00 AM the deadlines will be calculated in the following way:
 


* Response deadline: Monday. 10:15 AM (registration time + response time unit).
* Resolution deadline: Monday. 11:00 AM (registration time + resolution time unit).


#### 
 Calculate response and resolution deadlines for customers who are in the same time zone as the support service



 Creatio uses the service calendar data (service in SLA data in Service Creatio, enterprise edition)
 **.** 
 The calendar settings are configured via the
 
 Calendars
 
 lookup. Read more in the “
 
[Set up calculation of response and resolution deadlines](/docs/8-0/user/service_tools/service_cases/case_settings/response_and_resolution_deadlines/set_up_response_and_resolution_deadlines#HT_specs_service_requests_deadlines_calculation) 

 ” article.
 



 The
 **service calendar** 
 (
 **service in SLA calendar** 
 for Service Creatio, enterprise edition) has the following parameters:
 


* Workweek from Monday till Friday.
* Work time from 9:00 AM till 6:00 PM, technical break from 1:00 PM till 2:00 PM.
* Days off: Saturday, Sunday.
* Additional day off: May 30, 2017.
* The time zone is UTC -5.



 The deadlines are calculated in the time zone of the corresponding service calendar. The results are adjusted based on the time zone of the viewer.
 



 Support agent and customer are in the same time zone (UTC -5).
 





 Note.
 
 If the response and resolution time is specified in “calendar time” (minutes, hours or days), the service calendar does not affect the deadline calculation. If the response and resolution time is specified in workhours or workdays, the response time will be calculated from the start of the next business period (next business day, etc.). For example, if a case was at 13.00, and the response time is 1 work day, the planned response time will be set to the end of the work interval of the next calendar day.
 




 Below are examples of deadline calculation for a case created during weekend (05/30) and a workday. The resolution deadlines are calculated in a similar way.
 





|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 
 Date/time when the case was registered
 

 on the portal (UTC -5)
  | 
 Date/time when the case was registered
 

 on the case page (UTC -5)
  | 
 Date/time when the case was registered
 

 in the service calendar (UTC -5)
  | 
 Response time
  | 
 Planned response
 

 in the service calendar (UTC -5)
  | 
 Planned response
 

 on the portal (UTC -5)
  | 
 Planned response
 

 on the case page (UTC -5)
  |
| 
 05/02 1:00 PM
  | 
 05/02 1:00 PM
  | 
 05/02 1:00 PM
  | 
 10 calendar minutes
  | 
 05/02 1:10 PM
  | 
 05/02 1:10 PM
  | 
 05/02 1:10 PM
  |
| 
 05/02 1:05 PM
  | 
 05/02 1:05 PM
  | 
 05/02 1:05 PM
  | 
 10 work minutes
  | 
 05/02 2:10 PM
  | 
 05/02 2:10 PM
  | 
 05/02 2:10 PM
  |
| 
 05/01 1:00 PM
  | 
 05/01 1:00 PM
  | 
 05/01 1:00 PM
  | 
 10 calendar minutes
  | 
 05/01 1:10 PM
  | 
 05/01 1:10 PM
  | 
 05/01 1:10 PM
  |
| 
 05/01 1:05 PM
  | 
 05/01 1:05 PM
  | 
 05/01 1:05 PM
  | 
 10 work minutes
  | 
 05/02 9:10 AM
  | 
 05/02 9:10 AM
  | 
 05/02 9:10 AM
  |
| 
 05/02 1:00 PM
  | 
 05/02 1:00 PM
  | 
 05/02 1:00 PM
  | 
 1 calendar hour
  | 
 05/02 2:00 PM
  | 
 05/02 2:00 PM
  | 
 05/02 2:00 PM
  |
| 
 05/02 1:00 PM
  | 
 05/02 1:00 PM
  | 
 05/02 1:00 PM
  | 
 1 work hour
  | 
 05/02 3:00 PM
  | 
 05/02 3:00 PM
  | 
 05/02 3:00 PM
  |
| 
 05/01 1:00 PM
  | 
 05/01 1:00 PM
  | 
 05/01 1:00 PM
  | 
 1 calendar hour
  | 
 05/01 2:00 PM
  | 
 05/01 2:00 PM
  | 
 05/01 2:00 PM
  |
| 
 05/01 1:00 PM
  | 
 05/01 1:00 PM
  | 
 05/01 1:00 PM
  | 
 1 work hour
  | 
 05/02 10:00 AM
  | 
 05/02 10:00 AM
  | 
 05/02 10:00 AM
  |
| 
 05/02 1:00 PM
  | 
 05/02 1:00 PM
  | 
 05/02 1:00 PM
  | 
 1 calendar day
  | 
 05/03 1:00 PM
  | 
 05/03 1:00 PM
  | 
 05/03 1:00 PM
  |
| 
 05/02 1:00 PM
  | 
 05/02 1:00 PM
  | 
 05/02 1:00 PM
  | 
 1 work day
  | 
 05/03 6:00 PM
  | 
 05/03 6:00 PM
  | 
 05/03 6:00 PM
  |
| 
 05/01 1:00 PM
  | 
 05/01 1:00 PM
  | 
 05/01 1:00 PM
  | 
 1 calendar day
  | 
 05/02 1:00 PM
  | 
 05/02 1:00 PM
  | 
 05/02 1:00 PM
  |
| 
 05/01 1:00 PM
  | 
 05/01 1:00 PM
  | 
 05/01 1:00 PM
  | 
 1 work day
  | 
 05/02 6:00 PM
  | 
 05/02 6:00 PM
  | 
 05/02 6:00 PM
  |







#### 
 Calculate response and resolution deadlines for customers who are in a different time zone from that of the support service



 The deadlines are calculated in the time zone of the base calendar. The results are adjusted based on the time zone of the viewer.
 



 The
 **service calendar** 
 (
 **service in SLA calendar** 
 for Service Creatio, enterprise edition) has the following parameters:
 


* Workweek from Monday till Friday.
* Work time from 9:00 AM till 6:00 PM, break from 1:00 PM till 2:00 PM.
* Days off: Saturday, Sunday.
* Additional day off: May 30, 2017.
* The time zone is UTC -8.



 The helpdesk agent’s time zone is UTC -5.
 



 The customer’s time zone is UTC +5.
 





 Note.
 
 The current user’s time zone is specified the user profile. If the time zone is not specified in the user profile, the time zone specified in the
 
 Defaulr TimeZone
 
 system setting. If no time zone is specified in the user profile and the
 
 Defaulr TimeZone
 
 system setting, Creatio server local time is used to determine the time zone.
 




 Below are examples of deadline calculation for a case created during weekend (05/30) and a workday. The resolution deadlines are calculated in a similar way.
 





|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 
 Date/time when the case was registered
 

 on the portal (UTC -3)
  | 
 Date/time when the case was registered
 

 on the case page (UTC -5)
  | 
 Date/time when the case was registered
 

 in the service calendar (UTC -8)
  | 
 Response time
  | 
 Planned response
 

 in the service calendar (UTC -8)
  | 
 Planned response
 

 on the portal (UTC -3)
  | 
 Planned response
 

 on the case page (UTC -5)
  |
| 
 05/02 6:00 PM
  | 
 05/02 4:00 PM
  | 
 05/02 1:00 PM
  | 
 10 calendar minutes
  | 
 05/02 1:10 PM
  | 
 05/02 6:10 PM
  | 
 05/02 4:10 PM
  |
| 
 05/02 6:00 PM
  | 
 05/02 4:00 PM
  | 
 05/02 1:00 PM
  | 
 10 work minutes
  | 
 05/02 2:10 PM
  | 
 05/02 7:10 PM
  | 
 05/02 5:10 PM
  |
| 
 05/01 6:00 PM
  | 
 05/01 4:00 PM
  | 
 05/01 1:00 PM
  | 
 10 calendar minutes
  | 
 05/01 1:10 PM
  | 
 05/01 6:10 PM
  | 
 05/01 4:10 PM
  |
| 
 05/01 6:00 PM
  | 
 05/01 4:00 PM
  | 
 05/01 1:00 PM
  | 
 10 work minutes
  | 
 05/02 9:10 AM
  | 
 05/02 2:10 PM
  | 
 05/02 12:10 PM
  |
| 
 05/02 6:00 PM
  | 
 05/02 4:00 PM
  | 
 05/02 1:00 PM
  | 
 1 calendar hour
  | 
 05/02 2:00 PM
  | 
 05/02 7:00 PM
  | 
 05/02 5:00 PM
  |
| 
 05/02 6:00 PM
  | 
 05/02 4:00 PM
  | 
 05/02 1:00 PM
  | 
 1 work hour
  | 
 05/02 3:00 PM
  | 
 05/02 8:00 PM
  | 
 05/02 6:00 PM
  |
| 
 05/01 6:00 PM
  | 
 05/01 4:00 PM
  | 
 05/01 1:00 PM
  | 
 1 calendar hour
  | 
 05/01 2:00 PM
  | 
 05/01 7:00 PM
  | 
 05/01 5:00 PM
  |
| 
 05/01 6:00 PM
  | 
 05/01 4:00 PM
  | 
 05/01 1:00 PM
  | 
 1 work hour
  | 
 05/02 10:00 AM
  | 
 05/02 3:00 PM
  | 
 05/02 1:00 PM
  |
| 
 05/02 6:00 PM
  | 
 05/02 4:00 PM
  | 
 05/02 1:00 PM
  | 
 1 calendar day
  | 
 05/03 1:00 PM
  | 
 05/03 6:00 PM
  | 
 05/03 4:00 PM
  |
| 
 05/02 6:00 PM
  | 
 05/02 4:00 PM
  | 
 05/02 1:00 PM
  | 
 1 work day
  | 
 05/03 6:00 PM
  | 
 05/03 11:00 PM
  | 
 05/03 9:00 PM
  |
| 
 05/01 6:00 PM
  | 
 05/01 4:00 PM
  | 
 05/01 1:00 PM
  | 
 1 calendar day
  | 
 05/02 1:00 PM
  | 
 05/02 6:00 PM
  | 
 05/02 4:00 PM
  |
| 
 05/01 6:00 PM
  | 
 05/01 4:00 PM
  | 
 05/01 1:00 PM
  | 
 1 work day
  | 
 05/02 6:00 PM
  | 
 05/02 11:00 PM
  | 
 05/02 9:00 PM
  |









