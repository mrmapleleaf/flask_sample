from setuptools import setup, find_packages

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    # staticファイルやテンプレートファイルを含めるための設定
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)