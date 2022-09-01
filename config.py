from dataclasses import dataclass


@dataclass
class DB:
    driver: str
    user: str
    pwd: str


@dataclass
class TestConfig:
    dbs: DB
