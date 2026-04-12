from src.exporters.reading_list import ReadingListExporter


def test_reading_list_default_output_lives_in_shared_digests():
    exporter = ReadingListExporter()
    assert exporter.output_path.as_posix() == "digests/shared/reading_list.md"
