from app.core.entities.pago import Pago
from app.application.services.payment_service import PaymentService
from app.adapters.repositories.payment_repository import InMemoryPaymentRepository

def test_registrar_y_listar():
    repo = InMemoryPaymentRepository()
    service = PaymentService(repo)
    pago = service.registrar_pago("Lucas", 10000)
    assert pago.nombre_cliente == "Lucas"
    assert pago.estado == "COMPLETADO"
    assert pago.monto == 10000
    assert len(service.listar_pagos()) == 1

def test_buscar_por_cliente():
    repo = InMemoryPaymentRepository()
    service = PaymentService(repo)
    service.registrar_pago("Ana", 5000)
    service.registrar_pago("Ana", 2000)
    resultados = service.buscar_por_cliente("Ana")
    assert len(resultados) == 2

def test_eliminar_pago():
    repo = InMemoryPaymentRepository()
    service = PaymentService(repo)
    pago = service.registrar_pago("Pepe", 8000)
    service.eliminar_pago(pago.id)
    assert len(service.listar_pagos()) == 0
