from pathlib import Path
import pandas as pd

from knowledge_graph import build_knowledge_graph


def detect_sensor_failure(df):
    """
    Detect whether there are inactive sensors
    or missing PM2.5 measurements.
    """

    inactive_records = df[df["status"] == "inactive"]

    missing_pm25 = df[df["pm25"].isna()]

    return not inactive_records.empty or not missing_pm25.empty


def analyse_dependencies(graph):
    """
    Trace the dependency chain:
    Sensor -> Dataset -> Model -> Output
    """

    query = """
    PREFIX dt: <http://example.org/digital-twin/>
    PREFIX ex: <http://example.org/environment/>

    SELECT ?dataset ?model ?output
    WHERE {
        ex:BZ_SENSOR_001 dt:providesDataTo ?dataset .

        ?dataset dt:providesInputTo ?model .

        ?model dt:generates ?output .
    }
    """

    return graph.query(query)

def make_orchestration_decision(df):
    """
    Detect sensor problems and determine
    which Digital Twin components are affected.
    """

    print("\nINTELLIGENT ORCHESTRATION")
    print("=" * 60)

    sensor_failure = detect_sensor_failure(df)

    if not sensor_failure:
        print("\nSYSTEM STATUS: HEALTHY")
        print("All required sensor data is available.")
        print("No orchestration action is required.")
        return

    print("\nSENSOR FAILURE DETECTED")
    print("Required environmental data is unavailable.")

    graph = build_knowledge_graph()
    dependencies = analyse_dependencies(graph)

    print("\nDEPENDENCY ANALYSIS")
    print("-" * 60)

    for row in dependencies:
        print("Sensor: BZ_SENSOR_001")
        print(f"Dataset affected: {row.dataset}")
        print(f"Model affected: {row.model}")
        print(f"Output affected: {row.output}")

    print("\nORCHESTRATION DECISION")
    print("-" * 60)

    print("Air Quality Model may not produce reliable results.")
    print("Recommended action: Check for an alternative sensor or data source.")

if __name__ == "__main__":

    project_root = Path(__file__).resolve().parent.parent

    file_path = project_root / "data" / "sensor_data.csv"

    df = pd.read_csv(file_path)

    make_orchestration_decision(df)