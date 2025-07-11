import logging

from adapters.schemas.marca_input import MarcaInputObtener
from core.ports.repositories.marca_repository_base import MarcaRepositoryBase


logger = logging.getLogger(__name__)


class MarcaRepository(MarcaRepositoryBase):

    def __init__(self, db):
        self.db = db

    def obtener_marcas(self, marca_input: MarcaInputObtener, limit: int):
        logger.info(f"Ejecuando query (obtener marca) con limite {limit}")
        return {'marcas': ['nike', 'adidas']}
