import json
from pathlib import Path
from typing import Any, Dict, List, Union, TypeVar

JSONPrimitive = Union[str, int, float, bool, None]
JSONValue = Union[JSONPrimitive, Dict[str, Any], List[Any]]
JSONType = Union[JSONPrimitive, Dict[str, JSONValue], List[JSONValue]]

T = TypeVar('T', bound=JSONType)

def convert_paths_to_json_safe(json_str: str) -> str:
    try:
        json_str = json_str.strip()
        escaped_json_str = json_str.replace("\\", "\\\\")
        data: JSONType = json.loads(escaped_json_str)
        processed_data = process_item(data)
        return json.dumps(processed_data, indent=2)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON input: {e}") from e

def process_item(item: T) -> T:
    if isinstance(item, str):
        return item.replace("\\", "/")  # type: ignore
    elif isinstance(item, dict):
        return {k: process_item(v) for k, v in item.items()}  # type: ignore
    elif isinstance(item, list):
        return [process_item(i) for i in item]  # type: ignore
    return item

def append_json_strings_to_array(
    json_strings: Union[str, List[str]], 
    file_path: Path, 
    indent: int = 2
) -> None:
    input_strings: List[str] = [json_strings] if isinstance(json_strings, str) else json_strings
    existing_data: List[JSONType] = []

    if file_path.exists() and file_path.stat().st_size > 0:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                loaded_data: JSONType = json.load(f)
                existing_data = (
                    [loaded_data] 
                    if not isinstance(loaded_data, list) 
                    else loaded_data
                )
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in existing file: {e}") from e
        except OSError as e:
            raise OSError(f"Error reading file {file_path}: {e}") from e

    for json_str in input_strings:
        try:
            parsed_json: JSONType = json.loads(json_str.strip())
            existing_data.append(parsed_json)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON string: {json_str}") from e

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, indent=indent, ensure_ascii=False)
    except OSError as e:
        raise OSError(f"Error writing to file {file_path}: {e}") from e

if __name__ == "__main__":
    example_json = """
    {
        "class": "Record",
        "path": "C:\\atari-monk\\code\\utility-scripts\\core\\task_log\\models\\record.py",
        "type": "model",
        "purpose": "Represents a work record with task details, time tracking, and validation for date, time, and descriptions.",
        "state": [
            "id",
            "date",
            "task_id",
            "description",
            "estimate_minutes",
            "start_time",
            "end_time",
            "actual_minutes",
            "note"
        ],
        "interface": [
            "__post_init__",
            "_calculate_actual_minutes",
            "get_table_string"
        ],
        "deps": {
            "internal": [
                "core.task_log.models.base_model.BaseModel",
                "core.utils.time_validator.validate_date_string",
                "core.utils.time_validator.validate_time_range",
                "core.utils.time_validator.validate_time_string"
            ],
            "external": [
                "typing.List",
                "dataclasses.dataclass"
            ]
        },
        "metrics": {
            "complexity": 10,
            "loc": 42
        }
    }
    """

    try:
        converted_json = convert_paths_to_json_safe(example_json)
        output_file = Path("output.json")
        append_json_strings_to_array(converted_json, output_file)
        print(f"Successfully processed and saved to {output_file}")
    except (ValueError, OSError) as e:
        print(f"Error: {e}")
