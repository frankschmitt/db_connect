from neo4j import GraphDatabase
import csv

def read_input(filename):
    result = []
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            result.append(row)
    return result

class DependencyVisualizer:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def add_dependency(self, dependency):
        with self.driver.session() as session:
            dep = session.write_transaction(self._create_and_return_dependency, dependency)
            print(dep)

    def remove_schema_nodes(self):
        with self.driver.session() as session:
            session.write_transaction(self._remove_schema_nodes)

    @staticmethod
    def _remove_schema_nodes(tx):
        result = tx.run("MATCH (s:Schema) DETACH DELETE s")
        return result.single()

    @staticmethod
    def _create_and_return_dependency(tx, dependency):
        source = tx.run("MERGE (n:Schema {name: $name}) RETURN n", name = dependency['source'])
        target = tx.run("MERGE (n:Schema {name: $name}) RETURN n", name = dependency['target'])
        result = tx.run("MATCH (s:Schema {name: $source} ), (t:Schema {name: $target})  \
                  MERGE (s)-[:depends_on]->(t)", source = dependency['source'], target = dependency['target'])
        return result.single()


if __name__ == "__main__":
    dv = DependencyVisualizer("bolt://localhost:7687", "neo4j", "test")
    # remove old schema nodes
    dv.remove_schema_nodes()
    # add parsed nodes / dependencies
    input = read_input("input.csv")
    for row in input:
        print(row)
        dv.add_dependency(row)
    dv.close()
