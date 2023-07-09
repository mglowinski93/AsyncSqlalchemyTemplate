from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.future import select

from persistence_layer import get_async_session, Template as TemplateDb
from .dto import Template as TemplateDto
from .exceptions import FailedToSaveTemplate, TemplateDoesntExist
from .mappers import map_template_db_to_dto, map_template_dto_to_db


async def save_template(template: TemplateDto):
    async with get_async_session() as async_session:
        async_session.add(map_template_dto_to_db(template))
        try:
            await async_session.flush()
        except IntegrityError as err:
            raise FailedToSaveTemplate(message=str(err)) from err


async def get_template(template_id: int) -> TemplateDto:
    async with get_async_session() as async_session:
        try:
            return map_template_db_to_dto(
                (
                    await async_session.scalars(
                        select(TemplateDb).where(TemplateDb.id == template_id)
                    )
                ).one()
            )
        except NoResultFound as err:
            raise TemplateDoesntExist(template_id) from err
