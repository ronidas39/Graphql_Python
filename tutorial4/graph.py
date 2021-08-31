from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()
q1="""
create(a:student{Name:"Roni"})-[:has_ph_no]->(n:Mobile{no:"837"})
"""
for i in range(10000):
    session.run(q1)

