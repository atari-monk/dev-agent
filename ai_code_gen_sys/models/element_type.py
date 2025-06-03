from enum import Enum


class ElementType(str, Enum):
    MODULE = "module"
    INTERFACE = "interface"
    CLASS = "class"
    FUNCTION = "function"
    COMPONENT = "component"
    API_ENDPOINT = "api_endpoint"
    DATABASE_MODEL = "database_model"
    CONFIG = "configuration"
    TEST = "test"