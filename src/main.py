from dataset_inspector import DatasetInspector


def main():
    dataset_path = "data/sample.csv"

    inspector = DatasetInspector(dataset_path)

    inspector.validate_dataset()

    inspector.load_dataset()

    inspector.show_basic_info()

    inspector.detect_missing_values()

    inspector.infer_schema()

    inspector.generate_statistics()


if __name__ == "__main__":
    main()