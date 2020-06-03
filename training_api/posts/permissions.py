from rest_framework.permissions import SAFE_METHODS, BasePermission
from restfw_composed_permissions.base import (
    BaseComposedPermission,
    Or,
    And,
)
from restfw_composed_permissions.generic.components import (
    AllowOnlyAuthenticated,
    ObjectAttrEqualToObjectAttr,
)


class ReadOnlyCreateOrOwnPost(BaseComposedPermission):
    def global_permission_set(self):
        return AllowOnlyAuthenticated

    def object_permission_set(self):
        return ObjectAttrEqualToObjectAttr("obj.user", "request.user")
