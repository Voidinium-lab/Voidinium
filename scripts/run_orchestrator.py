"""
Script to run the Voidinium orchestrator
"""

import asyncio
import sys
sys.path.insert(0, '.')

from Voidinium import VoidiniumOrchestrator, PrivateWorkflow


async def main():
    print("=" * 60)
    print("🌌 VOIDINIUM - ZK Swarm Intelligence Platform")
    print("   Build with Privacy, Powered by ZK")
    print("=" * 60)
    print()
    
    # Create orchestrator
    orchestrator = VoidiniumOrchestrator(
        mode="zk",
        swarm_size=5,
        privacy_level="maximum"
    )
    
    # Initialize swarm
    await orchestrator.initialize_swarm()
    
    print()
    
    # Create and execute a workflow
    workflow = PrivateWorkflow(
        name="secure_analytics",
        agents=["data_processor", "model_trainer", "aggregator"]
    )
    
    result = await orchestrator.execute(workflow)
    
    print()
    print("📊 Result:")
    print(f"   Status: {result['status']}")
    print(f"   Privacy Verified: {result['privacy_verified']}")
    print(f"   ZK Proof: {result['zk_proof'][:32]}...")
    
    print()
    
    # Shutdown
    await orchestrator.shutdown()
    
    print()
    print("=" * 60)
    print("✅ Voidinium demo completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
