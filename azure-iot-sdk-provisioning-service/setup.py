from setuptools import setup, find_packages

with open("doc/package-readme.md", "r") as fh:
    _long_description = fh.read()

setup(
    name='azure-iot-sdk-provisioning-service',
    version='1.1.0',
    description='Microsoft Azure IoT Provisioning Service SDK',
    license='MIT License',
    url='https://github.com/Azure/azure-iot-sdk-python',
    author='aziotclb',
    author_email='aziotclb@microsoft.com',
    #long_description=_long_description,
    #long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'],
    install_requires=[
        'msrest',
        'azure-iot-sdk-common'
        ],
    packages=find_packages(exclude=[
        'tests'
    ]),
)
