import graphene
from bson.objectid import ObjectId
from app.database import db

class RollMarkingActivitiesSchema(graphene.ObjectType):
    _id = graphene.ID()
    activityType = graphene.Int()
    students = graphene.List(lambda: UserSchema)
    userId = graphene.ID()
    timestamp = graphene.DateTime()

    def resolve_students(self, info):
        studentList = self.students
        studentList = map(lambda student: db.users.find_one(
            {"_id": ObjectId(student)}, {"activities": 0}),  studentList)
        return map(lambda student: UserSchema(**student), studentList)

from app.graphql.schemas.user import UserSchema