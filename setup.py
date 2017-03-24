from setuptools import setup, find_packages

setup(
    name='plugins',
    version="1.0",
    description="demo of plugin system via setuptools",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'img.plugin':
        ['jpg=foo:make_jpg_image_plugin',
         'png=foo:make_png_image_plugin']
    },)
