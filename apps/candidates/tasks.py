import logging
from celery import shared_task
from .models import Candidate
from ..races.models import Race
logger = logging.getLogger(__name__)


@shared_task
def update_br_candidate(obj_id, publish=True):
    obj = Candidate.objects.get(pk=obj_id)

    try:
        logger.info(f"update_br_candidate task has received {obj}")
        obj.update_br_data()
        obj.save(publish=publish)
    except Exception:
        logger.error("Task error: update_br_candidate", exc_info=True)


@shared_task
def update_br_candidates_all():
    candidates = Candidate.objects.all()
    races = Race.objects.all()

    try:
        logger.info(
            f"update_br_candidates_all task has received {len(candidates)} candidates")
        for candidate in candidates:
            obj_id = candidate.pk
            update_br_candidate(obj_id, publish=False)
            # don't publish so we send 53 publish_object tasks, not 190
        for race in races:
            race.save()
    except Exception:
        logger.error("Task error: update_br_candidates_all", exc_info=True)