from setuptools import setup

setup(
    name='iot_pir',
    version='0.2',
    packages=['iot_pir'],
    url='https://github.com/pawelkolodziej/',
    license='MiT',
    author='PawelK',
    author_email='pakolodziej@gmail.com',
    description='motion detector with PIR sensor',
    install_requires=['PyFCM']
)
