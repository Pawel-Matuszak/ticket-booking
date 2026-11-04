import asyncpg

async def test_can_connect_to_booking_test_db():
    conn = await asyncpg.connect(user='tickets', password='tickets',
                                     database='booking_test', host='127.0.0.1')
    try:
        assert (await conn.fetchval('SELECT 1')) == 1
    finally:
        await conn.close()