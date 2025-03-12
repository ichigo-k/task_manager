from setuptools import setup

setup(
    name="Task Manager",
    version="1.0",
    py_modules=["main"],
    install_requires=["click", "humanize", "mongoengine", "setuptools"],
    entry_points={
        "console_scripts": [
            "task-cli=main:cli"
        ],
    },
)
