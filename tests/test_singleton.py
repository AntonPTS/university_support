import pytest
from concurrent.futures import ThreadPoolExecutor
from singleton_variant.config import AppConfigSingleton
from singleton_variant.audit import AuditLoggerSingleton

def test_singleton_thread_safety():
    instances = []
    def fetch(): instances.append(AppConfigSingleton.get_instance("config.yaml"))
    with ThreadPoolExecutor(max_workers=10) as exe:
        list(exe.map(lambda _: fetch(), range(10)))
    assert all(i is instances[0] for i in instances), "Singleton не потокобезопасен!"

def test_singleton_state_leakage():
    cfg1 = AppConfigSingleton.get_instance()
    cfg2 = AppConfigSingleton.get_instance()
    assert cfg1 is cfg2  # Глобальный доступ: все получают один объект

def test_singleton_audit_integration():
    audit = AuditLoggerSingleton.get_instance()
    audit.log("S1", 1, "email", True)
    assert len(audit.logs) == 1