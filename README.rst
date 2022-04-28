Quaver.py
=========

.. image:: https://i.imgur.com/NB5D8o3.jpg
    ..align:: center

Installing
----------

**Python 3.8 or higher is required**

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U quaver.py

    # Windows
    py -3 -m pip install -U quaver.py
..

Quick Startup
=============

.. code:: py

  import quaver
  import asyncio

  wave = quaver.Quaver()

  async def main():
      await wave.get_users('BiZee')
      await wave.get_users(['BiZee', 'Swan'], full=True)
    
  asyncio.run(main())

  
Documentation (Return Types)
============================

.. code:: py

    class quaver.Quaver(session=Optional[aiohttp.ClientSession]):

        # Attributes
        # ----------

            session: Optional[aiohttp.ClientSession]
                # - Optional session user can provide to use for requests, if not provided, a new session will be created.
        
        # Methods
        # -------
        
            await get_users(self, name: Union[str, int, Union[Iterable[int], Iterable[str]]], *, full: Optional[bool] = False) -> List[User]:

                # Parameters
                # ----------

                    name: Union[str, int, Union[Iterable[int], Iterable[str]]]
                        # - Name or id of user to get, or list of names/ids.

                    full: Optional[bool]
                        # - Whether to fetch full user data or not.
                    
                # Returns
                # -------

                    List[User]
                        # - List of users.
            
            await search_user(self, name: str, *, full: Optional[bool] = False) -> Union[User, List[User]]:
                    
                # Parameters
                # ----------
    
                    name: str
                        # - string to search for.
    
                    full: Optional[bool]
                        # - Whether to fetch full user data or not.
                        
                # Returns
                # -------
    
                    Union[User, List[User]]
                        # - User or list of users.

            await get_user_best(self, _id: Union[int, str], *, mode: Union[int, GameMode] = GameMode.FOUR_KEYS, paginate: bool = False, limit: int = 50) -> Optional[UserPlay]:

                # Parameters
                # ----------

                    _id: Union[int, str]
                        # - User id or name.

                    mode: Union[int, GameMode]
                        # - Game mode to get best plays for.
                        # - Default: GameMode.FOUR_KEYS - `value`=1

                    paginate: bool
                        # - Whether to paginate or not.

                    limit: int
                        # - Number of plays to get.
                    
                # Returns
                # -------

                    Optional[UserPlay]
                        # - User's best plays.

            await get_user_recent(self, _id: Union[int, str], *, mode: Union[int, GameMode] = GameMode.FOUR_KEYS, paginate: bool = False, limit: int = 50) -> Optional[UserPlay]:

                # Parameters
                # ----------

                    _id: Union[int, str]
                        # - User id or name.

                    mode: Union[int, GameMode]
                        # - Game mode to get recent plays for.
                        # - Default: GameMode.FOUR_KEYS - `value`=1

                    paginate: bool
                        # - Whether to paginate or not.

                    limit: int
                        # - Number of plays to get.
                    
                # Returns
                # -------

                    Optional[UserPlay]
                        # - User's recent plays.

                await get_user_firstplaces(self, _id: Union[int, str], *, mode: Union[int, GameMode] = GameMode.FOUR_KEYS, paginate: bool = False, limit: int = 50) -> Optional[UserPlay]:

                # Parameters
                # ----------

                    _id: Union[int, str]
                        # - User id or name.

                    mode: Union[int, GameMode]
                        # - Game mode to get first places for.
                        # - Default: GameMode.FOUR_KEYS - `value`=1

                    paginate: bool
                        # - Whether to paginate or not.

                    limit: int
                        # - Number of plays to get.

                # Returns
                # -------

                    Optional[UserPlay]
                        # - User's first places.



    class quaver.Achievements(**kwargs):

        # Attributes
        # ----------

            id: int
                # - The id of the achievement.
                # - Type: int

            steam_api_name: str
                # - The name of the achievement as it appears in the Steam API.
                # - Type: str

            name: str
                # - The name of the achievement in proper English.
                # - Type: str
        
            description: str
                # - The description of the achievement.
                # - Type: str
            
            difficulty: str
                # - The difficulty of the achievement.
                # - Type: str

            unlocked: bool
                # - Whether or not the achievement is unlocked by user.
                # - Type: bool

        # Methods
        # -------

            @classmethod from_dict(data: dict) -> quaver.Achievements:
                # - Creates an instance of the Achievements class from a dictionary.
                # - Type: dict -> quaver.Achievements
                # - Only meant to be used internally.

     class quaver.Map(**kwargs):

        # Attributes
        # ----------

            id: int
                # - The id of the map.
                # - Type: int

            name: str
                # - The name of the map.
                # - Type: str
            
            mapset_id: Optional[int]
                # - The id of the mapset the map belongs to.
                # - Type: int | None
            
            md5: Optional[str]
                # - The md5 hash of the map.
                # - Type: str | None
            
            artist: Optional[str]
                # - The artist of the map.
                # - Type: str | None
            
            creator_id: Optional[int]
                # - The id of the creator of the map.
                # - Type: int | None
            
            creator_username: Optional[str]
                # - The username of the creator of the map.
                # - Type: str | None
            
            ranked_status: Optional[str]
                # - The ranked status of the map.
                # - Type: str | None
            
            difficulty_name: Optional[str]
                # - The difficulty of the map.
                # - Type: str | None

        # Methods

            @classmethod from_dict(data: dict) -> quaver.Map:
                # - Creates an instance of the Map class from a dictionary.
                # - Type: dict -> quaver.Map
                # - Only meant to be used internally.

            await get_cover() -> str
                # - Gets the cover of the map.
                # if the mapset_id of the map is None, then mapset_id will be fetched from the API.
                # - Type: str
        

    quaver.PartialMap(**kwargs):

        # Attributes
        # ----------

        id: int
            # - The id of the map.
            # - Type: int

        name: Optional[str]
            # - The name of the map.
            # - Type: str | None
        
        mapset_id: Optional[int] = None
            # - The id of the mapset the map belongs to.
            # - Type: int | None

        md5: Optional[str]
            # - The md5 hash of the map.
            # - Type: str | None

        game_mode: Optional[GameMode]
            # - The game mode of the map.
            # - Type: GameMode | None

        difficulty_rating: Optional[float]
            # - The difficulty rating of the map.
            # - Type: float | None

        map: Optional[str]
            # - The map of the map.
            # - Type: str | None
        
    # Methods
    # -------

        @classmethod from_dict(data: dict) -> quaver.PartialMap:
            # - Creates an instance of the PartialMap class from a dictionary.
            # - Type: dict -> quaver.PartialMap
            # - Only meant to be used internally.

        async def get_cover():
            # - Gets the cover of the map.
            # if the mapset_id of the map is None, then mapset_id will be fetched from the API.
            # - Type: str

    class UserPlay(**kwargs):

        # Attributes
        # -----------

            id: int
                # - The id of the user.
                # - Type: int

            time: str
                # - The time the user played the map.
                # - Type: str

            mode: int
                # - The mode the user played the map in.
                # - Type: int

            mods: int
                # - The mods the user used to play the map.
                # - Type: int

            mods_string: str
                # - The mods the user used to play the map as a string.
                # - Type: str

            performance_rating: float
                # - The performance rating of the user.
                # - Type: float

            personal_best: bool
                # - Whether or not the play was a personal best.
                # - Type: bool

            is_donator_score: bool
                # - Whether or not the play was a donator score.
                # - Type: bool
            
            total_score: int
                # - The total score of the user.
                # - Type: int
            accuracy: float
                # - The accuracy of the user.
                # - Type: float

            grade: str
                # - The grade of the user.
                # - Type: str

            max_combo: int
                # - The max combo of the user.
                # - Type: int

            count_marv: int
                # - The count of marvellous's the user got.
                # - Type: int

            count_perf: int
                # - The count of perfect's the user got.
                # - Type: int

            count_great: int
                # - The count of great's the user got.
                # - Type: int

            count_good: int
                # - The count of good's the user got.
                # - Type: int

            count_okay: int
                # - The count of okay's the user got.
                # - Type: int

            count_miss: int
                # - The count of miss's the user got.
                # - Type: int

            scroll_speed: int
                # - The scroll speed of the user.
                # - Type: int

            tournament_game_id: int
                # - The id of the tournament game the user played in.
                # - Type: int
                
            ratio: float
                # - The ratio of the user.
                # - Type: float
            
            map: Map
                # - The map of the user.
                # - Type: quaver.Map

        # Methods
        # -------

            @classmethod from_dict(data: dict) -> UserPlay:
                # - Creates an instance of the UserPlay class from a dictionary.
                # - Type: dict -> quaver.UserPlay
                # - Only meant to be used internally.

    class quaver.PartialStats(**kwargs):

        # Attributes
        # -----------

            user_id: int
                # - The id of the user.
                # - Type: int

            total_score: int
                # - The total score of the user.
                # - Type: int

            ranked_score: int
                # - The ranked score of the user.
                # - Type: int

            overall_accuracy: float
                # - The overall accuracy of the user.
                # - Type: float

            overall_performance_rating: float
                # - The overall performance rating of the user.
                # - Type: float

            play_count: int
                # - The play count of the user.
                # - Type: int

            fail_count: int
                # - The fail count of the user.
                # - Type: int

            max_combo: int
                # - The max combo of the user.
                # - Type: int

            rank: Optional[int]
                # - The rank of the user.
                # - Type: int | None

        # Methods
        # -------

            @classmethod from_dict(data: dict) -> quaver.PartialStats:
                # - Creates an instance of the PartialStats class from a dictionary.
                # - Type: dict -> quaver.PartialStats
                # - Only meant to be used internally.

    class quaver.PartialUser(**kwargs):

        # Attributes
        # -----------



            

    
        
    


        



 



