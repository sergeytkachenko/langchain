


 Use
 
 Text
 
 fields to manage relatively unique strings, for example, brief record descriptions or names of non-numbered records.
 





 Example.
 
 Set up a
 
 Request description
 
 required text field on the request page. Limit the field to 500 characters and enable users to enter the description on multiple lines.
 





 Fig. 1 Set up a
 
 Text
 
 field
 

![scr_text_field_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_text_field_setup_area.png)


1. Drag a
 
 Text
 
 field to the canvas and open the field setup area.
2. Enter “Request description” in the
 
 Title
 
 parameter. You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/set_title_field_localization.png)
 button to the right to localize the title to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article:
 [Localize a Freedom UI element](https://academy.creatio.com/documents?id=2441) 
 .
3. Review the unique name Creatio uses to add a column in the
 
 Code
 
 parameter. The parameter is populated automatically. You can specify a custom code that starts with the prefix specified in the “Prefix for object name” (“SchemaNamePrefix”) system setting (by default, “Usr”) if needed. This helps no-code creators and software developers to grow and maintain the app easier. For this example, change the code to “UsrRequestDescription.”
4. Select
 
 Text (500 characters)
 
 in the
 
 Format
 
 parameter. Required.
5. Enter internal information about the field that helps to understand its functionality in the
 
 Description
 
 parameter. Creatio displays this information in the Object Designer. For this example, enter “Request description, specified by the requester”. You can localize the parameter similarly to the
 
 Title
 
 parameter.
6. Select
 
 Yes
 
 in the
 
 Required
 
 parameter to make the field required.
7. Select the
 
 Autonumber
 
 checkbox to change the field type to
 
 Autonumber
 
 . For this example, leave the checkbox empty. Learn more about setting up the
 
 Autonumber
 
 field in a separate article:
 [Set up an [Autonumber] field](https://academy.creatio.com/documents?id=2431) 
 .
8. Clear the
 
 Copy this value while copying records
 
 checkbox to prevent Creatio from copying the field value to the record copy in the list. This option is useful for fields that contain system values, auto-populated data, or unique record data.
9. Select the
 
 Localizable text
 
 checkbox to make the field values localizable. For this example, leave the checkbox clear.
10. Select the
 
 Read-only
 
 checkbox to make the field read-only. For this example, leave the checkbox clear.
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
 
 parameter if the title on the live page must differ from the title in the Freedom UI Designer. For this example, enter “Description.” You can localize the parameter similarly to the
 
 Title
 
 parameter.
15. Enter the hint on how to fill out the field in the
 
 Placeholder
 
 parameter. Creatio displays hints in fields before a user starts entering a value. For this example, enter “Tell more about the request.” You can localize the parameter similarly to the
 
 Title
 
 parameter.
16. Enter the tooltip that contains an additional hint in the
 
 Tooltip
 
 parameter. After you fill out the parameter, Creatio displays the
 ![icn_tooltip.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_tooltip.png)
 icon next to the field. Hold the pointer over the icon to view the tooltip. For this example, enter “Description can contain up to 500 characters.” You can localize the parameter similarly to the
 
 Title
 
 parameter.
17. Select the
 
 Multiline text
 
 checkbox to wrap text when it exceeds the field width.
18. Change the data source in the
 
 Data source
 
 parameter. For this example, use the original data source.
19. View the unique field code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar fields on the page. For this example, leave the code as is.



 As a result, Creatio will add the
 
 Request description
 
 required text field to the page of a finance request. The field will have a 500 character limit.
 




