from abc import ABC, abstractmethod

from adapters.schemas.marca_input import MarcaInputObtener


class MarcaRepositoryBase(ABC):

    @abstractmethod
    def obtener_marcas(self, marca_input: MarcaInputObtener, limit: int):
        pass