from pathlib import Path
from utils.json_utils import append_json_strings_to_array, convert_paths_to_json_safe

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
