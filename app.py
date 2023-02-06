
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
from refresh import add_refresh
from database import ingest



df = pd.read_csv(
    os.getcwd() + '/iris.csv', encoding='unicode_escape')
html_path = '/var/temp/index.html'
path_to_new = "/var/temp/currentdata.csv"

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
           
    with open("json_file.json", 'w') as fp:
        fp.write(report.json())


    # print(report.json())
    report.save_html(html_path)
    add_refresh(html_path=html_path)
    ingest()


if __name__ == "__main__":
    get_report(dummy)

