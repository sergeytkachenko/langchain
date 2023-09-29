


 The
 
 HTML
 
 , aka “Smart block”, element (Fig. 1) enables implementing custom HTML code into your template and enriching it with reusable user-defined macros.
 





 Fig. 1
 
 Adding an
 
 HTML
 
 element to a template
 

![adding_smartblock_from_toolbar.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_html/adding_smartblock_from_toolbar.gif)



 Use the
 
 HTML
 
 element to set custom styles such as elliptical rounding of corners, non-uniform borders, multiple background images, etc. You can also use this element to import templates designed in third-party software. To do this, add all the HTML code of such a template to the
 
 HTML
 
 element.
 





 Note.
 
 The
 
 HTML
 
 element is intended for use by HTML-savvy users who are familiar with web design and can code their custom designs in HTML.
 



 Creatio will check your custom code for errors before adding it to the template. You can review the errors and warnings in the validation panel. Warnings do not affect the validation while saving. To save the
 
 HTML
 
 element to the template, fix all detected errors.
 






 Adding a macro
------------------



 You can add custom macros to the HTML code of the
 
 HTML
 
 element. When sending an email, Creatio replaces the user-defined macros with the corresponding values specified in the
 
 HTML
 
 setup area. The
 
 HTML
 
 element enables marking variables (text, font color or images) in the element code and set up custom macros for editing.
 



 When the user creates a macro, the Content Designer generates a corresponding field and maps the value of the field to the macro. If the macro is reused in the same
 
 HTML
 
 element, the value of the field will be mapped to every instance of the macro.
 



 The following types of macros are available:
 


* New String – a single-line macro.
 
[Read more >>>](#HT_block_content_designer_smartblock_macros_string)
* New Text – a multiline macro.
 
[Read more >>>](#HT_block_content_designer_smartblock_macros_text)
* New Picture – an image source macro.
 
[Read more >>>](#HT_block_content_designer_smartblock_macros_pic)
* New Color – a color picker macro.
 
[Read more >>>](#HT_block_content_designer_smartblock_macros_color)
* The setup procedure is as follows:


1. Select an
 
 HTML
 
 element on the template and click
 
 Edit HTML
 
 .
2. Select the part of the code that you want to replace with a macro.
3. Right-click the selected code. A macro context menu will appear.
 





 Note.
 
 Right-clicking when nothing is selected in the editor does not produce a macro context menu.
4. Select the type of macro in the menu. You can create a new macro or add another instance of a previously created macro to the code. If macros have already been added to the
 
 HTML
 
 element, they will also be displayed in the context menu.
5. Specify the title of the currently selected macro in the
 
 Macro constructor
 
 area on the right (Fig. 2), so that you can identify this macro later.
 





 Fig. 2
 
 Editing the title of a macro
 

![scr_html_element_configuration_macro_constructor_area_changing_values.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_html/scr_html_element_configuration_macro_constructor_area_changing_values.png)
6. Click
 
 Save
 
 to apply changes.
 



 As a result, a new field will be available in the
 
 HTML
 
 setup area on the right (Fig. 3). Changing the value of the field will immediately update all macro instances throughout your
 
 HTML
 
 element.
 





 Fig. 3
 
 New macro field
 

![scr_html_element_new_macro_field.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_html/scr_html_element_new_macro_field.png)





 Deleting a macro
--------------------


1. Select an
 
 HTML
 
 element where you need to delete a macro and click
 
 Edit HTML
 
 .
2. In the
 
 Macro constructor
 
 area on the right, click
 ![content_section_item_view_model_remove_icon.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_html/content_section_item_view_model_remove_icon.png)
 next to the macro that you want to delete (Fig. 4).
 





 Fig. 4
 
 Deleting a macro field
 

![scr_html_element_deleting_a_macro_field.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_html/scr_html_element_deleting_a_macro_field.png)
3. Click
 
 Save
 
 to apply changes.
 



 As a result, all instances of the macro will be replaced with the current value of the macro. The macro will be no longer available in the setup area of the
 
 HTML
 
 element.





 Macro types
---------------


### 

 String macros



 Use this macro type to insert a
 **short single-line text** 
 that is not white space pre-formatted (Fig. 5).
 





 Fig. 5
 
 Configuring “New String” macros
 

![adding_string_macros.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_html/adding_string_macros.gif)



 Any white space characters in the macro value will be inserted as-is. This means that some breakable white space characters (particularly, character tabulations and new lines) or a sequence of such characters will display as a single space character. Additionally, pressing the Enter key when editing the field does not produce a new character.
 



 As a result, the text will display as a single line unless user-defined CSS rules forbid such behavior.
 


### 

 Text macros



 Use this macro type to insert
 **long multiline white space pre-formatted texts** 
 (Fig. 6).
 





 Fig. 6
 
 Configuring “New Text” macros
 

![adding_text_macros.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_html/adding_text_macros.gif)



 When the user populates a “New Text” macro field with a string, new lines will be converted to line breaks, multiple space characters will be replaced with unbreakable space characters, and character tabulations will be replaced with a sequence of four unbreakable space characters. Additionally, pressing the Enter key when editing the field will produce a new line character.
 



 As a result, the displayed text preserves white space pre-formatting of the source text in the source macro field.
 


### 

 Picture macros



 Use this macro type to replace or provide the value of the “
 **src** 
 ” attribute of an  container or the value of a “
 **url** 
 ” CSS property.
 



 When the macro is created, the Content Designer generates an image source field (
 ![scr_field_image_proper.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_html/scr_field_image_proper.png)
 ) mapped to the macro. Use this field to add image to the template. You can upload a local image or specify an image URL (Fig. 7).
 





 Fig. 7
 
 Adding “New Picture” macros
 

![adding_pic_macros.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_html/adding_pic_macros.gif)





 Note.
 
 The
 ![scr_field_image_proper00001.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_html/scr_field_image_proper00001.png)
 field supports Data URIs. You can insert a base64-encoded image instead of a URL.
   

 Base64-encoded images are part of the HTML code of the message and are not normally filtered by email clients that prevent external images from loading by default.
 



### 

 Color macros



 Use this macro type to replace or provide
 **color definitions** 
 for embedded style sheets and in-line element styles (Fig. 8).
 





 Fig. 8
 
 Configuring “New Color” macro
 

![adding_color_macros.gif](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_add_html/adding_color_macros.gif)



 When a new “Color” macro is created, the Content Designer generates a color picker field mapped to the macro. Use the field to pick a color for your macro. The macro will generate a hexadecimal RGB color code, preceded with the “#” sign, e.g. “
 **#0d2e4e** 
 ”.
 




