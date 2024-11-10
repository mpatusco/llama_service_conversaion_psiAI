from fastapi import APIRouter, HTTPException
from app.services.conversation_service import create_conversation, get_conversation
from app.entities.conversation import ConversationRequest, ConversationQuery

router = APIRouter()

@router.post("/")
async def create_conversation_route(conversation: ConversationRequest):
    """Create a conversation record.

    Args:
        conversation (ConversationRequest): The conversation data.

    Returns:
        dict: Status of the conversation creation.

    Raises:
        HTTPException: If there's an error in the process.
    """
    try:
        return await create_conversation(conversation)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
async def get_conversation_route(query: ConversationQuery):
    """Retrieve a conversation record.

    Args:
        query (ConversationQuery): Query data to identify the conversation.

    Returns:
        dict: The requested conversation data.

    Raises:
        HTTPException: If there's an error in the process.
    """
    try:
        return await get_conversation(query)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
