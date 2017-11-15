from backend.celery import app
from celery import group

#core tasks

@app.task
def test_queue():
    print ('im working')
