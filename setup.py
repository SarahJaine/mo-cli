from setuptools import setup

long_description = open('README.md').read()

setup(
        name='mo-cli',
        version='0.1',
        description='starts new "mo" cookiecutter template',
        long_description=long_description,
        url='https://github.com/SarahJaine/mo-cli',
        author='Sarah Jaine Szekeresh',
        author_email='sarahjaine@isl.co',
        liscense='MIT',
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3.5',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        py_modules=['mo'],
        install_requires=[
            'click==6.6',
            'cookiecutter==1.4.0',
            'requests>=2.9.1',
         ],
        entry_points='''
            [console_scripts]
            mo=mo:cli
        '''
)
