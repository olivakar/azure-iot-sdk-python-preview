from setuptools import setup, find_packages

setup(
    name="azure-iot-sdk-common",
    version='0.0.1',
    description='Microsoft Azure IoT SDK Common',
    license='MIT License',
    author='aziotclb',
    author_email='aziotclb@microsoft.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'six'
    ],
    packages=find_packages(exclude=[
        'tests'
    ])
)