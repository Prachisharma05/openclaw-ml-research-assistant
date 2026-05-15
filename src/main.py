from dataset_inspector import DatasetInspector
from report_generator import ReportGenerator


def main():
    dataset_path = "data/sample.csv"

    inspector = DatasetInspector(dataset_path)

    inspector.validate_dataset()

    inspector.load_dataset()

    inspector.show_basic_info()

    missing_report = inspector.detect_missing_values()

    schema_report = inspector.infer_schema()

    statistics_report = inspector.generate_statistics()

    report_content = f"""
DATASET INSPECTION REPORT
==========================

Missing Values:
{missing_report}

Schema Information:
{schema_report}

Statistical Summary:
{statistics_report}
"""

    report_generator = ReportGenerator(
        "reports/dataset_report.txt"
    )

    report_generator.generate_text_report(report_content)


if __name__ == "__main__":
    main()