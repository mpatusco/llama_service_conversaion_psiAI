from app.entities.conversation import ConversationRequest, ConversationQuery
from app.repositories.mongo_repository import save_to_mongo, fetch_from_mongo
from app.utils.base64_encoder import encode_key
from app.usecases.create_query import create_query

async def create_conversation(conversation: ConversationRequest):
    """Create and save a conversation.

    Args:
        conversation (ConversationRequest): The conversation data.

    Returns:
        dict: Success status.
    """
    key = encode_key(conversation.nome_psicologo, conversation.registro_psicologo, conversation.nome_person)
    data = conversation.dict()
    await save_to_mongo(key, data, overwrite=True)
    return {"status": "success"}

async def get_conversation(query: ConversationQuery):
    """Retrieve conversation data based on a query.

    Args:
        query (ConversationQuery): Query data to identify the conversation.

    Returns:
        dict: The conversation data.
    """
    key = encode_key(query.nome_psicologo, query.registro_psicologo, query.nome_person)
    query_dict = create_query([key])
    return await fetch_from_mongo(query_dict)
