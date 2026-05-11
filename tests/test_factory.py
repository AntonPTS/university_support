import pytest, sys, os
from notifications.factory import ProviderAFamily, ProviderBFamily
from notifications.providers.provider_a import AuthA, SerializerA, ErrorHandlerA, ClientA
from notifications.providers.provider_b import AuthB, SerializerB, ErrorHandlerB, ClientB

def test_provider_a_family_creates_a_components():
    family = ProviderAFamily()
    assert isinstance(family.create_auth(), AuthA)
    assert isinstance(family.create_serializer(), SerializerA)
    assert isinstance(family.create_error_handler(), ErrorHandlerA)
    assert isinstance(family.create_client(), ClientA)

def test_provider_b_family_creates_b_components():
    family = ProviderBFamily()
    assert isinstance(family.create_auth(), AuthB)
    assert isinstance(family.create_serializer(), SerializerB)
    assert isinstance(family.create_error_handler(), ErrorHandlerB)
    assert isinstance(family.create_client(), ClientB)

def test_a_components_are_not_b():
    family_a = ProviderAFamily()
    auth_a = family_a.create_auth()
    assert not isinstance(auth_a, AuthB)  # Критично: компоненты не пересекаются

def test_b_components_are_not_a():
    family_b = ProviderBFamily()
    serializer_b = family_b.create_serializer()
    assert not isinstance(serializer_b, SerializerA)