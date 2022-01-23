from cryptoadvance.specter.services.service import Service, devstatus_alpha
from dummy.service import Service

class DummyService(Service):
    id = "dummy"
    name = "Dummy Service"
    icon = "dummy/img/ghost.png"
    logo = "dummy/img/dummy_logo.jpeg"
    desc = "Where a Dummy grows bigger."
    has_blueprint = True
    blueprint_module = "dummy.controller"
    devstatus = devstatus_alpha

    # TODO: As more Services are integrated, we'll want more robust categorization and sorting logic
    sort_priority = 2
