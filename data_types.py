from dataclasses import dataclass
from typing import Optional


@dataclass
class ClientConfigs:
    timeout_sec: Optional[int]
    num_retries: Optional[int]
