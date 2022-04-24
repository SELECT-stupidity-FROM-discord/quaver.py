Quaver.py
=========

.. image:: https://i.imgur.com/NB5D8o3.jpg

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

  
Documentation
=============

``class quaver.Quaver(session: Optional[aiohttp.ClientSession] = None)``
       - ``session:`` an existing session can be passed to Quaver class, else it will create a new session
       - This class can also be used as an async context manager
 
``await Quaver.get_users(name: Union[int, str, Union[Iterable[str], Iterable[int]]], full: bool = False)``
       - ``name:`` A username, user id, or a list of usernames and user ids
       - ``full`` Whether or not to fetch full information of the given usernames/ids
       
``await Quaver.search_users(search: str, full: bool = False)``
       - ``search:`` The string to search for in usernames
       - ``full:`` Whether or not to fetch full information of all the search results
   



