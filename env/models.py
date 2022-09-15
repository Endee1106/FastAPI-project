import email
from enum import unique
import database as _dt
import sqlalchemy as _sql

import database as _database

class Contact(_database):
    __tablename__ = "contact"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    first_name = _sql.Column(_sql.String, index=True)
    last_name = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, index=True, unique=True)
    phone_number = _sql.Column(_sql.Integer,index=True, unique=True)