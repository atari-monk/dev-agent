from setuptools import setup, find_packages

setup(
    name="dev-agent",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "chatgpt_agent=agents.chatgpt_agent:main",
            "code_base_agent=agents.code_base_agent:main",
            "generate_class_template=prompt_generators.generate_class_template:main",
            "coder_agent_prompt_generator=prompt_generators.coder_agent_prompt_generator:main",
        ],
    },
    python_requires=">=3.7",
)
