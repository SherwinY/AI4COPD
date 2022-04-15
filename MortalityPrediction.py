from autogluon.tabular import TabularDataset, TabularPredictor

train_data = TabularDataset('/content/COPD_NLP/qiancaiyang-mult-train.csv')
subsample_size = 400  # subsample subset of data for faster demo, try setting this to much larger values
train_data = train_data.sample(n=subsample_size, random_state=0)
train_data.head()

time_limit = None
label='label'
save_path = 'agModels-predictClass'
predictor = TabularPredictor(eval_metric = 'acc',label=label, path=save_path).fit(train_data,
                                            hyperparameters='multimodal',
                                            num_stack_levels=1,
                                            num_bag_folds=5,
                                            time_limit=time_limit,
                                            presets='best_quality'
                                            )


test_data = TabularDataset('/content/qiancaiyang-mult-test.csv')
y_test = test_data[label]  # values to predict
test_data_nolab = test_data.drop(columns=[label])  # delete label column to prove we're not cheating
test_data_nolab.head()

predictor.feature_importance(test_data)

predictor.leaderboard(test_data,extra_metrics=['accuracy', 'f1', 'roc_auc'],silent=True)

predictor = TabularPredictor.load(save_path)
y_pred = predictor.predict(test_data_nolab)
print("Predictions:  \n", y_pred)
perf = predictor.evaluate_predictions(y_true=y_test, y_pred=y_pred, auxiliary_metrics=True)

test_data_nolabel = test_data.drop(columns=[label])
datapoint = test_data_nolabel.iloc[[1]]
predictor.predict_proba(datapoint)

