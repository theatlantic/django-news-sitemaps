from setuptools import setup, find_packages

setup(
    name='django-news-sitemaps',
    version='1.3.0',
    description='Generates sitemaps compatible with the Google News schema',
    author='TWT Web Devs',
    author_email='webdev@washingtontimes.com',
    maintainer='The Atlantic',
    maintainer_email='programmers@theatlantic.com',
    url='http://github.com/washingtontimes/django-news-sitemaps/',
    download_url='https://github.com/theatlantic/django-news-sitemaps/releases',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['Django>=1.11', 'six'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
