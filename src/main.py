from config_generator import ConfigLoader
from dataset_inspector import DatasetInspector
from preprocessing_advisor import PreprocessingAdvisor
from report_generator import ReportGenerator


def main():
    config_loader = ConfigLoader("configs/default_config.yaml")
    config = config_loader.load_config()

    dataset_path = config["dataset"]["path"]
    report_output_path = config["report"]["output_path"]
    analysis_config = config["analysis"]

    inspector = DatasetInspector(dataset_path)

    inspector.validate_dataset()

    inspector.load_dataset()

    if analysis_config["show_basic_info"]:
        inspector.show_basic_info()

    missing_report = None
    schema_report = None
    statistics_report = None
    preprocessing_recommendations = []

    if analysis_config["detect_missing_values"]:
        missing_report = inspector.detect_missing_values()

    if analysis_config["infer_schema"]:
        schema_report = inspector.infer_schema()

    if analysis_config["generate_statistics"]:
        statistics_report = inspector.generate_statistics()

    if analysis_config["generate_recommendations"]:
        advisor = PreprocessingAdvisor(inspector.dataset)
        preprocessing_recommendations = advisor.generate_recommendations()

    report_content = f"""
DATASET INSPECTION REPORT
==========================

Missing Values:
{missing_report}

Schema Information:
{schema_report}

Statistical Summary:
{statistics_report}

Preprocessing Recommendations:
{chr(10).join(preprocessing_recommendations)}
"""

    report_generator = ReportGenerator(report_output_path)

    report_generator.generate_text_report(report_content)


if __name__ == "__main__":
    main()