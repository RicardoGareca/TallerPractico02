
from adapters.repositories.marca_repository import MarcaRepository
from application.services.marca_service import MarcaService


def get_marca_service() -> MarcaService:
    marca_repository = MarcaRepository(None)
    return MarcaService(marca_repository)

