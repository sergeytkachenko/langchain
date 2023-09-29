


 You can expand the list of fonts used in your email templates. When using rare fonts you can have your messages displayed in these fonts for your customers, even if they initially do not have these fonts.
 


* **Adding a custom font** 
 enables you to select it in the
 
 Font
 
 property in the setup area of
 
 Text
 
 ,
 
 Button
 
 , and
 
 Navlink
 
 elements.
 
[Read more >>>](#HT_block_content_designer_font_add_custom)
* **Embedding a custom font** 
 lets email clients display emails using that font without having to use the “fallback fonts.” The email client will access the font using the URL that you specify.
 
[Read more >>>](#HT_block_content_designer_font_embed)
* **Modifying a font** 
 in the Content Designer to rename a font family or add, change, delete, and rearrange the fonts in the font-family.
 
[Read more >>>](#HT_block_content_designer_font_edit_fontfamily)







 Add a custom font
-----------------------



 Use the “Content builder font set” lookup to manage the list of fonts.
 





 Case.
 
 Add a custom “Parchment Regular” font.
 



1. Click
 ![btn_system_designer.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_fonts/btn_system_designer.png)
 to open the System Designer.
2. Go to the
 
 System setup
 
 block → click
 **Lookups** 
 .
3. Open the
 **Content builder font set** 
 lookup.
4. Click
 **New** 
 .
5. Specify the font family in the
 
 Name
 
 column on the left. In this case, specify “
 **Parchment** 
 .”
6. Specify the font family value in the
 
 Fonts
 
 column on the right. The font family value is a prioritized comma-separated list of the primary font and fallback fonts, from most preferable to least preferable. We recommend adding at least one generic font family as a fallback font. For example, specify “
 **Parchment, cursive** 
 .”
7. Click
 ![btn_com_apply.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_fonts/btn_com_apply.png)
 .
 



 As a result, a new font family will be available in the
 
 Font
 
 property in the setup area of
 
 Text
 
 ,
 
 Button
 
 , and
 
 Navlink
 
 elements as soon as the new item is saved.
 



 Note that adding a custom font and then using it means that the email clients will be instructed to apply the font whether it is available in the client application or not. If the email client fails to apply a font, it will use the next fallback font in the font family list. If the email client exhausts the list of fallback fonts, it will apply a default font.
 



 If you expect that your custom font will not be available in most client applications,
 
[make it an embedded font](#HT_block_content_designer_font_embed) 

 .







 Embed a custom font
-------------------------



 Use the “Content builder customer fonts” lookup to manage embedded fonts. To embed a font (e.g., “Montserrat”):
 


1. Click
 ![btn_system_designer00001.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_fonts/btn_system_designer00001.png)
 to open the System Designer.
2. Click
 **Lookups** 
 in the
 
 System setup
 
 block in the System designer.
3. Open the
 
 Content builder customer fonts
 
 lookup.
4. Click
 **New** 
 .
5. Specify the font family in the
 
 Name
 
 column on the left. For example, specify “
 **Montserrat** 
 .” Make sure that the font name that you specify matches the actual font name.
6. Specify the font URL in the
 
 URL
 
 column on the right. For example, specify
   


<https://fonts.googleapis.com/css2?family=Montserrat:wght@200&display=swap>







 Note.
 
 The value of the
 
 URL
 
 column is not restricted to the API URLs of Google Fonts. The
 
 URL
 
 field can be populated with the link to any font available online, including a self-hosted font.
7. Click
 ![btn_com_apply00002.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_fonts/btn_com_apply00002.png)
 .
 



 Log out of the application and log back in to apply changes.
 





 Attention.
 
 We do not recommend relying too much on embedding custom fonts. Some email client applications lack the feature to import custom fonts and will always use a fallback or default font.







 Edit a Content builder font
---------------------------------



 Use the “Content builder font set” lookup to manage font properties. To edit a font (e.g., “Parchment”):
 


1. Click
 ![btn_system_designer00003.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_fonts/btn_system_designer00003.png)
 to open the System Designer.
2. Click
 **Lookups** 
 in the
 
 System setup
 
 block in the System designer.
3. Open the
 
 Content builder font set
 
 lookup.
4. Click the entry to edit. For example, click the
 
**Parchment** 

 entry.
5. Redefine the font family name in the
 
 Name
 
 column on the left. For example, change it to “
 **MyCursives** 
 .”
6. Redefine the font family value in the
 
 Fonts
 
 column on the right. For example, add Pristina as the first fallback font: “
 **Parchment, Pristina, cursive** 
 .”
7. Click
 ![btn_com_apply00004.png](/sites/en/files/documentation/user/en/email_marketing/BPMonlineHelp/email_marketing_set_fonts/btn_com_apply00004.png)
 .
 



 As a result, if the Parchment font is not available in the email client application, the application will now attempt to apply Pristina before defaulting to the “cursive” generic font.




