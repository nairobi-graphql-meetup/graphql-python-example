from models import Department as DepartmentModel
from models import Employee as EmployeeModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Department(SQLAlchemyObjectType):

    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node, )


class Employee(SQLAlchemyObjectType):

    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = graphene.List(Employee)
    all_departments = graphene.List(Department)

    def resolve_all_employees(self, info, **args):
        query = Employee.get_query(info)
        return query.all()
    
    def resolve_all_departments(self, info, **args):
        query = Department.get_query(info)
        return query.all()


schema = graphene.Schema(query=Query, types=[Department, Employee])