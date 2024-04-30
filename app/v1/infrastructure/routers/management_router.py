from fastapi import APIRouter, status

from app.v1.infrastructure.dto.microservice_info_dto import MicroserviceInfoDTO

management_router = APIRouter()


@management_router.get("/info", status_code=status.HTTP_200_OK)
def get_microservice_information() -> MicroserviceInfoDTO:
    return MicroserviceInfoDTO()
