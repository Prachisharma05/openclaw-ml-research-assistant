"""
Dataset Inspector Module

Responsibilities:
- Load datasets
- Validate supported formats
- Display dataset overview
- Detect missing values
- Infer schema information
- Generate summary statistics
"""

from pathlib import Path
import pandas as pd


class DatasetInspector:
    """
    Core dataset inspection engine.
    """

    SUPPORTED_FORMATS = [".csv", ".json"]

    def __init__(self, dataset_path: str):
        self.dataset_path = Path(dataset_path)

    def validate_dataset(self):
        """
        Validate dataset existence and supported format.
        """
        if not self.dataset_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {self.dataset_path}"
            )

        if self.dataset_path.suffix not in self.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported dataset format: {self.dataset_path.suffix}"
            )

        print("Dataset validation successful.")

    def load_dataset(self):
        """
        Load dataset into memory.
        """
        import pandas as pd

        if self.dataset_path.suffix == ".csv":
            self.dataset = pd.read_csv(self.dataset_path)

        elif self.dataset_path.suffix == ".json":
            self.dataset = pd.read_json(self.dataset_path)

        else:
            raise ValueError(
                f"Unsupported dataset format: {self.dataset_path.suffix}"
            )

        print("Dataset loaded successfully.")
        return self.dataset

    def show_basic_info(self):
        """
        Display shape, columns, and dataset overview.
        """
        print("\nDataset Overview")
        print("-" * 40)

        print(f"Rows: {self.dataset.shape[0]}")
        print(f"Columns: {self.dataset.shape[1]}")

        print("\nColumn Names:")
        print(self.dataset.columns.tolist())

        print("\nData Types:")
        print(self.dataset.dtypes)

        print("\nDataset Preview:")
        print(self.dataset.head())

    def detect_missing_values(self):
        """
        Analyze missing values in dataset.
        """
        print("\nMissing Values")
        print("-" * 40)

        missing_counts = self.dataset.isnull().sum()
        missing_percentages = (missing_counts / len(self.dataset)) * 100

        missing_report = pd.DataFrame({
            "missing_count": missing_counts,
            "missing_percentage": missing_percentages
        })

        print(missing_report)

        return missing_report

    def infer_schema(self):
        """
        Infer datatypes and schema structure.
        """
        pass

    def generate_statistics(self):
        """
        Generate statistical summary.
        """
        pass