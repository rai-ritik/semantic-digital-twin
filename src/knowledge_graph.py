from rdflib import Graph, Namespace, RDF, RDFS, Literal


def build_knowledge_graph():
    """
    Build a semantic knowledge graph representing the
    Environmental Monitoring Digital Twin.
    """

    # Create RDF graph
    graph = Graph()

    # Define namespaces
    DT = Namespace("http://example.org/digital-twin/")
    EX = Namespace("http://example.org/environment/")

    # Bind namespaces for readable output
    graph.bind("dt", DT)
    graph.bind("ex", EX)

    # -----------------------------
    # Define Digital Twin concepts
    # -----------------------------

    graph.add((DT.Sensor, RDF.type, RDFS.Class))
    graph.add((DT.Observation, RDF.type, RDFS.Class))
    graph.add((DT.Dataset, RDF.type, RDFS.Class))
    graph.add((DT.Model, RDF.type, RDFS.Class))
    graph.add((DT.Output, RDF.type, RDFS.Class))

    # -----------------------------
    # Create system components
    # -----------------------------

    pm25_sensor = EX.BZ_SENSOR_001
    environmental_dataset = EX.Bolzano_Environmental_Dataset
    air_quality_model = EX.Air_Quality_Model
    air_quality_output = EX.Air_Quality_Status

    # Define component types
    graph.add((pm25_sensor, RDF.type, DT.Sensor))
    graph.add((environmental_dataset, RDF.type, DT.Dataset))
    graph.add((air_quality_model, RDF.type, DT.Model))
    graph.add((air_quality_output, RDF.type, DT.Output))

    # -----------------------------
    # Define relationships
    # -----------------------------

    graph.add((pm25_sensor, DT.providesDataTo, environmental_dataset))

    graph.add(
        (
            environmental_dataset,
            DT.providesInputTo,
            air_quality_model
        )
    )

    graph.add(
        (
            air_quality_model,
            DT.generates,
            air_quality_output
        )
    )

    return graph


if __name__ == "__main__":

    graph = build_knowledge_graph()

    print("\nSEMANTIC DIGITAL TWIN KNOWLEDGE GRAPH")
    print("=" * 50)

    for subject, predicate, obj in graph:
        print(f"{subject} → {predicate} → {obj}")

    print("\nTotal relationships:", len(graph))