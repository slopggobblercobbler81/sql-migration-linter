import re

def lint_migration(sql: str) -> list:
    errors = []
    # Check for DROP INDEX without CONCURRENTLY
    pattern = r'(?i)\bdrop\s+index\b(?!.*\bconcurrently\b)'
    if re.search(pattern, sql):
        errors.append('DROP INDEX must use CONCURRENTLY to avoid table locks')
    return errors

