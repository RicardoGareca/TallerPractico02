from abc import abstractmethod, ABC

from adapters.schemas.marca_input import MarcaInputObtener
from core.ports.repositories.marca_repository_base import MarcaRepositoryBase


class MarcaServiceBase(ABC):

    def __init__(self, marcas_repository_base: MarcaRepositoryBase):
        self.marcas_repository_base = marcas_repository_base

    @abstractmethod
    def consultar_marcas(self, marca_input: MarcaInputObtener, limit: int):
        pass
