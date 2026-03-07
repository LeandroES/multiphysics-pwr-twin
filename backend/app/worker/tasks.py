from app.worker.celery_app import celery_app


@celery_app.task(name="simulation.run_steady_state")
def run_steady_state(reactor_params: dict) -> dict:
    """Placeholder for steady-state neutronics + thermal-hydraulics simulation."""
    return {"status": "queued", "params": reactor_params}
