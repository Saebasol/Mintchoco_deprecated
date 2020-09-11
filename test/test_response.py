import pytest


@pytest.mark.asyncio
async def test_galleryinfo(rose_client):
    response = await rose_client.galleryinfo(1)
    assert response


@pytest.mark.asyncio
async def test_info(rose_client):
    response = await rose_client.info(1)
    assert response


@pytest.mark.asyncio
async def test_integrated(rose_client):
    response = await rose_client.integrated(1)
    assert response


@pytest.mark.asyncio
async def test_list_(rose_client):
    response = await rose_client.list(1)
    assert response


@pytest.mark.asyncio
async def test_download(rose_client):
    response = await rose_client.download(1)
    assert response
