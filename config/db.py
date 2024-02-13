FastAPI_TO_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",  # 选择MySQL OR MAriaDB
            "credentials": {
                "host": "192.168.1.107",
                "port": "3306",
                "user": "auska",
                "password": "qwer1234",
                "database": "test_data",
                "charset": "utf8mb4",
                "minsize": 1,
                "maxsize": 5,
                "echo": True
            }
        }
    },
    # 模型注册
    "apps": {
        "models": {
            "models": ["db.models", "aerich.models"],
            "default_connection": "default"
        }
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai"  # 时区
}
