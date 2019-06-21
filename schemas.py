from models import Department as DepartmentModel
from models import Employee as EmployeeModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Company(graphene.ObjectType):
    name = graphene.String()
    address = graphene.String()


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
    company = graphene.Field(Company)
    companies = graphene.List(Company)

    def resolve_all_employees(self, info, **args):
        query = Employee.get_query(info)
        return query.all()

    def resolve_all_departments(self, info, **args):
        query = Department.get_query(info)
        return query.all()

    def resolve_company(self, info, **args):
        return {"name": "my name", "address": "my address"}

    def resolve_companies(self, info, **args):
        return [
            {"name": "my name 1", "address":"hfhfhf","hello":"world"},
            {"name": "my name 2", "address": "my address 2"},
            {"name": "my name 3", "address": "my address 3"}
        ]


schema = graphene.Schema(query=Query, types=[Department, Employee, Company])
