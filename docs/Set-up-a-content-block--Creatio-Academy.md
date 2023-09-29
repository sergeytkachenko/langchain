


 Content block elements arrange other elements of a template. You need at least one block in your template to be able to add non-block elements. Blocks cannot contain other blocks.
 




 Fig. 1 Sample template layout
 

![scr_template_empty_callouts.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_template_empty_callouts.png)



 A block has a table-like layout. Blocks can hold two types of rows:
 


* **Sections** 
 are multi-column rows. A section can have up to 6 columns. Use sections to arrange most types of content. They are also preferable in general because of their flexibility.
* **Banners** 
 are single-column rows. Use banners to insert images that will fill all available space and fit inside the element regardless of the image size. You can align the background image of a banner vertically and horizontally.
 



 As an alternative to using banners, you can specify a background image of an entire block. However, this background image will not stretch or shrink to fit the borders of the block.



 By default, a block has one section and no banners. A block must have at least one section or banner. It is not possible to delete the only section or banner of a block.
 



 You can add multiple sections to a single block or add multiple blocks. There will be no visible differentce for the email recipients. We recommend adding any reusable content as separate blocks and saving them to the Block Library for later.
 



 Create a content block
------------------------



 To add a block to a template, drag the
 
 Block
 
 (
 ![content_builder_block_view_model_icon.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/content_builder_block_view_model_icon.png)
 ) element from the element grid to the working area (Fig. 1).
 




 Fig. 1 Using the Content Designer
 

![block_use_case.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/block_use_case.gif)



 There are several ways you can select a block in the working area:
 


* Click on the right border of the block (Fig. 2).
* Click any element inside the section or banner, then press
 
 Esc
 
 to go up the navigation tree until the
 
 Block
 
 element is selected.
* Click any element inside the section or banner, then click “Block” in the breadcrumb navigation in the setup area. Click the leftmost element if “Block” is not yet visible (Fig. 3).




 Fig. 2 Selecting the block by clicking on the right border
 

![selecting_block_by_three_dots_cropped.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/selecting_block_by_three_dots_cropped.gif)




 Fig. 3 Selecting the block by using the setup area
 

![selecting_block_by_breadcrumbs_cropped.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/selecting_block_by_breadcrumbs_cropped.gif)



 When a block element is selected, its context menu appears on the right (Fig. 4).
 




 Fig. 4 Block context menu
 

![scr_block_context_menu.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_block_context_menu.png)


* ![scr_block_context_menu_move_icon.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_block_context_menu_move_icon.png)
 : change block position. Drag the block up or down to reorder the blocks in the template.
* ![scr_block_context_menu_copy_icon.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_block_context_menu_copy_icon.png)
 : copy the block. A copy block will appear directly under the original block.
* ![scr_block_context_menu_remove_icon.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_block_context_menu_remove_icon.png)
 : remove the block from the template. This will permanently remove any blocks that have not been saved in the block library. Deleting a block from the template will not delete it from the block library.
* ![scr_block_context_menu_save_icon.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_block_context_menu_save_icon.png)
 : save the block in the Block Library. Creatio will prompt you to enter the name under which the block will be saved.



 Set up a content block
------------------------



 Use the setup area on the right to configure the
 
 Block
 
 element.
 



 The setup area comprises of three tabs:
 


* Structure
 
 . The default tab available in the Campaign Designer and Process Designer. It is the only tab available when you open the Content Designer from the Process Designer.
* Dynamic Content
 
 . This tab is only available in the marketing Content Designer for Marketing Creatio. Use it to set up different variations of a block for different conditions, configured on the
 
 Rules
 
 tab.
* Rules
 
 . This tab is only available in the marketing Content Designer for Marketing Creatio. Use it to set up rules that can be used for defining dynamic content.



 The
 
 Structure
 
 tab (Fig. 5) includes the following properties:
 




 Fig. 5 Block setup area
 

![scr_content_designer_block_setup_area_steps.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_content_designer_block_setup_area_steps.png)





 Note.
 
 Tabs other than the
 
 Structure
 
 tabs are only available in Creatio Marketing and Creatio CRM bundle.
 






| 
 Property
  | 
 Functionality
  |
| --- | --- |
| 
 Breadcrumb navigation (1)
  | 
 Use breadcrumbs at the top of the setup area to navigate the parent (column, section, banner, block, and template) elements.
  |
| 
**Section constructor** 
 | 
 Add, remove, and move the sections and banners of the block.
 

 To access the setup area of a section or banner, click the corresponding item in the section list.
 

 Click
 
 Add section
 
 or
 
 Add banner
 
 to add sections and banners.
 

 Click
 content_section_item_view_model_remove_icon.png
 to remove a section or banner. Note that you cannot delete the last section (banner) from a content block.
  |
| 
**Background** 
 | 
 Set background image and/or color for the entire block. Note that sections and banners can have their own background settings that may cover the background of the block.
 

 Background style settings are disabled by default. Select the checkbox
 **(2)** 
 to enable them.
 

 Clear this checkbox to disable all background settings of the current block.
 

 Click
 content_designer_background_color.png
 to open the color picker and select the background color.
 

 Click
 icn_content_designer_background_image.png
 and enter the URL of the image to display on the background.
 



 Note.
 
 If the recipient’s email client fails to load the image, the recipient will see the background color instead.
 
 |




 Banners
---------



 A banner is a single-column block “row”. The main purpose of the banner element is to display a background image and some content over it (Fig. 6). Unlike the
 
 Block
 
 element, you can align the banner background image.
 




 Fig. 6 Adding a banner
 

![banner_use_case.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/banner_use_case.gif)



 A banner has a fixed height. If it is set to a value that is too large, the banner might not fit the display vertically (Fig. 7).
 




 Fig. 7 600 px vs. 320 px banner
 

![scr_banner_600px_vs_320px_on_mobile.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_banner_600px_vs_320px_on_mobile.png)



 The
 
 Banner
 
 setup area comprises of the following setup groups:
 
 Size, px
 
 ,
 
 Vertical align
 
 ,
 
 Padding, px
 
 , and
 
 Background
 
 (Fig. 8).
 




 Fig. 8 Banner setup area
 

![scr_banner_setup_area.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_banner_setup_area.png)





| 
 Property
  | 
 Functionality
  |
| --- | --- |
| 
**Breadcrumb navigation (1)** 
 | 
 Use breadcrumbs at the top of the setup area to navigate the parent (column, section, banner, block, and template) elements.
  |
| 
**Size, px** 
 | 
 Configure the height of the banner by specifying the
 
 Height
 
 field value.
 

 This value is used to set up the minimum height. If the height of the content of the banner exceeds this value, the banner will stretch vertically.
  |
| 
**Vertical align** 
 | 
 Align the contents of the banner vertically (top
 btn_alignment_vertical_top.png
 , middle
 btn_alignment_vertical_middle.png
 , or bottom
 btn_alignment_vertical_bottom.png
 ).
  |
| 
**Padding, px** 
 | 
 Specify the distance (in pixels) between the content of the banner and each of its borders.
 

 Padding is specified separately for each side.
  |
| 
**Background** 
 | 
 Set background image and/or color for the entire banner. Note that elements dropped onto the banner can have their own background settings that may cover the background of the banner.
 

 Background style settings are disabled by default. Select the checkbox
 **(2)** 
 to enable them.
 

 Clear this checkbox to disable all background settings of the current banner.
 

 Click
 content_designer_background_color00001.png
 to open the color picker and select the background color.
 

 Click
 content_designer_background_image.png
 to enter the URL of the image to display on the background.
 



 Note.
 
 If the recipient’s email client fails to load the image, the recipient will see the background color instead.
 


 The image will stretch or shrink to fit the banner. We recommend using large or vector images as a background.
 

 Align the background image of the banner vertically (top
 btn_alignment_vertical_top00002.png
 , middle
 btn_alignment_vertical_middle00003.png
 , or bottom
 btn_alignment_vertical_bottom00004.png
 ) or horizontally (left
 btn_alignment_horizontal_left.png
 , center
 btn_alignment_horizontal_center.png
 , or right
 btn_alignment_horizontal_right.png
 ).
 



 Note.
 
 Alignment may produce no visible effect depending on the ratio of the image and the current ratio of the banner.
 
 |




 Section
---------



 A section (Fig. 9) is a multi-column block row. This is the default subordinate element of the
 
 Block
 
 element. A section does not have its own background image.
 




 Fig. 9 Adding a section
 

![section_use_case.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/section_use_case.gif)



 The
 
 Section
 
 setup area consists of several groups of settings:
 
 Column constructor
 
 ,
 
 Padding, px
 
 ,
 
 Corner radius, px
 
 ,
 
 Background
 
 and
 
 Borders
 
 .
 




 Fig. 10 Section setup area
 

![scr_section_setup_area.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_section_setup_area.png)





| 
 Property
  | 
 Functionality
  |
| --- | --- |
| 
**Breadcrumb navigation (1)** 
 | 
 Use breadcrumbs at the top of the setup area to navigate the parent (column, section, banner, block, and template) elements.
  |
| 
**Column constructor** 
 | 
 Add and delete columns, specify their widths, or equalize them and reverse the order of the columns on mobile devices.
 

 To access the setup area of a column, click the corresponding item in the column list.
 

 Click the
 
 %
 
 field and specify a new value to change the width of a column. The width of the next adjacent column will be adjusted.
 



 Note.
 
 The minimal column width is 5%.
 


 Click
 
 Add column
 
 to add a column.
 

 Click
 content_section_item_view_model_remove_icon00005.png
 to remove the column. You cannot delete the only column.
 

 Select the
 
 Equalize
 
 checkbox to ensure that all of the columns have equivalent width. If you add or remove a column when this checkbox is selected, the widths of all columns will be adjusted to match each other.
 

 Select the
 
 Reverse the order of columns on mobile
 
 checkbox to reverse the order of ungrouped columns and column groups on mobile devices.
 

 As a result, the last column or column group will be at the top of the section, and the first column or column group at the bottom.
 



 Note.
 
 This does not affect columns displayed side-by-side on mobile, i. e., columns inside column groups.
 
 |
| 
**Padding, px** 
 | 
 Specify the distance (in pixels) between the content of the section and each of its borders.
 

 Padding is specified separately for each side.
  |
| 
**Corner radius, px** 
 | 
 Specify the circular radius of the corners of the section. Leave this property empty for sharp corners. This defines the circular radius of all 4 corners of an element.
 



 Note.
 
 Use the
 
 HTML
 
 element with inline or embedded CSS styles to specify elliptical corners and other exotic effects.
 
 |
| 
**Background** 
 | 
 Set background color for the entire section. Note that elements dropped onto the section can have their own background settings that may cover the background of the section.
 

 Background style settings are disabled by default. Select the checkbox
 **(2)** 
 to enable them.
 

 Clear this checkbox to disable all background settings of the current section.
 

 Click
 content_designer_background_color00006.png
 to open the color picker and select the background color.
  |
| 
**Borders** 
 | 
 Configure the borders of the section.
 

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
 : Hidden




 Note.
 
 The border is defined but invisible. The border width effectively equals 0.
 
* border_style_dotted.png
 : Dotted
* border_style_dashed.png
 : Dashed
* border_style_solid.png
 : Solid
* border_style_double.png
 : Double
* border_style_groove.png
 : Groove
* border_style_ridge.png
 : Ridge
* border_style_inset.png
 : Inset
* border_style_outset.png
 : Outset


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



### 
 Columns



 A column is a structural element used to arrange other elements in a section. To add a column, click the
 
 Add column
 
 button the
 
 Section
 
 element setup area.
 





 Fig. 11
 
 Working with columns
 

![column_use_case_slow.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/column_use_case_slow.gif)



 The
 
 Column
 
 setup area comprises of the following setup groups:
 
 Vertical align
 
 ,
 
 Padding, px
 
 ,
 
 Corner radius, px
 
 ,
 
 Background
 
 , and
 
 Borders
 
 .
 




 Fig. 12 Column setup area
 

![scr_column_setup_area.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_column_setup_area.png)





| 
 Property
  | 
 Functionality
  |
| --- | --- |
| 
**Breadcrumb navigation** 
**(1)** 
 | 
 Use breadcrumbs at the top of the setup area to navigate the parent (column, section, banner, block, and template) elements.
  |
| 
**Align** 
 | 
 Align the contents of the column vertically (top
 btn_alignment_vertical_top00007.png
 , middle
 btn_alignment_vertical_middle00008.png
 , or bottom
 btn_alignment_vertical_bottom00009.png
 ).
 



 Attention.
 
 Vertical align for a column on mobile may not work in case when the vertical alignment of the highest column in the section is not set to middle.
 
 |
| 
**Padding, px** 
 | 
 Specify the distance in pixels between the content of the column and each of its borders.
 

 Padding is specified separately for each side.
  |
| 
**Corner radius, px** 
 | 
 Specify the circular radius of the corners of the column. Leave this property empty for sharp corners. This defines the circular radius of all 4 corners of an element.
 



 Note.
 
 Use the
 
 HTML
 
 element with inline or embedded CSS styles to specify elliptical corners and other exotic effects.
 
 |
| 
**Background** 
 | 
 Set background color for the entire column. Note that elements dropped onto the column can have their own background settings that may cover the background of the column.
 

 Background style settings are disabled by default. Select the checkbox
 **(2)** 
 to enable them.
 

 Clear this checkbox to disable all background settings of the current column.
 

 Click
 content_designer_background_color00010.png
 to open the color picker and select the background color.
  |
| 
**Borders** 
 | 
 Configure the borders of the column.
 

 Border style settings are disabled by default. Select the checkbox
 **(3)** 
 to enable them.
 

 Click to open the color picker and select the border color.
 

 Update the
 icon_border_width00012.png
 field to specify the border width. To hide the border, select the “Hidden” border style.
 

 Use the drop-down menu
 **(4)** 
 to select the border style. When the border settings are enabled, the “Solid” style is selected by default. Thse following styles are available:
 * border_style_hidden00013.png
 : Hidden




 Note.
 
 The border is defined but invisible. The border width effectively equals 0.
 
* border_style_dotted00014.png
 : Dotted
* border_style_dashed00015.png
 : Dashed
* border_style_solid00016.png
 : Solid
* border_style_double00017.png
 : Double
* border_style_groove00018.png
 : Groove
* border_style_ridge00019.png
 : Ridge
* border_style_inset00020.png
 : Inset
* border_style_outset00021.png
 : Outset


 Select or clear
 
 Top
 
 ,
 
 Bottom
 
 ,
 
 Left
 
 , and
 
 Right
 
 checkboxes to enable or disable the border style settings for the corresponding border.
  |



### 
 Column layout on desktop and mobile



 On the desktop, the columns will be arranged exactly how they are displayed in the Content Designer (Fig. 13).
 




 Fig. 13 Standard layout of a section with 6 columns
 

![6_columns_standard_layout.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/6_columns_standard_layout.png)



 On mobile devices, columns are normally not displayed side by side. Instead, they are re-arranged vertically (Fig. 14).
 




 Fig. 14 Mobile layout of a section with 6 columns
 

![6_columns_mobile_layout.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/6_columns_mobile_layout.png)



 You can force columns to display side by side on mobile by grouping them. A column group is a sequence of columns displayed side-by-side on mobile.
 



 To group two adjacent columns:
 


1. Select the
 
 Section
 
 element using the
 
 Section constructor
 
 of a
 
 Block
 
 element or the breadcrumbs navigation of a column or its child elements.
 ![btn_link_content_designer_inactive.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/btn_link_content_designer_inactive.png)
 buttons will appear between columns (Fig. 15).
 




 Fig. 15 Link columns
 

![scr_section_link_columns.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_section_link_columns.png)
2. Click the
 ![btn_link_content_designer_inactive00022.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/btn_link_content_designer_inactive00022.png)
 (Fig. 15) button between the columns that you want to group.
 



 If one of the columns is already a part of a column group, the ungrouped column will become part of the column group. If both columns are parts of their respective column groups, both column groups will become one column group.



 On mobile, grouped columns display side by side. Use the
 
 Preview
 
 tab at the top of the page to view how your email template displays on mobile.
 



 You can also reverse the order of columns on mobile so that the last column is displayed at the top of the section and the first at the bottom. For example, if you have a two-column header with a logo on the right and a title on the left, a mobile device will normally display the title first and the logo second. However, if the order of columns is reversed, the logo will display on top.
 



 To reverse the order of ungrouped columns and column groups on mobile devices, select the
 
 Reverse the order of columns on mobile
 
 checkbox (Fig. 16).
 




 Fig. 16 Reverse on mobile
 

![scr_reverse_on_mobile.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_reverse_on_mobile.png)




 Fig. 17 Working with columns
 

![mobile_use_case_slow.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/mobile_use_case_slow.gif)



 As a result, the last column or column group will be at the top of the section, and the first column or column group at the bottom.
 




 Fig. 18 Normal column order vs. reverse column order
 

![scr_normal_vs_reverse_column_order.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_block/scr_normal_vs_reverse_column_order.png)





 Note.
 
 This does not affect columns displayed side-by-side on mobile, i. e., columns inside column groups.
 




 Anchors
---------



 The Content Designer lets you use anchors. This enables the audience to navigate through larger emails easier.
 


### 
 Add an anchor


1. Select template text to use as an anchor.
2. Click
 ![btn_link.png](/docs/sites/en/files/images/Marketing_Tools/set_up_a_content_block/btn_link.png)
 on the text toolbar →
 
 Web link
 
 . This opens a window.
3. Enter the anchor name in the
 
 URL
 
 field on the
 
 Link info
 
 tab. For example, “webinars.”
4. Open the
 
 Advanced
 
 tab → specify the anchor ID in the
 
 id
 
 field. For example, “webinars.”
5. Click
 
 OK
 
 .
6. Click
 ![btn_html.png](/docs/sites/en/files/images/Marketing_Tools/set_up_a_content_block/btn_html.png)
 on the text toolbar. This opens a window.
7. Delete the “href” attribute of the anchor link together with the attribute value. For example, delete “href="http://webinars"” entirely.
8. Click
 
 Save
 
 .




 Fig. 19 Adding an anchor
 

![gif_adding_an_anchor.gif](/docs/sites/en/files/images/Marketing_Tools/set_up_a_content_block/gif_adding_an_anchor.gif)


### 
 Link an anchor


1. Create an anchor. Learn more:
 [Add an anchor](#title-1565-8) 
 .
2. Select template text to link to the anchor.
3. Click
 ![btn_link.png](/docs/sites/en/files/images/Marketing_Tools/set_up_a_content_block/btn_link.png)
 on the text toolbar →
 
 Web link
 
 . This opens a window.
4. Select “Link to anchor in the text” in the
 
 Link Type
 
 field.
5. Click
 
 OK
 
 .
6. Click
 ![btn_html.png](/docs/sites/en/files/images/Marketing_Tools/set_up_a_content_block/btn_html.png)
 on the text toolbar. This opens a window.
7. Add the anchor ID to the “href” attribute after the #. For example, “href="#webinars".”
8. Click
 
 Save
 
 .




 Fig. 20 Linking to an anchor
 

![gif_linking_to_an_anchor.gif](/docs/sites/en/files/images/Marketing_Tools/set_up_a_content_block/gif_linking_to_an_anchor.gif)



 As a result, users will be able to click the link to scroll the email to the anchor.
 




