from setuptools import setup, find_packages

setup(
    name='myapp',
    version='0.1.0',
    description='A brief description of my app',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my-app',
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'myapp=myapp.main:main',  # Entry point definition
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
