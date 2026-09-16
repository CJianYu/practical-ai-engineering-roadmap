from scripts.validate_roadmap import load_roadmap, validate


def test_roadmap_is_valid() -> None:
    assert validate(load_roadmap()) == []
