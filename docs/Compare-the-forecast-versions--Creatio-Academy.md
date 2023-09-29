



 This feature is only available for forecast tab versions created after updating Creatio to version 7.17.3.
 




 Track forecast changes with the forecast tab versioning. Creatio saves the forecast as a separate version if you specify the daily autosave parameters in the
 
 Automation
 
 tab when setting up the forecast object and period. Read more:
 [Set up the forecast object and period](/docs/8-0/user/sales_tools/forecasting/set_up_a_forecast_shortcut/set_up_a_forecast#title-338-1) 
 .
 



 You can:
 


* Select and view a specific forecast version.
* Set up the daily forecast autosave time. Read more:
 [Set up the forecast object and period](/docs/8-0/user/sales_tools/forecasting/set_up_a_forecast_shortcut/set_up_a_forecast#title-338-1) 
 .
* Compare a selected forecast version with the current version.



 You must have access
 [permissions](/docs/8-0/user/sales_tools/forecasting/forecast_access_permissions/managing_access_to_forecasts) 
 to view the forecast tab and its records.
 



 Click the
 ![btn_calendar.png](/docs/sites/en/files/images/Sales_Tools/forecasting/btn_calendar.png)
 button and select the relevant day to
 **select** 
 and view the forecast version for a specific date. You can only select the days when Creatio autosaved the forecast version, starting from the date when you set up the version saving. The dates with saved forecast tab versions are clickable and marked in the calendar.
 





 Note.
 
 If you edit a forecast several times a day, you will be able to view only the data available at the time specified in the autosave settings.
 




 Click the
 ![btn_close.png](/docs/sites/en/files/images/Sales_Tools/forecasting/btn_close.png)
 button next to the date to
 **return to the up-to-date forecast tab** 
 . Select another date to load a different forecast tab version.
 



 After you select the date, Creatio will highlight the changes relative to the selected version on the current forecast tab:
 


* Values
 **higher** 
 in the current version will be highlighted
 **green** 
 .
* Values
 **lower** 
 in the current version will be highlighted
 **red** 
 (Fig. 1).



 When you view a specific forecast tab version, Creatio will only display the rows that existed when this version was saved. Rows that existed in the forecast tab on a specific date yet
 **do not exist in the current tab** 
 will be
 **greyed out** 
 .
 




 Fig. 1 Comparing data between the forecast tab versions
 

![forecasting_versions.png](/docs/sites/en/files/images/Sales_Tools/forecasting/forecasting_versions.png)



 You can drill down the data used for formula calculations in the forecast columns. To do this, select the relevant date and click a cell you need to drill down. You can only select the cells of the “Value from object” type displayed as links.
 




