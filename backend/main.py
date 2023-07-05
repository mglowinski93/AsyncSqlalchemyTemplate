import asyncio

from services.use_cases import save, get
from services.dto import Template


async def main():
    await save(Template(id=1, value=1))
    await get(template_id=1)


if __name__ == "__main__":
    asyncio.run(main())
