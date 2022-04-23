from __future__ import annotations

from typing import Literal, Optional, Union

import aiohttp

from .errors import APIDown


class Route:
    BASE_URL = "https://api.quavergame.com/v1"

    __slots__ = ('url', 'method', 'params')

    def __init__(self, url, method, params) -> None:
        self.method = method
        self.url = url
        self.params = params

    @classmethod
    def create(cls, path: str, method: Literal['GET', 'POST'], params: Optional[Union[dict, aiohttp.MultiDict]] = None) -> Route:
        url = cls.BASE_URL + path
        return cls(url, method, params)


class HTTPClient:
    def __init__(self, session: aiohttp.ClientSession):
        self.__session: aiohttp.ClientSession = session

    async def _require_session(self) -> None:
        if not self.__session:
            self.__session = aiohttp.ClientSession()

    async def make_request(self, route: Route) -> aiohttp.ClientResponse:
        await self._require_session()
        async with self.__session.request(route.method, route.url, params=route.params) as response:
            print(response.url)
            if response.ok:
                return await response.json()
            elif response.status == 500:
                raise APIDown("API is down please try again later")
            else:
                raise Exception(f"{response.status} {response.reason}")

    async def close(self) -> None:
        if not self.__session.closed:
            await self.__session.close()

    
