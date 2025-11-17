"""
Federated Learning with Privacy Guarantees
"""

from .trainer import FederatedTrainer
from .aggregator import SecureAggregator

__all__ = ["FederatedTrainer", "SecureAggregator"]
