from dataclasses import dataclass

@dataclass
class ChatGPTConfig:
    page: str
    config_path: str
    detach: bool = True
    delay_seconds: int = 10