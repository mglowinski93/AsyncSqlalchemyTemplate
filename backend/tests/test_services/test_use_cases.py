import pytest
from sqlalchemy.future import select

from persistence_layer import get_async_session, Template as TemplateDb
from services import (
    get_template,
    save_template,
    TemplateDoesntExist,
)
from services.mappers import map_template_dto_to_db
from .. import factories


@pytest.mark.asyncio
async def test_get_template_raises_exception_when_template_doesnt_exist(event_loop):
    with pytest.raises(TemplateDoesntExist):
        await get_template(
            template_id=factories.fake_template_id(),
        )


@pytest.mark.asyncio
async def test_get_template_returns_template_when_template_exist(event_loop):
    # Given
    faked_template = factories.fake_template()
    async with get_async_session() as async_session:
        async_session.add(map_template_dto_to_db(faked_template))

    # When
    template = await get_template(
        template_id=faked_template.id,
    )

    # Then
    assert faked_template == template


@pytest.mark.asyncio
async def test_save_template_saves_template(event_loop):
    # Given
    template = factories.fake_template()

    # When
    await save_template(
        template=template,
    )

    # Then
    async with get_async_session() as async_session:
        assert (
            await async_session.scalars(
                select(TemplateDb).where(TemplateDb.id == template.id)
            )
        ).first() is not None
