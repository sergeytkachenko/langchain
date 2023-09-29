


 An event audience in Creatio is a list of event participants, i. e. contacts connected to the event. Keep track of the event audience responses in marketing campaigns, business processes, dashboards, and on the event page.
 



 Manage the list of event participants in the
 
 Audience
 
 tab:
 


* add contacts and contact folders
* remove participants
* update the event responses
* set up columns and apply filters.



 Add audience
--------------


1. Go to the
 
 Audience
 
 tab on the relevant event page.
2. Click
 ![The “+” button](/docs/sites/en/files/2020-11/btn_plus_0.png)
 (Fig. 1) on the
 
 Audience
 
 detail. This will open a contact list.
 


 Fig. 1 Add audience
 

![Add audience](/docs/sites/en/files/2020-11/scr_events_add_audience_click.png)
3. Select the desired records manually or filter them by set conditions in the contact list. After that, click
 
 Import
 
 and select the import option from the menu:
 


	* If you applied the
	 **filter conditions** 
	 or selected a
	 **folder** 
	 to import, click
	 
	 Import by filter
	 
	 (Fig. 2).
	* If you selected the desired records
	 **manually** 
	 , click
	 
	 Import selected
	 
	 .
4. Click
 
 Close
 
 .




 Fig. 2 Import by filter
 

![Adding contact](/docs/sites/en/files/2020-11/event_add_audience_by_filter.png)



 As a result, Creatio will import the desired records to the event audience and display them on the
 
 Audience
 
 tab of the event page.
 



 Alternatively, set up a
 [marketing campaign](/docs/8-0/user/marketing_tools/marketing_campaings/create_a_campaign/add_campaign) 
 to add the event audience automatically. Use a special element to add the campaign audience to the event audience. Learn more:
 [The
 
 Add to event
 
 element](/docs/8-0/user/marketing_tools/marketing_campaings/campaign_elements/campaign_element_reference#title-347-100) 
 .
 



 Track event responses
-----------------------



 An event response is the status of an event participant, such as whether they planned to participate, participated, canceled their participation, or did not respond. View the responses on the
 
 Audience
 
 tab next to each record.
 





 Note.
 
 Create a lookup named “Response in events” and add the desired statuses as values to change the list of available response statuses. This lookup is not available by default.
 




 Track the event responses and analyze the financial indicators in the
 
 Dashboards
 
 section view.
 



 The
 
 Dashboards
 
 view includes the following tabs:
 


1. The
 
 Audience
 
 tab. This tab contains event participant statistics.
 


 Note.
 
 Creatio will apply the filters set in the section to all dashboards on the tab.
 






|  |  |
| --- | --- |
| 
 Audience by response
  | 
 A diagram with the event audience grouped by their responses.
  |
| 
 Event participants with leads
  | 
 An indicator displaying the number of event participant contacts with leads. The indicator only shows contacts with the “Participation confirmed,” “Participated,” and “Planned” responses.
  |
| 
 Event participants without leads
  | 
 An indicator displaying the number of event participant contacts without leads. The indicator only shows contacts with the “Participation confirmed,” “Participated,” and “Planned” responses.
  |
2. The
 
 Event totals
 
 tab. This tab contains event summary statistics.
 


 Note.
 
 Creatio will apply the filters set in the section to all dashboards on the tab except for the
 
 Upcoming events
 
 block.
 







|  |  |
| --- | --- |
| 
 Expected budget
  | 
 An indicator displaying the total expected event budget, in the base currency.
  |
| 
 Actual cost
  | 
 An indicator displaying the total actual event costs, in the base currency.
  |
| 
 Expected revenue
  | 
 An indicator displaying the total expected event revenue, in the base currency.
  |
| 
 Actual revenue
  | 
 An indicator displaying the total actual event revenue, in the base currency.
  |
| 
 Upcoming events
  | 
 A list of 5 events that start today or later. The data is sorted by date in ascending order. The closest event appears at the top of the list.
  |
| 
 Events by type
  | 
 A diagram with the events grouped by their type.
  |




