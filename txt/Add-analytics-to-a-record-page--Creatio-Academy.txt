


 You can configure displaying of dashboard tiles on any record page tab or in the record profile. The following types of dashboards are available on record pages:
 


* [Chart](https://academy.creatio.com/documents?product=base&ver=7&id=1237) 

 .
* [Metric](/docs/8-0/user/customization_tools/analytics/setup/set_up_dashboards#HT_chapter_dashboards_setup_indicator_setup_page) 

 .
* [Gauge](/docs/8-0/user/customization_tools/analytics/setup/set_up_dashboards#HT_chapter_dashboards_setup_scale_setup_page) 

 .
* [Web page](/docs/8-0/user/customization_tools/analytics/setup/set_up_dashboards#HT_chapter_dashboards_setup_webpage_setup_page) 

 .



 The analytics can be added on the section record page using the
 
[section wizard](https://academy.creatio.com/documents?product=base&ver=7&id=1705) 

 or
 
[detail wizard](https://academy.creatio.com/documents?product=base&ver=7&id=1403) 

 .
 





 Note.
 
 The settings of dashboard tiles on record pages are similar to those of the corresponding regular tiles You can find more information about the setup in tile descriptions.
 






 Case.
 
 Create a chart that would display dynamics of communications with the customer on the
 
 History
 
 tab of the contact page.
 



1. In the
 
 View
 
 menu of the contact page, select the
 **Open section wizard** 
 action.
2. Open the page designer by clicking the
 **Page** 
 button on the wizard navigation panel (
 [Fig. 1](#XREF_23498_243)
 ).
 





 Fig. 1
 

 Page designer
 

![chapter_analytics_add_analytics_to_page_open_page_designer.png](/guides/sites/en/files/documentation/user/en/analytics/BPMonlineHelp/analytics_add_on_record_page/chapter_analytics_add_analytics_to_page_open_page_designer.png)
3. Click the
 
 History
 
 tab (the one that will display the diagram) on the right side of the wizard panel (
 [Fig. 2](#XREF_77170_244)
 ).
 





 Fig. 2
 

 Switching to the
 
 History
 
 tab
 

![chapter_analytics_add_analytics_to_page_page_designer_history_tab.png](/guides/sites/en/files/documentation/user/en/analytics/BPMonlineHelp/analytics_add_on_record_page/chapter_analytics_add_analytics_to_page_page_designer_history_tab.png)
4. Add a new field group, which will contain the diagram by clicking the
 **New filed group** 
 button at the bottom of the page. Locate the field group at the top of the
 
 History
 
 tab page.
 





 Note.
 
 If you need to add analytics on a page detail, use the detail wizard instead of the section wizard.
5. Expand the “Add widget” block and
 **select a dashboard tile** 
 . In this case, it is the “Chart” tile. Drag it on the tab (
 [Fig. 3](#XREF_39255_5)
 ). Areas, where you can add the chart, will be highlighted in blue.
 





 Fig. 3
 

 Adding a chart on the contact page
 

![chapter_analytics_add_dashboard_to_page.png](/guides/sites/en/files/documentation/user/en/analytics/BPMonlineHelp/analytics_add_on_record_page/chapter_analytics_add_dashboard_to_page.png)
6. On the opened setup page (
 [Fig. 4](#XREF_46702_246) 
 ), specify parameters for the chart with two
 
[series](/docs/8-0/user/customization_tools/analytics/setup/set_up_dashboards#HT_chapter_analytics_several_series_on_a_chart) 

 that would display the number of calls and emails of the contact for the current month. Set the parameters as follows:
 


	1. Title
	 
	 – “Calls and emails for the current month”.
	2. Object
	 
	 – for the first series, it is the “Call” object, and for the second series, it is the “Activity” object.
	3. Function
	 
	 – “Count”.
	4. Chart type
	 
	 – “Line”.
	5. Grouping by the “End date” column for calls and the “Due” column for activities.
	6. Configure filters. Specify the “End date = Current month” for calls. Specify two conditions for activities: “Type = Email” and “Due = Current month”.
	7. Associate the object with the section by the “Id” column of the “Contact” object.
	8. Save your settings.
	 
	
	
	
	
	
	 Fig. 4
	 
	
	 Setting up the “Calls and emails for the current month” chart
	 
	
	![chapter_analytics_add_analytics_to_page_chart_setup_example.png](/guides/sites/en/files/documentation/user/en/analytics/BPMonlineHelp/analytics_add_on_record_page/chapter_analytics_add_analytics_to_page_chart_setup_example.png)
 More information about the “Chart” dashboard configuration is available in the
 
[Set up dashboards](/docs/8-0/user/customization_tools/analytics/setup/set_up_dashboards#HT_chapter_dashboards_setup_chart_designer) 

 article.
7. For correct displaying of the data, adjust the size of the chart (
 [Fig. 5](#XREF_48720_6)
 ).
 





 Fig. 5
 

 Resizing the chart
 

![chapter_analytics_change_dashboard_size.png](/guides/sites/en/files/documentation/user/en/analytics/BPMonlineHelp/analytics_add_on_record_page/chapter_analytics_change_dashboard_size.png)



 As a result, the chart showing the dynamics of communications with the contact for the current month will be displayed on the contact page (
 [Fig. 6](#XREF_26330_5)
 ).
 





 Fig. 6
 

 Record page with a configured dashboard tile
 

![scr_analytics_dashboard_on_page.png](/guides/sites/en/files/documentation/user/en/analytics/BPMonlineHelp/analytics_add_on_record_page/scr_analytics_dashboard_on_page.png)





 Note.
 
 You can display the data used for building the chart as a list.
 
[Read more >>>](/docs/8-0/user/customization_tools/analytics/view_analytics_shortcut/view_analytics#HT_chapter_analytics_list_mode) 







