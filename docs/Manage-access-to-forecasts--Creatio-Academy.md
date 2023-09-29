


 Manage Creatio forecasts in the
 
 Forecasts
 
 section.
 



 Set up permissions to the section data by setting up permissions to the “Forecast” and “ForecastSheet” objects.
 



 Creatio generates individual system objects for the forecast by a dimension automatically. For example, “ContactForecast,” “AccountForecast,” “ProductForecast” for contact, account, product dimension, respectively. These objects inherit permissions from the “ForecastRow” object.
   

 As such, to ensure the correct operation of the forecast, configure permissions to operations and forecast rows, e. g., add new rows, edit cells, etc., in the “ForecastRow” object.
 



 Learn more:
 [Object operation permissions](https://academy.creatio.com/documents?id=262) 
 .
 



 You can set up permissions to forecasts and separate records within them, as well as permissions to calculate forecasts.
 





 Example.
 
 Only sales associates and their superiors must be able to access the configured forecast. Only the sales department managers must be able to access individual forecast records.
 




 Set up the forecast permissions
---------------------------------



 To enable only sales associates and their superiors to access the configured forecast, assign the access permissions for the forecast tab. To do this:
 


1. Go to the
 
 Forecasts
 
 section and open the needed forecast tab.
2. Click
 ![btn_com_menu_gear.png](/guides/sites/en/files/documentation/user/en/forecasting/BPMonlineHelp/forecasting_permissions/btn_com_menu_gear.png)
 →
 
 Set up access rights
 
 . This will open a new page.
3. Set up access permissions to the forecast on the page.
 


	1. Click
	 
	 New
	 
	 and select the “Read access right” option in the menu. This will open a selection box. Select the “Sales Department” role in the box.
	2. Grant the read, edit, and delete permissions to the superiors of the sales associates in a similar way.
4. Save the changes. As a result, only the sales department employees will be able to view the forecast.



 Set up permissions to a forecast record
-----------------------------------------



 To enable only the sales department managers to access individual forecast records, restrict the access permissions of sales associates. To do this:
 


1. Go to the
 
 Forecasts
 
 section and open the needed forecast tab.
2. Select the record whose permissions to set up.
3. Hover over the record and click the
 ![btn_user_access.png](/guides/sites/en/files/documentation/user/en/forecasting/BPMonlineHelp/forecasting_permissions/btn_user_access.png)
 button (Fig. 1). This will open a new page.
 




 Fig. 1 Select a record whose permissions to set up
 

![scr_section_planning_select_record_access.png](/guides/sites/en/files/documentation/user/en/forecasting/BPMonlineHelp/forecasting_permissions/scr_section_planning_select_record_access.png)
4. Click
 
 New
 
 and select the “Read access right”, “Edit access right”, or “Delete access right” option in the menu (Fig. 2) on the page. This will open a selection box. Learn more:
 [Object operation permissions](https://academy.creatio.com/documents?id=262) 
 .
 




 Fig. 2 Set up the record access permissions
 

![scr_section_planning_set_record_access.png](/guides/sites/en/files/documentation/user/en/forecasting/BPMonlineHelp/forecasting_permissions/scr_section_planning_set_record_access.png)
5. Select the “Sales Department. Head Office” role in the box. You can also grant permissions to this record to individual users.
6. Click
 
 Save
 
 . As a result, only the sales department managers will be able to view, edit, or delete the record.



 Set up permission to calculate a forecast
-------------------------------------------



 Set up permission to calculate a forecast in the “Can Calculate Forecast” (the “CanCalculateForecast” code) system operation. By default, any user in the “All employees” role can run this operation, but you can restrict it to specific employees. For example, only the managers of the sales and finance departments. Learn more about managing system operation permissions in a separate article:
 [System operation permissions](https://academy.creatio.com/documents?id=2000) 
 .
 




