


 Creatio provides tools to create and set up machine learning models that predict the numeric field values. The predictions are based on the data available in the record and the previously processed records. For example, you can create a model that will predict the lead budget based on the customer need type and the customer's company size, country, and industry.
 





 Note.
 
 Learn more about ML models and their business use:
 [Artificial intelligence and machine learning in Creatio](https://academy.creatio.com/node/620681/takecourse) 
 .
 






 Attention.
 
 Using predictive analysis in Creatio on-site requires additional preliminary setup. Learn more:
 [Machine learning service](/docs/node/257) 
 .
 




 1. Add a new recommendation prediction model
----------------------------------------------





 Example.
 
 Create a model that will predict the lead budget based on the customer need type and the customer's company size, country, and industry.
 



 To do so, set up and train a numeric field prediction model.
 




 To create a numeric value prediction model:
 


1. Open the
 
 ML models
 
 section in the
 
 Studio
 
 workplace.
2. Click
 
 New
 
 →
 
 Numeric prediction
 
 .
3. Fill out the ML model creation mini page (Fig. 1):
	1. Name
	 
	 – the name of the prediction model. The name helps to identify the model in the
	 
	 ML models
	 
	 section list and select it when configuring the
	 
	 Predict data
	 
	 business process element.
	2. Type
	 
	 – the ML model type. For example, “Numeric prediction.” Creatio populates the field automatically when you select the model in the previous step.
	3. Object
	 
	 – the prediction model will predict the records of this object (a section, a detail, or a lookup). For example, “Lead.”

 Fig. 1 The numeric value prediction model mini page
 

![chapter_predicting_numeric_value_model_minicard.png](/docs/sites/en/files/images/NoCode_Customization/set_numeric_prediction_model/chapter_predicting_numeric_value_model_minicard.png)
4. Click
 
 Next
 
 to save the mini page and open the numeric prediction model setup page.



 2. Set up the model parameters
--------------------------------



 After you fill out the required model fields, specify the parameters:
 


1. What value should be predicted?
 
 – select the field to be predicted. For example, to predict the lead budget, select the
 
 Budget
 
 field from the list. The list contains all the numeric fields of the selected object.
2. Which columns does the predicted value depend on?
 
 – select the “Object column” or “Linked column” to add columns that determine the behavior algorithms connected to the predicted field. For example, if a lead budget depends on the customer need, the number of employees, the country, and the industry – add the
 
 Customer need
 
 ,
 
 No. of employees
 
 ,
 
 Country
 
 , and
 
 Industry
 
 object columns. Creatio will analyze the historic values of these columns and how the values correlate with the relevant values in the
 
 Budget
 
 field.
3. Which records should be included in the training dataset?
 
 – set up a filter Creatio will use to select the training records. For example, select only the records with the lead budget. To do this, configure the following filter: “Budget is filled in.”
 



 You do not have to specify the filter conditions. Creatio will use all available records for training by default.
 





 Note.
 
 You can already save the model and start training it by clicking the
 
 Train model
 
 button at this stage. You will see the training results in the
 
 Expected accuracy
 
 field. Fill out the
 
 What column to use for saving prediction result?
 
 field to save the prediction results.
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
	 
	 field. When you train the model for the first time, this threshold will determine the minimum acceptable quality that the model needs to reach before Creatio can use it. If the model quality drops below this limit, the model is deemed unusable. We recommend setting the quality metric lower limit to at least 0.50. The machine learning model accuracy score ranges from 0.00 to 1.00 (higher is better). Creatio calculates the machine learning model accuracy by dividing the number of successful predictions by the total number of predictions. Learn more about how the prediction accuracy score is calculated in the
	 [Google documentation](https://developers.google.com/machine-learning/crash-course/classification/accuracy) 
	 .
6. Turn on the switch in the
 
 Setting up background update of prediction results
 
 field group to enable daily prediction result updates for all records during the minimum load period (Fig. 2). If you need to update only the specific records, set up the filter conditions.





 Note.
 
 Specify the period when the batch prediction will take place in the
 
 Maintenance periods
 
[lookup](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/create_a_lookup/create_new_lookups) 
 .
 





 Fig. 2 The ML numeric prediction model parameters
 

![chapter_predicting_numeric_value_model_additional_parameters.png](/docs/sites/en/files/images/NoCode_Customization/set_numeric_prediction_model/chapter_predicting_numeric_value_model_additional_parameters.png)



 3. Add the advanced settings
------------------------------



 Click the
 
 Advanced settings
 
 tab if you want to specify additional prediction model parameters. Fill out the fields similarly to the
 [lookup value prediction model](/docs/8-0/user/customization_tools/ai_tools/lookup_field/lookup_value_prediction_model#title-2056-12) 
 settings (Fig. 3) and click
 
 Save
 
 . To start training a numeric prediction model, click
 
 Train model
 
 .
 




 Fig. 3 The advanced ML numeric prediction model parameters
 

![chapter_predicting_numeric_value_model_advanced_parameters.png](/docs/sites/en/files/images/NoCode_Customization/set_numeric_prediction_model/chapter_predicting_numeric_value_model_advanced_parameters.png)



 Prediction results
--------------------



 This will add a new ML model to Creatio.
 



 If you set up batch prediction, the model will update predictions for the selected records daily during the maintenance period without the use of business processes.
 



 Set up a business process with the
 
 Predict data
 
 element to gain complete control over what records to predict and when. If a business process triggers the model, it will predict and populate the values for the needed records. Learn more:
 [Implement prediction models](/docs/8-0/user/customization_tools/ai_tools/set_up_a_process/implement_prediction_models) 
 .
 



 The lead budged prediction model will analyze the values in the
 
 Customer need
 
 ,
 
 No. of employees
 
 ,
 
 Country
 
 , and
 
 Industry
 
 fields of leads with the populated
 
 Budget
 
 field. The more data it analyzes, the higher the quality of the metric.
 



 Once the quality is high enough, the model will predict the lead budget based on the values in the
 
 Customer need
 
 ,
 
 No. of employees
 
 ,
 
 Country
 
 , and
 
 Industry
 
 columns.
 




