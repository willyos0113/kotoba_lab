# 從指定地點的 weatherElement 中擷取第一筆資料
def _get_first_param(location: dict, element_name: str) -> str:
    """
    從 weatherElement 擷取指定 element 的第一筆資料
    """
    for element in location["weatherElement"]:
        if element["elementName"] == element_name:
            return element["time"][0]["parameter"]["parameterName"]
    return "無資料"
