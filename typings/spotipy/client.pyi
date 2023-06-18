from _typeshed import Incomplete


class Spotify:
    max_retries: int
    default_retry_codes: Incomplete
    country_codes: Incomplete
    prefix: str
    client_credentials_manager: Incomplete
    oauth_manager: Incomplete
    proxies: Incomplete
    requests_timeout: Incomplete
    status_forcelist: Incomplete
    backoff_factor: Incomplete
    retries: Incomplete
    status_retries: Incomplete
    language: Incomplete

    def __init__(self, auth: Incomplete | None = ..., requests_session: bool = ..., client_credentials_manager: Incomplete | None = ..., oauth_manager: Incomplete | None = ..., auth_manager: Incomplete | None = ..., proxies: Incomplete | None = ..., requests_timeout: int = ..., status_forcelist: Incomplete | None = ..., retries=..., status_retries=..., backoff_factor: float = ..., language: Incomplete | None = ...) -> None:
        ...

    def playlist(self, playlist_id: str, fields: Incomplete | None = ..., market: Incomplete | None = ..., additional_types: Incomplete = ...) -> dict[str, dict[str, dict[int, dict[str, dict[str, dict[str, str]]]]]]:
        ...
