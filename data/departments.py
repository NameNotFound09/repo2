import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm

department_member = sqlalchemy.Table(
    'department_member',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column(
        'department_id',
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('departments.id'),
        primary_key=True),
    sqlalchemy.Column('user_id',
                      sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id'),
                      primary_key=True)
)


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    chief = sqlalchemy.Column(sqlalchemy.Integer)
    location = sqlalchemy.Column(sqlalchemy.String)
    members = orm.relationship(
        "User",
        secondary=department_member,
        back_populates="departments"
    )
    email = sqlalchemy.Column(sqlalchemy.String)



