import pytest
from api_reqres.utils.constants import URL


@pytest.fixture
def base_url():
    return URL