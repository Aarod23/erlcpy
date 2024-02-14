import httpx
import asyncio
import logging
from .Functions.Server.getPlayers import players
from .Functions.Server.getStatus import status
from .Functions.Server.getBans import bans
from .Functions.Server.getJoins import joinlogs
from .Functions.Server.getQueue import Queue
from .Functions.Server.runCmd import run_command
from .Functions.Server.getKills import killlogs
from .Functions.Server.getCmds import commands



class Server:
    def __init__(self, async_client):
        self.async_client = async_client
        
    async def players(self):
        """Fetches the ERLC server Players
                
        Parameters:
            None
                
        Returns:
            Tuple (status_code, data)
            """
        status_code, data = await players(self=self, async_client=self.async_client)
    
    async def status(self):
        """Fetches the ERLC server Status
                
        Parameters:
            None
                
        Returns:
            Tuple (status_code, data)
            """
        status_code, data = await status(self=self, async_client=self.async_client)
        
    async def bans(self):
        """Fetches the ERLC server Ban Logs
                
        Parameters:
            None
                
        Returns:
            Tuple (status_code, data)
            """
        status_code, data = await bans(self=self, async_client=self.async_client)
        
    async def joinlogs(self):
        """Fetches the ERLC server Join Logs
                
        Parameters:
            None
                
        Returns:
            Tuple (status_code, data)
            """
        status_code, data = await joinlogs(self=self, async_client=self.async_client)
    
    async def killlogs(self):
        """Fetches the ERLC server Kill Logs
                
        Parameters:
            None
                
        Returns:
            Tuple (status_code, data)
            """
        status_code, data = await killlogs(self=self, async_client=self.async_client)
    
    async def queue(self):
        """Fetches the ERLC server Queue
                
        Parameters:
            None
                
        Returns:
            Tuple (status_code, data)
            """
        status_code, data = await Queue(self=self, async_client=self.async_client)
        
    async def run_command(self, command: str):
        """Runs a command in the ERLC server
                
        Parameters:
            None
                
        Returns:
            Tuple (status_code, data)
            """
        status_code, data = await run_command(self=self, async_client=self.async_client, command=command)
    
    async def commandlogs(self):
        """Fetches the ERLC server Command Logs
                
        Parameters:
            None
                
        Returns:
            Tuple (status_code, data)
            """
        status_code, data = await commands(self=self, async_client=self.async_client)
        
        


        


        


        

