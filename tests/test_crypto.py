"""
Tests for cryptographic modules
"""

import pytest
from Voidinium.crypto import ZKProofSystem, HomomorphicEncryption, ThresholdKMS


@pytest.mark.asyncio
async def test_zk_proof_generation():
    """Test ZK proof can be generated"""
    zk = ZKProofSystem(proof_type="snark")
    
    statement = {"claim": "test"}
    witness = {"secret": "value"}
    
    proof = await zk.generate_proof(statement, witness)
    
    assert proof.startswith("zk_snark_proof_")


@pytest.mark.asyncio
async def test_zk_proof_verification():
    """Test ZK proof can be verified"""
    zk = ZKProofSystem()
    
    statement = {"claim": "test"}
    witness = {"secret": "value"}
    
    proof = await zk.generate_proof(statement, witness)
    is_valid = await zk.verify_proof(statement, proof)
    
    assert is_valid is True


def test_homomorphic_encryption():
    """Test homomorphic encryption"""
    he = HomomorphicEncryption(scheme="paillier")
    he.generate_keys()
    
    plaintext = 42
    ciphertext = he.encrypt(plaintext)
    decrypted = he.decrypt(ciphertext)
    
    assert str(decrypted) == str(plaintext)


def test_threshold_kms():
    """Test threshold key management"""
    kms = ThresholdKMS(threshold=3, total_shares=5)
    
    shares = kms.generate_key_shares()
    assert len(shares) == 5
    
    # Reconstruct with threshold shares
    key = kms.reconstruct_key(shares[:3])
    assert key.startswith("reconstructed_key_")
    
    # Should fail with insufficient shares
    with pytest.raises(ValueError):
        kms.reconstruct_key(shares[:2])
