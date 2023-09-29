


 In Creatio, you can set up corporate logo that will display for all users.
 



 You can customize the following elements:
 


* **Logo** 
 that will display:
 


	+ on the loading screen and the Excel import page;
	+ in the upper panel;
	+ on the main page (
	 [Fig. 1](#XREF_97344_186)
	 ).
	 
	
	
	
	
	
	 Fig. 1
	 
	
	 Custom logo on the main page
	 
	
	![scr_logo_setup_example.png](/guides/sites/en/files/documentation/user/en/appearance_customization/BPMonlineHelp/appearance_customization_logo/scr_logo_setup_example.png)


* **Browser tab** 
 :
 


	+ Application name (
	 [Fig. 2](#XREF_16909_76)
	 ).
	 
	
	
	
	
	
	 Fig. 2
	 
	
	 The new application name in the browser tab
	 
	
	![scr_logo_setup_browser_name.png](/guides/sites/en/files/documentation/user/en/appearance_customization/BPMonlineHelp/appearance_customization_logo/scr_logo_setup_browser_name.png)
	+ Favicon – a thumbnail image in the browser tab (
	 [Fig. 3](#XREF_11663_486)
	 ).
	 
	
	
	
	
	
	 Fig. 3
	 
	
	 The new favicon in the browser tab
	 
	
	![scr_logo_setup_favicon.png](/guides/sites/en/files/documentation/user/en/appearance_customization/BPMonlineHelp/appearance_customization_logo/scr_logo_setup_favicon.png)





 Changing the logo
---------------------


1. Open the system designer by clicking the
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/appearance_customization/BPMonlineHelp/appearance_customization_logo/btn_system_designer.png)
 button.
2. Click
 **Logo customization** 
 in the
 
 Set up view
 
 block.
 





 Note.
 
 You can customize the logo only if you have permission to perform the "Logo customization changes" (CanManageLogo) system operation. Learn more about operation permissions in the “
 
[System operation permissions](https://academy.creatio.com/documents?product=administration&ver=7&id=258) 

 ” article.
3. The page displays current logos:
 





|  |  |
| --- | --- |
| 
 Login page logo
  | 
 This logo displays on the main page, the login page and the Excel import page. Recommended image size: 61x310 pixels. The image is stored in the "Logo" (LogoImage) system setting.
  |
| 
 Main page logo
  | 
 This logo displays on the main page and the System Designer page. Recommended image size: 37x274 pixels. The image is stored in the "Logo in main menu" (MenuLogoImage) system setting.
  |
| 
 Upper panel logo
  | 
 This logo displays in the top right corner of section pages. Recommended image size: 27x127 pixels. The image is stored in the "Upper panel logo" (HeaderLogoImage) system setting.
  |
4. Click
 ![btn_add_userpic.png](/guides/sites/en/files/documentation/user/en/appearance_customization/BPMonlineHelp/appearance_customization_logo/btn_add_userpic.png)
 to
 **upload** 
 images.
 **PNG** 
 is the recommended image format. You can use other standard image formats supported in modern browsers. If you use SVG files, you need to specify the width='...' height='...’ parameters, otherwise some browsers may fail to render the image properly. If you upload a larger image, it will be scaled down to match the required dimensions.
5. **Save** 
 the changes.
 



 To enable new logo in the interface, log out of Creatio and log back in.





 Changing the application name in the browser tab
----------------------------------------------------


1. Open the system designer by clicking the
 ![btn_system_designer00001.png](/guides/sites/en/files/documentation/user/en/appearance_customization/BPMonlineHelp/appearance_customization_logo/btn_system_designer00001.png)
 button.
2. Click
 
**System settings** 

 in the
 
 System setup
 
 block.
3. Open the “
 **Product name** 
 ” system setting and
4. **Change the default value** 
 . For example, specify “Our company” instead of “Creatio”. Specify any special characters in the name as an HTML code.
5. **Save** 
 the changes. As a result, the name of the application in the browser tab will change.
 



 To enable new logo in the interface, log out of Creatio and log back in.





 Changing the favicon
------------------------



 You can change the default favicon in the browser tab. To do this:
 


1. Open the system designer by clicking the
 ![btn_system_designer00002.png](/guides/sites/en/files/documentation/user/en/appearance_customization/BPMonlineHelp/appearance_customization_logo/btn_system_designer00002.png)
 button.
2. Click
 **“System settings** 
 ” in the
 
 System setup
 
 block.
3. Open the
 **“FaviconImage** 
 ” system setting. Click
 
 Clear value
 
 . Click
 
 Select file
 
 and choose the image. Save the changes.
4. Open the “
 **UseFaviconFromSysSettings** 
 ” system setting. Select the
 
 Default value
 
 checkbox to use the favicon uploaded in the previous step.
 



 As a result, the new favicon will display in the browser tab.
 



 To enable new logo in the interface, log out of Creatio and log back in.




