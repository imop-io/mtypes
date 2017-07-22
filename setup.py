from setuptools import setup


setup(
    name="mtypes",
    version="0.0.1",
    license='https://www.gnu.org/licenses/gpl-3.0.en.html',
    description="Awesome type class",
    author='songww',
    author_email='sww4718168@gmail.com',
    url='https://github.com/imop/mtypes',
    packages=['mtypes'],
    package_data={
        'types': ['README.rst', 'LICENSE']
    },
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: Proxy Servers',
    ]
)
