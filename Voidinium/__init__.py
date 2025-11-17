"""
Voidinium - Build with Privacy, Powered by ZK Swarm Intelligence

A zero-knowledge orchestrated swarm intelligence platform for privacy-preserving
collaborative computation.
"""

__version__ = "0.1.0"
__author__ = "Voidinium Team"

from .orchestrator import VoidiniumOrchestrator, SwarmConfig
from .workflow import PrivateWorkflow
from .agents import Agent, AgentConfig

__all__ = [
    "VoidiniumOrchestrator",
    "SwarmConfig",
    "PrivateWorkflow",
    "Agent",
    "AgentConfig",
]
