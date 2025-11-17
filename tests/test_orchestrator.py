"""
Tests for Orchestrator functionality
"""

import pytest
from Voidinium import VoidiniumOrchestrator, PrivateWorkflow


@pytest.mark.asyncio
async def test_orchestrator_initialization():
    """Test orchestrator can be initialized"""
    orchestrator = VoidiniumOrchestrator(
        mode="zk",
        swarm_size=3,
        privacy_level="high"
    )
    
    await orchestrator.initialize_swarm()
    
    assert orchestrator.initialized is True
    assert len(orchestrator.agents) == 3


@pytest.mark.asyncio
async def test_workflow_execution():
    """Test workflow can be executed"""
    orchestrator = VoidiniumOrchestrator()
    workflow = PrivateWorkflow(
        name="test_workflow",
        agents=["agent1", "agent2"]
    )
    
    result = await orchestrator.execute(workflow)
    
    assert result["status"] == "completed"
    assert result["privacy_verified"] is True


@pytest.mark.asyncio
async def test_orchestrator_shutdown():
    """Test orchestrator can be shut down"""
    orchestrator = VoidiniumOrchestrator()
    await orchestrator.initialize_swarm()
    await orchestrator.shutdown()
    
    assert orchestrator.initialized is False
    assert len(orchestrator.agents) == 0
