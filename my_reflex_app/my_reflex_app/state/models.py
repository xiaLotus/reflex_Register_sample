import reflex as rx

class User(rx.Model, table=True):
    name: str
    password: str