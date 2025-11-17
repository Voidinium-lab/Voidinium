"""
Example: IPFS Distributed Storage with Privacy
"""

import asyncio
from ipfs import IPFSClient, DistributedStorage


async def main():
    print("📦 IPFS Distributed Storage Example\n")
    
    # Create distributed storage
    storage = DistributedStorage()
    
    # Store private data
    data = b"Sensitive information that must remain private"
    
    print("Storing encrypted data to IPFS...")
    cid = await storage.store_private("my_secret", data)
    print(f"✅ Stored with CID: {cid}\n")
    
    # Retrieve private data
    print("Retrieving encrypted data from IPFS...")
    retrieved = await storage.retrieve_private("my_secret")
    print(f"✅ Retrieved: {len(retrieved)} bytes\n")
    
    print("Data stored and retrieved with end-to-end encryption!")


if __name__ == "__main__":
    asyncio.run(main())
