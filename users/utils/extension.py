# guestfirst_gateway_django/auth/extensions.py
from strawberry.extensions import Extension
from strawberry.types import Info


class AuthExtension(Extension):
    async def on_operation(self):
        info: Info = self.execution_context.context["info"]
        request = info.context.get("request")

        # Allow only public operations
        public_operations = {"registerUser", "loginUser"}

        operation_name = info.field_name

        if operation_name not in public_operations and not request.user.is_authenticated:
            raise Exception("Authentication required")
