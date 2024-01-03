from fastapi import APIRouter

from controllers.papeis_controllers import router as papeis_router

router = APIRouter()
router.include_router(papeis_router, prefix="/papeis", tags=["papeis"])