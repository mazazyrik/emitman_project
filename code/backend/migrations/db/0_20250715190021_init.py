from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "admin" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "password" VARCHAR(50) NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    "surname" VARCHAR(50) NOT NULL,
    "is_ss" INT NOT NULL DEFAULT 0,
    "is_superuser" INT NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "decanat" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(54) NOT NULL /* OPI: Отделение прикладной информатики\nOMES: Отделение международного экономического сотрудничества\nOE: Отделение экономики\nONE: Отделение национальной экономики\nBI: Отдеделение бизнес-информатики\nONLINE: Онлайн-программы\nIT_MANAGMENT: Школа IT-менеджмента */,
    "contacts" VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS "group" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    "decanat_id" INT NOT NULL REFERENCES "decanat" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "teacher" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    "program" VARCHAR(54) NOT NULL /* OPI: Отделение прикладной информатики\nOMES: Отделение международного экономического сотрудничества\nOE: Отделение экономики\nONE: Отделение национальной экономики\nBI: Отдеделение бизнес-информатики\nONLINE: Онлайн-программы\nIT_MANAGMENT: Школа IT-менеджмента */,
    "mail" VARCHAR(50) NOT NULL,
    "decanat_id" INT NOT NULL REFERENCES "decanat" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    "surname" VARCHAR(50) NOT NULL,
    "father_name" VARCHAR(50) NOT NULL,
    "is_activist" INT NOT NULL DEFAULT 1,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "telegram_id" BIGINT UNIQUE,
    "grade" INT NOT NULL DEFAULT 1,
    "program" VARCHAR(54) NOT NULL /* OPI: Отделение прикладной информатики\nOMES: Отделение международного экономического сотрудничества\nOE: Отделение экономики\nONE: Отделение национальной экономики\nBI: Отдеделение бизнес-информатики\nONLINE: Онлайн-программы\nIT_MANAGMENT: Школа IT-менеджмента */,
    "brs_rate" INT NOT NULL DEFAULT 0,
    "group_id_id" INT NOT NULL REFERENCES "group" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
