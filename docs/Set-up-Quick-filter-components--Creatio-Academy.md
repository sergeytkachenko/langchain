


 Use
 
 Quick filter
 
 components to filter lists or charts except for “Sales pipeline” and “Full pipeline” by custom conditions, date/time, or lookup values.
 



 Set up a custom filter
------------------------





 Example.
 
 Set up the
 
 Quick filter
 
 component that filters the list by open requests on the list page.
 





 Fig. 1 Set up a
 
 Quick filter
 
 component that uses a custom filter
 

![scr_custom_quick_filter_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_custom_quick_filter_setup_area.png)


1. Add and set up a “Request status” field. Connect the field to the
 
 Status
 
 custom lookup that has multiple values, including “Closed”. Learn more about the setup in separate articles:
 [Set up a [Dropdown] field](https://academy.creatio.com/documents?id=2424) 
 ,
 [Manage lookup values](https://academy.creatio.com/documents?id=271) 
 .
2. Drag a
 
 Quick filter
 
 component to the canvas and open the component setup area
3. Select “Custom” in the
 
 Choose a filter type
 
 parameter. This brings up new parameters.
4. Select the list in the
 
 Component to filter
 
 parameter.
5. Click
 
 Setup filter
 
 and configure the “Status ≠ Closed” filter. The filter setup process is similar to classic UI. Learn more in a separate article:
 [Advanced filter](https://academy.creatio.com/documents?id=1017#title-1755-10) 
 .
6. Specify whether to keep the filter checkbox selected or cleared on page load in the
 
 Default checkbox state
 
 parameter. For this example, set the checkpoint to be selected.
7. Specify whether to apply the filter when a user selects or clears the filter checkbox in the
 
 Filtering approach
 
 parameter. For this example, leave the filter applied when a user selects the checkbox.
8. Enter “Show closed requests” in the
 
 Title
 
 parameter. You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/set_title_field_localization.png)
 button to the right to localize the title to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article:
 [Localize a Freedom UI element](https://academy.creatio.com/documents?id=2441) 
 .
9. Enter the filter tooltip in the
 
 Hint
 
 parameter. Hold the pointer over the filter to view the tooltip. For this example, enter “Excludes requests whose status is “Closed.”” You can localize the parameter similarly to the
 
 Title
 
 parameter.
10. View the unique component code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar components on the page. For this example, leave the code as is.



 As a result, Creatio will add the
 
 Quick filter
 
 component that filters the list by open requests to the list page.
 



 Set up a date/time filter
---------------------------





 Example.
 
 Set up the
 
 Quick filter
 
 component that filters records by creation date on the list page.
 





 Fig. 2 Set up a
 
 Quick filter
 
 component that uses a date/time filter
 

![scr_datetime_quick_filter_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_datetime_quick_filter_setup_area.png)


1. Drag a
 
 Quick filter
 
 component to the canvas and open the component setup area
2. Select “Date/Time” in the
 
 Choose a filter type
 
 parameter. This brings up new parameters.
3. Select the list in the
 
 Component to filter
 
 parameter.
4. Specify whether to use single dates or date ranges for the filter boundaries in the in the
 
 Choose a filtering method
 
 parameter. For this example, select “Set up filter by one date.”
5. Select “Created on” in the
 
 Filter column
 
 parameter.
6. Specify the filter period to apply on page load in the
 
 Default period
 
 parameter. If you leave the parameter empty, Creatio does not apply any filter period on page load. For this example, leave the parameter empty.
7. Enter the filter caption in the
 
 Title
 
 parameter. Creatio populates the parameter using the filter column name, but you can change the parameter if needed. For this example, leave the parameter as is. You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/set_title_field_localization.png)
 button to the right to localize the title to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article:
 [Localize a Freedom UI element](https://academy.creatio.com/documents?id=2441) 
 .
8. Enter the filter tooltip in the
 
 Hint
 
 parameter. Hold the pointer over the filter to view the tooltip. For this example, leave the parameter empty. If you fill out the parameter, you can localize it similarly to the
 
 Title
 
 parameter.
9. Click the
 
 Use icon
 
 toggle to remove the icon from the filter. For this example, leave the parameter as is.
10. Select the needed filter icon in the
 
 Icon
 
 parameter. For this example, use the
 ![icn_datetime_filter.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_datetime_filter.png)
 icon.
11. Specify the icon position or toggle the filter caption in the
 
 Position
 
 parameter. For this example, place the icon to the left of the caption.
12. View the unique component code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar components on the page. For this example, leave the code as is.



 As a result, Creatio will add the
 
 Quick filter
 
 component that filters the list by record creation date to the list page.
 



 Set up a lookup filter
------------------------





 Example.
 
 Set up the
 
 Quick filter
 
 component that filters list records by requester on the list page.
 





 Fig. 3 Set up a
 
 Quick filter
 
 component that uses a lookup filter
 

![scr_lookup_quick_filter_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_lookup_quick_filter_setup_area.png)


1. Add and set up a “Requester” field. Connect the field to the
 
 Contacts
 
 lookup. To do this, follow the steps in separate article:
 [Set up a dropdown field](https://academy.creatio.com/documents?id=2425) 
 .
2. Drag a
 
 Quick filter
 
 component to the canvas and open the component setup area
3. Select “Lookup” in the
 
 Choose a filter type
 
 parameter. This brings up new parameters.
4. Select the list in the
 
 Component to filter
 
 parameter.
5. Select “Requester” in the
 
 Filter column
 
 parameter. This brings up new parameters.
6. Specify the lookup value to apply to the filter on page load in the
 
 Default value
 
 parameter. If you clear the parameter, Creatio does not apply any lookup value to the filter on page load. For this example, clear the parameter.
7. Click
 
 Setup filter
 
 to narrow down the lookup values available in the component. For example, display only employees of a specific department. The filter setup process is similar to classic UI. Learn more in a separate article:
 [Advanced filter](https://academy.creatio.com/documents?id=1017#title-1755-10) 
 . For this example, do not set up the filter.
8. Enter the filter caption in the
 
 Title
 
 parameter. Creatio populates the parameter using the filter column name, but you can change the parameter if needed. For this example, leave the parameter as is. You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCode_Customization/designer_interfaces/set_title_field_localization.png)
 button to the right to localize the title to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article:
 [Localize a Freedom UI element](https://academy.creatio.com/documents?id=2441) 
 .
9. Enter the filter tooltip in the
 
 Hint
 
 parameter. Hold the pointer over the filter to view the tooltip. For this example, leave the parameter empty. If you fill out the parameter, you can localize it similarly to the
 
 Title
 
 parameter.
10. Click the
 
 Use icon
 
 toggle to remove the icon from the filter. For this example, leave the parameter as is.
11. Select the needed filter icon in the
 
 Icon
 
 parameter. For this example, use the
 ![icn_lookup_filter.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_lookup_filter.png)
 icon.
12. Specify the icon position or toggle the filter caption in the
 
 Position
 
 parameter. For this example, place the icon to the left of the caption.
13. View the unique component code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar components on the page. For this example, leave the code as is.



 As a result, Creatio will add the
 
 Quick filter
 
 component that filters list records by specific requester to the list page.
 




