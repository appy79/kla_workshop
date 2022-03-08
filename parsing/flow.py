import time, threading
from parsing.get_config import current_config
from parsing import logger


config = current_config()

config = config[0]


def TimeFunction(exec_time):
    exec_time = int(exec_time)
    time.sleep(exec_time)


def execute_activity(activity, level):
    if activity["Type"] == "Task":
        if activity["Function"] == "TimeFunction":
            func_input = activity["Inputs"]["FunctionInput"]
            exec_time = activity["Inputs"]["ExecutionTime"]
            logger.info(
                level
                + " Executing"
                + " TimeFunction("
                + func_input
                + ","
                + exec_time
                + ")"
            )
            TimeFunction(exec_time)
    elif activity["Type"] == "Flow":
        execute_workflow(activity, level)


def execute_workflow(workflow, level):
    op_type = workflow["Type"]
    exec_type = workflow["Execution"]
    concurrent = []
    for activity_name, activity in workflow["Activities"].items():
        sub_level = level + "." + activity_name
        logger.info(sub_level + " Entry")
        if exec_type == "Sequential":
            execute_activity(activity, sub_level)
            logger.info(sub_level + " Exit")
        elif exec_type == "Concurrent":
            thread = threading.Thread(
                target=execute_activity, args=(activity, sub_level)
            )
            thread.start()
            concurrent.append([thread, sub_level])

    for thread, sub_level in concurrent:
        thread.join()
        logger.info(sub_level + " Exit")


for workflow_name, workflow in config.items():
    level = workflow_name
    logger.info(level + " Exit")
    execute_workflow(workflow, level)
    logger.info(level + " Exit")
