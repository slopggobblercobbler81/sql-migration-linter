from sql_migration_linter.mysql_rules import lint_mysql_statement

def test_lint_mysql_statement():
    assert lint_mysql_statement("SELECT 1") == True
