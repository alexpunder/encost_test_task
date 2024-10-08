from typing import Annotated

from fastapi import APIRouter, Query

from src.models import EndpointStates
from src.schemas import (FilterParams, SchemaEndpointStates, SchemaTask1,
                         SchemaTaskAnswer1)
from src.utils import (combine_filtes_query,
                       convertation_datetime_to_microseconds)

app = APIRouter(
    prefix='/task',
    tags=['Task']
)


@app.post(
    '/first',
    name='task:first',
    summary='Get an answer to the first question',
    response_model=SchemaTaskAnswer1
)
async def first_task(
    input_start: SchemaTask1,
):
    conv_dt = await convertation_datetime_to_microseconds(
        input_dt=input_start.input_start,
    )

    c_point = await (
        EndpointStates
        .all()
        .select_related('client', 'endpoint')
        .filter(state_start__gte=conv_dt, endpoint__id=139)
        .order_by('-state_start')
    )

    d_point = [query for query in c_point if query.id % 3 == 0]

    return {
        'filtered_count': len(d_point),
        'state_id': d_point[2].state_id,
    }


@app.get(
    '/second',
    name='task:second',
    summary='Get an answer to the second question',
    response_model=list[SchemaEndpointStates]
)
async def second_task(
    filter_query: Annotated[FilterParams, Query()]
):
    filters_data = await combine_filtes_query(
        filters_query=filter_query
    )

    return await (
        EndpointStates
        .all()
        .select_related('client', 'endpoint')
        .filter(**filters_data)
        .order_by('-state_start')
    )
