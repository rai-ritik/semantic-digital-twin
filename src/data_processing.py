from pathlib import Path
import pandas as pd

from air_quality_model import run_air_quality_model

def load_sensor_data(file_path):
    """Load environmental sensor data."""
    return pd.read_csv(file_path)


def validate_sensor_data(df):
    """Validate the quality and availability of sensor data."""

    print("\nDATA VALIDATION REPORT")
    print("=" * 50)

    # Dataset size
    print(f"\nTotal records: {len(df)}")

    # Missing values
    print("\nMissing Values:")
    missing_values = df.isnull().sum()

    print(missing_values[missing_values > 0])

    # Inactive sensors
    inactive_records = df[df["status"] == "inactive"]

    print(f"\nInactive sensor records: {len(inactive_records)}")

    if not inactive_records.empty:
        print(inactive_records[["timestamp", "sensor_id", "location"]])

    # Air quality model readiness
    required_columns = ["pm25", "pm10"]

    missing_required_data = df[required_columns].isnull().any().any()

    print("\nAIR QUALITY MODEL STATUS")

    if missing_required_data:
        print("⚠️ WARNING: Required air-quality data is missing.")
        print("Model reliability may be affected.")
    else:
        print("✅ All required air-quality data is available.")
        print("Air Quality Model can run safely.")


if __name__ == "__main__":

    # Find project root
    project_root = Path(__file__).resolve().parent.parent

    # Dataset path
    file_path = project_root / "data" / "sensor_data.csv"

    # Load data
    df = load_sensor_data(file_path)

    # Display dataset
    print("\nENVIRONMENTAL SENSOR DATA")
    print("=" * 50)
    print(df.to_string(index=False))

    # Validate dataset
    validate_sensor_data(df)

    # Run Air Quality Model
results = run_air_quality_model(df)

print("\nAIR QUALITY MODEL RESULTS")
print("=" * 50)

print(
    results[
        [
            "timestamp",
            "sensor_id",
            "pm25",
            "pm10",
            "air_quality_status"
        ]
    ].to_string(index=False)
)