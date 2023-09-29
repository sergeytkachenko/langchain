


 Creatio provides tools to create and set up machine learning models that predict record scoring in any Creatio section. Predictive scoring estimates the probability of an event. For example, you can create a model that rates the lead conversion probability based on the budget and the history of successful hand-off to sales.
 [Predictive lead scoring](/docs/8-0/user/marketing_tools/leads/lead_scoring/predictive_scoring_of_leads) 
 based on this prediction model is available out of the box. This model is implemented via developer queries and tools. This article demonstrates how you can configure this prediction model without coding.
 



 Creatio calculates the predictive score using a scale from 1 to 100 points. You can display the calculated value on the record page as a numeric field or a chart. Learn more:
 [Add analytics to a record page](/docs/8-0/user/customization_tools/analytics/add_page_analytics/add_analytics_to_a_record_page) 
 .
 





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
 
 Set up the lead conversion probability prediction in the
 
 Leads
 
 section based on the lead stage, budget, and the annual revenue.
 



 To do this, set up and train a predictive scoring model.
 




 To create a predictive scoring model:
 


1. Open the
 
 ML models
 
 section in the
 
 Studio
 
 workplace.
2. Click
 
 New
 
 →
 
 Predictive scoring
 
 .
3. Fill out the ML model creation mini page (Fig. 1):
	1. Name
	 
	 – the name of the prediction model. The name helps to identify the model in the
	 
	 ML models
	 
	 section list and select it when configuring the
	 
	 Predict data
	 
	 business process element.
	2. Type
	 
	 – the ML model type. For example, “Predictive scoring.” Creatio populates the field automatically when you select the model in the previous step.
	3. Object
	 
	 – the prediction model will predict the records of this object (a section, a detail, or a lookup). For example, “Lead.”


 Fig. 1
 
 The predictive scoring model mini page
 

![chapter_predicting_scoring_model_minicard.png](/docs/sites/en/files/images/NoCode_Customization/set_predicting_scoring_model/chapter_predicting_scoring_model_minicard.png)
4. Click
 
 Next
 
 to save the mini page and open the predictive scoring model setup page.



 2. Set up the model parameters
--------------------------------



 After you fill out the required model fields, specify the parameters:
 


1. What records to be considered as successful?
 
 – set up a filter Creatio will use to determine the most “successful” records, i. e., the records that should have the highest score. In this example, a lead is considered successful if its budget is higher than $50,000 and if it was successfully handed off to sales (Fig. 3). To do this, configure the following filters: “Budget > 50,000.00” and “Stage = Handoff to sales.”
2. Which columns does the predicted value depend on?
 
 – select the “Object column” or “Linked column” to add columns that Creatio will analyze to predict the lead quality. For example, if the lead quality is based on the budget, annual revenue, and its stage in the pipeline, add the
 
 Budget
 
 ,
 
 Annual revenue
 
 , and
 
 Lead stage
 
 object columns here. Creatio will analyze the historic values of these columns, compare the columns to the most successful records, and predict the score.
3. Which records should be included in the training dataset?
 
 – specify the filter Creatio will use to select the training records. Creatio will use these records to determine the correlation between the predicted lead quality and the columns used for prediction. For example, select only the records with the lead budget. To do this, configure the following filter: “Budget is filled in.”
 



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
 
 – specify where Creatio will store the prediction results. Usually, Creatio saves the results to the column whose value was predicted. If you would rather save the prediction result to another column, specify it in this field. For example, add a
 
 Predictive budget
 
 column to the lead page and save the results there. You can add a special column that will store the prediction result in the Section wizard. Learn more:
 [Set up page fields](/docs/8-0/user/customization_tools/ui_and_business_logic_customization/page_layout/fields/set_up_page_fields) 
 .
5. Automatic model training settings
 
 – turn on the switch and set the parameters for automatic model retraining with updated historical data.
 


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
 
 field group to enable daily prediction result updates for all records during the minimum load period (Fig. 2). If you need to update only the specific records, set up the filter conditions.





 Note.
 
 Specify the period when the batch prediction will take place in the
 
 Maintenance periods
 
[lookup](/docs/8-0/user/setup_and_administration/system_settings_and_lookups/create_a_lookup/create_new_lookups) 
 .
 





 Fig. 2 The predictive scoring model parameters
 

![chapter_predicting_predictive_score_additional_parameters.png](/docs/sites/en/files/images/NoCode_Customization/set_predicting_scoring_model/chapter_predicting_predictive_score_additional_parameters.png)



 3. Add the advanced settings
------------------------------



 Click the
 
 Advanced settings
 
 tab if you want to specify additional prediction model parameters. Fill out the fields similarly to the
 [lookup value prediction model](/docs/8-0/user/customization_tools/ai_tools/lookup_field/lookup_value_prediction_model#title-2056-12) 
 settings (Fig. 3) and click
 
 Save
 
 . To start training a predictive scoring model, click
 
 Train model
 
 .
 




 Fig. 3 The advanced settings of the predictive scoring model
 

![chapter_predicting_predictive_score_model_advanced_parameters.png](/docs/sites/en/files/images/NoCode_Customization/set_predicting_scoring_model/chapter_predicting_predictive_score_model_advanced_parameters.png)



 Prediction results
--------------------



 This will add a new ML model to Creatio.
 



 If you set up batch prediction, the model will update predictions for the selected records daily during the maintenance period without the use of business processes.
 



 Set up a business process with the
 
 Predict data
 
 element to gain complete control over what records to predict and when. If a business process triggers the model, it will predict the score for the needed records. Learn more:
 [Implement prediction models](/docs/8-0/user/customization_tools/ai_tools/set_up_a_process/implement_prediction_models) 
 .
 



 The lead score prediction model will analyze the values in the
 
 Budget
 
 ,
 
 Annual revenue
 
 , and
 
 Lead stage
 
 columns of leads with the populated
 
 Budget
 
 field and compare the values to all the leads that have been handed off to sales. The more data the model analyzes, the higher the quality of the metric.
 



 Once the quality is high enough, the section will provide the predicted lead rating based on the values in the
 
 Budget
 
 ,
 
 Annual revenue
 
 , and
 
 Lead stage
 
 columns.
 




