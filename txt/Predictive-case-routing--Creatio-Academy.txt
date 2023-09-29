


 Predictive case routing in the
 
 Cases
 
 section is an AI tool that helps saving operators’ time at the initial case processing and assigning the corresponding support team. The
 **Service** 
 and
 **Assignee group** 
 field prediction is performed in the background mode upon case registration based on an email.
 





 Note.
 
 You can also enable the case priority prediction. To do this, activate the corresponding model in the
 
 ML models
 
 section.
 




 To view the prediction:
 



 Open the case page and click the button next to the necessary field, for example,
 
 Assignee group
 
 (
 [Fig. 1](#XREF_79324_194)
 ). The predicted value is saved in the field only after you save the case page.
 





 Fig. 1
 

 Certain prediction on a case page
 

![scr_chapter_predicting_watch_predicting_results_case.png](/guides/sites/en/files/documentation/user/en/cases_service/BPMonlineHelp/service_cases_predictive_routing/scr_chapter_predicting_watch_predicting_results_case.png)


#### 
 Train the assignee group prediction model



 The machine-learning model for predicting the assignee group is activated by default, but requires training. The training for the machine-learning model is launched automatically. If you reach the quality metric low limit (50%), the model instance will be saved in Creatio and will begin working. If the prediction accuracy after model training is lower than 50%, the model instance is sent for retraining.
 



 In this case, the assignee group field value is not predicted. The machine learning model training process takes 30 days in the base configuration of Creatio. You can set up a different retrain period in the
 
 Machine learning models
 
 section.
 


#### 
 Predict the assignee group of a case



 The machine learning model checks emails and cases to collect frequently used words and phrases in the email body. A collection of words and phrases that are most frequently used for case resolutions and replies via email by each assignee group is formed for each trained machine-learning model instance. No confidential data (email addresses, email bodies, contact and account data, case resolution history, etc.) is stored in this collection. When Creatio compares the data from a new case to the collection of words and phrases, a prediction of the
 
 Assignee group
 
 field data takes into account all possible probabilities. If Creatio generates a definite prediction, the
 
 Assignee group
 
 field will be populated automatically.
 



 The prediction accuracy depends on the amount of collected data, used for machine learning model training. The use of constantly updated historical data in the training enables you to achieve the prediction accuracy of more than 90%.
 





 Note.
 
 Predictive analytics in Creatio enables you to train models on collections containing up to 75,000 historical records. If a collection contains more than 75,000 records, the service will randomly select 75,000 records from the collection to train the machine-learning model.
   

 We recommend to use at least 20,000 historical records to achieve the quality metric lower limit of 50%
 





