


 The
 
 Products
 
 section contains information about products and servicesoffered by your company. Use this section to create a product catalog, specify product prices and stock, as well as store detailed description and features for each product.
 



 Add a product record
----------------------


1. Open the
 
 Products
 
 section and click
 
 New product
 
 .
2. On the
 
 General information
 
 tab, populate the following information about the product:
 






|  |  |
| --- | --- |
| 
 Photo
  | 
 Image of the product. Click
 btn_com_add_photo.png
 to add a new image by using the standard file selection window. We recommend uploading a square image (aspect ratio: 1:1). Click
 btn_com_delete_photo.png
 to remove the image.
  |
| 
 Name
  | 
 Name of the product or service.
  |
| 
 Code
  | 
 Identifier of the product. The product code is often used, for example, if two products have the same name.
  |
| 
 Link
  | 
 Link to a web resource related to the product, for example, the product page on the manufacturer's website or in the online shop catalog.
  |
| 
 Unit of measure
  | 
 Product measuring unit. The field is only available for Sales Creatio, team edition.
  |
| 
 Owner
  | 
 The employee who is responsible for this product.
  |
| 
 Inactive
  | 
The checkbox indicates that the product cannot be offered to customers. For example, the product has been withdrawn from sale or is no longer delivered. Inactive products are not displayed on the product selection page.
 |
3. Specify product segmentation parameters (available for Creatio Sales, commerce edition; Creatio Sales, enterprise edition; Creatio Marketing):
 






|  |  |
| --- | --- |
| 
 Category
  | 
 Product category, for example, “Hardware” or “Software”.
  |
| 
 Type
  | 
 Type of product. The list of types depends on the selected category. For example, products of the “Hardware” category can be of the following types: “Graphics cards”, “Motherboards”, etc.
  |
| 
 Brand
  | 
 Product brand.
  |
4. Populate the base price value according to which the product prices will be specified in the price lists.
 






|  |  |
| --- | --- |
| 
 Price
  | 
 Price of the good or service. The amount can be specified in any currency.
 

 For more on the currency conversion, see the “
 
[Working with currencies](https://academy.creatio.com/documents?product=base&ver=7&id=1584) 

 ” article.
  |
| 
 Tax
  | 
 The tax rate that will be used by default with this product, for example, “VAT” (available for Creatio Sales editions).
  |
| 
 Unit of measure
  | 
 The base unit of measure of the product. When you save the record, the selected unit of measure is added to the
 
 Units
 
 detail with the
 
 Base
 
 checkbox selected.
  |
5. 5.Click
 
 Save
 
 .



 Specify product availability
------------------------------





 Note.
 
 The feature is only available for Creatio Sales, enterprise edition and Creatio Sales, commerce edition.
 




 Use the
 
 Availability
 
 detail on the product page to enter information about the number of products available at the warehouses. If you store products in several warehouses, the number of products in stock, reserved products, and products on hand will display for each product.
 



 You can populate the detail manually. If you set up an integration with a third-party system, the information from your external account appears in the detail automatically. To add a record on the detail, click
 ![btn_com_add_tab.png](/guides/sites/en/files/documentation/user/en/products_and_prices/BPMonlineHelp/add_products/btn_com_add_tab.png)
 and populate the page that opens:
 






|  |  |
| --- | --- |
| 
 Warehouse
  | 
 The warehouse where the product is stored.
  |
| 
 Balance
  | 
 The total quantity of the product stored in the warehouse.
  |
| 
 Reserved
  | 
 Reserved quantity of products.
  |
| 
 Available
  | 
 Product quantity that can be sold. The field is non-editable. Its value is calculated as the subtraction of the
 
 Reserved
 
 and
 
 In stock
 
 fields.
  |





 Specify product features
--------------------------





 Note.
 
 The feature is only available for Creatio Sales, enterprise edition; Creatio Sales, commerce edition and Creatio Marketing.
 




 Use the
 
 Features
 
 tab of the product page to customize the product features. For example, computer CPU speed or supported memory. You can search for a product by the product feature in the product catalog.
 



 You can add the following types of product features:
 



 Once you save the feature, it will be available on the
 
 Features
 
 detail of the product page.
 


1. In the
 
 Products
 
 section, open the needed product.
2. Go to the
 
 Features
 
 tab and click
 ![](/guides/sites/en/files/documentation/user/en/products_and_prices/BPMonlineHelp/add_products/btn_com_add_tab00001.png)
 . A new product feature page opens.
3. Populate the
 
 Feature
 
 field:
 


	1. To add an existing feature, type in the feature name or use the lookup window to select a feature.
	2. To add a new feature, open the lookup window and click
	 
	 New
	 
	 , then populate the feature name and select its value (e.g., for example, “Drop-down list” or “Decimal”). After saving a new feature the
	 
	 Value type
	 
	 field becomes non-editable.
4. Populate the value of the feature. If you select the “Drop-down list” data type, the
 
 Values
 
 detail appears on the page. You can add the needed list of feature values to it. The value displays on the page once you select a feature. The field type depends on the type of the selected feature value. For example, you can enter a digit for the decimal feature, and select or clear the checkbox for the boolean feature.
5. Click
 
 Save
 
 on the feature page to save the product feature.
 



 You can add the following
 **types of product features** 
 :
 


	* “Decimal”; “Integer” – numeric type. For example, the “CPU Speed, GHz” or “Number of cores” features.
	* “Drop-down list” – data type for which you can select a value from the list. For example, the “Computer case color” feature for which the following list of values is specified: “Black” and “Silver.”
	* “Boolean” – data type for which you can specify the “Yes” or “No” value. For example, “DVD”.
	* “String” – data type for which you can manually enter a text value. For example, the “Additional information” detail.




