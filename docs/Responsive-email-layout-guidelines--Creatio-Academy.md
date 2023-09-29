


 When you prepare an email template, you cannot predict which mail client or which device the recipient will use to open it. That is why we recommend considering general rules for the
 **responsive email layout** 
 for your email templates. Complying with these rules will ensure the correct display of your email at different devices.
 



 The pre-configured Creatio content blocks are responsive by default. This article covers the nuances that influence the correctness of displaying the emails created using
 **custom content blocks** 
 or
 **imported** 
 in Creatio via HTML elements.
 



 General responsive layout principles
--------------------------------------



 Abide by the following recommendations to ensure your email is readable regardless of the device and mail client:
 


* The email template layout is table-based. Many HTML and CSS properties that work for websites do not work for emails. In Creatio, the table layout is managed via the “block” template element.
* We recommend creating templates no wider than 700 pixels since many mail clients limit the email width, and a recipient might see a horizontal scroll bar.
* Use standard fonts for email copy. They are easy to read at any screen resolution. Besides, if you use one of the fonts that are not supported by the recipient’s mail client, it will be automatically converted to a standard font, which might damage the layout.
* If you need to use non-standard fonts in the headers, paste them into your email as images and use alternative text for cases when the recipient mail provider does not upload images by default.
* Make your email text no smaller than 12–13 pixels to save your recipient from straining their eyes. Some mobile clients can increase the size of the font automatically if it is smaller than 12 pixels in the original, which might interfere with your email layout.
* Use the screen effectively: place the most important information, including the call-to-action buttons, above the fold of the email so that the information is visible both on the computer and mobile screens without scrolling.
* Stick to minimalistic design. The templates that use 2–3 primary colors and few images load faster and adapt to mobile devices better.
* We do not recommend using background images in templates. They increase the loading time and might fail to display in some mail clients. If you still use such an image, add a color background to it so that your text is well visible if the image fails to display.
* Use large buttons to make them convenient to use for the recipient, especially if they use a mobile device. The recommended button size is 44x44 pixels.



 Microsoft Outlook layout specifics
------------------------------------



 When sending emails to customers, Microsoft Outlook users should take into account that when viewing emails in MS Outlook, some elements may be displayed differently than in the template preview. For example, the buttons might not display the corner radius. Also, for security reasons, Microsoft Outlook blocks the downloading of images in emails by default.
 



 For the correct display of email template styles in Microsoft Outlook, add comments that determine styles for MS Outlook to each table cell in the HTML code. For example, for an employee signature the Microsoft Outlook comments will look as follows:
 






```

<tr>
    <td valign="top" style="vertical-align: middle;">
        <!--[ if (gte mso 9)|(IE) ]>
        <table width="100%" cellpadding="0" cellspacing="0" border="0" style="vertical-align:top;">
            <tr>
                <td width="300" valign="top" style="vertical-align: middle; margin: 0; padding:0;">
                    <![ endif ]-->
                    <div style="display: inline-block; vertical-align: middle;max-width: 300px; width:100%; margin: 0; padding:0;">
```






 Fig. 1 An example of the sender’s signature in Microsoft Outlook
 


![scr_chapter_content_designer_signature.png](/docs/sites/en/files/images/Marketing_Tools/email_recommendations/scr_chapter_content_designer_signature.png)




 Creatio ready-made content blocks, as well as any content designed using standard Content Designer elements, are already optimized for Microsoft Outlook.
 



 The “corner radius” settings (rounded edges) for CTA buttons will be ignored in Microsoft Outlook, and the buttons will display as if the
 
 Corner radius, px
 
 property is set to “0.”
 




 Fig. 2 Buttons in Creatio
 


![chapter_content_button_standard_view.png](/docs/sites/en/files/images/Marketing_Tools/email_recommendations/chapter_content_button_standard_view.png)





 Fig. 3 Buttons display in Microsoft Outlook
 


![chapter_content_button_outlook_view.png](/docs/sites/en/files/images/Marketing_Tools/email_recommendations/chapter_content_button_outlook_view.png)




 Specifics of email layout on mobile
-------------------------------------



 The following layout types are used to adapt the display of custom email templates to mobile devices:
 


* **Single-column layout** 
 . If you do not use columns in the “Block” elements of your emails, their layout will be the same for desktop and mobile devices. Note that most out-of-the-box template content blocks use multiple columns.
* **Multi-column layout** 
 also known as module grid layout. In this case, the email layout is divided into several columns and is regrouped for the display on a mobile device.



 The number of columns in an email template depends on the structure of its content blocks. By default, all new “Block” elements have a single row and a single column. You can check the column layout of each section in a content block by clicking this section in the setup area.
 




 Fig. 4 Mobile-friendly email layout example
 


![gif_multiple_columns.gif](/docs/sites/en/files/images/Marketing_Tools/email_recommendations/gif_multiple_columns.gif)



### 
 One-column layout



 For a single-column layout, we recommend using templates containing one column, 600-700 pixels wide. Otherwise, the message may not be displayed correctly. For example, parts of tables or images can exceed the size of the recipient’s mobile device screen, which might reduce or increase the font size to the point when it becomes unreadable, as in the figure below.
 




 Fig. 5 Example of non-adaptive layout
 


![chapter_content_designer_non_adaptive_page_layout.png](/docs/sites/en/files/images/Marketing_Tools/email_recommendations/chapter_content_designer_non_adaptive_page_layout.png)




 If you design your emails in Creatio Content Designer, you can set the template width in the
 
 Width
 
 field of the template setup area.
 




 Fig. 6 Example of adaptive layout in Creatio
 


![gif_set_template_width.gif](/docs/sites/en/files/images/Marketing_Tools/email_recommendations/gif_set_template_width.gif)




 Please note that the preview of the generated message in the Content Designer does not guarantee that the email recipient will see the same thing. This is due to the settings and features of different email clients.
 



 Before you start sending an email, we recommend testing the message layout by sending it to addresses registered on different email services. Send a
 [test email](/docs/7-18/user/marketing_tools/email_marketing/additional_setup/test_emails/send_a_test_email) 
 using the corresponding action.
 


### 
 Multi-column layout



 We recommend using a multi-column layout for marketing emails. It works well for templates with different types of content: texts, images, buttons, or HTML elements. Use 2-4 columns in a multi-column layout. This structure is convenient for adapting to mobile devices – the content elements are restructured to fit one column, for example, as displayed in the figure below.
 




 Fig. 7 Example of multi-column mobile layout
 


![scr_chapter_content_designer_2_columns_design_mobile.png](/docs/sites/en/files/images/Marketing_Tools/email_recommendations/scr_chapter_content_designer_2_columns_design_mobile.png)




 In templates, designed with Creatio Content Designer, you can manage the order in which the columns will go in the mobile layout. You can group columns to force them to display side-by-side on mobile devices.
 




