


 Use
 
 Color
 
 fields to manage color data. This is particularly useful for physical products.
 





 Example.
 
 Set up a
 
 Requested business card color
 
 color field on the page of a request to print out business cards. Enable users to specify custom colors.
 





 Fig. 1 Set up a
 
 Color
 
 field
 

![scr_color_field_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_color_field_setup_area.png)


1. Drag a
 
 Color
 
 field to the canvas and open the field setup area.
2. Enter “Requested business card color” in the
 
 Title
 
 parameter. You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/set_title_field_localization.png)
 button to the right to localize the title to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article:
 [Localize a Freedom UI element](https://academy.creatio.com/documents?id=2441) 
 .
3. Review the unique name Creatio uses to add a column in the
 
 Code
 
 parameter. The parameter is populated automatically. You can specify a custom code that starts with the prefix specified in the “Prefix for object name” (“SchemaNamePrefix”) system setting (by default, “Usr”) if needed. This helps no-code creators and software developers to grow and maintain the app easier. For this example, change the code to “UsrRequestBusinessCardColor.”
4. View the field format in the
 
 Format
 
 parameter. Only “Color” value is available.
5. Enter internal information about the field that helps to understand its functionality in the
 
 Description
 
 parameter. Creatio displays this information in the Object Designer. For this example, enter “Business card color specified by the requester”. You can localize the parameter similarly to the
 
 Title
 
 parameter.
6. Clear the
 
 Copy this value while copying records
 
 checkbox to prevent Creatio from copying the field value to the record copy in the list. This option is useful for fields that contain system values, auto-populated data, or unique record data.
7. Click the
 ![btn_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_visible.png)
 or
 ![btn_not_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_not_visible.png)
 button in the
 
 Visibility
 
 group to make the element visible or invisible by default on the page, respectively. For this example, leave the field visible.
8. Click
 
 Setup conditions
 
 in the
 
 Visibility
 
 group to set up element business rules. For this example, do not add business rules. Learn more about setting up business rules in a separate article:
 [Set up business rules](https://academy.creatio.com/documents?id=2409) 
 .
9. Specify the position of the title relative to the field in the
 
 Title position
 
 parameter. For this example, select “Left.”
10. Enter
 
 Title on page
 
 parameter if the title on the page must differ from the title in Creatio. For this example, enter “Color.” You can localize the parameter similarly to the
 
 Title
 
 parameter.
11. Select the color palette to use in the
 
 Palette
 
 parameter. Basic palette enables users to select from a preconfigured set of colors. Extended palette enables users to select custom colors using a color picker, hex code, or RGB code as well as specify the color transparency. For this example, select
 
 Extended pallet
 
 .
12. Change the data source in the
 
 Data source
 
 parameter. For this example, use the original data source.
13. View the unique field code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar fields on the page. For this example, leave the code as is.



 As a result, Creatio will add the
 
 Requested business card color
 
 field to the request page. Users will be able to specify custom colors.
 




