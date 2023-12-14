# -*- encoding: utf-8 -*-
from nebula_bench.common.base import BaseScenario


class BaseMatchScenario(BaseScenario):
    abstract = True
    csv_path = "social_network/dynamic/person.csv"

class Match1HopDst(BaseMatchScenario):
    abstract = False
    nGQL = 'MATCH (v1:Person)-[e:KNOWS]->(v2:Person) WHERE id(v1) == {0} RETURN v2.Person.firstName'

class Match2HopDst(BaseMatchScenario):
    abstract = False
    nGQL = 'MATCH (v1:Person)-[e:KNOWS*2]->(v2:Person) WHERE id(v1) == {0} RETURN v2.Person.firstName'

class Match3HopDst(BaseMatchScenario):
    abstract = False
    nGQL = 'MATCH (v1:Person)-[e:KNOWS*3]->(v2:Person) WHERE id(v1) == {0} RETURN v2.Person.firstName'

class Match1HopDstCount(BaseMatchScenario):
    abstract = False
    nGQL = 'MATCH (v1:Person)-[e:KNOWS]->(v2:Person) WHERE id(v1) == {0} RETURN count(v2.Person.firstName)'

class Match2HopDstCount(BaseMatchScenario):
    abstract = False
    nGQL = 'MATCH (v1:Person)-[e:KNOWS*2]->(v2:Person) WHERE id(v1) == {0} RETURN count(v2.Person.firstName)'

class Match3HopDstCount(BaseMatchScenario):
    abstract = False
    nGQL = 'MATCH (v1:Person)-[e:KNOWS*3]->(v2:Person) WHERE id(v1) == {0} RETURN count(v2.Person.firstName)'

class Match1HopEdge(BaseMatchScenario):
    abstract = False
    nGQL = 'MATCH (v1:Person)-[e:KNOWS]->(v2:Person) WHERE id(v1) == {0} RETURN e.creationDate'

class Match2HopEdge(BaseMatchScenario):
    abstract = False
    nGQL = 'MATCH (v1:Person)-[e:KNOWS*2]->(v2:Person) WHERE id(v1) == {0} RETURN e.creationDate'

class Match3HopEdge(BaseMatchScenario):
    abstract = False
    nGQL = 'MATCH (v1:Person)-[e:KNOWS*3]->(v2:Person) WHERE id(v1) == {0} RETURN e.creationDate'
    