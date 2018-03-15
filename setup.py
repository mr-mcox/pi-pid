from setuptools import setup, find_packages

setup(
    name='pi_pid',
    version='0.3.2',
    author='Matthew Cox',
    author_email='mr.mcox@gmail.com',
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=['click', 'attrs', 'numpy', 'pyyaml'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    packages=find_packages(where='src'),
    entry_points='''
        [console_scripts]
        pi_pid=pi_pid.cli:cli
    ''',
)
