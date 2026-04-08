from src.pipeline import CollectionPipeline


def test_pipeline_skips_disabled_source(tmp_path):
    pipeline = CollectionPipeline(db_path=str(tmp_path / "papers.db"))
    pipeline.settings["collection"]["source_policies"]["semantic_scholar"]["enabled"] = False

    summary = pipeline.collect(source="semantic_scholar", run_exports=False)

    assert summary["sources"]["semantic_scholar"]["status"] == "skipped"
    assert summary["sources"]["semantic_scholar"]["reason"] == "disabled_in_config"
