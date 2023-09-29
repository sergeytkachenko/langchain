


 Set up bank product recommendations (Next Best Offers) using predictive data analysis. Use Next Best Offers to nurture a personalized approach, improve communication with existing customers, and attract new customers.
 



 The recommendation prediction setup consists of the following steps:
 


1. [Set up the recommendation prediction model](/docs/user/customization_tools/ai_tools/recommendations/recommendation_prediction) 
 .
2. [Configure a prediction business process](/docs/user/customization_tools/ai_tools/set_up_a_process/implement_prediction_models) 
 .



 The recommendation prediction model in Financial Services Creatio must save the prediction result and the contact or legal entity for whom the prediction is made to the
 
 Product recommendations
 
 lookup. In this case, the page of the corresponding contact or legal entity will display a Next Best Offers message.
 




 Fig. 1 A Next Best Offers message
 

![scr_NBO_on_contact_page_bank.png](/docs/sites/en/files/images/Finance_and_Banking/next_best_offer/scr_NBO_on_contact_page_bank.png)



 To view the Next Best Offers:
 


* Click the notification on the legal entity or contact page.
* Go to the product selection step in a business process.



 If Creatio finds Next Best Offers for a customer, the product selection page will display a separate “Next Best Offer” catalog level (Fig. 2).
 




 Fig. 2 Next Best Offers
 

![scr_product_selection_page_with_NBO_bank.png](/docs/sites/en/files/images/Finance_and_Banking/next_best_offer/scr_product_selection_page_with_NBO_bank.png)



 Creatio will show the probability of a successful sale for each Next Best Offer. Click the product to view the brief description of its main features and advantages (Fig. 3).
 




 Fig. 3 A recommended product’s description
 

![scr_recommended_product_overview_bank.png](/docs/sites/en/files/images/Finance_and_Banking/next_best_offer/scr_recommended_product_overview_bank.png)



 The following actions are available for recommended products:
 


* Application
 
 – click to initiate the application for the selected product. Creatio will set the corresponding record’s status to “Accepted” in the
 
 Recommended product status
 
 lookup. The product will no longer be available on the product selection page of the current customer.
 





 Note.
 
 The application process may vary depending on how you open to the recommended products page. If you click the
 
 Application
 
 button on the recommended products page opened from the customer page, Creatio will run the process specified in the “
 [Process for registration selected product](/docs/7-17/user/setup_and_administration/system_settings_and_lookups/system_setting_reference/description_of_system_settings#title-1880-35) 
 ” (“SelectedProductRegistrationProcess” code) system setting. If you click the button on the page opened as part of a product selection business process or case, Creatio will perform actions configured in the business process or case.
* Details
 
 – click the button to open the product page with the product details.
* Close
 
 – click the button to close the window with additional information. The product will still be available in the recommendation list.
* Not interested
 
 – if clicked, Creatio will display the “Why is the result "Not interested"?” response form. Enter the reason in the form. After you save the corresponding record, Creatio will set its status to “Not interested” in the
 
 Recommended product status
 
 lookup. The reason will be available in the
 
 Result description
 
 column of the lookup. This recommendation will no longer be available on the product selection page.




