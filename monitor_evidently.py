import os
import pandas as pd
from sklearn.datasets import load_iris
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

iris = load_iris(as_frame=True).frame
reference = iris.iloc[:75]
current = iris.iloc[75:]

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=reference, current_data=current)

os.makedirs("reports", exist_ok=True)
report.save_html("reports/drift_report.html")
print("Evidently report generated: reports/drift_report.html")