from context_vars import ContextVar

user_context: dict | None = ContextVar("current_user", default=None)
