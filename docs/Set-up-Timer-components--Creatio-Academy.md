


 Use
 
 Timer
 
 components to set up a counter to or from a specific date. For example, this is useful for specfifying deadlines or helping users to prioritize records to process.
 



 Set up a [Timer] component that counts to a date
--------------------------------------------------





 Example.
 
 Set up the
 
 Timer
 
 component that displays the time before the requester requires a corporate vehicle on the request page.
 





 Fig. 1 Set up a
 
 Timer
 
 component that counts to a date
 

![scr_countdown_timer_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_countdown_timer_setup_area.png)


1. Add and set up a “Date and time to provide a corporate vehicle” field. To do this, follow the steps in a separate article:
 [Set up a date/time field](https://academy.creatio.com/documents?id=2425) 
 .
2. Drag a
 
 Timer
 
 component to the canvas and open the component setup area
3. Select “Countdown to specific date” in the
 
 Type
 
 parameter.
4. Click the
 ![icn_select_column.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/icn_select_column.png)
 icon next to the
 
 Start date time column
 
 parameter →
 
 Requests
 
 →
 
 Requests fields
 
 tab →
 
 Date and time to provide a corporate vehicle
 
 checkbox →
 
 Select
 
 .
5. Enter the timer caption before the countdown reaches the end date in the
 
 Text for positive values
 
 parameter. Use the “[#timer#]” macro to add the timer value. If you leave the parameter empty, the timer uses the “[#timer#] left” caption.
 



 For this example, enter “Vehicle required in [#timer#].” You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/set_title_field_localization.png)
 button to the right to localize the text to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article:
 [Localize a Freedom UI element](https://academy.creatio.com/documents?id=2441) 
 .
6. Enter the timer caption after the countdown reaches the end date in the
 
 Text for negative values
 
 parameter. Use the “[#timer#]” macro to add the timer value. If you leave the parameter empty, the timer uses the “[#timer#] overdue” caption.
 



 For this example, enter “Vehicle required immediately. [#timer#] overdue.” You can localize the text similarly to the positive caption.
7. Specify whether to display the overdue time in the
 
 Show negative countdown value
 
 checkbox. If you clear the checkbox, the timer displays “Time is up” caption once the end date is reached. For this example, leave the checkbox selected.
8. Select the timer style to display on the app page in the
 
 Style
 
 parameter. For this example, select “Headline 3.”
9. Select the font format in the
 
 Format
 
 parameter. For this example, select “Normal.”
10. Select the text alignment option in the
 
 Align
 
 parameter. For this example, select center.
11. Select the color of the positive caption in the
 
 Text color
 
 parameter. For this example, leave it green.
12. Select the color of the positive caption in the
 
 Text color
 
 parameter. For this example, leave it green.
13. Select the timer background color in the
 
 Background color
 
 parameter. For this example, leave the color transparent.
14. Click the
 ![btn_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_visible.png)
 or
 ![btn_not_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_not_visible.png)
 button in the
 
 Visibility
 
 group to make the component visible or invisible by default on the page, respectively. For this example, leave the component visible.
15. Click
 
 Setup conditions
 
 in the
 
 Visibility
 
 group to set up element business rules. For this example, do not add business rules. Learn more about setting up business rules in a separate article:
 [Set up business rules](https://academy.creatio.com/documents?id=2409) 
 .
16. View the unique component code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar components on the page. For this example, leave the code as is.



 As a result, Creatio will add the timer that displays the time before the requester requires a corporate vehicle to the request page.
 



 Set up a [Timer] component that counts from a date
----------------------------------------------------





 Example.
 
 Set up the
 
 Timer
 
 component that displays the record age on the page of the request. This will helps employees to prioritize records to process without setting a strict deadline.
 





 Fig. 2 Set up a
 
 Timer
 
 component that counts from a date
 

![scr_count_up_timer_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_count_up_timer_setup_area.png)


1. Drag a
 
 Timer
 
 component to the page and open its setup area.
2. Select “Timer from date” in the
 
 Type
 
 parameter.
3. Click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/set_title_field_localization.png)
 icon next to the
 
 Start date time column
 
 parameter →
 
 Requests
 
 →
 
 Requests fields
 
 tab →
 
 Created on
 
 checkbox →
 
 Select
 
 .
4. Enter the timer caption after the count starts in the
 
 Text for positive values
 
 parameter. Use the “[#timer#]” macro to add the timer value. If you leave the parameter empty, the timer uses the “[#timer#] passed” caption.
 



 For this example, enter “Request is [#timer#] old.” You can click the
 ![set_title_field_localization.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/set_title_field_localization.png)
 button to the right to localize the text to other languages you are going to use in the app. Learn more about localizing Freedom UI elements in a separate article:
 [Localize a Freedom UI element](https://academy.creatio.com/documents?id=2441) 
 .
5. Enter the timer caption before the count starts in the
 
 Text for negative values
 
 parameter. Use the “[#timer#]” macro to add the timer value. If you leave the parameter empty, the timer uses the “[#timer#] before countdown begins” caption.
 



 For this example, enter “Request is older than its creation date. Contact system administrator.” You can localize the text similarly to the positive caption.
6. Select the timer style to display on the app page in the
 
 Style
 
 parameter. For this example, select “Headline 3.”
7. Select the font format in the
 
 Format
 
 parameter. For this example, select “Normal.”
8. Select the text alignment option in the
 
 Align
 
 parameter. For this example, select center.
9. Select the color of the positive caption in the
 
 Text color
 
 parameter. For this example, leave it green.
10. Select the color of the positive caption in the
 
 Text color
 
 parameter. For this example, leave it green.
11. Select the label background color in the
 
 Background color
 
 parameter. For this example, leave the color transparent.
12. Click the
 ![btn_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_visible.png)
 or
 ![btn_not_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_not_visible.png)
 button in the
 
 Visibility
 
 group to make the component visible or invisible by default on the page, respectively. For this example, leave the component visible.
13. Click
 
 Setup conditions
 
 in the
 
 Visibility
 
 group to set up element business rules. For this example, do not add business rules. Learn more about setting up business rules in a separate article:
 [Set up business rules](https://academy.creatio.com/documents?id=2409) 
 .
14. View the unique component code in the page schema in the
 
 Element code
 
 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar components on the page. For this example, leave the code as is.



 As a result, Creatio will add the timer that displays the record age to the page of the request.
 




