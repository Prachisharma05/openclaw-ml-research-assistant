"""
Preprocessing Advisor Module

Responsibilities:
- Analyze dataset schema
- Recommend missing-value handling
- Recommend categorical encoding
- Recommend numeric scaling
- Identify potential identifier columns
"""


class PreprocessingAdvisor:
    """
    Generates preprocessing recommendations from a pandas DataFrame.
    """

    def __init__(self, dataset):
        self.dataset = dataset

    def generate_recommendations(self):
        """
        Generate preprocessing recommendations.
        """
        import pandas as pd

        recommendations = []

        for column in self.dataset.columns:
            dtype = self.dataset[column].dtype
            missing_count = self.dataset[column].isnull().sum()
            unique_count = self.dataset[column].nunique()

            if missing_count > 0:
                if pd.api.types.is_numeric_dtype(self.dataset[column]):
                    recommendations.append(
                        f"Column '{column}' has {missing_count} missing values. "
                        "Recommended: use median or mean imputation."
                    )
                else:
                    recommendations.append(
                        f"Column '{column}' has {missing_count} missing values. "
                        "Recommended: use mode imputation or create an 'Unknown' category."
                    )

            if pd.api.types.is_object_dtype(dtype):
                recommendations.append(
                    f"Column '{column}' is categorical. "
                    "Recommended: apply one-hot encoding or label encoding."
                )

            if pd.api.types.is_numeric_dtype(dtype):
                recommendations.append(
                    f"Column '{column}' is numeric. "
                    "Recommended: consider scaling if used in distance-based or gradient-based models."
                )

            if unique_count == len(self.dataset):
                recommendations.append(
                    f"Column '{column}' has all unique values. "
                    "Recommended: check if it is an identifier and exclude it from model training."
                )

        print("\nPreprocessing Recommendations")
        print("-" * 40)

        for recommendation in recommendations:
            print(f"- {recommendation}")

        return recommendations