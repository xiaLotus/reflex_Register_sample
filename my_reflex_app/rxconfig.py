import reflex as rx

class MyreflexappConfig(rx.Config):
    pass

config = MyreflexappConfig(
    app_name="my_reflex_app",
    # env = rx.Env.DEV,
    db_url = "sqlite:///xia.db",
    tailwind = {
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)