from autogluon.tabular import TabularDataset, TabularPredictor

train_data = TabularDataset('/content/COPD_NLP/NLP-LOS.csv')
subsample_size = 2200  # subsample subset of data for faster demo, try setting this to much larger values
train_data = train_data.sample(n=subsample_size, random_state=0)
train_data.head()

time_limit = None
label='label'
save_path = 'agModels-predictClass'
predictor = TabularPredictor(verbosity = 4,eval_metric = 'acc',label=label, path=save_path).fit(train_data,
                                            hyperparameters='multimodal',
                                            num_stack_levels=1,
                                            num_bag_folds=5,
                                            time_limit=time_limit,
                                            presets='best_quality',
                                            ag_args_fit={'num_gpus': 1})

test_data = TabularDataset('/content/COPD_NLP/NLP-LOS-TEST.csv')
y_test = test_data[label]  # values to predict
test_data_nolab = test_data.drop(columns=[label])  # delete label column to prove we're not cheating
test_data_nolab.head()

results = predictor.fit_summary()

predictor.leaderboard(test_data,silent=True)

predictor = TabularPredictor.load(save_path)  # unnecessary, just demonstrates how to load previously-trained predictor from file
y_pred_proba = predictor.predict_proba(test_data)
y_pred = predictor.predict(test_data_nolab)
print("Predictions:  \n", y_pred)
perf = predictor.evaluate_predictions(y_true=y_test, y_pred=y_pred,detailed_report=True,auxiliary_metrics=True)

datapoint = test_data_nolab.iloc[[1]]
print(datapoint)
predictor.predict_proba(datapoint)