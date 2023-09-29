


 In Creatio, you can store monetary values in multiple currencies. The values that you enter will be automatically converted to different currencies according to the exchange rates. These functions are available in products with the
 
 Products
 
 ,
 
 Orders
 
 ,
 
 Invoices,
 
 and
 
 Contracts
 
 sections.
 



 The currencies are used in special “currency fields”.
 




 Select currency
------------------



 In Creatio, you can enter monetary amounts in the special
 **currency fields** 
 . For example, you can specify a product price in a “currency” field.
 



 Currency fields store both the monetary amount and the currency in which this amount is specified. Click a currency field title to view the list of available currencies. The list contains currencies that are available in the
 
 Currency
 
 lookup (
 [Fig. 1](#XREF_74298_156)
 ).
 





 Fig. 1
 

 Selecting currency from the list in the currency field
 

![scr_chapter_currencies_select_currency.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_currencies/scr_chapter_currencies_select_currency.png)





 Note.
 
 If the
 
 Currency
 
 lookup contains only one record, the list of currencies in the currency field will be unavailable.
 




 If you change the currency in a populated currency field, the amount will be automatically converted to the new value according to currency exchange rates.
 





 Note.
 
 Read more about how Creatio converts currencies in a
 
[separate article](#HT_faq_exchange_rates) 

 .
 




 Clicking the
 ![btn_com_edit_multicurrency_control.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_currencies/btn_com_edit_multicurrency_control.png)
 button in the currency field displays an additional edit window (
 [Fig. 2](#XREF_57754_157)
 ).
 





 Fig. 2
 

 Additional currency field edit window
 

![scr_chapter_currencies_popup.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_currencies/scr_chapter_currencies_popup.png)



 In this window you can:
 


* View the equivalent of the specified monetary amount in the base currency in the
 
 Amount
 
 field. This is a non-editable field.
* Change the currency of the monetary amount (will be recalculated automatically).
* Edit the exchange rate of a currency to the base currency, the amount will be recalculated automatically. The new rate will be in effect only for the current record.





 Note.
 
 Use the
 
 Base currency
 
 system setting to specify the “base currency”. All exchange rates will be calculated according to the base currency.
 



* View the value of the multiplicity ratio between the specified currency and the base currency when determining the exchange rate.





 Note.
 
 When you select the base currency, the
 
 Rate
 
 field is automatically filled in with the “1” value and becomes grayed-out.
 




 To save changes in the additional window, click the
 
 Apply
 
 button or anywhere outside of the currency field edit window.
 








 Work with currency conversion
------------------------------------



 You can work with various currencies in Creatio. The conversion is performed automatically, taking into account the conversion currency exchange rate to the base currency and multiplicity ratio.
 


* The
 **base currency** 
 is the currency based on which the rate for all other currencies is set. Use the
 
 Base currency
 
 system setting to select a base currency.
* The
 **conversion currency** 
 is any other currency to which the money is converted.
* The
 **exchange rate** 
 determines the conversion currency amount in the base currency.
* The
 **multiplicity ratio** 
 indicates how many monetary units of the base currency correspond to the set exchange rate.



 The exchange rate and ratio of the currency are specified in the
 
 Currencies
 
 lookup (
 [Fig. 3](#XREF_85903_158)
 ).
 



 The exchange rate of the conversion currency is specified in terms of the base currency taking into account the ratio. Currency rates are automatically re-calculated according to their base currency exchange rates and ratio.
 



 For example, if the Yen is the base currency and the USD will have the 56537.3 exchange rate value for the 1000 ratio in the
 
 Currencies
 
 lookup, the exchange rate will be displayed in the additional window of the currency field as 17.6874 USD for 1000 Yen.
 





 Fig. 3
 

 – Possible content of the
 
 Currencies
 
 lookup
 

![scr_chapter_currencies_lookup.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_currencies/scr_chapter_currencies_lookup.png)





 Note.
 
 The
 
[Currencies
 
 lookup](#HT_common_lookups_lookup_currencies) 

 structure is described in a separate chapter. Use the “Base currency” system setting to select a base currency.
 






 Set up exchange rates
-------------------------



 Set up the exchange rates for proper currency conversion towards the base currency. To do this:
 


1. Open the
 
 Currencies
 
 lookup.
2. Set the “1” value for the rate of the base currency.
3. Select the currency to set up the rate (for example, euro). Click
 ![btn_edit.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_currencies/btn_edit.png)
 .
4. On the opened currency settings page, set the ratio, for example, “1000”.
 





 Note.
 
 For a more accurate calculation of prices during conversion, specify a high ratio for currencies, for example, “1000”.
5. Specify the exchange rate between the current currency and the base currency in the
 
 Rate
 
 field, considering the ratio. Save the changes.
 





 Example.
 
 If the base currency is yen and the euro to yen ratio is 63.9655, specify the “63965.5” as the exchange
 
 Rate
 
 and “1000” as the
 
 Ratio
 
 .
6. Repeat steps 3 through 7 for all currencies specified in the lookup.
 



 Update all data in the lookup if the exchange rates are changed,





 Calculate exchange rates using a ratio
------------------------------------------



 The following formula is used for calculating exchange rates in Creatio:
 






```

Rate=Amount in conversion currency*Ratio/Amount in base currency
```







 Example.
 
 1000 Japanese yen is worth 0.84 US Dollars. Yen is selected as the base currency and the dollar ratio is 100. The actual conversion is as follows:
 







```

Rate=19.40*100/1000=1.94
```





 Thus, when the ratio is 100, the US dollar exchange rate to yen is 1.94
 





 Currency conversion
-----------------------



 When converting monetary amounts from the base currency into another currency, use the following formula:
 






```

Amount in conversion currency=Rate*Amount in base currency/Ratio
```





 For example, 1,000 yen must be converted to US dollars. Yen is selected as the base currency, the USD / yen exchange rate is 1.94 and the ratio is 100. The actual conversion is as follows:
 






```

Amount in conversion currency=1.94*1000/100=19.4
```





 Thus, the amount of 1000 yen is equal to 19.40 USD.
 



 When converting monetary amounts from one currency to another, calculations are made based on the base currency. The following formula is used:
 






```

Amount in conversion currency(2)=Amount in conversion currency(1)*Ratio(1)*Rate(2)/Ratio(2)*Rate(1)
```





 For example, USD 100 must be converted to euro Yen is selected as the base currency. The dollar/yen exchange rate is 1.94, with a ratio of 100, and the euro/yen exchange rate is 1.73, with a ratio of 100. The actual conversion is as follows:
 






```

Amount in euro=100*100*1.73/100*1.94=89.2
```





 Thus, USD 100 is converted to EUR 89,20.
 






 Calculate product price in an order
----------------------------------------



 Let's see how the product price is calculated in order.
 





 Example.
 
 The order currency is yen. Add a product with the price is specified in US dollars to the order. The base system currency is the yen, the ratio of the US dollar is 100, the product price is USD 14.6.
 




 Click
 ![btn_chapter_mobile_wizard_new_role.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_currencies/btn_chapter_mobile_wizard_new_role.png)
 on the
 
 Products
 
 detail to add products to the order. On the product selection page, all products are priced in the currency used for the order (
 [Fig. 4](#XREF_32202_159) 
 ). In this case, “yen”.
 





 Fig. 4
 

 The ordered product selection page
 

![scr_chapter_currencies_produst_in_order.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_currencies/scr_chapter_currencies_produst_in_order.png)



 For the products with the base price specified in foreign currency, the product price is automatically converted to the base currency according to the current exchange rate specified as follows:
 






```

Product price*Ratio/Exchange rate – 14.6*100/1.5092=967.40
```





 As a result, a new product will be added to the detail. The price of the product will be specified in yen. The
 
 Price
 
 and
 
 Total
 
 fields are populated automatically and are not available for editing.
 








 Manage currencies
------------------------



 This lookup contains a list of currencies used in mutual payments with customers, partners, suppliers, and the like.
 





|  |  |
| --- | --- |
| 
 Name
  | 

 Name
 
 – indicate the name of the currency, for example, “US Dollar” or “Euro”.
  |
| 
 Code
  | 
 Specify a banking code that is used for a specific currency, for example, the US dollar code is 840.
  |
| 
 Short name
  | 
 Shortened currency name, such as “USD” or “EUR”.
  |
| 
 Symbol
  | 
 Currency symbol, such as “$” or “€”.
  |
| 
 Ratio
  | 
 Specify the currency amount for which the exchange rate will be calculated (for example, 1, 10, 100).
  |
| 
 Description
  | 
 Additional information about the currency.
  |
| 
 Show currency sign
  | 
 Choose the appropriate option from the drop-down list. Choose
 
 on the left
 
 or
 
 on the right
 
 options to display the sign before or after the amount.
  |



##### 
 [Exchange rate] detail



 Information about exchange rates is stored on the
 
 Exchange rate
 
 detail.
 





|  |  |
| --- | --- |
| 
 Start
  | 
 The starting date for the exchange rate. The start date of a new exchange rate is considered the end date of the previous exchange rate.
  |
| 
 Exchange rate
  | 
 The exchange rate between the base currency and the current currency. Enter a value according to the currency ratio, specified in the currency card. The value for the base currency must be set to “1”.
  |
| 
 End
  | 
 The ending date for the exchange rate. Populated automatically, when the starting date of the new exchange rate is set. This is a non-editable field.
  |






 Note.
 
 The base currency is used to calculate the financial performance indicators, for example, it can be “US Dollar”. Use the “Base currency”
 
system setting

 to select a certain base currency.
 









 Currencies FAQ
---------------------


### 



 How to calculate the price of the product in an opportunity, if the base price list is listed in US dollars, and the base system currency is the Yen?



 The price of a product in opportunity is always converted to the system base currency. When the product is added to the opportunity the automatic conversion of the product price to the base currency is performed according to the exchange rate specified in the
 
 Currencies
 
 lookup. The page of a product in the opportunity displays the product price for one unit and the total price of products specified in base currency and calculated according to the exchange rate available at the date of the offer. These data will be displayed in the order created based on an opportunity.
 



 If the exchange rate has changed dramatically before order creation, remove the obsolete product data from the opportunity after the agreement with the customer. When you re-add the product to the opportunity, its price and total cost will be recalculated according to the current exchange rate.
 


### 



 How the currency conversion is performed in orders?



 Currency conversion in order occurs when you select or change the order currency. When adding products to the order, their prices will be automatically converted into the currency indicated on the order page at the current exchange rate. In case of changing the currency of an already created order, the prices and the total amount specified on the
 
 Products
 
 tab of the order page will be converted to the new currency. More information about the price calculation of a product in an order is described in a
 
[separate article](#HT_faq_exchange_rates_amount_in_order) 

 .
 


### 



 Can I use different currencies for orders and their invoices?



 Yes, you can. For example, when selling products or services to foreign customers, you can keep information on products in an opportunity and order in the base currency and still issue invoices in the corresponding foreign currency at the exchange rate available on the date of invoice.
 








