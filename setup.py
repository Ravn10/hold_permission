# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in sales_order_role_based_hold_restrictions/__init__.py
from sales_order_role_based_hold_restrictions import __version__ as version

setup(
	name='sales_order_role_based_hold_restrictions',
	version=version,
	description='Sales Order Role Based Hold Restrictions',
	author='Firsterp',
	author_email='support@firsterp.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
