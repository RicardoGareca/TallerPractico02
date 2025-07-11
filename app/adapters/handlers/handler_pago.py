from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from uuid import UUID
from app.application.services.payment_service import PaymentService

router = APIRouter()

class RegistrarPagoInput(BaseModel):
    nombre_cliente: str
    monto: float

def create_pago_routes(service: PaymentService):

    @router.post("/pagos", status_code=201)
    def registrar_pago(data: RegistrarPagoInput):
        try:
            return service.registrar_pago(data.nombre_cliente, data.monto)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @router.get("/pagos")
    def listar_pagos():
        return service.listar_pagos()

    @router.get("/pagos/buscar")
    def buscar_por_cliente(nombre_cliente: str):
        return service.buscar_por_cliente(nombre_cliente)

    @router.delete("/pagos/{pago_id}", status_code=204)
    def eliminar_pago(pago_id: UUID):
        try:
            service.eliminar_pago(pago_id)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
