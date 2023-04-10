import graphene
from graph_api.core.mutations import EmployeeMutations

from graph_api.core.schema import EmployeeQuery


class Query(EmployeeQuery,
            graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

class Mutations(EmployeeMutations,
                graphene.ObjectType):
        pass

schema = graphene.Schema(mutation=Mutations, query=Query)