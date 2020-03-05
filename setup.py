from distutils.core import setup

setup(
    name='check-seo',
    version='1.0',
    packages=['check_seo'],
    author='AngeMort',
    author_email='contact@analy.fr',
    url='https://github.com/angemort/check-seo',
    license='Apache 2.0',
    description='Un outil de référencement qui analyse la structure d\'un site, parcourt le site, compte les mots dans le corps du site et prévient de tout problème technique de référencement..',
    scripts=['check-seo'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
