


 Use
 
 Autonumber
 
 fields for managing record number data automatically. This is particularly useful for cases, requests, or contracts.
 





 Example.
 
 Set up a
 
 Request number
 
 required read-only autonumber field on the request page.
 





 Fig. 1 Set up an
 
 Autonumber
 
 field
 

![scr_autonumber_field_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_autonumber_field_setup_area.png)


1. Drag an
 
 Autonumber
 
 field to the canvas and open the field setup area.
2. Enter “Request number” in the
 
 Title
 
 parameter. You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/set_title_field_localization.png)
 button to the right to localize the title to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article:
 [Localize a Freedom UI element](https://academy.creatio.com/documents?id=2441) 
 .
3. Review the unique name Creatio uses to add a column in the
 
 Code
 
 parameter. The parameter is populated automatically. You can specify a custom code that starts with the prefix specified in the “Prefix for object name” (“SchemaNamePrefix”) system setting (by default, “Usr”) if needed. This helps no-code creators and software developers to grow and maintain the app easier. For this example, change the code to “UsrRequestNumber.”
4. View the field format in the
 
 Format
 
 parameter. You can change the format to
 
 Phone number
 
 to change the field type. For this example, leave the format at
 
 Text(50 characters)
 
 . Learn more about setting up
 
 Phone
 
 fields in a separate article:
 [Set up a [Phone] field](https://academy.creatio.com/documents?id=2427) 
 .
5. Enter internal information about the field that helps to understand its functionality in the
 
 Description
 
 parameter. Creatio displays this information in the Object Designer. For this example, enter “Request number, populated automatically, non-editable.” You can localize the parameter similarly to the
 
 Title
 
 parameter.
6. Select
 
 Yes
 
 in the
 
 Required
 
 parameter.
7. Clear the
 
 Autonumber
 
 checkbox to change the field type to
 
 Text
 
 . For this example, leave the checkbox selected. Learn more about setting up
 
 Text
 
 fields in a separate article:
 [Set up a [Text] field](https://academy.creatio.com/documents?id=2421) 
 .
8. Enter the prefix before the request number in the
 
 Prefix
 
 parameter. For this example, enter “IRQ-.”
9. Specify the number of digits in the request number in the
 
 Number of characters
 
 parameter. For this example, leave the parameter value at “5.”
10. Select the
 
 Read-only
 
 checkbox to make the field read-only.
11. Click the
 ![btn_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_visible.png)
 or
 ![btn_not_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_not_visible.png)
 button in the
 
 Visibility
 
 group to make the element visible or invisible by default on the page, respectively. For this example, leave the field visible.
12. Click
 
 Setup conditions
 
 in the
 
 Visibility
 
 group to set up element business rules. For this example, do not add business rules. Learn more about setting up business rules in a separate article:
 [Set up business rules](https://academy.creatio.com/documents?id=2409) 
 .
13. Specify the position of the title relative to the field in the
 
 Title position
 
 parameter. For this example, select “Above.”
14. Enter
 
 Title on page
 
 parameter if the title on the page must differ from the title in Creatio. For this example, enter “Number.” You can localize the parameter similarly to the
 
 Title
 
 parameter.
15. Enter the hint on how to fill out the field in the
 
 Placeholder
 
 parameter. Creatio displays hints in fields before a user starts entering a value. For this example, leave the parameter empty. If you fill out the parameter, you can localize it similarly to the
 
 Title
 
 parameter.
16. Enter the tooltip that contains an additional hint in the
 
 Tooltip
 
 parameter. After you fill out the parameter, Creatio displays the
 ![icn_tooltip.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_tooltip.png)
 icon next to the field. Hold the pointer over the icon to view the tooltip. For this example, leave the parameter empty. If you fill out the parameter, you can localize it similarly to the
 
 Title
 
 parameter.
17. Select the
 
 Multiline text
 
 checkbox to wrap request number when it exceeds the field width. For this example, leave the checkbox clear.
18. Change the data source in the
 
 Data source
 
 parameter. For this example, use the original data source.
19. View the unique field code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar fields on the page. For this example, leave the code as is.



 As a result, Creatio will add the
 
 Request number
 
 required read-only autonumber field to the request page. The field will be populated automatically.
 




