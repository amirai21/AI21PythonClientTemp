from dataclasses import dataclass
from typing import Optional, Dict, List, Tuple


@dataclass
class AI21StudioResponse:
    data: Dict
    headers: Dict
    execution_time: float

    def __str__(self):
        return f'AI21StudioResponse: execution_time: {self.execution_time} seconds, data: {self.data}, response headers: {self.headers}'


@dataclass
class ClientConfigs:
    api_host: Optional[int] = None
    timeout_sec: Optional[int] = None
    num_retries: Optional[int] = None
    headers: Optional[Dict] = None


@dataclass
class Penalty:
    scale: float
    applyToNumbers: Optional[bool] = False
    applyToPunctuations: Optional[bool] = False
    applyToStopwords: Optional[bool] = False
    applyToWhitespaces: Optional[bool] = False
    applyToEmojis: Optional[bool] = False


@dataclass
class CompletionParams:
    prompt: str
    numResults: Optional[int] = 1
    maxTokens: Optional[int] = 64
    topP: Optional[float] = 1
    topKReturn: Optional[int] = 0
    temperature: Optional[float] = 0.7
    stopSequences: Optional[List[str]] = None
    countPenalty: Optional[Penalty] = Penalty(scale=0)
    frequencyPenalty: Optional[Penalty] = Penalty(scale=0)
    presencePenalty: Optional[Penalty] = Penalty(scale=0)


@dataclass
class DatasetMetadata:
    dataset_name: str
    selected_columns: Optional[Tuple[str, str]] = None
    approve_whitespace_correction: Optional[bool] = False
    delete_long_rows: Optional[bool] = False
    split_ratio: Optional[float] = 0.1
