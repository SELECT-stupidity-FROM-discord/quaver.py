import asyncio
import datetime
from typing import Iterable, Optional, Union

import multidict

from quaver.errors import InvalidArgumentPassed

from .enums import GameMode, RankStatus
from .http import Route

__all__ = ('UserBasedRequests', 'MapsetsBasedRequests', 'LeaderboardBasedRequests', 'PlaylistBasedRequest', 'MapBasedRequests', 'MultiplayerBasedRequests', 'MiscBasedRequest')

class UserBasedRequests:
    

    async def _get_full_user(self, name: Union[int, str]):
        """
        Get the full user.

        Parameters
        ----------
        name: Union[int, str]
            The username or game ID of the user.

        Returns
        -------
        dict
            The user's information.

        Raises
        ------
        APIDown
            If the API is down.
        """
        route = Route.create(f'/users/full/{name}', 'GET')
        return await self._client.make_request(route)

    async def get_users(self, name: Union[Union[str, int], Iterable[Union[str, int]]], *, full: Optional[bool] = False) -> dict:
        """
        Function for getting users by their username or game ID.

        Parameters
        ----------
        name: Union[str, int] or Iterable[Union[str, int]]
            The username or game ID of the user.
        full: Optional[bool]
            Whether or not to fetch the full user.

        Returns
        -------
        dict
            The user's information.

        Raises
        ------
        InvalidArgumentPassed
            If the argument passed is not an integer, string or an iterable of integer or strings.
        APIDown
            If the API is down.
        """
        if isinstance(name, str):
            parameters = {'name': name}
        elif isinstance(name, Iterable):
            args = []
            for username in name:
                if isinstance(username, str):
                    args.append(('name', username))
                elif isinstance(username, int):
                    args.append(('id', username))
                else:
                    raise InvalidArgumentPassed(
                        f'{username} is not a valid argument for the username.')
            parameters = multidict.MultiDict(args)
        elif isinstance(name, int):
            parameters = {'id': name}
        else:
            raise InvalidArgumentPassed(
                "The name argument must be a string, int or an iterable of strings or ints. Got, %s" % type(name).__name__)
        if full:
            return await asyncio.gather(*[self._get_full_user(username) for username in parameters.values()])
        else:
            path = '/users'
        return await self._client.make_request(
            Route.create(path, 'GET', parameters)
        )

    async def search_user(self, name: str, *, fetch_full: Optional[bool] = False) -> dict:
        """
        Function to search for a specific user containing a string.

        Parameters
        ----------
        name: str
            The string to search for.
        fetch_full: Optional[bool]
            Whether or not to fetch the full user.

        Returns
        -------
        dict
            The user's information.

        Raises
        ------
        APIDown
            If the API is down.
        """
        route = Route.create(f'users/search/{name}', 'GET')
        response = await self._client.make_request(route)
        if fetch_full:
            usernames = [json['username'] for json in response['users']]
            return await self.get_users(*usernames, full=True)
        else:
            return response

    async def get_user_best(self, _id: Union[int, str], *, mode: int = GameMode.FOUR_KEYS.value, paginate: bool = False, limit: int = 50) -> dict:
        """
        Function to get the best scores of a user.

        Parameters
        ----------
        id: int
            The user's ID. If the username is passed, the ID will be fetched from the API.
        mode: int
            The mode to get the best scores for.
        paginate: bool
            Whether or not to paginate the results.
        limit: int
            The amount of results to return.

        Returns
        -------
        dict
            The best scores of the user.

        Raises
        ------
        APIDown
            If the API is down.
        """
        payload = {}
        if isinstance(_id, int):
            payload['id'] = _id
        elif isinstance(_id, str):
            json = await self.get_users(_id)
            payload['id'] = json['users'][0]['id']
        payload['page'] = int(paginate)
        payload['limit'] = limit if limit <= 50 else 50
        payload['mode'] = mode.value if isinstance(mode, GameMode) else (
            mode if mode in range(1, 3) else GameMode.FOUR_KEYS.value)
        return await self._client.make_request(
            Route.create(f'/users/scores/best', 'GET', payload)
        )

    async def get_user_recent(self, _id: Union[int, str], *, mode: int = GameMode.FOUR_KEYS.value, paginate: bool = False, limit: int = 50) -> dict:
        """
        Function to get the recent scores of a user.

        Parameters
        ----------
        id: int
            The user's ID. If the username is passed, the ID will be fetched from the API.
        mode: int
            The mode to get the best scores for.
        paginate: bool
            Whether or not to paginate the results.
        limit: int
            The amount of results to return.

        Returns
        -------
        dict
            The recent scores of the user.

        Raises
        ------
        APIDown
            If the API is down.
        """
        payload = {}
        if isinstance(_id, int):
            payload['id'] = _id
        elif isinstance(_id, str):
            json = await self.get_users(_id)
            payload['id'] = json['users'][0]['id']
        payload['page'] = int(paginate)
        payload['limit'] = limit if limit <= 50 else 50
        payload['mode'] = mode.value if isinstance(mode, GameMode) else (
            mode if mode in range(1, 3) else GameMode.FOUR_KEYS.value)
        return await self._client.make_request(
            Route.create(f'/users/scores/recent', 'GET', payload)
        )

    async def get_user_firstplace(self, _id: Union[int, str], *, mode: int = GameMode.FOUR_KEYS.value, paginate: bool = False, limit: int = 50) -> dict:
        """
        Function to get the first place scores user has

        Parameters
        ----------
        id: int
            The user's ID. If the username is passed, the ID will be fetched from the API.
        mode: int
            The mode to get the best scores for.
        paginate: bool
            Whether or not to paginate the results.
        limit: int
            The amount of results to return.


        Returns
        -------
        dict
            The first place scores of the user.

        Raises
        ------
        APIDown
            If the API is down.
        InvalidArgumentPassed
            If the id is not an integer or a string.
        """
        payload = {}
        if isinstance(_id, int):
            payload['id'] = _id
        elif isinstance(_id, str):
            json = await self.get_users(_id)
            payload['id'] = json['users'][0]['id']
        else:
            raise InvalidArgumentPassed(
                f'{_id} is not a valid argument for the id.')
        payload['page'] = int(paginate)
        payload['limit'] = limit if limit <= 50 else 50
        payload['mode'] = mode.value if isinstance(mode, GameMode) else (
            mode if mode in range(1, 3) else GameMode.FOUR_KEYS.value)
        return await self._client.make_request(
            Route.create(f'/users/scores/firstplace', 'GET', payload)
        )

    async def user_mapsets(self, _id: Union[str, int], *, mode=GameMode.FOUR_KEYS.value, status: Optional[int] = None, paginate: bool = False) -> dict:
        """
        Function to get the mapsets of a user.

        Parameters
        ----------
        id: int
            The user's ID. If the username is passed, the ID will be fetched from the API.
        mode: int
            The mode to get the best scores for.
        status: int
            The status of the mapsets to get.
        paginate: bool
            Whether or not to paginate the results.

        Returns
        -------
        dict
            The mapsets of the user.

        Raises
        ------
        APIDown
            If the API is down.
        """
        payload = {}
        payload['page'] = int(paginate)
        if status:
            payload['status'] = status.value if isinstance(status, RankStatus) else (
                status if status in range(1, 3) else RankStatus.RANKED.value)
        payload['mode'] = mode.value if isinstance(mode, GameMode) else (
            mode if mode in range(1, 3) else GameMode.FOUR_KEYS.value)
        return await self._client.make_request(
            Route.create(f'/users/mapsets/{_id}', 'GET', payload)
        )

    async def get_user_graph(self, _id: Union[str, int], *, mode: Union[GameMode, int] = GameMode.FOUR_KEYS.value):
        """
        Function to get the graph of a user.

        Parameters
        ----------
        id: int
            The user's ID. If the username is passed, the ID will be fetched from the API.
        mode: int
            The mode to get the best scores for.

        Returns
        -------
        dict
            The graph of the user.

        Raises
        ------
        APIDown
            If the API is down.
        """
        payload = {}
        if isinstance(_id, int):
            payload['id'] = _id
        elif isinstance(_id, str):
            json = await self.get_users(_id)
            payload['id'] = json['users'][0]['id']
        else:
            raise InvalidArgumentPassed(
                f'{_id} is not a valid argument for the id.')
        payload['mode'] = mode.value if isinstance(mode, GameMode) else (
            mode if mode in range(1, 3) else GameMode.FOUR_KEYS.value)
        return await self._client.make_request(
            Route.create(f'/users/graph/rank', 'GET', payload)
        )

    async def get_user_playlist(self, _id: Union[str, int]):
        if isinstance(_id, int):
            pass
        elif isinstance(_id, str):
            json = await self.get_users(_id)
            _id = json['users'][0]['id']
        else:
            raise InvalidArgumentPassed(
                f'{_id} is not a valid argument for the id.')
        return await self._client.make_request(
            Route.create(f'/users/{_id}/playlists', 'GET')
        )

    async def check_song_in_user_playlist(self, _id: Union[str, int], map_id: int):
        if isinstance(_id, int):
            pass
        elif isinstance(_id, str):
            json = await self.get_users(_id)
            _id = json['users'][0]['id']
        else:
            raise InvalidArgumentPassed(
                f'{_id} is not a valid argument for the id.')
        return await self._client.make_request(
            Route.create(f'/users/{_id}/playlists/map/{map_id}', 'GET')
        )

    async def get_user_achievements(self, _id: Union[str, int]):
        if isinstance(_id, int):
            pass
        elif isinstance(_id, str):
            json = await self.get_users(_id)
            _id = json['users'][0]['id']
        else:
            raise InvalidArgumentPassed(
                f'{_id} is not a valid argument for the id.')
        return await self._client.make_request(
            Route.create(f'/users/{_id}/achievements', 'GET')
        )


class MapsetsBasedRequests:
    

    async def get_ranked_maps(self):
        """
        Function to get ids of all the ranked mapsets in Quaver.

        Returns
        -------
        dict
            The ranked maps ids.

        Raises
        ------
        APIDown
            If the API is down.
        """
        return await self._client.make_request(
            Route.create('/mapsets/ranked', 'GET')
        )

    async def get_mapsets_pending(self, *, paginate: bool = False, mode: Union[RankStatus, int] = RankStatus.RANKED.value) -> dict:
        """
        Function to get ids of all the pending mapsets in Quaver.

        Returns
        -------
        dict
            The pending maps ids.

        Raises
        ------
        APIDown
            If the API is down.
        """
        payload = {}
        payload['page'] = int(paginate)
        payload['mode'] = mode.value if isinstance(mode, RankStatus) else (
            mode if mode in range(1, 3) else RankStatus.RANKED.value)
        return await self._client.make_request(
            Route.create('/mapsets/queue', 'GET', payload)
        )

    async def get_mapset_data(self, ids: Union[int, list[int]]):
        if isinstance(ids, int):
            return await self._client.make_request(
                Route.create(f'/mapsets/{ids}', 'GET')
            )
        routes = [Route.create(f'/mapsets/{id}', 'GET') for id in ids]
        return await asyncio.gather(*[self._client.make_request(route) for route in routes])

    async def search_mapset(
        self,
        search: str,
        *,
        mode: Union[GameMode, int],
        status: Union[RankStatus, int],
        pagination: Optional[bool] = False,
        limit: Optional[int] = 50,
        mindiff: Optional[int] = None,
        maxdiff: Optional[int] = None,
        minbpm: Optional[int] = None,
        maxbpm: Optional[int] = None,
        minlns: Optional[int] = None,
        maxlns: Optional[int] = None,
        minplaycount: Optional[int] = None,
        maxplaycount: Optional[int] = None,
        mindate: Optional[datetime.datetime],
        maxdate: Optional[datetime.datetime]
    ):
        payload = {}

        payload['search'] = search

        if isinstance(mode, GameMode):
            mode = mode.value
        if isinstance(status, RankStatus):
            status = status.value
        payload['mode'] = int(mode)
        payload['status'] = int(status)
        payload['page'] = int(pagination)
        payload['limit'] = int(limit)

        if mindiff is not None:
            payload['mindiff'] = int(mindiff)
        if maxdiff is not None:
            payload['maxdiff'] = int(maxdiff)
        if minbpm is not None:
            payload['minbpm'] = int(minbpm)
        if maxbpm is not None:
            payload['maxbpm'] = int(maxbpm)

        if minlns is not None:
            payload['minlns'] = int(minlns)
        if maxlns is not None:
            payload['maxlns'] = int(maxlns)

        if minplaycount is not None:
            payload['minplaycount'] = int(minplaycount)
        if maxplaycount is not None:
            payload['maxplaycount'] = int(maxplaycount)

        if mindate is not None:
            payload['mindate'] = int(mindate.timestamp())
        if maxdate is not None:
            payload['maxdate'] = int(maxdate.timestamp())

        return await self._client.make_request(
            Route.create('/mapsets/maps/search', 'GET', payload)
        )

    async def get_map_comments(self, map_id: int):
        return await self._client.make_request(
            Route.create(f'/mapsets/{map_id}/comments', 'GET')
        )


class MapBasedRequests:

    async def get_map(self, map_id: Union[int, str]):
        """
        Function to get a map by its id.

        Parameters
        ----------
        map_id: Union[int, str]
            The id of the map to get or the md5 hash of the map.
        """
        return await self._client.make_request(
            Route.create(f'/maps/{map_id}/', 'GET')
        )

    async def get_map_scores(self, map_id: int):
        """
        Function to get scores of a map.

        Parameters
        ----------
        map_id: int
            The id of the map to get scores of.
        """
        return await self._client.make_request(
            Route.create(f'/scores/map/{map_id}/', 'GET')
        )

    async def get_hit_graph(self, score_id: int):
        """
        Function to get the hit graph of a score.

        Parameters
        ----------
        score_id: int
            The id of the score to get the hit graph of.
        """
        return await self._client.make_request(
            Route.create(f'/scores/data/{score_id}', 'GET')
        )


class LeaderboardBasedRequests:
    

    async def get_leaderboard(self, *, country: Optional[str] = None, mode: Union[GameMode, int] = GameMode.FOUR_KEYS.value, pagination: bool = False):
        """
        Function to get the leaderboard.

        Parameters
        ----------
        mode: Union[GameMode, int]
            The mode of the leaderboard.
        pagination: bool
            Whether or not to paginate the leaderboard.
        """
        payload = {}
        payload['mode'] = int(mode)
        payload['page'] = int(pagination)
        if country:
            payload['country'] = country
        return await self._client.make_request(
            Route.create('/leaderboards', 'GET', payload)
        )

    async def get_leaderboard_hits(self, pagination: bool = False):
        """
        Function to get the leaderboard hits.
        """
        payload = {}
        payload['page'] = int(pagination)
        return await self._client.make_request(
            Route.create('/leaderboards/hits', 'GET', payload)
        )


class PlaylistBasedRequest:
    

    async def get_playlist(self, playlist_id: int):
        """
        Function to get a playlist by its id.

        Parameters
        ----------
        playlist_id: int
            The id of the playlist to get.
        """
        return await self._client.make_request(
            Route.create(f'/playlists/{playlist_id}', 'GET')
        )

    async def get_playlist_maps(self, playlist_id: int):
        """
        Function to get maps of a playlist.

        Parameters
        ----------
        playlist_id: int
            The id of the playlist to get maps of.
        """
        return await self._client.make_request(
            Route.create(f'/playlists/{playlist_id}/maps', 'GET')
        )

    async def search_playlist(self, search: str, *, paginate: bool = False):
        """
        Function to search playlists.

        Parameters
        ----------
        search: str
            The search query.
        paginate: bool
            Whether or not to paginate the search.
        """
        payload = {}
        payload['search'] = search
        if paginate:
            payload['page'] = int(paginate)
        return await self._client.make_request(
            Route.create('/playlists/all/search', 'GET', payload)
        )


class MultiplayerBasedRequests:
    

    async def get_multiplayer_rooms(self):
        """
        Function to get all the active multiplayer rooms.

        Parameters
        ----------
        paginate: bool
            Whether or not to paginate the rooms.
        """
        return await self._client.make_request(
            Route.create('/multiplayer/games', 'GET')
        )

    async def get_multiplayer_room(self, room_id: int):
        """
        Function to get a multiplayer room by its id.

        Parameters
        ----------
        room_id: int
            The id of the room to get.
        """
        return await self._client.make_request(
            Route.create(f'/multiplayer/games/{room_id}', 'GET')
        )

    async def get_multiplayer_room_members(self, room_id: int):
        """
        Function to get the members of a multiplayer room.

        Parameters
        ----------
        room_id: int
            The id of the room to get the members of.
        """
        return await self._client.make_request(
            Route.create(f'/multiplayer/games/{room_id}/live', 'GET')
        )

    async def get_multiplayer_leaderboard(self, *, paginate: bool = False, mode: Union[GameMode, int] = GameMode.FOUR_KEYS.value):
        """
        Function to get the leaderboard of multiplayer wins.

        Parameters
        ----------
        room_id: int
            The id of the room to get the leaderboard of.
        """
        payload = {}
        payload['mode'] = int(mode)
        payload['page'] = int(paginate)
        return await self._client.make_request(
            Route.create(f'/multiplayer/leaderboard', 'GET', payload)
        )

    async def get_one_match(self, match_id: int):
        """
        Function to get a match by its id.

        Parameters
        ----------
        match_id: int
            The id of the match to get.
        """
        return await self._client.make_request(
            Route.create(f'/multiplayer/match/{match_id}', 'GET')
        )


class MiscBasedRequest:
    

    async def get_team(self):
        """
        Function to get the team which is the part of Quaver

        Parameters
        ----------
        team_id: int
            The id of the team to get.
        """
        return await self._client.make_request(
            Route.create(f'/team', 'GET')
        )

    async def get_server_stats(self):
        """
        Function to get the server stats.
        """
        return await self._client.make_request(
            Route.create(f'/stats', 'GET')
        )

    async def get_country_stats(self):
        """
        Function to get the country stats.
        """
        return await self._client.make_request(
            Route.create(f'/stats/country', 'GET')
        )
