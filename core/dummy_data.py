from datetime import datetime, timedelta
from random import choice, randint
import asyncio

async def generate_call_data(start_date: datetime, end_date: datetime, call_type: str, limit: int, page: int):
    await asyncio.sleep(5)
    calls = []
    status_options = ["completed", "started", "failed"]
    for i in range((page - 1) * limit + 1, page * limit + 1):
        generated_start_date = start_date + timedelta(days=randint(0, (end_date - start_date).days))
        
        # Calcular la duración aleatoria de la llamada en segundos
        duration = randint(1, 900)  # Duración aleatoria de hasta 15 minutos (900 segundos)
        
        # Calcular la fecha de finalización de la llamada sumando la duración
        generated_end_date = generated_start_date + timedelta(seconds=duration)

        generated_call_type = choice(["inbound", "outbound"])
        status = choice(status_options)
        num_calls = randint(1, 10)
        first_contact = num_calls <= 1
        origin_length = choice([4, 10])
        origin = ''.join(["{}".format(randint(0, 9)) for num in range(0, origin_length)])
        destination_length = choice([4, 10])
        destination = ''.join(["{}".format(randint(0, 9)) for num in range(0, destination_length)])
        call_type_specific = choice(["CC", "PBX", "VIDEO", "AI"])
        
        if call_type is None or generated_call_type == call_type:
            calls.append({
                "id": i,
                "call_id": f"call_{i}",
                "name": f"Call {i}",
                "start_date": generated_start_date,
                "end_date": generated_end_date,
                "duration": duration,
                "call_type": generated_call_type,
                "status": status,
                "agent": f"Agent {randint(1, 10)}",
                "first_contact": first_contact,
                "num_calls": num_calls,
                "origin": origin,
                "destination": destination,
                "source": call_type_specific
            })
    return calls
