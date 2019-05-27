from setuptools import setup, find_packages

requires = [
    "pymysql",
    "django",
    "django-bootstrap4",
]

setup(
    name="mybook",
    version="0.1",
    packages=find_packages(),
    install_requires=requires,
    extras_require={
        "testing": [
            "pytest",
            "pytest-flake8",
            "pytest-cov",
        ],
        "dev": [
            "pytest",
            "pytest-flake8",
            "pytest-cov",
            "pep8",
            "autopep8",
        ],
    },
)
