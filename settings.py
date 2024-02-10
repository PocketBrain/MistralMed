class ModelSettings:
    SYSTEM_PROMPT: str = """Ты - ассистент, помогаешь пользователям отвечать на их вопросы, исходя из контекста.
Отвечай только полезной информацией. Не задавай встречные вопросы.
Вопрос от пользователя:
"""
    SYSTEM_TOKEN: int = 1587
    USER_TOKEN: int = 2188
    BOT_TOKEN: int = 12435
    LINEBREAK_TOKEN: int = 13
    PATH: str = "model-q4_K.gguf"
    PATH_DATA: str = "model-q4_K.gguf"
    ROLE_TOKENS: dict = {
        "user": USER_TOKEN,
        "bot": BOT_TOKEN,
        "system": SYSTEM_TOKEN
    }