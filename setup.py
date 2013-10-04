from setuptools import setup, find_packages


setup(
    name='rapidsms-alerts',
    version=__import__('alerts').__version__,
    author='Evan Wheeler',
    author_email='evan@leapfrog.io',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['Django',],
    url='https://github.com/ewheeler/rapidsms-alerts/',
    license='BSD',
    description=u' '.join(__import__('alerts').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=open('README.rst').read(),
    zip_safe=False,
)
