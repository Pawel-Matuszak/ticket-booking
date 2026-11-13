from datetime import UTC, datetime

from booking.seed import seed_event


async def test_seed_event_creates_seats(session):
    event = await seed_event(
        session,
        "Event One",
        ["A-1", "A-2", "A-3"],
        datetime(2026, 11, 10, 19, 0, tzinfo=UTC),
    )
    assert len(event.seats) == 3
    assert all(seat.version == 0 for seat in event.seats)
    assert all(seat.event_id == event.id for seat in event.seats)
