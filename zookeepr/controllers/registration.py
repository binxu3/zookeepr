from formencode import validators, compound, variabledecode
from formencode.schema import Schema

from zookeepr.lib.auth import SecureController, AuthRole
from zookeepr.lib.base import *
from zookeepr.lib.crud import Create, List
from zookeepr.lib.validators import BaseSchema

class RegistrationSchema(Schema):
    address1 = validators.String(not_empty=True)
    address2 = validators.String()
    city = validators.String(not_empty=True)
    state = validators.String()
    country = validators.String(not_empty=True)
    postcode = validators.String(not_empty=True)

    company = validators.String()

    shell = validators.String()
    shelltext = validators.String()
    editor = validators.String()
    editorstring = validators.String()
    distro = validators.String()
    distrostring = validators.String()

    prevlca = validators.Set()

    type = validators.String(not_empty=True)
    discount = validators.String()

    teesize = validators.String(not_empty=True)
    dinner = validators.Int()
    diet = validators.String()
    special = validators.String()
    miniconf = validators.Set()
    opendaydrag = validators.Int()

    partneremail = validators.String()
    kids_0_3 = validators.Int()
    kids_4_6 = validators.Int()
    kids_7_9 = validators.Int()
    kids_10 = validators.Int()

    accommodation = validators.String()
    checkin = validators.Int()
    checkout = validators.Int()

    lasignup = validators.Bool()
    announcesignup = validators.Bool()
    delegatessignup = validators.Bool()

class PersonSchema(Schema):
    email_address = validators.String(not_empty=True)
    password = validators.String(not_empty=True)
    password_confirm = validators.String(not_empty=True)
    fullname = validators.String(not_empty=True)
    handle = validators.String(not_empty=True)
    
class NewRegistrationSchema(BaseSchema):
    person = PersonSchema()
    registration = RegistrationSchema()

    pre_validators = [variabledecode.NestedVariables]
    
class RegistrationController(BaseController, Create, List):
    individual = 'registration'
    model = model.Registration
    schemas = {'new': NewRegistrationSchema(),
               }