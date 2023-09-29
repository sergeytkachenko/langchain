


 Use
 
 Attachments
 
 components to manage record attachments. This is particularly useful for scanned documents.
 





 Example.
 
 Set up the
 
 Attachments
 
 component that enables users to upload and download receipts and invoices to the request page. The component must have a gallery view and accept \*.jpg, \*.pdf, and .\*png files up to 8 MB.
 





 Fig. 1 Set up an attachment list
 

![scr_attachment_list_setup_area.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/scr_attachment_list_setup_area.png)


1. Drag an
 
 Attachments
 
 component to the canvas. The component comprises expansion panel, upload button, refresh button, flex container, search, and attachment list. You can rearrange these components arbitrarily.
2. Open the setup area of the attachment list:
 


	1. Specify the object to attach the files in the
	 
	 Record to attach files
	 
	 parameter. The object of the current record is selected by default. For this example, leave the parameter as is.
	2. Select the view type of the attachment list in the
	 
	 Appearance
	 
	 group. List and gallery view are available. For this example, select
	 
	 Gallery
	 
	 .
	3. Specify the gallery item size for the gallery view in the
	 
	 Gallery item size
	 
	 parameter. For this example, select “L.”
	4. Enter a file tag in the
	 
	 File tag
	 
	 parameter. If the parameter contains a tag, the component assigns the tag to each uploaded attachment and displays only the attachments that have the corresponding tag. Otherwise, the component displays every record attachment. This is useful if you need to add multiple attachment lists to a single object. For this example, enter “Expense compensation.”
	5. Click the
	 ![btn_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_visible.png)
	 or
	 ![btn_not_visible.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_not_visible.png)
	 button in the
	 
	 Visibility
	 
	 group to make the component visible or invisible by default on the page, respectively. For this example, leave the component visible.
	6. Click
	 
	 Setup conditions
	 
	 in the
	 
	 Visibility
	 
	 group to set up element business rules. For this example, do not add business rules. Learn more about setting up business rules in a separate article:
	 [Set up business rules](https://academy.creatio.com/documents?id=2409) 
	 .
	7. Specify where to store the attachments in the
	 
	 Table to store the files
	 
	 parameter. For this example, leave the parameter as is.
	8. View the unique component code in the page schema in the
	 
	 Element code
	 
	 parameter. Creatio uses this code in page schemas. You can change it if needed. This helps software developers to customize the app easier, especially if you have multiple similar components on the page. For this example, leave the code as is.
3. Set up the expansion panel. You can do it similarly to other
 
 Expansion panel
 
 elements Learn more in a separate article:
 [Set up an [Expansion panel] layout element](https://academy.creatio.com/documents?id=2437) 
 . For this example, leave the layout element as is.
4. Set up the
 ![btn_upload.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_upload.png)

 Upload
 
 button. You can do it similarly to other
 
 Button
 
 components. Learn more in a separate article:
 [Set up [Button] components](https://academy.creatio.com/documents?id=2401) 
 . For this example, change the following parameters:
 


	1. Set
	 
	 What is the maximum allowed file size in MB?
	 
	 to “8.” If you leave the parameter empty, the component uses the maximum size from the “Attachment max size” (“MaxFileSize” code) system setting.
	2. Set
	 
	 What file extensions are allowed to upload?
	 
	 to “.jpg, .pdf, .png.” If you leave the parameter empty, the component accepts the file extensions from the “File extensions AllowList” (“FileExtensionsAllowList” code) system setting.
5. Set up the
 ![btn_refresh.png](/docs/sites/en/files/images/NoCodePlatform/element_setup_examples/btn_refresh.png)

 Refresh
 
 button. You can do it similarly to other
 
 Button
 
 components. Learn more in a separate article:
 [Set up [Button] components](https://academy.creatio.com/documents?id=2401) 
 . For this example, leave the parameter as is.
6. Set up the search bar. You can do it similarly to other
 
 Search
 
 components.



 As a result, Creatio will add the
 
 Attachments
 
 component to the request page. Creatio will display the component as a gallery. The component will accept \*.jpg, \*.pdf, and .\*png files up to 8 MB.
 




