import pandas as pd


def calculate_air_quality_status(row):
    """
    Calculate a simplified air-quality status based on
    PM2.5 and PM10 measurements.

    This is a proof-of-concept rule-based model.
    """

    pm25 = row["pm25"]
    pm10 = row["pm10"]

    # Check whether required measurements exist
    if pd.isna(pm25) or pd.isna(pm10):
        return "Unavailable"

    # Simplified air-quality rules
    if pm25 <= 15 and pm10 <= 30:
        return "Good"

    elif pm25 <= 25 and pm10 <= 50:
        return "Moderate"

    else:
        return "Poor"


def run_air_quality_model(df):
    """
    Run the simplified Air Quality Model
    for all sensor observations.
    """

    results = df.copy()

    results["air_quality_status"] = results.apply(
        calculate_air_quality_status,
        axis=1
    )

    return results


if __name__ == "__main__":

    print("Air Quality Model module")