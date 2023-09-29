


 Creatio provides tools to create and set up machine learning models that predict the lookup field values. The predictions are based on the data available in the record and the previously processed records For example, you can create a model that will predict the customer account category.
 [Case service agreement and assignee group prediction](/docs/8-0/user/service_tools/service_cases/case_processing/service_agreement_selection_shortcut/service_agreement_selection) 
 with such an ML model is available in Creatio out of the box.
 





 Note.
 
 Learn more about ML models and their business use:
 [Artificial intelligence and machine learning in Creatio](https://academy.creatio.com/node/620681/takecourse) 
 .
 






 Attention.
 
 Using predictive analysis in Creatio on-site requires additional preliminary setup. Learn more:
 [Machine learning service](/docs/node/257) 
 .
 




 1. Add a new model
--------------------





 Example.
 
 Set up a machine learning model that will predict account categories in the
 
 Accounts
 
 section based on the industry, annual revenue, and the number of employees.
 



 To do this, set up and train a lookup prediction model.
 




 To add a new ML lookup prediction model:
 


1. Open the
 
 ML models
 
 section in the
 
 Studio
 
 workplace.
2. Click
 
 New
 
 →
 
 Lookup prediction
 
 .
3. Fill out the ML model creation mini page (Fig. 1):
	1. Name
	 
	 – the name of the prediction model. The name helps to identify the model in the
	 
	 ML models
	 
	 section list and select it when configuring the
	 
	 Predict data
	 
	 business process element.
	2. Type
	 
	 – the ML model type. For example, “Lookup prediction.” Creatio populates the field automatically when you select the model in the previous step.
	3. Object
	 
	 – the prediction model will predict the records of this object (a section, a detail, or a lookup). For example, “Account.”


 Fig. 1
 
 The lookup value prediction model mini page
 

![chapter_predicting_lookup_value_model_minicard.png](/docs/sites/en/files/images/Service_Tools/set_lookup_prediction_model/chapter_predicting_lookup_value_model_minicard.png)
4. Click
 
 Next
 
 to save the mini page and open the lookup prediction model setup page.



 2. Set up the model parameters
--------------------------------



 After you fill out the required model fields, specify the parameters:
 


1. What value should be predicted?
 
 – select the field to be predicted. For example, to predict the account category, select the
 
 Category
 
 field from the list. The list contains all lookup fields of the selected object. Creatio will display the prediction result as one of the
 
 Category
 
 lookup values.
2. Which columns does the predicted value depend on?
 
 – select the “Object column” or “Linked column” to add columns that determine the behavior algorithms connected to the predicted field. For example, if you normally determine an account's category based on the number of company employees, revenue, and the account's industry, add the
 
 No of employees
 
 ,
 
 Annual revenue
 
 , and
 
 Industry
 
 object columns here. Creatio will analyze the historic values of these columns and how the values correlate with the relevant values in the
 
 Category
 
 column.
3. Which records should be included in the training dataset?
 
 – set up a filter Creatio will use to select the training records. For example, narrow down the training data range to only the records that have the account category. To do this, configure the following filter: “Category is filled in.”
   

  

 You do not have to specify the filter conditions. Creatio will use all available records for training by default.
 





 Note.
 
 You can already save the model and start training it by clicking the
 
 Train model
 
 button at this stage. You will see the training results in the
 
 Expected accuracy
 
 field. Fill out the
 
 What column to use for saving prediction result?
 
 Field to save the prediction results.
4. What column to use for saving prediction result?
 
 – specify where Creatio will store the prediction results. Usually, Creatio saves the results to the column whose value was predicted. If you would rather Creatio did not modify the predicted column, select a different column here.
5. Automatic model training settings
 
 – toggle the switch and set the parameters for automatic model retraining with updated historical data.
 


	1. Specify the interval between model training sessions in the
	 
	 Retrain after, days
	 
	 field. After the specified number of days, Creatio will retrain the model based on historical records that match the filter. The first model training starts when you click the
	 
	 Train model
	 
	 button. If you would rather not retrain the model, leave the field blank or enter “0.”
	2. Specify the lowest prediction model accuracy threshold in the
	 
	 Quality metric lower limit
	 
	 field. When you train the model for the first time, this threshold will determine the minimum acceptable quality that the model needs to reach before Creatio can use it. If the model quality drops below the lower limit, the model is deemed unusable. We recommend setting the quality metric lower limit to at least 0.50. The machine learning model accuracy score ranges from 0.00 to 1.00 (higher is better). Creatio calculates the machine learning model accuracy by dividing the number of successful predictions by the total number of predictions. Learn more about how the prediction accuracy score is calculated in the
	 [Google documentation](https://developers.google.com/machine-learning/crash-course/classification/accuracy) 
	 .
6. Turn on the switch in the
 
 Setting up background update of prediction results
 
 field group to enable daily prediction result updates for the selected records during the minimum load period (Fig. 2). If you turn on the background updates without specifying the filter conditions, the model will update all records.





 Note.
 
 Specify the period when the batch prediction will take place in the
 
 Maintenance periods
 
[lookup](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/create_a_lookup/create_new_lookups) 
 .
 





 Fig. 2 The ML lookup prediction model parameters
 

![chapter_predicting_lookup_value_model_additional_parameters.png](/docs/sites/en/files/images/Service_Tools/set_lookup_prediction_model/chapter_predicting_lookup_value_model_additional_parameters.png)



 3. Add the advanced settings
------------------------------



 Click the
 
 Advanced settings
 
 tab if you need to specify additional prediction model parameters.
 


1. Set up a query that selects additional columns used for value prediction in the
 
 Advanced tools to add columns
 
 field group. Note that the query setup requires coding. Learn more:
 [Creating data queries for the machine learning model](/docs/8-0/developer/application_components/machine_learning/overview#title-1471-9/) 
 .
2. Creatio populates the values in the
 
 Advanced model parameters
 
 field group (Fig. 3) automatically. You can edit the values, if necessary.
 


	1. Minimum training record count
	 
	 – the minimum number of records needed to train a model.
	2. Maximum training record count
	 
	 – the maximum number of records needed to train a model.
	3. Predicted value selection method
	 
	 – can be “ML Engine Significance” or “Maximum probability.”
		* “
		 **ML Engine Significance** 
		 ” – default method. If selected, Creatio will determine the prediction quality based on the ML mechanism. If the prediction quality is sufficiently high, Creatio will save the predicted value to the relevant field.
		* “
		 **Maximum probability** 
		 ” – enables a custom predicted value selection method. If you select this option, a new field will appear:
		 
		
		
		
		
		 Lower limit of probability for predicted value selection
		 
		 – the minimum probability where the predicted value will still be saved automatically. If the predicted value is below this threshold, Creatio will not populate the field automatically. However, Creatio will display the prediction when you fill out the field manually.
	
	 Fig. 3 The advanced ML lookup prediction model parameters
	 
	
	![chapter_predicting_lookup_value_model_advanced_parameters.png](/docs/sites/en/files/images/Service_Tools/set_lookup_prediction_model/chapter_predicting_lookup_value_model_advanced_parameters.png)
3. Click
 
 Save
 
 . To start training a lookup prediction model, click
 
 Train model
 
 .



 Prediction results
--------------------



 This will add a new ML model to Creatio.
 



 If you set up batch prediction, the model will update predictions for the selected records daily during the maintenance period without the use of business processes.
 



 Set up a business process with the
 
 Predict data
 
 element to gain complete control over what records to predict and when. If a business process triggers the model, it will predict and populate the values for the needed records. Learn more:
 [Implement prediction models](/docs/8-0/user/customization_tools/ai_tools/set_up_a_process/implement_prediction_models) 
 .
 



 The account category prediction model will analyze the values in the
 
 No of employees
 
 ,
 
 Annual revenue
 
 , and
 
 Industry
 
 columns of accounts with the populated
 
 Category
 
 column. The more data it analyzes, the higher the quality of the metric.
 



 Once the quality is high enough, the model will predict the value in the
 
 Category
 
 field based on the values in the
 
 No of employees
 
 ,
 
 Annual revenue
 
 , and
 
 Industry
 
 fields. Creatio will automatically populate the lookup fields with predicted values, sorted by probability.
 



 Depending on the probability ratio, Creatio distinguishes among the following prediction types:
 


* certain prediction
* near-certain prediction
* weak prediction


### 
 Certain prediction



 A certain prediction is a prediction with an evident leader. In this case, Creatio automatically populates the field with the predicted value, and the
 ![btn_strong_prediction.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_page/btn_strong_prediction.png)
 button appears next to it. Save the page if the field is populated correctly.
 



 Click the
 ![btn_strong_prediction00001.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_page/btn_strong_prediction00001.png)
 button to display all possible predictions and their probabilities with the most probable item highlighted.
 



 If you modify the field, the
 ![btn_middle_prediction.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_page/btn_middle_prediction.png)
 button will appear. Click the button to display all predictions.
 


### 
 Near certain prediction



 If there are multiple values with close probabilities, Creatio will not populate the field, and the
 ![btn_middle_prediction00002.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_page/btn_middle_prediction00002.png)
 button will appear next to it. Click the button to display the list of predictions and their probabilities.
 


### 
 Weak prediction



 A weak prediction occurs when Creatio cannot compare the historical data to the data used for analysis. Creatio does not populate the field with a weak prediction, and the
 ![btn_weak_prediction.png](/guides/sites/en/files/documentation/user/en/base/BPMonlineHelp/chapter_page/btn_weak_prediction.png)
 button appears next to it. Click the button to display the list of predictions and their probabilities.
 




