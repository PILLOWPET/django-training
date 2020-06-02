from rest_framework.permissions import SAFE_METHODS, BasePermission
from restfw_composed_permissions.base import (
    BaseComposedPermission,
    Or,
    And,
)
from restfw_composed_permissions.generic.components import (
    AllowOnlySafeHttpMethod,
    AllowOnlyAuthenticated,
    ObjectAttrEqualToObjectAttr,
)


class ReadOnlyCreateOrOwnPost(BaseComposedPermission):
    def global_permission_set(self):
        print("gen perm called")
        return Or(And(AllowOnlyAuthenticated), (AllowOnlySafeHttpMethod),)

    def object_permission_set(self):
        print("object perm called")
        return ObjectAttrEqualToObjectAttr("obj.user", "request.user")
