import reflex as rx
import pandas as pd
from typing import List
from typing import Optional
import sqlite3
from my_reflex_app.state import State



class RegisterState(State):
    # Register to xia.db
    name_field: str = ""
    password_field: str = ""

    def sign_up(self):
        dbfile = "xia.db"
        conn = sqlite3.connect(dbfile)
        name = self.name_field
        password = self.password_field
        sql_str = "insert into users(name, password) values('{}',{});".format(name, password)
        conn.execute(sql_str)
        conn.commit()
        conn.close()
        print('save')



def index():
    return rx.vstack(
        rx.box(
            rx.heading("註冊", margin_bottom = "1rem"),
            rx.input(
                placeholder = "名字",
                margin_bottom = "1rem",
                on_change = RegisterState.set_name_field,
            ),
            rx.input(
                type_= " password",
                placeholder = "密碼",
                margin_bottom = "1rem",
                on_change = RegisterState.set_password_field,
            ),
            rx.button(
                "註冊", 
                on_click = RegisterState.sign_up,
            ),
        ),
    )


app = rx.App(
    stylesheets=[
        "styles.css",  # This path is relative to assets/
    ],
)
app.add_page(index)
app.compile()
