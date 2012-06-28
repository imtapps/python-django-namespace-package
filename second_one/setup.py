from distutils.core import setup


setup(
    name='sample.main.two',
    version='2.0.0',
    namespace_packages=['sample', 'sample.main'],
    packages=['sample.main.two'],
    zip_safe=False,
    include_package_data=True,
)

