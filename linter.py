import re

def lint_migration(sql: str) -> list:
    errors = []
    
    # Check for DROP INDEX without CONCURRENTLY
    drop_index_pattern = r'(?i)\bdrop\s+index\b(?!.*\bconcurrently\b)'
    if re.search(drop_index_pattern, sql):
        errors.append('DROP INDEX must use CONCURRENTLY to avoid table locks')

    # Check for CREATE INDEX without CONCURRENTLY
    create_index_pattern = r'(?i)\bcreate\s+(unique\s+)?index\b(?!.*\bconcurrently\b)'
    if re.search(create_index_pattern, sql):
        errors.append('CREATE INDEX must use CONCURRENTLY to avoid blocking table writes')

    # Check for ADD CONSTRAINT without NOT VALID
    add_constraint_pattern = r'(?i)\balter\s+table\b.*\badd\s+constraint\b(?!.*\bnot\s+valid\b)'
    if re.search(add_constraint_pattern, sql):
        errors.append('ADD CONSTRAINT should use NOT VALID to prevent exclusive table lock escalation')

    return errors
