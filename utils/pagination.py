from typing import Generic, List, TypeVar, Any
from pydantic import BaseModel, conint
from pydantic.generics import GenericModel


class PageParams(BaseModel):
    """ Request query params for paginated API. """
    page: conint(ge=1) = 1
    size: conint(ge=1, le=100) = 10


T = TypeVar("T")


class PagedResponseSchema(GenericModel, Generic[T]):
    """Response schema for any paged API."""

    total: int
    page: int
    size: int
    results: List[T]


def paginate(page_params: PageParams, query, response_schema: BaseModel | Any) -> PagedResponseSchema[T]:
    """Paginate the query."""

    paginated_query = query.offset((page_params.page - 1) * page_params.size).limit(page_params.size).all()

    return PagedResponseSchema(
        total=query.count(),
        page=page_params.page,
        size=page_params.size,
        results=[response_schema.from_orm(item) for item in paginated_query],
    )
