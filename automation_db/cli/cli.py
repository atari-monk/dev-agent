from typing import Any, Dict, Tuple, Type
import argparse
from automation_db.cli.command import Command
from automation_db.cli.model_type import ModelType
from automation_db.project.cli.command import PROJECT_COMMAND
from automation_db.code_style.cli.command import CODE_STYLE_COMMAND
from automation_db.agent.cli.command import AGENT_COMMAND
from automation_db.file.cli.command import FILE_COMMAND
from automation_db.feature.cli.command import FEATURE_COMMAND
from automation_db.task.cli.command import TASK_COMMAND

COMMAND_REGISTRY: Dict[Tuple[ModelType, str], Type[Command]] = {}
COMMAND_REGISTRY.update(PROJECT_COMMAND)
COMMAND_REGISTRY.update(CODE_STYLE_COMMAND)
COMMAND_REGISTRY.update(AGENT_COMMAND)
COMMAND_REGISTRY.update(FILE_COMMAND)
COMMAND_REGISTRY.update(FEATURE_COMMAND)
COMMAND_REGISTRY.update(TASK_COMMAND)

def init_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Automation DB")
    subparsers = parser.add_subparsers(dest='model', required=True)
    
    model_parsers: dict[Any, Any] = {}
    for (model_type, cmd_name), cmd_class in COMMAND_REGISTRY.items():
        if model_type.value not in model_parsers:
            model_parsers[model_type.value] = subparsers.add_parser(
                model_type.value, 
                help=f"{model_type.value.capitalize()} operations"
            ).add_subparsers(dest='subcommand', required=True)
        
        cmd_parser = model_parsers[model_type.value].add_parser(
            cmd_name, 
            help=f"{cmd_name} {model_type.value}"
        )
        cmd_class.init_parser(cmd_parser)
    
    return parser

def handle_cli(args: argparse.Namespace) -> None:
    if not hasattr(args, 'model'):
        print(f'No such model: {args.model}')
        return
    
    model_type = ModelType(args.model)
    command_key = (model_type, args.subcommand)
    
    if command_key in COMMAND_REGISTRY:
        COMMAND_REGISTRY[command_key].handle(args)
    else:
        raise ValueError(f"Unknown command: {args.model} {args.subcommand}")