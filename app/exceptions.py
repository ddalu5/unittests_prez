class ResultNotFoundError(Exception):
    def __init__(self, url: str):
        super().__init__(
            f'[!] API returned a 404 HTTP error for URL: "{url}"'
        )


class MetaWeatherAPIUnreachableError(Exception):
    def __init__(self, message: str):
        super().__init__(f'[!] Couldn\'t reach the MetaWeatherAPI, error: "{message}"')
