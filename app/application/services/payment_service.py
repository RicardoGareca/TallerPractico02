from uuid import UUID
from typing import List
from app.core.entities.pago import Pago
from app.core.ports.repositories.payment_repository_base import PaymentRepositoryBase

class PaymentService:
    def __init__(self, repo: PaymentRepositoryBase):
        self.repo = repo

    def registrar_pago(self, nombre_cliente: str, monto: float) -> Pago:
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")
        pago = Pago(nombre_cliente=nombre_cliente, monto=monto)
        return self.repo.guardar(pago)

    def listar_pagos(self) -> List[Pago]:
        return self.repo.listar()

    def buscar_por_cliente(self, nombre_cliente: str) -> List[Pago]:
        return self.repo.buscar_por_cliente(nombre_cliente)

    def eliminar_pago(self, pago_id: UUID) -> None:
        pago = self.repo.obtener_por_id(pago_id)
        if not pago:
            raise ValueError("Pago no encontrado")
        if pago.estado != "COMPLETADO":
            raise ValueError("Solo se puede eliminar pagos COMPLETADOS")
        if not self.repo.eliminar(pago_id):
            raise ValueError("No se pudo eliminar el pago")
