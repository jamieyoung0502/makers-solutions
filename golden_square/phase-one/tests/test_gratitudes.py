from lib.gratitudes import Gratitudes


def test_gratitudes_single_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("my health")
    result = gratitudes.format()
    assert result == "Be grateful for: my health"


def test_gratitudes_lists_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("my health")
    gratitudes.add("my family")
    result = gratitudes.format()
    assert result == "Be grateful for: my health, my family"
