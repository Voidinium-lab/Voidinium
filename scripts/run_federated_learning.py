"""
Script to demonstrate federated learning with privacy
"""

import asyncio
import sys
sys.path.insert(0, '.')

from federated_learning import FederatedTrainer


async def main():
    print("=" * 60)
    print("🤖 VOIDINIUM - Federated Learning Demo")
    print("=" * 60)
    print()
    
    # Create federated trainer
    trainer = FederatedTrainer(
        model="neural_net",
        nodes=10,
        encryption="homomorphic"
    )
    
    # Train model
    model = await trainer.train_federated()
    
    print()
    print("📊 Final Model:")
    print(f"   Version: {model['version']}")
    print(f"   Weights: {len(model['weights'])} tensors")
    
    print()
    print("=" * 60)
    print("✅ Federated learning demo completed!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
