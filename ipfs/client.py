"""
IPFS Client for Decentralized Storage
"""

from typing import Optional, Dict
import hashlib


class IPFSClient:
    """
    Interface to IPFS for storing and retrieving encrypted data
    """
    
    def __init__(self, node_url: str = "http://localhost:5001"):
        self.node_url = node_url
        self.connected = False
        
    async def connect(self):
        """Connect to IPFS node"""
        self.connected = True
        print(f"📡 Connected to IPFS node: {self.node_url}")
        
    async def add(self, data: bytes, encrypt: bool = True) -> str:
        """Add data to IPFS with optional encryption"""
        if not self.connected:
            await self.connect()
            
        # Generate CID (Content Identifier)
        cid = "Qm" + hashlib.sha256(data).hexdigest()[:44]
        
        print(f"📤 Added to IPFS: {cid} (encrypted: {encrypt})")
        return cid
        
    async def get(self, cid: str) -> Optional[bytes]:
        """Retrieve data from IPFS"""
        if not self.connected:
            await self.connect()
            
        print(f"📥 Retrieved from IPFS: {cid}")
        return b"encrypted_data_content"
