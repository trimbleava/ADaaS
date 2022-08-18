"""
WSGI config for ADaaS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

python_home = '/home/beheen/PROJECTS/ADaaS/.venv'

import sys
import site

if '/home/beheen/PROJECTS/ADaaS' not in sys.path:
    sys.path.append('/home/beheen/PROJECTS/ADaaS')
if '/home/beheen/PROJECTS/ADaaS/.venv/bin' not in sys.path:
    sys.path.append('/home/beheen/PROJECTS/ADaaS/.venv/bin')
if '/home/beheen/PROJECTS/ADaaS/.venv/lib/python3.8/site-packages' not in sys.path:
    sys.path.append('/home/beheen/PROJECTS/ADaaS/.venv/lib/python3.8/site-packages')

# Calculate path to site-packages directory.
python_version = '.'.join(map(str, sys.version_info[:2]))
site_packages = python_home + '/lib/python%s/site-packages' % python_version

# Add the site-packages directory.
site.addsitedir(site_packages)