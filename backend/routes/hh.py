from fastapi import APIRouter, Query
import httpx

router = APIRouter(prefix="/hh", tags=["hh"])

@router.get("/vacancies")
async def get_vacancies(text: str = Query(...), area: str = "1"):  # Москва по умолчанию
    url = f"https://api.hh.ru/vacancies?text={text}&area={area}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()
