from setuptools import setup, find_packages

setup(
    name='pi_pid',
    version='0.0.1',
    author='Matthew Cox',
    author_email='mr.mcox@gmail.com',
    package_dir={'': 'src'},
    install_requires=['click', 'attrs'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    packages=find_packages(where='src'),
)
