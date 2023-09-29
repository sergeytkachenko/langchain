


 Use the
 
 Campaigns
 
 section in Creatio to plan and conduct marketing campaigns. Inform customers about your upcoming events, invite participants, get in touch with the contacts who are interested in your products and nurture your customer needs using personalized email correspondence.
 



 General campaign workflow
---------------------------



 Planning and running automated marketing campaigns in Creatio involves more than simply adding a new record in the
 
 Campaigns
 
 section. A campaign may require adding new records in other sections, e.g., new trigger emails in the
 
 Email
 
 section. The general workflow for most campaigns is as follows:
 


1. **Define the goal** 
 , the target audience, and the communication chain with potential or existing customers.
2. **Add a new campaign** 
 in the
 
 Campaigns
 
 section and populate the campaign profile. Build a campaign diagram using the campaign designer elements.
3. **Create records** 
 (trigger emails, events, and landing pages) that you plan to include in the campaign. Connect the campaign diagram elements to records in the corresponding sections.
4. **Start the campaign** 
 and follow its progress in the campaign log. Creatio manages the status of campaign participants by analyzing their responses.
5. Once the campaign is finished,
 **view the dashboards** 
 to see if your campaign reached its goal.






 Populate campaign profile
------------------------------



 To run a campaign in Creatio, add a new record in the
 
 Campaigns
 
 section. To do so:
 


1. Open the
 
 Campaigns
 
 section.
2. Click
 
 New campaign
 
 . A new campaign page opens.
 





 Note.
 
 If the “At the specified time” start mode is selected for a campaign, the start/end time of a campaign is displayed in the time zone of the user who created the campaign.
3. Populate the fields on the campaign page:
 





|  |  |
| --- | --- |
| 
 Database object
  | 
 The name of the campaign. Populating this field enables accessing the Campaign Designer.
  |
| 
 Start mode
  | 
 Campaign start/stop options: You can start and stop campaigns manually or set up automatic start and end of a campaign at the specified time.
 
	* “manual” – the campaign will be started/stopped manually by clicking the
	 
	 Start campaign
	 
	 /
	 
	 Stop campaign
	 
	 button.
	* “at the specified time” – select this option to start/stop the campaign automatically at the specific date and time.
 Selecting this option enables additional
 
 Scheduled start date
 
 /
 
 Scheduled end date
 
 fields, where you can specify the scheduled start and end time. Click the
 
 Schedule campaign
 
 button to finalize planning the campaign time frame (Fig. 1).
  |
| 
 End mode
  |
| 
 Owner
  | 
 Select the employee responsible for the campaign.
  |
| 
 utm\_campaign
  | 
 The UTM-mark containing the campaign name. It is used to track the lead sources received as a result of the campaign.
  |







 Fig. 1 Scheduling automatic start and stop of a campaign
 

![section_campaigns_scheduled.png](/docs/sites/en/files/images/Marketing_Tools/add_campaign/section_campaigns_scheduled.png)
4. Click
 
 Save
 
 .



 As a result, a new campaign record will be added in the
 
 Campaigns
 
 section. You can now proceed with creating a
 
[campaign diagram](https://academy.creatio.com/documents?product=marketing&ver=7&id=1487) 

 in the Campaign Designer.
 




