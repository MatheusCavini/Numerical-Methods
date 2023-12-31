from setuptools import find_packages, setup
setup(
    name='NumMethPy',
    packages=find_packages(include=['NumMethPy', 'zeros']),
    version='0.1.0',
    description='Library including some numerica methods.',
    author='Matheus Latorre Cavini',
    license='None',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)