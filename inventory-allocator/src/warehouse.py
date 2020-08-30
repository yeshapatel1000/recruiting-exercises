from collections import OrderedDict
import os
import json
import logging
import traceback
import datetime
__location__ = os.path.abspath(os.getcwd())
logfile_name = datetime.datetime.now()
logfile_name = str(logfile_name).split(
    ".")[0].replace(" ", "_").replace(":", "_")
append_file = "logs\\"+logfile_name+str(".log")
logpath = os.path.join(
    __location__, append_file)
logging.basicConfig(level=os.environ.get(
    "LOGLEVEL", "DEBUG"), filename=logpath)

logger = logging.getLogger()


def get_input(order, warehouses):
    warehouse_dict = OrderedDict()
    return_stock = {}
    for w in warehouses:
        warehouse_dict[w['name']] = w['inventory']

    for fruit, requirement in order.items():
        remaining = requirement
        for warehouse_name, inventory in warehouse_dict.items():
            if fruit in inventory.keys():
                min_value = min(remaining, inventory[fruit])
                remaining = remaining - min_value
                inventory[fruit] = inventory[fruit] - min_value
                if warehouse_name in return_stock.keys():
                    return_stock[warehouse_name][fruit] = min_value
                else:
                    return_stock[warehouse_name] = {}
                    return_stock[warehouse_name][fruit] = min_value
            if remaining == 0:
                break
    li = []
    li.append(return_stock)
    return li


if __name__ == "__main__":

    test_path = os.path.join(
        __location__, "test.txt")
    output_path = os.path.join(
        __location__, "output.txt")
    try:
        with open(test_path, "r+") as file_open:
            logging.debug("FILE OPENED")
            while 1:
                input_str = file_open.readline()
                if not input_str:
                    break
                output_str = file_open.readline()
                if not output_str:
                    break
                end_line = file_open.readline()
                if not end_line:
                    break
                demand = input_str.split("},", 1)
                supply = demand[1]
                demand = demand[0]+"}"

                demand = json.loads(demand)
                supply = json.loads(supply)
                try:
                    return_value = get_input(demand, supply)
                except BaseException as e:
                    logging.exception(traceback.format_exc())
                with open(output_path, "a+") as file_op:
                    if return_value == json.loads(output_str):

                        file_op.write("TEST PASSED\n")
                        print("TEST PASSED")
                        logging.debug("TESTCASE PASSED")
                    else:

                        file_op.write("TEST FAILED\n")
                        print("TEST FAILED")
                        logging.DEBUG("TESTCASE FAILED")
    except BaseException as e:
        logging.exception(traceback.format_exc())
