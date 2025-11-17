"""
Example: Multi-Party Secure Computation
"""

import asyncio
from Voidinium import VoidiniumOrchestrator, PrivateWorkflow


async def main():
    print("🤝 Multi-Party Secure Computation Example\n")
    
    # Setup orchestrator
    orchestrator = VoidiniumOrchestrator(
        mode="hybrid",
        swarm_size=3,
        privacy_level="maximum"
    )
    
    await orchestrator.initialize_swarm()
    
    # Define multi-party workflow
    workflow = PrivateWorkflow(
        name="multi_party_analytics",
        agents=["party_a", "party_b", "party_c"],
        privacy_constraints={
            "data_isolation": True,
            "result_sharing": "encrypted",
            "audit_trail": True
        }
    )
    
    print("\n🔒 Executing secure multi-party computation...")
    result = await orchestrator.execute(workflow)
    
    print(f"\n✅ Computation completed!")
    print(f"   All parties collaborated without exposing private data")
    print(f"   ZK Proof: {result['zk_proof'][:32]}...\n")
    
    await orchestrator.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
