
# Imports

import pandas as pd
import numpy as np
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metrics.base_metric import generate_column_metrics
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset
from evidently.metrics import *
from evidently import ColumnMapping
from evidently.test_suite import TestSuite
from evidently.tests.base_test import generate_column_tests
from evidently.test_preset import DataStabilityTestPreset, NoTargetPerformanceTestPreset
from evidently.tests import *
import os



df = pd.read_csv(
    os.getcwd() + '\iris.csv', encoding='unicode_escape')
html_path = 'out.html'
path_to_new = r'C:\Users\INDHK6\Desktop\Model Monitoring on Edge\Demo v1\implementation_evidently\evid\dummyyy.csv'

dummy = pd.read_csv(path_to_new)



column_mapping = ColumnMapping()
column_mapping.target = "species"
column_mapping.numerical_features = [
    "sepal_length","sepal_width","petal_length","petal_width"]
# column_mapping.categorical_features = ['gender']
column_mapping.task = 'classification'
column_mapping.prediction = "prediction"
column_mapping.target_names = ["setosa","versicolour", "virginica"]


def get_report(current):
    report = Report(metrics=[
        DataDriftPreset(),
        TargetDriftPreset(),
        DatasetCorrelationsMetric()
    ])

    report.run(reference_data=df, current_data=current,
           column_mapping=column_mapping)
    
    # print(report.json())
    report.save_html(html_path)

if __name__ == "__main__":
    get_report(dummy)