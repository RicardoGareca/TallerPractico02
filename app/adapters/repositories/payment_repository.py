from typing import List
from uuid import UUID
from app.core.entities.pago import Pago
from app.core.ports.repositories.payment_repository_base import PaymentRepositoryBase

class InMemoryPaymentRepository(PaymentRepositoryBase):
    def __init__(self):
        self._pagos: dict[UUID, Pago] = {}

    def guardar(self, pago: Pago) -> Pago:
        self._pagos[pago.id] = pago
        return pago

    def listar(self) -> List[Pago]:
        return list(self._pagos.values())

    def buscar_por_cliente(self, nombre_cliente: str) -> List[Pago]:
        return [
            p for p in self._pagos.values()
            if p.nombre_cliente.lower() == nombre_cliente.lower()
        ]

    def obtener_por_id(self, pago_id: UUID) -> Pago | None:
        return self._pagos.get(pago_id)

    def eliminar(self, pago_id: UUID) -> bool:
        if pago_id in self._pagos:
            del self._pagos[pago_id]
            return True
        return False
