




 Note.
 
 The feature is only available for Creatio Sales, enterprise edition and Creatio Sales, commerce edition.
 




 Use price lists to manage prices for different customer categories. You can include a product in multiple price lists. When issuing orders, use either the universal “base” price list or a price list that is specific for the customer or affiliate.
 



 Personal price lists are specified in the customer’s account profile.
 





 Note.
 
 For more information on using personal price lists in affiliate orders, see the “
 
[Special conditions of partner cooperation](https://academy.creatio.com/documents?product=portal&ver=7&id=2147) 

 ” article.
 




 When issuing an order, Creatio pulls the price from the customer’s personal price list, if the corresponding price list is available. If the product price is not found in the customer’s personal price lists, Creatio pulls the price from the base price list (specified in the “Base price list” system, setting). If the base price list is not set, Creatio pulls the product price from the product page.
 






 Create a personal price list
---------------------------------



 Use the
 
 Price lists
 
 lookup to manage your price lists. The prices for different price lists are specified in the
 
 Prices
 
 detail of the
 
 Prices and availability
 
 tab on the product page.
 


1. Click
 ![btn_system_designer.png](/guides/sites/en/files/documentation/user/en/products_and_prices/BPMonlineHelp/manage_prices/btn_system_designer.png)
 in the main Creatio application. The System Designer will open.
2. Click the
 
 Lookups
 
 link in the
 
 System setup
 
 block.
3. Open the
 
 Price lists
 
 lookup → click
 
 Add
 
 . Enter the price list name, e.g., “VIP Affiliates.”
4. Open the
 
 Products
 
 section. Open a product page.
5. Go to the
 
 Prices and availability
 
 tab →
 
 Prices
 
 →
 ![btn_com_add_tab.png](/guides/sites/en/files/documentation/user/en/products_and_prices/BPMonlineHelp/manage_prices/btn_com_add_tab.png)
 . The
 
 Product price
 
 page opens.
6. Select the price list in the
 
 Price list
 
 field.
7. Specify the product price for the selected price list in the
 
 Price
 
 field.
8. Click
 
 Save
 
 .
 



 As a result, the name of the new price list will be added to the
 
 Prices
 
 detail (
 [Fig. 1](#XREF_16322_294__VIP)
 ).
 





 Fig. 1
 

 Price list displayed on a product page
 

![scr_section_products_pricelist_example.png](/guides/sites/en/files/documentation/user/en/products_and_prices/BPMonlineHelp/manage_prices/scr_section_products_pricelist_example.png)






 Add the [Price list] field to the account page
---------------------------------------------------



 By default, the
 
 Price list
 
 field is hidden on the account page. You can add this field via the Section Wizard, for example, to the record profile (
 [Fig. 1](#XREF_20460_46)
 ).
 



 See the “
 
[Set up page fields](https://academy.creatio.com/documents?product=administration&ver=7&id=1399) 

 ” article for more about adding fields to pages, based on existing section columns.
 





 Fig. 1
 

 The
 
 Price list
 
 field displayed on the account page
 

![scr_chapter_portal_setup_personal_pricelist.png](/guides/sites/en/files/documentation/user/en/products_and_prices/BPMonlineHelp/manage_prices/scr_chapter_portal_setup_personal_pricelist.png)






 Select a personal price list on the account page
-----------------------------------------------------


1. Open the
 
 Accounts
 
 section.
2. Select an account and open the account page.
3. Populate the
 
 Price list
 
 field by selecting the new personal price list and click
 
 Save
 
 .
 





 Note.
 
 By default, the
 
 Price list
 
 field is hidden on the account page. Use the Section Wizard to add the field to the record page of the
 
 Accounts
 
 section.
 




 As a result, every time the account orders a product from the personal price list, Creatio will pull the product price from that price list.




