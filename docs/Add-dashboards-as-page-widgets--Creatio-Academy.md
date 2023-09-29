


 You can add
 [dashboards](https://academy.creatio.com/documents?product=administration&ver=7&id=1236) 
 on a record page tab or in the record profile. For this, use the “Widgets” page elements (Fig. 1) available on the left-side panel of the Page Designer.
 





 Fig. 1
 

 Widget area in the Page Designer
 

![chapter_section_wizard_page_designer_widgets.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_dashboards_as_page_widgets/chapter_section_wizard_page_designer_widgets.png)



 You can add the following types of dashboards on a record page:
 


* [Chart](https://academy.creatio.com/documents?product=base&ver=7&id=1237)
* [Metric](/docs/8-0/user/customization_tools/analytics/setup/set_up_dashboards#HT_chapter_dashboards_setup_indicator_setup_page)
* [Gauge](/docs/8-0/user/customization_tools/analytics/setup/set_up_dashboards#HT_chapter_dashboards_setup_scale_setup_page)
* [Web page](/docs/8-0/user/customization_tools/analytics/setup/set_up_dashboards#HT_chapter_dashboards_setup_webpage_setup_page)





 Note.
 
 More information about setting up different types of dashboards is available in the
 [Dashboards](https://academy.creatio.com/documents?product=administration&ver=7&id=1236) 
 article.
 






 Example.
 
 Create a chart that would display the dynamics of communication with a customer on the
 
 History
 
 tab of the contact page.
 




 To add a chart on the contact page:
 


1. Open the
 **Contacts** 
 section.
2. Click
 
 View
 
 →
 **Open Section Wizard** 
 .
 





 Note.
 
 If you need to add dashboards on a detail page, use the Detail Wizard instead of the Section Wizard.
3. In the “Section pages” block of the Section Wizard:
 


	1. if you have only one edit page in your section, click
	 **Edit page;**
	2. if you have several edit pages in your section, click
	 **the link of a corresponding page** 
	 in the list (Fig. 2).
	 
	
	
	
	
	
	 Fig. 2
	 
	
	 Selecting a section edit page from the list
	 
	
	![scr_section_wizard_multiple_contact_pages.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_dashboards_as_page_widgets/scr_section_wizard_multiple_contact_pages.png)
4. In the Page Designer that opens, click the
 
 History
 
 tab (Fig. 3). This tab will display your diagram.
 





 Fig. 3
 

 Switching to the
 
 History
 
 tab
 

![chapter_analytics_add_analytics_to_page_page_designer_history_tab.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_dashboards_as_page_widgets/chapter_analytics_add_analytics_to_page_page_designer_history_tab.png)
5. Add a new “Dynamics of communication” field group. Place the field group at the top of the
 
 History
 
 tab page. This field group will contain the newly created diagram.
6. Expand the
 
 Page elements
 
 block and drag the needed widget on the page. For example, drag-and-drop the
 
 Chart
 
 widget to the new
 
 Dynamics of communication
 
 field group. Areas, where you can place the chart, will be highlighted in blue (Fig. 4).
 





 Fig. 4
 

 Adding a chart on the contact page
 

![chapter_section_wizard_add_dashboard_to_page.gif](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_dashboards_as_page_widgets/chapter_section_wizard_add_dashboard_to_page.gif)
7. On the opened chart setup page, populate the first series of the chart that would display the number of calls of the contact for the needed period, e.g., the previous quarter. Set the parameters as follows:
 





 Fig. 5
 

 Setting up the “Calls and emails for the previous quarter” chart
 

![chapter_section_wizard_add_analytics_to_page_chart_setup_example.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_dashboards_as_page_widgets/chapter_section_wizard_add_analytics_to_page_chart_setup_example.png)


1. Title
 
 – “Calls and emails for the previous quarter”
2. X-Axis label
 
 – “Date”
3. Y-Axis label
 
 – “Number of calls and emails”
4. Object
 
 – “Call”
5. Function
 
 – “Count”
6. Chart type
 
 – “Line”
7. How to group
 
 – set grouping by the “End date” column for calls.
8. Format
 
 – “Day & month”
9. How to filter
 
 – Specify the “End date = Previous quarter” for calls.
10. How to associate with section data
 
 – Specify “Id” to display the data for the selected contact only.
11. Add another series to your chart widget by clicking
 ![btn_com_content_designer_gear_menu.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_dashboards_as_page_widgets/btn_com_content_designer_gear_menu.png)
 and selecting the “Add series” option (Fig. 6).
 





 Fig. 6
 

 Adding series to a chart widget
 

![chapter_section_wizard_adding_chart_widget_series.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_dashboards_as_page_widgets/chapter_section_wizard_adding_chart_widget_series.png)
12. Populate the properties of the second series:
 


	1. Object
	 
	 – “Activity”
	2. Function
	 
	 – “Count”
	3. Chart type
	 
	 – “Line”
	4. How to group
	 
	 – set grouping by the “Due” column for activities.
	5. Format
	 
	 – “Day & month”
	6. How to filter
	 
	 – Specify two conditions for activities: “Type = Email” and “Due = Previous quarter.”
	7. How to associate with section data
	 
	 – Specify “Id” to display the data for the selected contact only.
13. Click
 
 Save
 
 .
14. For the correct displaying of data, adjust the size of the chart (Fig. 7).
 





 Fig. 7
 

 Resizing the chart
 

![chapter_analytics_change_dashboard_size.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_dashboards_as_page_widgets/chapter_analytics_change_dashboard_size.png)



 As a result, the chart showing the dynamics of communication with the contact for the previous quarter will be displayed on the contact page (Fig. 8).
 





 Fig. 8
 

 Record page with a configured chart widget
 

![scr_chapter_section_wizard_dashboard_on_page.png](/guides/sites/en/files/documentation/user/en/ui_business_logic_customization/BPMonlineHelp/add_dashboards_as_page_widgets/scr_chapter_section_wizard_dashboard_on_page.png)





 Note.
 
 Learn more about configuring charts in the “
 [Chart” dashboard tile”](https://academy.creatio.com/documents?product=administration&ver=7&id=1237) 
 article.
 





