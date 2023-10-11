import reflex as rx
from typing import Optional
from .models import User


class State(rx.State):
    """The app state."""

    user: Optional[User] = None
