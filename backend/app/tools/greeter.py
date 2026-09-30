def generate_greeting(name: str) -> str:
    """
    根據輸入的名字生成一個問候語。
    """
    if not name:
        # 如果名字為空，則回傳通用問候
        return "Hello there! What's your name?"
    else:
        # 如果有名字，則回傳客製化問候
        return f"Hello, {name}! Nice to meet you."
