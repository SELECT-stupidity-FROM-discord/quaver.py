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

