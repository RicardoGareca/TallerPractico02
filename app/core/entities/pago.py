from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field

class Pago(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nombre_cliente: str
    monto: float
    fecha: datetime = Field(default_factory=datetime.utcnow)
    estado: str = "COMPLETADO"
