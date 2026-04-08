"""
采集器抽象基类。

所有数据源采集器继承此类，实现 collect() 方法。
统一返回标准化的论文/资源字典列表。
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import httpx


class BaseCollector(ABC):
    """采集器接口与通用 HTTP 客户端管理。"""

    def __init__(
        self,
        name: str,
        base_url: str = "",
        http_client: httpx.Client | None = None,
        timeout: float = 30.0,
    ):
        self.name = name
        self.base_url = base_url
        self._client = http_client
        self.timeout = timeout

    def _get_client(self) -> httpx.Client:
        if self._client is not None:
            return self._client
        return httpx.Client(timeout=self.timeout, follow_redirects=True)

    @abstractmethod
    def collect(self, query: str = "", **kwargs) -> list[dict[str, Any]]:
        """
        执行采集，返回标准化字典列表。

        论文记录至少应包含:
          - title: str
          - abstract: str
          - authors: list[str]
          - year: int
          - source: str
        """
        ...

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name='{self.name}')>"
