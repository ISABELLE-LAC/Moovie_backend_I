import httpx
from typing import Optional, List, Literal, Union

from .schemas import MovieSimple, MovieDetailed, RatingSimple, TagSimple, LinkSimple, AnalyticsResponse
from .film_config import MovieConfig

import pandas as pd


class MovieClient:
    def __init__(self, config: Optional[MovieConfig] = None):
        self.config = config or MovieConfig()
        self.movie_base_url = self.config.movie_base_url

    def _format_output(self, data, model, output_format: Literal["pydantic", "dict", "pandas"]):
        if output_format == "pydantic":
            return [model(**item) for item in data]
        elif output_format == "dict":
            return data
        elif output_format == "pandas":
            import pandas as pd
            return pd.DataFrame(data)
        else:
            raise ValueError("Invalid output_format. Choose from 'pydantic', 'dict', or 'pandas'.")

    def health_check(self) -> dict:
        url = f"{self.movie_base_url}/"
        response = httpx.get(url)
        response.raise_for_status()
        return response.json()

    def get_movie(self, movie_id: int) -> MovieDetailed:
        url = f"{self.movie_base_url}/movies/{movie_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return MovieDetailed(**response.json())

    def list_movies(
        self,
        skip: int = 0,
        limit: int = 100,
        title: Optional[str] = None,
        genre: Optional[str] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[MovieSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.movie_base_url}/movies"
        params = {"skip": skip, "limit": limit}
        if title:
            params["title"] = title
        if genre:
            params["genre"] = genre
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), MovieSimple, output_format)

    def get_rating(self, user_id: int, movie_id: int) -> RatingSimple:
        url = f"{self.movie_base_url}/ratings/{user_id}/{movie_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return RatingSimple(**response.json())

    def list_ratings(
        self,
        skip: int = 0,
        limit: int = 100,
        movie_id: Optional[int] = None,
        user_id: Optional[int] = None,
        min_rating: Optional[float] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[RatingSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.movie_base_url}/ratings"
        params = {"skip": skip, "limit": limit}
        if movie_id:
            params["movie_id"] = movie_id
        if user_id:
            params["user_id"] = user_id
        if min_rating:
            params["min_rating"] = min_rating
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), RatingSimple, output_format)

    def get_tag(self, user_id: int, movie_id: int, tag_text: str) -> TagSimple:
        url = f"{self.movie_base_url}/tags/{user_id}/{movie_id}/{tag_text}"
        response = httpx.get(url)
        response.raise_for_status()
        return TagSimple(**response.json())

    def list_tags(
        self,
        skip: int = 0,
        limit: int = 100,
        movie_id: Optional[int] = None,
        user_id: Optional[int] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[TagSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.movie_base_url}/tags"
        params = {"skip": skip, "limit": limit}
        if movie_id:
            params["movie_id"] = movie_id
        if user_id:
            params["user_id"] = user_id
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), TagSimple, output_format)

    def get_link(self, movie_id: int) -> LinkSimple:
        url = f"{self.movie_base_url}/links/{movie_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return LinkSimple(**response.json())

    def list_links(
        self,
        skip: int = 0,
        limit: int = 100,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[LinkSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.movie_base_url}/links"
        params = {"skip": skip, "limit": limit}
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), LinkSimple, output_format)

    def get_analytics(self) -> AnalyticsResponse:
        url = f"{self.movie_base_url}/analytics"
        response = httpx.get(url)
        response.raise_for_status()
        return AnalyticsResponse(**response.json())