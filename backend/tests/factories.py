import faker

from services.dto import Template


fake = faker.Faker()


def fake_template_id() -> int:
    return fake.pyint(min_value=0)


def fake_template_value() -> int:
    return fake.pyint()


def fake_template() -> Template:
    return Template(
        id=fake_template_id(),
        value=fake_template_value(),
    )
