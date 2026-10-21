import pytest
from linter import lint_migration


def test_create_index_without_concurrently():
    sql = "CREATE INDEX idx_users_name ON users(name);"
    errors = lint_migration(sql)
    assert len(errors) == 1
    assert "CREATE INDEX must use CONCURRENTLY" in errors[0]


def test_create_index_with_concurrently():
    sql = "CREATE INDEX CONCURRENTLY idx_users_name ON users(name);"
    errors = lint_migration(sql)
    assert len(errors) == 0


def test_create_unique_index_without_concurrently():
    sql = "CREATE UNIQUE INDEX idx_users_email ON users(email);"
    errors = lint_migration(sql)
    assert len(errors) == 1
    assert "CREATE INDEX must use CONCURRENTLY" in errors[0]


def test_create_unique_index_with_concurrently():
    sql = "CREATE UNIQUE INDEX CONCURRENTLY idx_users_email ON users(email);"
    errors = lint_migration(sql)
    assert len(errors) == 0


def test_add_constraint_without_not_valid():
    sql = "ALTER TABLE users ADD CONSTRAINT check_age CHECK (age >= 18);"
    errors = lint_migration(sql)
    assert len(errors) == 1
    assert "ADD CONSTRAINT should use NOT VALID" in errors[0]


def test_add_constraint_with_not_valid():
    sql = "ALTER TABLE users ADD CONSTRAINT check_age CHECK (age >= 18) NOT VALID;"
    errors = lint_migration(sql)
    assert len(errors) == 0
