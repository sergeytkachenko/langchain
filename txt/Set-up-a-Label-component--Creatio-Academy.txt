


 Use
 
 Label
 
 components to add captions to pages and page areas as well as to display information that contains the current user data.
 





 Example.
 
 Set up a
 
 Label
 
 component that displays the first name of the current user to the HR KPI panel on a list page.
 





 Fig. 1 Set up the
 
 Label
 
 component
 

![scr_label_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_label_setup_area.png)


1. Drag a
 
 Label
 
 component to the canvas and open the component setup area.
2. Enter the label text to display on the app page in the
 
 Text
 
 parameter. You can use macros that follow the [#CurrentUser.<Field>#] pattern, where <Field> is a field included in the
 
 Current user
 
 group of email macros. Learn more about macros in a separate article:
 [Personalize email content with macros](https://academy.creatio.com/documents?id=1502) 
 .
 



 For this example, enter “Hello, [#CurrentUser.Recipient Name#]!” You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/set_title_field_localization.png)
 button to the right to localize the text to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article:
 [Localize a Freedom UI element](https://academy.creatio.com/documents?id=2441) 
 .
3. Select the label style to display on the app page in the
 
 Style
 
 parameter. Required. For this example, select “Headline 3.”
4. Select the font format in the
 
 Format
 
 parameter. Required. For this example, select “Normal.”
5. Select the text alignment option in the
 
 Align
 
 parameter. For this example, select left.
6. Select the text color in the
 
 Text color
 
 parameter. For this example, change the color to black.
7. Select the label background color in the
 
 Background color
 
 parameter. For this example, leave the color transparent.
8. Click the
 ![btn_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_visible.png)
 or
 ![btn_not_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_not_visible.png)
 button in the
 
 Visibility
 
 group to make the component visible or invisible by default on the page, respectively. For this example, leave the component visible.
9. Click
 
 Setup conditions
 
 in the
 
 Visibility
 
 group to set up element business rules. For this example, do not add business rules. Learn more about setting up business rules in a separate article:
 [Set up business rules](https://academy.creatio.com/documents?id=2409) 
 .
10. View the unique component code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar components on the page. For this example, leave the code as is.



 As a result, Creatio will add a label that displays the business phone of the current user contact to the request page.
 




