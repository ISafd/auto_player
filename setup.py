from setuptools import setup, find_packages

setup(
    name='auto_player',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        auto-player=auto_player.cli:cli
    ''',
    data_files=[
      ('/etc/bash_completion.d/', ['extra/completion_script/auto_player']),
    ],
)
