import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.db import connection

# Tables to drop
tables_to_drop = [
    'auth_group',
    'auth_group_permissions',
    'auth_permission',
    'auth_user',
    'auth_user_groups',
    'auth_user_user_permissions',
    'django_admin_log',
    'django_session',
]

with connection.cursor() as cursor:
    for table in tables_to_drop:
        try:
            cursor.execute(f'DROP TABLE IF EXISTS {table} CASCADE;')
            print(f'✓ Dropped table: {table}')
        except Exception as e:
            print(f'✗ Error dropping {table}: {e}')

print('\nDone! Tables have been removed.')
print('Note: django_migrations and django_content_type tables were kept (required by Django)')
