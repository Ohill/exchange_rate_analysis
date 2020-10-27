from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='exchange_rate_analisys',
    version='1.0',
    url='https://github.com/raynem/exchange_rate_analysis.git',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    include_package_data=True,
    install_requires=[
        'asn1crypto==0.24.0',
        'attrs==17.4.0',
        'certifi==2018.1.18',
        'cffi==1.11.5',
        'chardet==3.0.4',
        'coverage==4.5.1',
        'cryptography==3.2',
        'eventlet==0.22.0',
        'greenlet==0.4.13',
        'idna==2.6',
        'linecache2==1.0.0',
        'lxml==4.1.1',
        'mock==2.0.0',
        'pbr==3.1.1',
        'pep8==1.7.1',
        'petl==1.1.1',
        'pluggy==0.6.0',
        'py==1.5.2',
        'pycparser==2.18',
        'pyOpenSSL==17.5.0',
        'PySocks==1.6.8',
        'pytest==3.4.2',
        'pytest-cov==2.5.1',
        'requests==2.18.4',
        'six==1.11.0',
        'timeout-decorator==0.3.2',
        'traceback2==1.4.0',
        'unittest2==1.1.0',
        'urllib3==1.22',
        'xmltodict==0.11.0',
    ]
)