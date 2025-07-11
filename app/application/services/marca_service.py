import logging

from adapters.schemas.marca_input import MarcaInputObtener
from core.ports.repositories.marca_repository_base import MarcaRepositoryBase
from core.services.marca_service_base import MarcaServiceBase

logger = logging.getLogger(__name__)

class MarcaService(MarcaServiceBase):

    def __init__(self, marca_repository: MarcaRepositoryBase):
        self.marcas_repository = marca_repository
        super().__init__(marca_repository)

    def consultar_marcas(self, marca_input: MarcaInputObtener, limit: int):
        logger.info("Consultando marcas")
        marca_result = self.marcas_repository.obtener_marcas(marca_input, limit)
        return marca_result
