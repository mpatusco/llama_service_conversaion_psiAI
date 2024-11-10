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
async def get_conversation_route(
    nome_psicologo: str,
    registro_psicologo: str,
    nome_person: str
):
    """Retrieve a conversation record.

    Args:
        nome_psicologo (str): Name of the psychologist.
        registro_psicologo (str): Registration number of the psychologist.
        nome_person (str): Name of the person.

    Returns:
        dict: The requested conversation data.

    Raises:
        HTTPException: If there's an error in the process.
    """
    try:
        query = ConversationQuery(
            nome_psicologo=nome_psicologo,
            registro_psicologo=registro_psicologo,
            nome_person=nome_person
        )
        return await get_conversation(query)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))