


 When working with partner orders, you can use either the general or personal price lists for different partner categories. We recommend setting up personal price lists if you need to take into consideration special conditions of cooperation with your partner. Learn more about price list types and setup in the “
 
 Creatio price lists
 
 ” article.
 



 When working with a partner order, the price is determined as follows:
 


* Creatio checks whether any personal price list is specified for the partner account and uses the price from that price list. A personal price list is specified on the page of the partner account.
* If the partner has no no personal price or such price list does not contain prices for the ordered products, the order will use the price from the price list specified on the
 
 Partnership parameters
 
 detail of the active partnership. You can specify this price list in the
 
 Level partnership parameters
 
 lookup when finalizing the partnership conditions. More information on setting up the partnership parameters is available in the “
 
[Set up partner program parameters](/docs/8-0/user/sales_tools/channel_sales/partnership_parameters/set_up_partner_program_parameters#HT_lookups_for_partmner_program_parameters) 

 ” article.
* If none of the above price lists are provided, then the price from the “Base price list” system setting is used.
* If the base price list is not set, the order will use the price specified on the product page.



 To set up price lists, do the following in the main Creatio application:
 


1. Create a price list with a special product price. To do this, use the
 
 Price lists
 
 lookup and the
 
 Prices
 
 detail on a product page.
2. Add a
 
 Price list
 
 field on the partner account page. To add a new field (column), use the Section Wizard tool in the
 
 Accounts
 
 section.
3. Specify the personal price list on the pages of the corresponding partners.
 



 You can learn more about setting up personal price lists in the “
 
 Creatio price lists
 
 ” article.
 



 As a result, each time a product with a special price is added to the order of the selected partner account, such price will be taken from the personal price list specified on the partner account page.




