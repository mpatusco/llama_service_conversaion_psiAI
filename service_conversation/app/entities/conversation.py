from pydantic import BaseModel

class ConversationRequest(BaseModel):
    """Data model for a conversation creation request.

    Attributes:
        nome_psicologo (str): Name of the psychologist.
        registro_psicologo (str): Registration number of the psychologist.
        nome_person (str): Name of the person.
        conversa (str): Text of the conversation.
    """
    nome_psicologo: str
    registro_psicologo: str
    nome_person: str
    conversa: str

class ConversationQuery(BaseModel):
    """Data model for a conversation retrieval query.

    Attributes:
        nome_psicologo (str): Name of the psychologist.
        registro_psicologo (str): Registration number of the psychologist.
        nome_person (str): Name of the person.
    """
    nome_psicologo: str
    registro_psicologo: str
    nome_person: str
