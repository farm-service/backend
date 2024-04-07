from dataclasses import dataclass
from sqladmin import Admin


@dataclass(frozen=True)
class Admins:
    admins: tuple

    def register_admins(self, admin_instance: Admin) -> None:
        for admin in self.admins:
            admin_instance.add_view(admin)
