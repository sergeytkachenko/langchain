


 This article covers the basics of working with predictive data analysis in Creatio.
 



 The
 **predictive analysis** 
 estimates the likelihood of specific events based on large volumes of historic data and current facts. It increases the speed and accuracy of business decisions, relieves the users from routine tasks, and improves overall efficiency and performance.
 



 Predictive analysis in Creatio is implemented via a set of algorithms – machine learning models. Create, train, and use your custom machine learning models to predict values for any business object in the
 
 ML models
 
 section.
 





 Attention.
 
 Using predictive analysis in Creatio on-site requires additional preliminary setup. Learn more:
 [Machine learning service](/docs/node/257) 
 .
 




 Creatio machine learning model types
--------------------------------------



 Creatio includes the following ML model types:
 


* **Lookup value prediction** 
 (classification) – populates lookup fields based on the analysis of existing data and trends. For example, predict the most likely account category.
* **Numeric prediction** 
 (regression) – populates numeric fields. For example, predict the lead budget based on the customer need type and the customer's company size, country, and industry.
* **Predictive scoring** 
 – grades Creatio records based on historical and current data. For example, rate the quality of your leads based on their budget and successful hand-off to sales.
* **Recommendation** 
 – predicts which Creatio records will interest customers the most. For example, find out which products or services you should recommend to a customer based on their previous activity. Alternatively, recommend any other Creatio objects to any Creatio subjects.
* **Similar text search** 
 – creates lists of similar records based on the analysis of unstructured text data. For example, find relevant knowledge base articles or replies based on case text.



 Find the available AI solutions for Creatio products on Fig. 1.
 





 Fig. 1
 
 The available AI solutions
 

![chapter_prediction_ai_solutions.png](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_predicting/chapter_prediction_ai_solutions.png)



 The ML model selection flowchart
----------------------------------



 Use the flowchart below (Fig. 2) to select a prediction model type.
 





 Fig. 2
 
 Selection flowchart for the model type
 

![chapter_predicting_choosing_model.png](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_predicting/chapter_predicting_choosing_model.png)



 Prediction setup procedure
----------------------------



 Create a prediction in several steps:
 


1. **Train a prediction model** 
 . Learn more about this step in separate articles about setting up the individual ML model types.
2. **Train the prediction model** 
 . Learn more:
 [Train prediction models](/docs/8-0/user/customization_tools/ai_tools/ml_training/train_prediction_models) 
 .
3. **Set up and run a business process** 
 with the
 
 Predict data
 
 element (Fig. 3). This is an optional step. If you set up batch prediction on step 1, the model will update predictions for the selected records daily during the maintenance period without the use of business processes. Set up a business process with the
 
 Predict data
 
 element to gain complete control over what records to predict and when. Learn more:
 [Implement prediction models](/docs/8-0/user/customization_tools/ai_tools/set_up_a_process/implement_prediction_models) 
 .





 Fig. 3
 
 The
 
 Predict data
 
 element in a business process
 

![chapter_predicting_business_process_account_category.png](/sites/default/files/documents/docs_en/product/bpm'online administration/administration/7.16.0/BPMonlineHelp/chapter_predicting/chapter_predicting_business_process_account_category.png)





 Note.
 
 We do not recommend running predictive scoring for a large number of records simultaneously. The best solution is running the operation for each separate record, e. g., when adding or modifying the record. We recommend launching the batch prediction when the use of Creatio is at its minimum, such as at night.
 





