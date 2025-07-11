from fastapi import FastAPI
from app.adapters.handlers.handler_pago import router, create_pago_routes
from app.adapters.repositories.payment_repository import InMemoryPaymentRepository
from app.application.services.payment_service import PaymentService

app = FastAPI()

# Inicializar el repositorio en memoria
repo = InMemoryPaymentRepository()

# Crear el servicio de pagos usando el repositorio
service = PaymentService(repo)

# Conectar las rutas HTTP al servicio
create_pago_routes(service)
app.include_router(router)


