from dotenv import load_dotenv
from hh import get_statistic as get_hh_statistic  
from sj import get_statistic as get_sj_statistic
from service_functions import get_table

import os


if __name__ == '__main__':
    load_dotenv()
    # sj_statistic = get_sj_statistic(api_key=os.getenv('API_SUPERJOB'))
    # print(get_table('SuperJob', statistic=sj_statistic))
    
    hh_statistic = get_hh_statistic()
    print(get_table('HeadHunter', statistic=hh_statistic))
