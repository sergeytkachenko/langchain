






 Image
-----------



 The
 
 Image
 
 element (
 [Fig. 1](#XREF_35823_Fig_394_Adding_an)
 ) displays images. This element consists of two parts: the image itself, and the image container.
 





 Fig. 1
 

 Adding an image
 

![adding_image_from_toolbar.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_elements/adding_image_from_toolbar.gif)


### 
 Image setup area



 Use the setup area on the right to configure the image and the image container.
 





 Fig. 1
 
 Image setup area
 

![scr_image_setup_area.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_elements/scr_image_setup_area.png)





| 
 Property
  | 
 Function
  |
| --- | --- |
| 
**Breadcrumb navigation (1)** 
 | 
 Use “breadcrumbs” at the top of the setup area to navigate the parent (column, section, banner, block, and template) elements.
  |
| 
**Image settings** 
 | 
 Use the
 icn_content_designer_background_image.png
 field to upload an image from your computer or insert the URI of an image.
 



 Note.
 
 The
 
 Image
 
 element supports Data URIs. You can insert a base64-encoded image instead of a URL.
 
 Base64-encoded images are part of the HTML code of the message and are not normally filtered by email clients that prevent external images from loading by default.
 



 Link to open
 
 – specify a URL to use the image as a hyperlink.
 


 Title
 
 – specify the text to display when the user hovers the mouse pointer over the image.
 



 Note.
 
 The title text is often used to describe things unclear at first glance.
 



 Alternative text
 
 – specify the alternative text. In some email clients, a specific setting might disable images in the incoming emails. As a result, recipients will see alternative text instead of images. Populate the
 
 Alternate Text
 
 field with a description of the image so that recipients can see it instead of the icon to replace the missing image.
  |
| 
**Size, px** 
 | 
 Specify the width and height of the image.
 

 By default, both
 
 Width
 
 and
 
 Height
 
 parameters have the “Auto” value. If you leave this parameter unchanged, the image will either stretch or shrink to fit the container.
 

 Change one of the values to resize the image and keep the ratio.
 

 Change both values to force resize the image to the specified height and width disregarding the ratio.
  |
| 
**Align** 
 | 
 Align the image horizontally (left
 btn_alignment_horizontal_left.png
 , center
 btn_alignment_horizontal_center.png
 , or right
 btn_alignment_horizontal_right.png
 ).
 



 Note.
 
 Alignment may produce no visible effect depending on the ratio of the image and the current ratio of the parent container.
 
 |
| 
**Padding, px** 
 | 
 Specify the distance (in pixels) between the image and each of the borders of the container.
 

 Padding is specified separately for each side.
  |
| 
**Corner radius** 
 | 
 Specify the circular radius of the corners of the image. Leave this property empty for sharp corners. This defines the circular radius of all 4 corners of the image.
 



 Note.
 
 Use the
 
 HTML
 
 element with inline or embedded CSS styles to specify elliptical corners and other exotic effects.
 
 |
| 
**Background** 
 | 
 Set background color for the entire image.
 

 Background style settings are disabled by default. Select the checkbox
 **(2)** 
 to enable them.
 

 Clear this checkbox to disable all background settings of the current image.
 

 Click
 content_designer_background_color.png
 to open the color picker and select the background color.
 



 Note.
 
 The background completely fills the entire graphics container. For example, if the padding setting values are not set to 0, the background color should be visible around the image. If the image has transparent areas, the background color will be visible through them.
 
 |
| 
**Borders** 
 | 
 Configure the borders of the image.
 

 Border style settings are disabled by default. Select the checkbox
 **(3)** 
 to enable them.
 

 Click
 border_color_picker.png
 to open the color picker and select the border color.
 

 Update the
 icon_border_width.png
 field to specify the border width. To hide the border, select the “Hidden” border style.
 

 Use the dropdown menu
 **(4)** 
 to select the border style. When the border settings are enabled, the “Solid” style is selected by default. The following styles are available:
 * border_style_hidden.png
 – Hidden
 



 Note.
 
 The border is defined but invisible. The border width effectively equals 0.
* border_style_dotted.png
 – Dotted
* border_style_dashed.png
 – Dashed
* border_style_solid.png
 – Solid
* border_style_double.png
 – Double
* border_style_groove.png
 – Groove
* border_style_ridge.png
 – Ridge
* border_style_inset.png
 – Inset
* border_style_outset.png
 – Outset


 Select or clear
 
 Top
 
 ,
 
 Bottom
 
 ,
 
 Left
 
 and
 
 Right
 
 checkboxes to enable or disable the border style settings for the corresponding border.
  |








 Button
------------



 The
 
 Button
 
 element (
 [Fig. 1](#XREF_32019_Fig_401_Adding_a)
 ) is designed for making clickable call-to-action buttons.
 
 Button
 
 elements are also referred to as a “call to action” (CTA) and are basically links presented as visually identifiable buttons.
 





 Fig. 1
 

 Adding a CTA button
 

![adding_button_from_toolbar.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_elements/adding_button_from_toolbar.gif)



 There is a difference between
 
 Button
 
 element and the HTML <button> element.
   

 To insert the HTML <button> element, please use the
 
 HTML
 
 element.
 


### 
 Button setup area



 Use the setup area on the right to configure the button text, background, and shape.
 





 Fig. 1
 
 Button setup area
 

![scr_button_setup_area.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_elements/scr_button_setup_area.png)





| 
 Property
  | 
 Function
  |
| --- | --- |
| 
**Breadcrumb navigation (1)** 
 | 
 Use “breadcrumbs” at the top of the setup area to navigate the parent (column, section, banner, block, and template) elements.
  |
| 
**Link to open** 
 | 
 The URL specified in the
 
 Link to open
 
 area opens when a recipient clicks the button.
  |
| 
**Font** 
 | 
 Use this settings group to configure the font settings of the CTA button caption.
 


 Content builder font set
 
 – select the font family of the button from the list of registered font families. To modify the list of fonts used in your template, update the “Content builder font set” lookup. Read more in the “
 [Updating available Content Designer fonts](/documents/?product=marketing&ver=7.17.0&id=2061)
 ” article.
 


 Size, px
 
 – specify the width and height of the button in pixels.
 

 Click
 font_color_picker.png
 to open the color picker and select the font color.
 


 Line height, px
 
 – specify the spacing between the lines and the borders of the button.
 

 The maximum height is 250px; the minimum line height cannot be less than the size of the font.
 


 Letter spacing, px
 
 – specify the spacing between the characters in pixels.
  |
| 
**Size, px** 
 | 
 Specify the width and height of the button in pixels.
  |
| 
**Align** 
 | 
 Adjust the horizontal (
 btn_alignment_horizontal_left00001.png
 left,
 btn_alignment_horizontal_center00002.png
 center, or
 btn_alignment_horizontal_right00003.png
 right) and vertical (
 btn_alignment_vertical_top.png
 top,
 btn_alignment_vertical_middle.png
 center, or
 btn_alignment_vertical_bottom.png
 bottom) alignment for the button for the button.
 



 Note.
 
 Selecting various vertical alignment settings is likely to produce no visible effect when trying them with the default sample CTA button because of the insufficient height.
 
 |
| 
**Margin, px** 
 | 
 Specify the distance (in pixels) between the borders of the CTA button and the adjacent borders of parent and sister elements.
 

 In the Content Designer, you must specify the margin setting for each side individually.
  |
| 
**Padding, px** 
 | 
 Specify the distance (in pixels) between the CTA text and each of the borders of the container.
 

 Padding is specified separately for each side.
  |
| 
**Corner radius** 
 | 
 Specify the circular radius of the corners of the button. Leave this property empty for sharp corners. This defines the circular radius of all 4 corners of the button.
 



 Note.
 
 Use the
 
 HTML
 
 element with inline or embedded CSS styles to specify elliptical corners and other exotic effects.
 
 |
| 
**Background** 
 | 
 Set the button background color.
 

 Background style settings are enabled by default. Clear the checkbox
 **(2)** 
 to enable them.
 

 Select this checkbox to enable all background settings of the current button.
 

 Click
 border_color_picker00004.png
 to open the color picker and select the background color.
  |
| 
**Borders** 
 | 
 Configure the borders of the button.
 

 Border style settings are disabled by default. Select the checkbox
 **(3)** 
 to enable them.
 

 Click
 border_color_picker00005.png
 to open the color picker and select the border color.
 

 Update the
 icon_border_width00006.png
 field to specify the border width. To hide the border, select the “Hidden” border style.
 

 Use the dropdown menu
 **(4)** 
 to select the border style. When the border settings are enabled, the “Solid” style is selected by default. The following styles are available:
 * border_style_hidden00007.png
 – Hidden
 



 Note.
 
 The border is defined but invisible. The border width effectively equals 0.
* border_style_dotted00008.png
 – Dotted
* border_style_dashed00009.png
 – Dashed
* border_style_solid00010.png
 – Solid
* border_style_double00011.png
 – Double
* border_style_groove00012.png
 – Groove
* border_style_ridge00013.png
 – Ridge
* border_style_inset00014.png
 – Inset
* border_style_outset00015.png
 – Outset


 Select or clear
 
 Top
 
 ,
 
 Bottom
 
 ,
 
 Left
 
 and
 
 Right
 
 checkboxes to enable or disable the border style settings for the corresponding border.
  |








 Text
----------



 The
 
 Text
 
 element (
 [Fig. 1](#XREF_32120_Fig_403_Adding_the)
 ) is used to add message text. This element has two configuration areas: the setup area and the rich text toolbar on the
 
 Text
 
 element itself.
 





 Fig. 1
 

 Adding the
 
 Text
 
 element
 

![adding_text_from_toolbar.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_elements/adding_text_from_toolbar.gif)


### 
 Text setup area



 In the setup area, you can configure the baseline font settings and the style settings of the
 
 Text
 
 element.
 





 Fig. 1
 
 Text setup area
 

![scr_text_setup_area.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_elements/scr_text_setup_area.png)





| 
 Property
  | 
 Function
  |
| --- | --- |
| 
**Breadcrumb navigation (1)** 
 | 
 Use “breadcrumbs” at the top of the setup area to navigate the parent (column, section, banner, block, and template) elements.
  |
| 
**Font** 
 | 
 Use this settings group to configure the baseline font settings of the
 
 Text
 
 element.
 


 Content builder font set
 
 – select the font family of the text from the list of registered font families. To modify the list of fonts used in your template, update the “Content builder font set” lookup. Read more in the “
 [Updating available Content Designer fonts](/documents/?product=marketing&ver=7.17.0&id=2061)
 ” article.
 


 Size, px
 
 – specify the width and height of the button in pixels.
 

 Click  to open the color picker and select the font color.
 


 Line height, px
 
 – specify the spacing between the lines and the borders of the button.
 

 The maximum height is 250px; the minimum line height cannot be less than the size of the font.
 


 Letter spacing, px
 
 – specify the spacing between the characters in pixels.
  |
| 
**Size, px** 
 | 

 Size, px
 
 – specify the width and height of the button in pixels.
  |
| 
**Align** 
 | 
 Align the baseline text horizontally (left
 icon_text_align_left.png
 , center
 icon_text_align_center.png
 , right
 icon_text_align_right.png
 or justify
 icon_text_align_justify.png
 ).
  |
| 
**Height, px** 
 | 
 Specify the height of the text container (in pixels).
 

 This field is used to specify the fixed height of the text container. It will not stretch or shrink to fit the text inside.
  |
| 
**Padding, px** 
 | 
 Specify the distance (in pixels) between the text and each of the borders of the container.
 

 Padding is specified separately for each side.
  |
| 
**Background** 
 | 
 Set background color for the text.
 

 Background style settings are disabled by default. Select the checkbox
 **(2)** 
 to enable them.
 

 Clear this checkbox to disable all background settings of the current spacer.
 

 Click
 content_designer_background_color00017.png
 to open the color picker and select the background color.
  |








 Divider
-------------



 The
 
 Divider
 
 element (
 [Fig. 1](#XREF_30218_Fig_406_Adding_a)
 ) is used for separating adjacent elements with horizontal lines or margins.
 





 Fig. 1
 

 Adding a divider
 

![adding_divider_from_toolbar.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_elements/adding_divider_from_toolbar.gif)



 You can use the setup area to configure the height of the divider and the color and width of the horizontal line.
 





 Fig. 2
 
 Divider setup area
 

![scr_divider_setup_area_callouts.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_elements/scr_divider_setup_area_callouts.png)





| 
 Property
  | 
 Function
  |
| --- | --- |
| 
**Breadcrumb navigation (1)** 
 | 
 Use “breadcrumbs” at the top of the setup area to navigate the parent (column, section, banner, block, and template) elements.
  |
| 
**Divider options** 
 | 
 Use this settings group to configure the width of the horizontal line, its color, width, and style.
  |
| 
**Padding, px** 
 | 
 Specify the distance (in pixels) between the horizontal line and each of the borders of the divider.
 

 Padding is specified separately for each side.
  |
| 
**Background** 
 | 
 Use this settings group to toggle background options on and off, and to select the background color.
  |







 Navbar
-----------



 The
 **Navbar** 
 element (
 [Fig. 1](#XREF_11970_Fig_408_Adding_a)
 ) is a navigation bar containing a list of menu links. The navbar element can be configured differently for mobiles.
 





 Fig. 1
 

 Adding a
 
 Navbar
 


[![adding_navbar_from_toolbar.gif](/sites/default/files/documents/docs_en/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_email/adding_navbar_from_toolbar.gif)](/sites/default/files/documents/docs_en/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_email/adding_navbar_from_toolbar.gif)





 Fig. 2
 
 Navbar setup area
 

[![scr_navbar_setup_area.png](/sites/default/files/documents/docs_en/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_email/scr_navbar_setup_area.png)](/sites/default/files/documents/docs_en/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_email/scr_navbar_setup_area.png)






| 
 Property
  | 
 Function
  |
| --- | --- |
| 
**Breadcrumb navigation (1)** 
 | 
 Use “breadcrumbs” at the top of the setup area to navigate the parent (column, section, banner, block and template) elements.
  |
| 
**Navbar constructor** 
 | 
 Add, remove, and move the navigation links.
 

 To access the setup area of a navlink, click the corresponding item in the navlink list.
 

 Click
 
 Add link
 
 to add a link
 

 Click
 content_section_item_view_model_remove_icon00066.png
 to remove a link (last link cannot be removed).
  |
| 
**Align** 
 | 
 Align the navlinks in the navbar.
  |
| 
**Hamburger menu** 
 | 
 Enable “hamburger” menu on mobile devices, displaying menu links one over another.
  |
| 
**Icon align** 
 | 
 Align the hamburger menu icon horizontally (left
 btn_alignment_horizontal_left00067.png
 , center
 btn_alignment_horizontal_center00068.png
 or right
 btn_alignment_horizontal_right00069.png
 ).
 

 This property is only available if the hamburger menu is enabled.
  |
| 
**Icon color** 
 | 
 Click
 
 to update the hamburger menu icon color.
 

 This property is only available if the hamburger menu is enabled.
  |




### 


 Navlink



 The
 **Navlink** 
 element (
 [Fig. 3](#XREF_56809_Fig_410_Adding)
 ) is a navigation link for the parent navigation bar containing a list of navigation links.
 





 Fig. 3
 

 Adding navlink
 

[![adding_navlink_from_toolbar.gif](/sites/default/files/documents/docs_en/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_email/adding_navlink_from_toolbar.gif)](/sites/default/files/documents/docs_en/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_email/adding_navlink_from_toolbar.gif)





 Fig. 4
 
 Navlink setup area
 

[![scr_navlinik_setup_area.png](/sites/default/files/documents/docs_en/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_email/scr_navlinik_setup_area.png)](/sites/default/files/documents/docs_en/product/bpm'online marketing/marketing/7.16.0/BPMonlineHelp/section_email/scr_navlinik_setup_area.png)






| 
 Property
  | 
 Function
  |
| --- | --- |
| 
**Breadcrumb navigation (1)** 
 | 
 Use “breadcrumbs” at the top of the setup area to navigate the parent (column, section, banner, block and template) elements.
  |
| 
**Link to open** 
 | 
 Provide the URL to the desired destination in the
 
 Link to open
 
 area.
  |
| 
**Font** 
 | 
 Use this settings group to configure the font settings of the link.
 


 Content builder font set
 
 – select the font family of the menu link from the list of registered font families. To modify the list of fonts used in your template, update the “Content builder font set” lookup. Read more in the “
 [Updating available Content Designer fonts](/documents/?product=marketing&ver=7.17.0&id=2061)
 ” article.
 


 Size, px
 
 – specify the width and height of the font in pixels.
 

 Click  to open the color picker and select the font color.
 


 Line height, px
 
 – specify the spacing between the lines and the borders of the button.
 

 The maximum line height is 250px; the minimum line height cannot be less than the size of the font.
  |
| 
**Padding, px** 
 | 
 Specify the distance (in pixels) between the text and each of the borders of the container.
 

 Padding is specified separately for each side.
  |









 Spacer
------------



 The
 
 Spacer
 
 element (
 [Fig. 1](#XREF_49337_Fig_412_Adding_the)
 ) is used for separating adjacent elements with empty spacer (an invisible horizontal line).
 





 Fig. 1
 

 Adding the
 
 Spacer
 
 element
 

![adding_spacer_from_toolbar.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_elements/adding_spacer_from_toolbar.gif)





 Fig. 2
 

 Spacer
 
 setup area
 

![scr_spacer_setup_area.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_elements/scr_spacer_setup_area.png)





| 
 Property
  | 
 Function
  |
| --- | --- |
| 
**Breadcrumb navigation (1)** 
 | 
 Use “breadcrumbs” at the top of the setup area to navigate the parent (column, section, banner, block, and template) elements.
  |
| 
**Size, px** 
 | 
 Update the
 
 Height
 
 field to specify the thickness of the spacer.
  |
| 
**Background** 
 | 
 Set background color for the spacer.
 

 Background style settings are disabled by default. Select the checkbox
 **(2)** 
 to enable them.
 

 Clear this checkbox to disable all background settings of the current spacer.
 

 Click
 content_designer_background_color00018.png
 to open the color picker and select the background color.
  |





