from app.configuration.admin.register_admin import Admins
from app.admin import __all__

__admins__ = Admins(admins=tuple(__all__))
