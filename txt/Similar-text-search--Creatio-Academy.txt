


 In Creatio, you can configure and train recommendation prediction models to create lists of similar records based on the unstructured text data analysis. For example, you can set up the automatic knowledge base article selection, automatic solution search, and more.
 [Similar case search](/docs/8-0/user/service_tools/service_cases/case_processing/search_for_similar_cases_shortcut/search_for_similar_cases) 
 based on this prediction model is available out-of-the-box.
 



 This recommendation prediction model training method known as content-based filtering. The method evaluates the text similarity using the content traits of specific objects, for example, text data. Creatio aggregates and ranks the prediction subject and object text parameters to generate lists of similar records, such as similar cases.
 





 Note.
 
 Read more about ML models and their business use in the
 [AI tools](https://academy.creatio.com/online-courses/node/artificial-intelligence-and-machine-learning-creatio/why-use-artificial-intelligence-and-machine-learning-technology) 
 e-learning course.
 




 To generate a list of similar objects:
 


1. Set up and train the similar text search model.
2. Set up a
 [business process](https://academy.creatio.com/documents?product=administration&ver=7&id=1950) 
 with the
 
 Data prediction
 
 element.
 





 Attention.
 
 Using predictive analysis in Creatio on-site requires additional preliminary setup. Read more:
 [Machine Learning service](https://academy.creatio.com/documents?product=administration&ver=7&id=1935) 
 .





 1. Add a new recommendation prediction model
------------------------------------------------





 Example.
 
 Set up a search for similar problems by subject and description in the
 
 Problems
 
 section. Users will be able to link them to the relevant problem.
   

 To do so, set up and train the similar text search model.
 




 To set up the similar text search model:
 


1. Open the
 
 ML models
 
 section in the
 
 Studio
 
 workplace.
2. Click
 
 New
 
 →
 
 Text similarity
 
 .
3. Fill out the ML mode creation mini page (Fig. 1):
	1. Name
	 
	 – the name of the prediction model. The name helps to identify the model in the
	 
	 ML models
	 
	 section list and select it when configuring the
	 
	 Data prediction
	 
	 business process element.
	2. Type
	 
	 – the ML model type. For example, “Text similarity.” Creatio populates the field automatically when you select the model in the previous step.
	3. Search for similar among (Object)
	 
	 – Creatio will search for similar texts within this object. For example, “Case.”
	4. Search for similar to (Subject)
	 
	 – Creatio will compare the records with this object. For example, select the “Problem” object to find cases related to the same issue.
	 
	
	
	
	
	
	
	
	
	 Fig. 1 The similar text search model mini page
	 
	
	
	![similar_text_model_minicard.png](/docs/sites/en/files/images/NoCode_Customization/set_similar_text_model/similar_text_model_minicard.png)
4. Click
 
 Next
 
 to save the mini page and open the similar text search model setup page.



 2. Set up the model parameters
--------------------------------



 After you fill out the required model fields, specify the parameters:
 


1. Which records should be included in the training dataset?
 
 – set up a filter Creatio will use to select the training records. For example, narrow down the training data range to texts in closed cases only. To do this, configure the following filter: “State = Closed”.
 



 You do not need to specify the filter conditions. Creatio will use all available records for training by default.
 





 Note.
 
 You can already save the model and start training it by clicking the
 
 Train model
 
 button at this stage. You will see the training results in the
 
 Expected accuracy
 
 field. To save the prediction results, fill out the
 
 Setting up saving prediction results
 
 detail.
2. Which columns does the predicted value depend on?
 
 – select “Object's columns” or “Linked columns” and add columns whose data will be searched. For example, select the
 
 Description
 
 and
 
 Subject
 
 columns. You can only select text fields.
3. Search similar values by these columns
 
 – select “Object's columns” or “Linked columns” and add columns required to search for similar data. For example, select the
 
 Resolution
 
 ,
 
 Subject
 
 , and
 
 Description
 
 fields. You can only select text fields.
4. Setting up saving prediction results
 
 – specify where Creatio will store the prediction results. You can save the prediction to any Creatio object that has the following required fields:
 
 Similar to (Subject)
 
 ,
 
 Similar object
 
 (“Lookup” type), and
 
 Probability
 
 (“Decimal” type) For example, you can add the
 
 Similar cases prediction
 
 detail on the problem page. Read more:
 [Create new detail](https://academy.creatio.com/documents?product=administration&ver=7&id=1403) 
 .
 


 If you select this detail as a prediction object, Creatio will select the columns of a suitable type automatically. If there is more than one such column, Creatio will automatically select the first column. You will be able to select a different column from the dropdown. If the object has no such columns, Creatio will not populate the field. We recommend checking the selected values before saving the model.
	1. Object
	 
	 – specify the object that will store similar records. It is usually a detail. Note that you can only specify an existing Creatio object. For example, specify the
	 
	 Similar cases prediction
	 
	 detail. When you select an object, the
	 
	 Similar to (Subject)
	 
	 and
	 
	 Similar object
	 
	 fields become required.
	2. Similar to (Subject)
	 
	 – determines the ML model object. For example, similar cases. Creatio automatically populates the field with the value of the object column specified in the previous step. For example, “Similar case.” If necessary, you can change the value by selecting another column of the appropriate type from the dropdown. The field is required.
	3. Similar object
	 
	 – determines the ML model subject. For example, the problem for which the search for similar cases is run. Creatio automatically populates the field with the value of the object column specified in the previous step. For example, “Problem.” If necessary, you can change the value by selecting another column of the appropriate type from the dropdown. The field is required.
	4. Probability
	 
	 – ranks the records. For example, the higher the column value is, the higher is the text similarity. Creatio automatically populates the field with the value of the object column specified in the previous step. For example, “Score.” If necessary, you can change the value by selecting another column of the appropriate type from the dropdown. The field is required.
	5. ML model
	 
	 – specifies the name of the ML model used for the prediction. In this example, specify the text similarity model name. Creatio automatically populates the field with the value of the object column specified in the previous step. For example, “ML model.” If necessary, you can change the value by selecting another column of the appropriate type from the dropdown. We recommend filling out this field if you use several prediction models.
	6. Prediction date
	 
	 – specifies when the prediction was made. Creatio automatically populates the field with the value of the object column specified in the previous step. For example, “Prediction date.” If necessary, you can change the value by selecting another column of the appropriate type from the dropdown. (Fig. 2).
	 
	
	
	
	
	 Fig. 2 The similar text search model parameters
	 
	
	
	![similar_text_model_additional_parametres.png](/docs/sites/en/files/images/NoCode_Customization/set_similar_text_model/similar_text_model_additional_parametres.png)
5. Automatic model training settings
 
 – toggle the switch and set the parameters for automatic model retraining with updated historical data.
 


	1. Specify the interval between model training sessions in the
	 
	 Retrain, days
	 
	 field. After the specified number of days, Creatio will retrain the model based on historical records that match the filter. The first model training starts when you click the
	 
	 Train model
	 
	 button. If you would rather not retrain the model, leave the field blank or enter “0.”
	2. Specify the lowest prediction model accuracy threshold in the
	 
	 Quality metric lower limit
	 
	 field. When you train the model for the first time, this threshold will determine the lowest possible quality the model needs to reach before Creatio can use it. If the model quality drops below this limit, the model is deemed unusable. We recommend setting the quality metric lower limit to at least 0.50. The machine learning model accuracy score ranges from 0.00 to 1.00 (higher is better). Creatio calculates the machine learning model accuracy by dividing the number of successful predictions by the total number of predictions. Use the
	 [Google documentation](https://developers.google.com/machine-learning/crash-course/classification/accuracy) 
	 to learn more about how the prediction accuracy score is calculated.
6. To enable daily prediction result updates for the selected records during the minimum load period, toggle the switch in the
 
 Setting up background update of prediction results
 
 field group and set the filter conditions.



 3. Add the advanced settings
------------------------------



 Click the
 
 Advanced settings
 
 tab if you need to specify additional prediction model parameters. Fill out the fields similarly to the
 [lookup prediction model](/docs/7-17/user/customization_tools/ai_tools/lookup_field/lookup_value_prediction_model#title-166-12) 
 settings. Additionally, check the auto-populated value in the field specific to this ML model.
 
 Lower score threshold
 
 – the lowest similarity score at which a record can be listed as a possible match (Fig. 5).
 




 Fig. 3 The advanced parameters of the similar text search model
 


![similar_model_advanced_parametres.png](/docs/sites/en/files/images/NoCode_Customization/set_similar_text_model/similar_model_advanced_parametres.png)




 Prediction result
-------------------



 This will add a new model to Creatio. You will be able to use the model to run processes that search for similar Creatio objects by unstructured text data.
 



 Read more:
 [Configure a prediction business process](https://academy.creatio.com/documents?product=base&ver=7&id=1950) 
 .
 



 For example, the similar text search model will analyze the text data of the
 
 Case
 
 object, compare it with the text data of the
 
 Problem
 
 subject, and then generate a list of similar records. The training record selection will be restricted to the closed cases. The model will rank the list of similar cases based on the similarity score.
 



 As a result, Creatio will display similar cases on the
 
 Similar cases prediction
 
 detail of the problem page (Fig. 4).
 




 Fig. 4 A list of similar cases
 


![similar_text_model_look_like_cases.png](/docs/sites/en/files/images/NoCode_Customization/set_similar_text_model/similar_text_model_look_like_cases.png)





