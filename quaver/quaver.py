from typing import Optional

import aiohttp

from .http import HTTPClient
from .models import (LeaderboardBasedRequests, MapBasedRequests,
                     MapsetsBasedRequests, MiscBasedRequest,
                     MultiplayerBasedRequests, PlaylistBasedRequest,
                     UserBasedRequests)

__all__ = ('Quaver',)


class Quaver (
        UserBasedRequests, MapsetsBasedRequests,
        LeaderboardBasedRequests, PlaylistBasedRequest,
        MapBasedRequests, MultiplayerBasedRequests,
        MiscBasedRequest
):
    __slots__ = ('_client',)

    def __init__(self, session: Optional[aiohttp.ClientSession] = None):
        """
        The class for the Quaver API.

        Parameters
        ----------
        session: Optional[aiohttp.ClientSession]
            The session to use for the HTTPClient to send requests to the API.

        Raises
        ------
        APIDown
            If the API is down.

        Attributes
        ----------
        _client: HTTPClient
            The HTTPClient to use for sending requests to the API.
        """
        self._client = HTTPClient(session)

    async def close(self) -> None:
        """
        Closes the HTTPClient.
        """
        await self._client.close()

    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
        
