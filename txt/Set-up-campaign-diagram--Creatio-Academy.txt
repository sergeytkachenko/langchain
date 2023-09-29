


 A campaign flow diagram (Fig. 1) includes:
 


* [Elements](/docs/8-0/user/marketing_tools/marketing_campaings/campaign_elements/campaign_element_reference) 
 .
* [Flows](/docs/8-0/user/marketing_tools/marketing_campaings/campaign_element_transition/transition_between_campaign_elements) 
 between campaign elements.
* [General campaign settings](#title-2066-1) 
 .



 Use the Campaign designer to set up campaign flow diagrams. To open the Campaign designer:
 


1. Open the needed record in the
 
 Campaigns
 
 section.
2. Go to the
 
 Campaign flow
 
 tab and click
 
 Create
 
 if no diagram exists or
 
 Edit
 
 to change an existing diagram.




 Fig. 1 Campaign designer overview
 

![setup_campaign_diagram_overview.png](/docs/sites/en/files/images/Marketing_Tools/set_up_campaign_diagram/setup_campaign_diagram_overview.png)



 Campaign designer features
----------------------------



 The Campaign designer lets you:
 


* **Save and cancel** 
 changes using the toolbar (1).
 


 Note.
 
 Creatio saves campaigns automatically. If you close a campaign diagram without saving, you will be able to load the autosaved data later.
 




 Use the corresponding buttons on the toolbar to open the element setup area, open the Academy, or search the diagram for campaign elements by name.
* **Set up the campaign diagram** 
 using
 [elements](/docs/8-0/user/marketing_tools/marketing_campaings/campaign_elements/campaign_element_reference) 
 and
 [flows](/docs/8-0/user/marketing_tools/marketing_campaings/campaign_element_transition/transition_between_campaign_elements) 
 in the Campaign designer working area (2). Select an element in the
 
 Elements
 
 area of the designer and drag it to the campaign area to add it to the diagram (Fig. 2).
 



 Select an element and select “Delete” to delete it.
 




 Fig. 2 Adding elements and flows to the working area
 

![section_campaigns_add_elements.gif](/docs/sites/en/files/images/Marketing_Tools/set_up_campaign_diagram/section_campaigns_add_elements.gif)
* **Select elements and tools** 
 in the element area (3). The area contains the
 [campaign elements](/docs/8-0/user/marketing_tools/marketing_campaings/campaign_elements/campaign_element_reference) 
 and the following tools:
 


	+ ![arrow_tool.png](/docs/sites/en/files/images/Marketing_Tools/set_up_campaign_diagram/arrow_tool.png)
	 “
	 **Arrow** 
	 .” Use this tool to select and move separate elements on the diagram.
	+ ![lasso_tool.png](/docs/sites/en/files/images/Marketing_Tools/set_up_campaign_diagram/lasso_tool.png)
	 “
	 **Lasso** 
	 .” Use this tool to select multiple elements on the diagram.
	+ ![space_tool.png](/docs/sites/en/files/images/Marketing_Tools/set_up_campaign_diagram/space_tool.png)
	 “
	 **Space** 
	 .” Use this tool to move parts of the diagram left/right or up/down. For example, drag the cursor down to move all the elements below the cursor.
	   
	
	 Learn more about these tools:
	 [Process designer](/docs/8-0/user/bpm_tools/business_process_setup/overview/process_designer) 
	 .


* **Specify parameter values** 
 for campaigns and campaign elements in the
 **element setup area** 
 (4).
* **Zoom and pan** 
 the campaign diagram (5).



 Set up the campaign properties
--------------------------------



 Configure the
 **campaign properties** 
 in the element setup area (4). Click anywhere on the campaign designer working area or click the
 ![btn_system_designer.png](/docs/sites/en/files/images/Marketing_Tools/set_up_campaign_diagram/btn_system_designer.png)
 button to open the campaign properties area.
 


1. Default campaign execution frequency
 
 – determines how often to execute the campaign steps without a set execution period.
 
 The frequency specified in this parameter applies to:
 


	* The campaign steps whose incoming
	 [flows](/docs/8-0/user/marketing_tools/marketing_campaings/campaign_element_transition/transition_between_campaign_elements) 
	 do not specify an exact time.
	* The
	 [Add audience](/docs/8-0/user/marketing_tools/marketing_campaings/campaign_elements/campaign_element_reference#title-347-1)
	 element that adds new participants to the campaign.
	* The
	 [Exit from campaign](/docs/8-0/user/marketing_tools/marketing_campaings/campaign_elements/campaign_element_reference#title-347-7)
	 element that removes participants from the campaign.
2. Time zone
 
 – sets the time zone for all the campaign's time frames. For example, the execution time of conditional flows. By default, Creatio sets the campaign time zone to:
	* The time zone of the user who created the campaign.
	* The time zone specified in the “Default TimeZone” (“DefaultTimeZone” code) system setting if there is no time zone set in the user profile.
 If Creatio cannot set the time zone according to the rules above, it will populate the
 
 Time zone
 
 field of the new campaign with the “(GMT) UTC Time Format” value. You can change the time zone at any time.
 





 Note.
 
 Set up the execution time according to additional time zones within the campaign using the
 [Timer](/docs/8-0/user/marketing_tools/marketing_campaings/campaign_elements/campaign_element_reference#title-347-11)
 element.
3. Set the period for campaign emergency stop in case of critical delay
 
 – select the checkbox to define the critical delay time. If the campaign does not run during this period, for example, due to application updates, Creatio will stop it automatically, and the campaign owner will receive a notification.
4. Specify the delay units and their value after selecting the checkbox.
 





 Note.
 
 If you do not select the
 
 Set the period for campaign emergency stop in case of critical delay
 
 checkbox, the default campaign frequency will equal the time of critical delay.



 Use preset campaign steps
---------------------------



 Save the element settings to reuse them in any campaign when setting up similar steps. This streamlines the campaign setup.
 





 Example.
 
 Save and reuse the settings of the
 
 Add audience
 
 element that adds contacts from the “Sales-ready” dynamic folder to the campaign.
 



### 
 Create an element template


1. Drag the
 
 Add audience
 
 element to the campaign diagram and fill out its properties:
	1. Select an object (entity) that holds the campaign audience data
	 
	 – “Contact.”
	2. Specify which records will be converted to the campaign audience
	 
	 – “Records in a specific folder.”
	3. Which folder to add participants from?
	 
	 – “Sales-ready.” Read more:
	 [The
	 
	 Add audience
	 
	 element](/docs/8-0/user/marketing_tools/marketing_campaings/campaign_elements/campaign_element_reference#title-347-1) 
	 .
2. Click
 
 Save
 
 (Fig. 3). This will open a dialog box.
 

 Fig. 3 Save the element settings
 



![campaign_elements_save_settings.png](/docs/sites/en/files/images/Marketing_Tools/set_up_campaign_diagram/campaign_elements_save_settings.png)
3. Enter the template name and click
 
 OK
 
 in the box (Fig. 4).
 

 Fig. 4 Save the element template
 



![campaign_elements_save_template.png](/docs/sites/en/files/images/Marketing_Tools/set_up_campaign_diagram/campaign_elements_save_template.png)



 As a result, Creatio will save the template to the
 
 Campaign element templates
 
 lookup. You will be able to reuse the template during the campaign setup.
 


### 
 Use a preset element in the campaign


1. Add the element to the diagram and click
 
 Select from lookup
 
 in the element settings (Fig. 5).
 

 Fig. 5 Add the template from the lookup
 



![campaign_elements_choose_from_lookup.png](/docs/sites/en/files/images/Marketing_Tools/set_up_campaign_diagram/campaign_elements_choose_from_lookup.png)
2. Select the relevant template from the list.



 As a result, the Campaign designer will apply the template settings to the element.
 



 This feature copies the element settings as opposed to the element itself. As such, you must create a new element of the corresponding type and load the template settings every time when using the preset step.
 




