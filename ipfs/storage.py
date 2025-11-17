"""
Distributed Storage Layer with Privacy
"""

from typing import Dict, Optional
from .client import IPFSClient


class DistributedStorage:
    """
    Privacy-preserving distributed storage using IPFS
    """
    
    def __init__(self):
        self.ipfs = IPFSClient()
        self.index: Dict[str, str] = {}
        
    async def store_private(self, key: str, data: bytes) -> str:
        """Store data with encryption"""
        cid = await self.ipfs.add(data, encrypt=True)
        self.index[key] = cid
        return cid
        
    async def retrieve_private(self, key: str) -> Optional[bytes]:
        """Retrieve and decrypt data"""
        cid = self.index.get(key)
        if cid:
            return await self.ipfs.get(cid)
        return None
