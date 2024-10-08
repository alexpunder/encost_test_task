from datetime import datetime, timezone

from src.schemas import FilterParams


async def convertation_datetime_to_microseconds(
    input_dt: datetime
) -> int:
    """
    Функция конвертирования строки в фармате datetime
    в формат Unix MicroSecond.
    """
    dt_utc = input_dt.astimezone(timezone.utc)
    return int(dt_utc.timestamp() * 1000)


async def combine_filtes_query(filters_query: FilterParams):
    """
    Функция формирования словаря с полями фильтрации для запроса.
    """
    data = {}

    if (query := filters_query.endpoint_id) is not None:
        data['endpoint_id'] = query

    if (query := filters_query.state_name) is not None:
        data['state_name'] = query

    if (query := filters_query.state_reason) is not None:
        data['state_reason'] = query

    if filters_query.state_start is not None:
        query = await convertation_datetime_to_microseconds(
            input_dt=filters_query.state_start,
        )
        data[f'state_start__{filters_query.state_start_choice.value}'] = query

    return data
