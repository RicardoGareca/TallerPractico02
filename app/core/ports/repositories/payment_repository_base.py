from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from app.core.entities.pago import Pago

class PaymentRepositoryBase(ABC):

    @abstractmethod
    def guardar(self, pago: Pago) -> Pago:
        pass

    @abstractmethod
    def listar(self) -> List[Pago]:
        pass

    @abstractmethod
    def buscar_por_cliente(self, nombre_cliente: str) -> List[Pago]:
        pass

    @abstractmethod
    def obtener_por_id(self, pago_id: UUID) -> Pago | None:
        pass

    @abstractmethod
    def eliminar(self, pago_id: UUID) -> bool:
        pass
