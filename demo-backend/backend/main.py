import os

import psutil
from fastapi import FastAPI

app = FastAPI()


@app.get("/status")
async def hello():
    env = os.environ.get("ENV", "dev")
    status = {
        "status": "ok",
        "ENV": env,
    }
    if env == "dev":
        status["cpu"] = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        status["memory_usage"] = memory.active
    return status


@app.get("/pi")
async def pi():
    return get_pi()


def get_pi(iteration: int = 800, k: int = 1, result: float = 0) -> float:
    # return pi using Leibniz’s formula
    if iteration == 0:
        return result

    if iteration % 2 == 0:
        return get_pi(iteration - 1, k + 2, result + 4 / k)
    return get_pi(iteration - 1, k + 2, result - 4 / k)
