from publisher import create_topic
import logging

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    create_topic("de2024-435320", "diabetes_req")   # replace your project id
    create_topic("de2024-435320", "diabetes_res") # replace your project id
