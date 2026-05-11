import pytest
from unittest.mock import MagicMock
from di_variant.config import AppConfigDI
from di_variant.audit import AuditLoggerDI

def test_di_independence():
    cfg1 = AppConfigDI(audit_enabled=True)
    audit1 = AuditLoggerDI(cfg1, storage=[])
    
    cfg2 = AppConfigDI(audit_enabled=False)
    audit2 = AuditLoggerDI(cfg2, storage=[])
    
    assert cfg1 is not cfg2
    assert audit1.storage is not audit2.storage

def test_di_easy_mocking():
    mock_cfg = MagicMock(audit_enabled=True)
    mock_storage = []
    audit = AuditLoggerDI(mock_cfg, mock_storage)
    
    audit.log("S1", 1, "email", True)
    assert len(mock_storage) == 1
    
    mock_cfg.audit_enabled = False
    audit.log("S2", 2, "email", True)
    assert len(mock_storage) == 1  # Второй вызов пропущен без изменения глобального состояния

def test_di_composition_root():
    # Имитация DI-контейнера: один экземпляр на приложение, но без глобального доступа
    config = AppConfigDI.from_file("config.yaml")
    shared_storage = []
    audit = AuditLoggerDI(config, shared_storage)
    
    assert isinstance(audit.config, AppConfigDI)
    audit.log("S1", 1, "email", True)
    assert len(shared_storage) == 1