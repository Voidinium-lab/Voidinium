"""
Tests for federated learning modules
"""

import pytest
from federated_learning import FederatedTrainer, SecureAggregator


@pytest.mark.asyncio
async def test_federated_trainer():
    """Test federated trainer initialization and training"""
    trainer = FederatedTrainer(
        model="test_model",
        nodes=5,
        encryption="homomorphic"
    )
    
    model = await trainer.train_federated()
    
    assert model["version"] == 5  # 5 rounds
    assert len(model["weights"]) == 10


@pytest.mark.asyncio
async def test_secure_aggregator():
    """Test secure aggregation"""
    aggregator = SecureAggregator(privacy_budget=1.0)
    
    updates = [
        {"node_id": i, "update": f"update_{i}"}
        for i in range(5)
    ]
    
    result = await aggregator.aggregate(updates)
    
    assert result["participants"] == 5
    assert result["privacy_loss"] < 1.0
