from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class ClientConfigs:
    timeout_sec: Optional[int] = None
    num_retries: Optional[int] = None
    headers: Optional[Dict] = None


@dataclass
class CompletionParams:
    prompt: str
