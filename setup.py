#!/usr/bin/env python
from setuptools import setup, find_packages
from os import environ as env
from os import path

# pull in active plugins
plugins = env['CABOT_PLUGINS_ENABLED'].split(',') if 'CABOT_PLUGINS_ENABLED' in env else ["cabot_alert_hipchat", "cabot_alert_twilio", "cabot_alert_email"]

other_requirements = plugins
if not env.get('DYNO', None):
    other_requirements += ['distribute==0.6.24']
if env.get('AUTH_LDAP', 'false').lower() == 'true':
    other_requirements += [
        'django-auth-ldap==1.2.6',
        'python-ldap==2.4.25',
    ]


def open_file(fname):
    return open(path.join(path.dirname(__file__), fname))


setup(
    name='cabot',
    version='0.0.1-dev',
    description="Self-hosted, easily-deployable monitoring and alerts service"
                " - like a lightweight PagerDuty",
    long_description=open('README.md').read(),
    author="Arachnys",
    author_email='info@arachnys.com',
    url='http://cabotapp.com',
    license='MIT',
    install_requires=open_file('requirements.txt').readlines() + other_requirements,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
