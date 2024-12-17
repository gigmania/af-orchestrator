from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

@dag(start_date=datetime(2024, 2, 2), schedule_interval='*/2 * * * *', catchup=False)
def get_team_feedback():

    # Define tasks
    task_1 = BashOperator(task_id='create_meeting', bash_command='echo "Set up meeting"', retries=3, retry_delay=timedelta(minutes=5))
    task_2 = BashOperator(task_id='discuss_designs', bash_command='echo "Discussed Designs"', retries=3, retry_delay=timedelta(minutes=5))
    task_3 = BashOperator(task_id='implement_suggestions', bash_command='echo "Implemented Feedback"', retries=3, retry_delay=timedelta(minutes=5))

    # Define Python tasks using @task decorator
    @task
    def jump():
        return 'Jumped off a cliff'

    @task
    def run():
        return 'Ran around the corner'

    @task
    def fly():
        return 'Flew to close to the sun'

    # Define the final tasks
    @task
    def review_acts(jumpy, runy, flyy):
        print(f"Jump: {jumpy}")
        print(f"Run: {runy}")
        print(f"Fly: {flyy}")

    # Set task dependencies
    task_1 >> task_2 >> task_3
    task_2 >> task_3

    # Set Python task dependencies
    news_result = jump()
    work_result = run()
    relax_result = fly()

    # Set final task dependency
    review_acts(news_result, work_result, relax_result)

get_team_feedback()
