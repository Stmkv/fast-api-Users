from fastapi import APIRouter
from core.schemas import UserRegisteredNotification

router = APIRouter()


@router.post("user-created")
def notify_user_created(info: UserRegisteredNotification):
    """
    This webhook will be triggered when a user is created
    """
