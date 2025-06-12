from setuptools import setup, find_packages

setup(
    name="dev-agent",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "automation_cli=automation_db.cli.main:main",
            "automation_agent=agents.smoke.run_code_agent_on_toml:main"
        ],
    },
    python_requires=">=3.7",
)
