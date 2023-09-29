


 Use
 
 Number
 
 fields to manage numeric data, including integers, decimals, and currency.
 





 Example.
 
 Set up a
 
 Request budget
 
 required currency field on the request page.
 





 Fig. 1 Set up a
 
 Number
 
 field
 

![scr_number_field_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_number_field_setup_area.png)


1. Drag a
 
 Number
 
 field to the canvas and open the field setup area.
2. Enter “Request budget” in the
 
 Title
 
 parameter. You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/set_title_field_localization.png)
 button to the right to localize the title to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article:
 [Localize a Freedom UI element](https://academy.creatio.com/documents?id=2441) 
 .
3. Review the unique name Creatio uses to add a column in the
 
 Code
 
 parameter. The parameter is populated automatically. You can specify a custom code that starts with the prefix specified in the “Prefix for object name” (“SchemaNamePrefix”) system setting (by default, “Usr”) if needed. This helps no-code creators and software developers to grow and maintain the app easier. For this example, change the code to “UsrRequestBudget.”
4. Select
 
 Currency
 
 in the
 
 Format
 
 parameter.
5. Enter internal information about the field that helps to understand its functionality in the
 
 Description
 
 parameter. Creatio displays this information in the Object Designer. For this example, enter “Budget estimate of a finance request in euros, specified by the requester”. You can localize the parameter similarly to the
 
 Title
 
 parameter.
6. Select
 
 Yes
 
 in the
 
 Required
 
 parameter.
7. Clear the
 
 Copy this value while copying records
 
 checkbox to prevent Creatio from copying the field value to the record copy in the list. This option is useful for fields that contain system values, auto-populated data, or unique record data.
8. Select the
 
 Read-only
 
 checkbox to make the field read-only. For this example, leave the checkbox clear.
9. Click the
 ![btn_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_visible.png)
 or
 ![btn_not_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_not_visible.png)
 button in the
 
 Visibility
 
 group to make the element visible or invisible by default on the page, respectively. For this example, leave the field visible.
10. Click
 
 Setup conditions
 
 in the
 
 Visibility
 
 group to set up element business rules. For this example, do not add business rules. Learn more about setting up business rules in a separate article:
 [Set up business rules](https://academy.creatio.com/documents?id=2409) 
 .
11. Specify the position of the title relative to the field in the
 
 Title position
 
 parameter. For this example, select “Left.”
12. Enter
 
 Title on page
 
 parameter if the title on the page must differ from the title in Creatio. For this example, enter “Budget, €.” You can localize the parameter similarly to the
 
 Title
 
 parameter.
13. Enter the hint on how to fill out the field in the
 
 Placeholder
 
 parameter. Creatio displays hints in fields before a user starts entering a value. For this example, enter “Enter the budget estimate.” You can localize the parameter similarly to the
 
 Title
 
 parameter.
14. Enter the tooltip that contains an additional hint in the
 
 Tooltip
 
 parameter. After you fill out the parameter, Creatio displays the
 ![icn_tooltip.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_tooltip.png)
 icon next to the field. Hold the pointer over the icon to view the tooltip. For this example, leave the parameter empty. If you fill out the parameter, you can localize it similarly to the
 
 Title
 
 parameter.
15. Change the data source in the
 
 Data source
 
 parameter. For this example, use the original data source.
16. View the unique field code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar fields on the page. For this example, leave the code as is.



 As a result, Creatio will add the
 
 Request budget
 
 required currency field to the request page.
 




