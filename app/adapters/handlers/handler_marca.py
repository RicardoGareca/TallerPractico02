import logging

from typing import List
from fastapi import APIRouter, Request, Depends

from adapters.dependency.dependencies import get_marca_service
from adapters.schemas.marca_input import MarcaInputObtener, MarcaInputGuardar
from adapters.schemas.marca_output import MarcaOutput
from app.application.services import marca_service
from application.services.marca_service import MarcaService

logger = logging.getLogger(__name__)
router_marca = APIRouter()


@router_marca.get("/logs")
async def obtener_marca(request: Request,
                        marca_service: MarcaService = Depends(get_marca_service)):
    """
    Obtener la marca.
    :param request: Objeto de solicitud que contiene el ID de la solicitud
    :param marca_input: Objeto de entrada que contiene el id de la marca
    :param marca_service: Servicio de marca inyectado por dependencia
    :param environ_vars: Variables de entorno
    :return: Marca
    """
    
    marca_output = marca_service.consultar_marcas(None, 10)
    if marca_output is None:
        raise HTTPException(status_code=404, detail="Marca no encontrada")
    return marca_output