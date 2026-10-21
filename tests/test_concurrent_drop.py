import pytest
from linter import lint_migration

def test_drop_index_without_concurrently():
    sql = 'DROP INDEX idx_users_email;'
    errors = lint_migration(sql)
    assert len(errors) == 1
    assert 'CONCURRENTLY' in errors[0]

def test_drop_index_with_concurrently():
    sql = 'DROP INDEX CONCURRENTLY idx_users_email;'
    errors = lint_migration(sql)
    assert len(errors) == 0

