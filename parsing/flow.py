import time, asyncio
from parsing.get_config import current_config
from parsing import logger


config = current_config()

config = config[0]


def TimeFunction(input, exec_time):
    exec_time = int(exec_time)
    time.sleep(exec_time)


def execute_activity(activity, level, exec_type):
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
            if exec_type == "Sequential":
                TimeFunction(func_input, exec_time)
            elif exec_type == "Concurrent":
                asyncio.run(TimeFunction(func_input, exec_time))
    elif activity["Type"] == "Flow":
        execute_workflow(activity, level)


def execute_workflow(workflow, level):
    logger.info(level + " Entry")
    op_type = workflow["Type"]
    exec_type = workflow["Execution"]
    for activity_name, activity in workflow["Activities"].items():
        sub_level = level + "." + activity_name
        logger.info(sub_level + " Entry")
        execute_activity(activity, sub_level, exec_type)
        logger.info(sub_level + " Exit")


for workflow_name, workflow in config.items():
    level = workflow_name
    execute_workflow(workflow, level)
