"""YouTube Data API 采集器。"""

from __future__ import annotations

from typing import Any

from src.utils.helpers import get_env, parse_datetime

from .base import BaseCollector


class YouTubeCollector(BaseCollector):
    def __init__(self, http_client=None):
        super().__init__(
            "youtube",
            base_url="https://www.googleapis.com/youtube/v3",
            http_client=http_client,
        )

    def collect(
        self,
        query: str = "",
        max_results: int = 5,
        channels: dict[str, list[dict[str, Any]]] | None = None,
        **_: Any,
    ) -> list[dict[str, Any]]:
        api_key = get_env("YOUTUBE_API_KEY")
        if not api_key:
            return []

        if channels:
            results: list[dict[str, Any]] = []
            for channel_group in channels.values():
                for channel in channel_group:
                    topic_key = (channel.get("topics") or [""])[0]
                    query_source = (
                        "search_terms"
                        if channel.get("search_terms")
                        else "relevant_playlists"
                        if channel.get("relevant_playlists")
                        else "fallback"
                    )
                    search_terms = channel.get("search_terms") or channel.get("relevant_playlists") or [query or channel["name"]]
                    for search_term in search_terms[:2]:
                        results.extend(
                            self._search_videos(
                                api_key=api_key,
                                query=search_term,
                                channel_id=channel.get("channel_id", ""),
                                max_results=max_results,
                                topic_key=topic_key,
                                channel_label=channel.get("name", ""),
                                query_source=query_source,
                            )
                        )
            return results

        return self._search_videos(api_key=api_key, query=query, max_results=max_results, topic_key="")

    def _search_videos(
        self,
        api_key: str,
        query: str,
        channel_id: str = "",
        max_results: int = 5,
        topic_key: str = "",
        channel_label: str = "",
        query_source: str = "",
    ) -> list[dict[str, Any]]:
        search_params = {
            "part": "snippet",
            "type": "video",
            "order": "date",
            "maxResults": max_results,
            "q": query,
            "key": api_key,
        }
        if channel_id:
            search_params["channelId"] = channel_id

        client = self._get_client()
        should_close = client is not self._client
        try:
            search_response = client.get(f"{self.base_url}/search", params=search_params)
            search_response.raise_for_status()
            search_payload = search_response.json()
            video_ids = [
                item["id"]["videoId"]
                for item in search_payload.get("items", [])
                if item.get("id", {}).get("videoId")
            ]
            if not video_ids:
                return []

            video_response = client.get(
                f"{self.base_url}/videos",
                params={
                    "part": "snippet,contentDetails,statistics",
                    "id": ",".join(video_ids),
                    "key": api_key,
                },
            )
            video_response.raise_for_status()
            payload = video_response.json()
        finally:
            if should_close:
                client.close()

        return [
            self._parse_video(
                item,
                topic_key=topic_key,
                matched_query=query,
                channel_label=channel_label,
                query_source=query_source,
            )
            for item in payload.get("items", [])
        ]

    @staticmethod
    def _parse_video(
        item: dict[str, Any],
        topic_key: str,
        matched_query: str,
        channel_label: str,
        query_source: str,
    ) -> dict[str, Any]:
        snippet = item.get("snippet", {})
        statistics = item.get("statistics", {})
        published_at = parse_datetime(snippet.get("publishedAt"))
        video_id = item.get("id", "")
        return {
            "title": snippet.get("title", ""),
            "channel_name": channel_label or snippet.get("channelTitle", ""),
            "channel_id": snippet.get("channelId", ""),
            "video_id": video_id,
            "playlist_id": None,
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "description": snippet.get("description", ""),
            "published_at": published_at,
            "duration": (item.get("contentDetails") or {}).get("duration", ""),
            "view_count": int(statistics.get("viewCount", 0) or 0),
            "topic_key": topic_key,
            "resource_type": "video",
            "matched_query": matched_query,
            "query_source": query_source,
        }
