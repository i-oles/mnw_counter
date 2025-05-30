from unittest.mock import patch

from project.core.mnw_provider import MNWProvider, separate_sets_and_singles


@patch("os.walk")
def test_get_objects_signatures(mock_os_walk):
    mock_os_walk.return_value = [
        (
            "some/dir",
            [],
            [
                "szm123_1mnw(1).tif",
                "szm123_1mnw(2).tif",
                "szm123_2mnw(1).tif",
                "szm123_2mnw(2).tif",
                "szm123_2mnw(3).tif",
                "szm123_1-2mnw(1).tif",
                "szm123_1-2mnw(2).tif",
                "szm123_a-bmnw(1).tif",
                "szm123_a-bmnw(2).tif",
                "szm123_a-bmnw(3).tif",
                "szm123_a-bmnw!a(1).tif",
                "szm123_a-bmnw!a(2).tif",
                "szm123_a-bmnw!b(1).tif",
                "szm123_a-bmnw!b(2).tif",
                "szm123_1mmw(1).tif",
                "szm123_1mmw(2).tif",
                "szm123_111(1).tif",
                "szm123_111(2).tif",
            ],
        )
    ]

    provider = MNWProvider("some/dir", "tif")
    got = provider.get_objects_signatures()

    want = sorted(["szm123_1", "szm123_2", "szm123_a-b", "szm123_1-2"])
    assert got == want


def test_separate_sets_and_singles():
    got1, got2 = separate_sets_and_singles(
        [
            "szm123_1",
            "szm123_2",
            "szm123_1-2",
            "szm123_a-b",
            "szm123_a-b",
        ]
    )
    want1 = ["szm123_1", "szm123_2", "szm123_a-b"]
    want2 = ["szm123_1-2"]
    assert got1 == want1
    assert got2 == want2
