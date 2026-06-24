from typing import Any, Optional, Dict
import httpx

def request(method: str, url: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None,
            data: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None, cookies: Optional[Dict[str, str]] = None, timeout: float = 10.0,) -> httpx.Response:
    
    try:
        response = httpx.request(
            method,
            url,
            headers=headers,
            params=params,
            data=data,
            json=json,
            cookies=cookies,
            timeout=timeout,
        )

        return response
    
    except httpx.RequestError as e:
        raise RuntimeError(f"Request failed for {url}: {e}") from e
