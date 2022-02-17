"""
Here Configuration of your Extension (and maybe your Application) takes place
"""
import os
from cryptoadvance.specter.config import ProductionConfig as SpecterProductionConfig


class BaseConfig:
    ''' This is a extension-based Config which is used as Base '''
    {{ext.id | upper}}_SOMEKEY = "some value"

class ProductionConfig(BaseConfig):
    ''' This is a extension-based Config for Production '''
    pass


class AppProductionConfig(SpecterProductionConfig):
    ''' The AppProductionConfig class can be used to user this extension as application
    '''
    # Where should the User endup if he hits the root of that domain?
    ROOT_URL_REDIRECT = "/spc/ext/{{ ext.id}}"
    # I guess this is the only extension which should be available?
    EXTENSION_LIST = [
        "{{ ext.org}}.specterext.{{ ext.id}}.service"
    ]
    # You probably also want a different folder here
    SPECTER_DATA_FOLDER=os.path.expanduser("~/.{{ ext.id}}")