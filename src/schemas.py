from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class SchemaTask1(BaseModel):
    input_start: datetime

    model_config = ConfigDict(
        json_schema_extra={
            'example': {'input_start': '2023-12-20T22:39:40'}
        }
    )


class SchemaTaskAnswer1(BaseModel):
    filtered_count: int
    state_id: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'filtered_count': 13,
                'state_id': (
                    'Опоздание|SimpleManualState|cid=139|'
                    'eid=139|chid=-1001921701685|mt=2024-02-09 10:16:23'
                )
            }
        }
    )


class StateStartChoice(StrEnum):
    gte = 'gte'
    gt = 'gt'
    lte = 'lte'
    lt = 'lt'


class FilterParams(BaseModel):
    endpoint_id: int = Field(None)
    state_name: str = Field(None)
    state_reason: str = Field(None)
    state_start: datetime = Field(None)
    state_start_choice: StateStartChoice = Field(default=StateStartChoice.gte)

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'endpoint_id': 139,
                'state_name': '',
                'state_reason': 'Опоздание',
                'state_start': '2024-01-30T08:57:56',
            }
        }
    )


class SchemaClient(BaseModel):
    id: int
    client_name: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 139,
                'client_name': 'Client'
            }
        }
    )


class SchemaEndpoint(BaseModel):
    id: int
    endpoint_name: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
                'endpoint_name': 'endpoint_4'
            }
        }
    )


class SchemaEndpointStates(BaseModel):
    id: int
    endpoint: SchemaEndpoint
    client: SchemaClient
    state_name: str
    state_reason: str
    state_start: int
    state_end: int | None = None
    state_id: str
    group_id: str
    reason_group: str | None = None
    info: dict[Any, Any] | None = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            'example': {
                'id': 139,
                'endpoint': {
                    'id': 1,
                    'endpoint_name': 'endpoint_4'
                },
                'client': {
                    'id': 139,
                    'client_name': 'Client'
                },
                'state_name': 'Поломка',
                'state_reason': 'Поломка',
                'state_start': 1707836222000,
                'state_end': 1707936154000,
                'state_id': 'Поломка|...|mt=2024-02-13 17:57:02',
                'group_id': 'Поломка|...|mt=2024-02-13 17:57:02',
                'reason_group': 'Техобслуживание',
                'info': {}
            }
        }
    )
