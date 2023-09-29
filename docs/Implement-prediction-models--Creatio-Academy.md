


 Once your prediction model is created, you can set up the actual data prediction in a business process using the
 
 Predict data
 
 process element. This will give you complete control over what records are predicted and when.
 



 Implement the lookup value prediction
---------------------------------------



 Set up a prediction of the account category whenever a new account with an empty
 
 Category
 
 field is saved (Fig. 1).
 



 In this example, we will be using the
 [account category prediction model](/docs/8-0/user/customization_tools/ai_tools/lookup_field/lookup_value_prediction_model) 
 created earlier.
 





 Fig. 1
 
 An ML model implementation process
 

![chapter_predicting_business_process_account_category.png](/guides/sites/en/files/documentation/user/en/ai_tools/BPMonlineHelp/implement_prediction_model/chapter_predicting_business_process_account_category.png)



 To implement this:
 


1. Create a new business process from the process library and add the
 
 Signal
 
 start event to the diagram. The start event should be triggered whenever a new record is added to the
 
 Accounts
 
 section. Specify the signal element properties (Fig. 2):
 





 Fig. 2
 
 The signal element properties
 

![chapter_predicting_predictive_signal_element_parameters.png](/guides/sites/en/files/documentation/user/en/ai_tools/BPMonlineHelp/implement_prediction_model/chapter_predicting_predictive_signal_element_parameters.png)


	1. Which type of signal is received?
	 
	 - “Object signal.”
	2. Object
	 
	 – “Account.”
	3. Which event should trigger the signal?
	 
	 – “Record added.”
	4. The added record must meet filter conditions
	 
	 – “Category is not filled in.”
	5. Run following elements in the background
	 
	 – selected. This way, the process will run all elements from the
	 
	 System actions
	 
	 group in the background and will not display the loading mask.
2. Select the
 
 Predict data
 
 element in the
 
 System actions
 
 group and add it to the process diagram. Set up the element properties (Fig. 3):
 





 Fig. 3
 
 The
 
 Predict data
 
 element setup area
 

![chapter_predicting_predict_data_element_parameters.png](/guides/sites/en/files/documentation/user/en/ai_tools/BPMonlineHelp/implement_prediction_model/chapter_predicting_predict_data_element_parameters.png)


	1. Select the prediction model in the
	 
	 Machine learning model
	 
	 list. For example, to predict the category of an account, select the “Account category” model created earlier. Learn more:
	 [Lookup value prediction model](/docs/8-0/user/customization_tools/ai_tools/lookup_field/lookup_value_prediction_model) 
	 .
	 
	
	
	 Note.
	 
	 Train prediction models before using them in business processes. Untrained models are not available in the
	 
	 Machine learning model
	 
	 field of the
	 
	 Predict data
	 
	 element. Learn more:
	 [Train prediction models](/docs/8-0/user/customization_tools/ai_tools/ml_training/train_prediction_models) 
	 .
	2. What type of prediction to use?
	 
	 – “Predicting for one record.”
	3. Click the
	 ![btn_process_element_settings_lookup.png](/guides/sites/en/files/documentation/user/en/ai_tools/BPMonlineHelp/implement_prediction_model/btn_process_element_settings_lookup.png)
	 button and select
	 
	 Process parameter
	 
	 in the
	 
	 What record to perform prediction on?
	 
	 field. Go to the
	 
	 Process elements
	 
	 tab in the opened window and select the signal created in the previous step, as well as the
	 
	 Unique identifier of record
	 
	 parameter.
3. Save the process.



 As a result, whenever the
 
 Predict data
 
 element is triggered during a business process, it will use the selected ML model to predict the data of the specified record. In this example, the model will predict and populate the
 
 Category
 
 field value each time a new record is saved in the
 
 Accounts
 
 section. The prediction will be based on the values specified by users when filling out the
 
 Category
 
 field of historical records.
 



 Implement the recommendation prediction
-----------------------------------------



 You can set up the product recommendation prediction for certain product types to hold an advertising campaign (Fig. 4). For example, run a business process manually to recommend five products of “Motherboards” type to all contacts of a “Customer” type.
 



 In this example, we will be using the
 [product recommendation model](/docs/8-0/user/customization_tools/ai_tools/recommendations/recommendation_prediction) 
 created earlier.
 





 Fig. 4
 
 A business process with the recommendation prediction
 

![chapter_predicting_business_process_reccomend.png](/guides/sites/en/files/documentation/user/en/ai_tools/BPMonlineHelp/implement_prediction_model/chapter_predicting_business_process_reccomend.png)



 To implement this:
 


1. Create a new business process from the process library. Use the
 
 Simple
 
 start event to start the business process manually. The event is added to the diagram by default.
2. Select the
 
 Predict data
 
 element in the
 
 System actions
 
 group and add it to the process diagram. Set up the element properties (Fig. 5):
 





 Fig. 5
 
 The
 
 Predict data
 
 element properties
 

![chapter_predicting_predict_data_element_bp_parameters.png](/guides/sites/en/files/documentation/user/en/ai_tools/BPMonlineHelp/implement_prediction_model/chapter_predicting_predict_data_element_bp_parameters.png)


	1. Machine learning model
	 
	 – specify the name of the recommendation model.
	2. Recommended to (Subject)
	 
	 – specify the filter. Select all or specific contacts that will receive recommendations. The filter must be specified to validate the element. For this example, select the contacts of the “Customer” type.
	3. Recommended object
	 
	 – specify the filter if you need to restrict the recommendation selection to solve a specific business problem. For example, you can recommend only products of a certain type to your customers. In this example, these are motherboards.
	4. Number of recommended items
	 
	 – specify how many records the recommendation list should contain. For example, restrict the number of recommendations to five.
	5. Receive recommendations for an item previously interacted
	 
	 – select the checkbox to include only the products with which the customers interacted into the recommendations.
3. Add the terminate event and save the process.



 As a result, whenever the
 
 Predict data
 
 element is triggered during a business process, it will use the specified ML model to generate a list of recommendations. In this example, the selection of training records will be restricted to the “Motherboards” product type. The list of recommendations consisting of five records will be generated for all contacts of the “Customer” type.
 




