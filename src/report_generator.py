import json
import logging

"""
Report Generator Module

Responsibilities:
- Generate analysis reports
- Save reports to disk
- Create structured summaries
- Support future markdown/PDF export
"""


class ReportGenerator:
    """
    Handles report creation and export.
    """

    def __init__(self, output_path: str):
        self.output_path = output_path

    def generate_text_report(self, report_content: str):
        """
        Generate and save text report.
        """
        with open(self.output_path, "w", encoding="utf-8") as file:
            file.write(report_content)

        print(f"Report saved to: {self.output_path}")
        
    def generate_json_report(self, report_data: dict):
        """
        Generate and save JSON report.
        """

        json_output_path = self.output_path.replace(".txt", ".json")

        with open(json_output_path, "w", encoding="utf-8") as file:
            json.dump(
                report_data,
                file,
                indent=4,
                allow_nan=False,
                default=str
            )

        logging.info(
            f"JSON report saved to: {json_output_path}"
        )