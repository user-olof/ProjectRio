#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
   
    is_testing = 'test' in sys.argv
    if is_testing:  
        from coverage import Coverage
        # cov = coverage.Coverage(source=['src'], omit=['*/tests/*'])
        # cov.set_option('report:show_missing', True)
        cov = Coverage()
        cov.erase()
        cov.start()
        

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    execute_from_command_line(sys.argv)

    if is_testing:
        cov.stop()
        cov.save()
        cov.report()
        cov.html_report(directory='htmlcov')


if __name__ == '__main__':
    is_testing = 'test' in sys.argv
    if is_testing:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rioacademy.settings.testing')  
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rioacademy.settings.development')

    import django
    django.setup()
    main()
