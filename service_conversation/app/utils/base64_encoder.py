import base64

def encode_key(nome_psicologo: str, registro_psicologo: str, nome_person: str) -> str:
    """Encode conversation identifiers into a Base64 key.

    Args:
        nome_psicologo (str): Psychologist's name.
        registro_psicologo (str): Psychologist's registration number.
        nome_person (str): Person's name.

    Returns:
        str: Base64 encoded key.
    """
    composite_key = f"{nome_psicologo}{registro_psicologo}{nome_person}"
    return base64.b64encode(composite_key.encode()).decode()
