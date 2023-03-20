from unittest.mock import Mock
import tmdb_client

def test_homepage(monkeypatch):

    movies = {"results": ["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5", "Movie 6", "Movie 7", "Movie 8"]}
    tmdb_mock = Mock(return_value=movies)
    monkeypatch.setattr(tmdb_client, "get_popular_movies", tmdb_mock)

    response = client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.content_type
    assert b"Movie 1" in response.data
    assert b"Movie 8" in response.data

    tmdb_mock.assert_called_once()
