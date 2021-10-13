import os, requests, json, pathlib, subprocess, pytz, time, stat, collections
from datetime import datetime
import logging, IO_Helper, traceback
import logging.config
import Logger
import concurrent.futures
from os import path


def updateMetaData(filename):
    print('Updating contest meta data..')
    data = {
    'operationName': 'null',
    'query': "{allContests {    titleSlug    startTime    originStartTime }}",
    'variables': '{}'
    }

    query_result = query_graphql(data)
    contest_data = {}
    for item in query_result['data']['allContests']:
        titleSlug = item['titleSlug']
        startTime = item['startTime']
        contest_data[titleSlug] = {
            'titleSlug' : titleSlug,
            'startTime' : startTime
        }

    IO_Helper.writeJSON(filename, contest_data)
    print('Finished updating contest meta data')


def query_graphql(data, url = 'https://leetcode.com/graphql'):
    CSRF_Token = '77HhPMor1cJWx7fEIZCrUkYvODrQCEf3QdcHUKSexKhpbRayWMtrREWiAsviKHls'

    COOKIE = 'csrftoken=' + CSRF_Token
    X_CSRFTOKEN = CSRF_Token
    
    headers = {
            'referer': 'https://leetcode.com/accounts/login/',
            'cookie' : COOKIE,
            'x-csrftoken' : X_CSRFTOKEN
    }

    sleep_time = 1
    while True:
        resp = requests.post(url, headers = headers, data = data)
        if sleep_time > 100:
                break
        elif resp.status_code == 200:
            resp = resp.json()
            break
        elif resp.status_code == 429:
            print('Next wait time..' + str(sleep_time))
            time.sleep(sleep_time)
            sleep_time *= 2
        else:
            print('Error Code=%s' % (resp.status_code))
            break
    
    return resp
    
def crawl_user_info_raw_CN(USERNAME, contest_title_slug):
    # print('Processing user rating [user=%s][region=CN]' % USERNAME)
    try:
        parsed_file = 'User_Rating_Parsed/' + USERNAME + '.json'
        if os.path.exists(parsed_file):
            user_rating = IO_Helper.loadJSON(parsed_file)
            if contest_title_slug in user_rating:
                return
        target_file = 'User_Rating_Raw/' + USERNAME + '.json'

        print('Crawling user rating raw file [user=%s][region=CN]' % USERNAME)

        data = {
            'operationName': "userContest",
            'query': "query userContest($userSlug: String!) {\n  userContestRanking(userSlug: $userSlug) {\n    ratingHistory\n contestHistory\n} }",
            'variables': '{"userSlug":"' + USERNAME + '"}'
        }

        url = 'https://leetcode-cn.com/graphql'
        graphql_result = query_graphql(data, url)
        
        # print(graphql_result)
        IO_Helper.writeJSON(target_file, graphql_result)
        
        Processing.parse_user_rating(USERNAME, 'CN', parsed_file)
    except Exception as err:
        traceback.print_exc()

def crawl_user_info_raw_US(USERNAME, contest_title_slug):
    # print('Processing user rating [user=%s][region=US]' % USERNAME)
    try:        
        parsed_file = 'User_Rating_Parsed/' + USERNAME + '.json'
        if os.path.exists(parsed_file):
            user_rating = IO_Helper.loadJSON(parsed_file)
            if contest_title_slug in user_rating:
                print('[Contest=%s] in user rating [user=%s]' % (contest_title_slug,USERNAME))
                return
        target_file = 'User_Rating_Raw/' + USERNAME + '.json'
        
        print('Crawling user rating raw file [user=%s][region=US]' % USERNAME)
        
        data = {
            'operationName': 'getContestRankingData',
            'query': "query getContestRankingData($username: String!) {\n  userContestRankingHistory(username: $username) {\n contest {\n titleSlug\n  }\n    rating\n   }\n}\n",
            'variables': '{"username":"' + USERNAME + '"}'
        }

        # print(data)
        graphql_result = query_graphql(data)
        # print(graphql_result)
        
        IO_Helper.writeJSON(target_file, graphql_result)
        Processing.parse_user_rating(USERNAME, 'US', parsed_file)
    except Exception as err:
        traceback.print_exc()

def crawl_user_info_raw(CONTEST_METADATA, CRAWLED_QUESTION_RECORD_FILNAME, CRAWLED_QUESTION_RECORD, logger):
    Passed_User_Folder = 'Passed_User/'
    print('crawl user info raw')
    try:
        
        for contest_title_slug in CONTEST_METADATA:
            if contest_title_slug in CRAWLED_QUESTION_RECORD: continue
            target_file = 'Contest_Ranking/' + contest_title_slug + '/1.json'
            # print('Target file = %s' % target_file)
            if not os.path.exists(target_file): continue
            submission_page = IO_Helper.loadJSON(target_file)
            # print(submission_page)
            questions_list = submission_page['questions']
            for questions in questions_list:
                with concurrent.futures.ProcessPoolExecutor() as executor:
                    question_title_slug = questions['title_slug']
                    Passed_User_File = Passed_User_Folder + question_title_slug + '.json'
                    Passed_Users = IO_Helper.loadJSON(Passed_User_File)
                    # print('Now crawling [Contest=%s][Question=%s]' % (contest_title_slug, question_title_slug))
                    print('Now processing [userfile=%s]' % (Passed_User_File))
                    for user_info in Passed_Users:
                        user_slug = user_info['user_slug']
                        user_region = user_info['user_region']

                        if user_region == 'US': 
                            executor.submit(crawl_user_info_raw_US, user_slug, contest_title_slug)
                        else: 
                            executor.submit(crawl_user_info_raw_CN, user_slug, contest_title_slug)

            CRAWLED_QUESTION_RECORD[contest_title_slug] = 1

    # user_folder = 'User_Rating/'
        IO_Helper.writeJSON(CRAWLED_QUESTION_RECORD_FILNAME, CRAWLED_QUESTION_RECORD)
    except:
        traceback.print_exc()


def fetch_rank_and_crawl_submission(contest):
    fetchContestRankingPage(contest)
    crawlSubmission_raw(contest, 21)
# def getLogger(logger_name):
    
#     # try:    
#     #     log_path = "logging/crawling_raw/{0}.log".format(logger_name)
#     #     logging_file_path = 'logging.conf'
#     #     logging.config.fileConfig(logging_file_path, defaults={'log_file_name':log_path})
#     #     logger = logging.getLogger(log_path)
#     #     val = 1 / 0
#     # except Exception as err:
#         # traceback.print_exc()
#         # print('Swithching to root logger')
#     log_file_name = 'logging/' + logger_name+ '.log'
#     logger = logging.getLogger(log_file_name)
#     logger.setLevel(logging.DEBUG)
#     consoleHandler = logging.StreamHandler()
#     fileHandler = logging.FileHandler(log_file_name)
#     consoleHandler.setLevel(logging.DEBUG)
#     fileHandler.setLevel(logging.DEBUG)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     # add formatter to ch
#     consoleHandler.setFormatter(formatter)
#     fileHandler.setFormatter(formatter)
#     # add ch to logger
#     logger.addHandler(consoleHandler)
#     logger.addHandler(fileHandler)
#     # pass
#     return logger

def rankingURL(contest):
    urlOne = "https://leetcode.com/contest/api/ranking/warm-up-contest/?pagination=%d"
    urlOld = "https://leetcode.com/contest/api/ranking/leetcode-weekly-contest-%s/?pagination=%d"
    url = "https://leetcode.com/contest/api/ranking/weekly-contest-%s/?pagination=%d"
    CNurl = "https://leetcode-cn.com/contest/api/ranking/weekly-contest-%s/?pagination=%d&region=local"
    url62 = "https://leetcode.com/contest/api/ranking/weekly-contest-by-app-academy/?pagination=%d"
    biweeklyURL = 'https://leetcode.com/contest/api/ranking/biweekly-contest-%s/?pagination=%d'
    CNBiweeklyURL = 'https://leetcode-cn.com/contest/api/ranking/biweekly-contest-%s/?pagination=%d&region=local'

    
    # contest_int = int(contest_str)


    # if contest_str == '16A' or contest_str == '16B' or contest_str == '18A' or contest_str == '18B': url = urlOld
    # elif contest_str == '1': url = urlOne
    # elif contest_str == '62': url = url62
    # elif contest_int <= 57: url = urlOld

    # if biweeklyContest: url = biweeklyURL
    # if CNRegion: url = CNurl
    # if CNRegion and biweeklyContest: url = CNBiweeklyURL
    return "https://leetcode.com/contest/api/ranking/%s/?pagination=%s"

def fetchContestRankingPage(contest):#, CNRegion = False, biweeklyContest = False):

    starttime = time.perf_counter()
    contest_str = str(contest)
    logger = Logger.getLogger(contest_str + "_ranking")
    
    target_folder = 'Contest_Ranking/' + contest_str + '/'
    
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    user_num = 0

    url = rankingURL(contest_str)

    
    start_page = 1
    end_page = 1000   # default to 1000 pages

    #########  multi processor #########

    # with concurrent.futures.ProcessPoolExecutor() as executor:
        # for page_num in range(start_page, end_page + 1):
        #     crawl_response = executor.submit(crawl_ranking_raw_file, url, contest_str, page_num)
        #     if crawl_response.result() == False: break
        #     crawl_ranking_raw_file(url, contest_str, page_num)
    
    #########  single processor #########
    for page_num in range(start_page, end_page + 1):            
        crawl_response = crawl_ranking_raw_file(url, contest_str, page_num)
        if crawl_response == False: break

        
    print("Finished crawling json files..")
    finishtime = time.perf_counter()
    print('finished in %d seconds' % (finishtime - starttime))
    

def crawl_ranking_raw_file(url, contest_str, page_num):



    requestURL = url % (contest_str, page_num)
    
    target_folder = 'Contest_Ranking/' + contest_str + '/'
    
    target_file = target_folder + str(page_num) + '.json'

    if os.path.exists(target_file): 
        print("Has record of [contest=%s][page=%s]" % (contest_str, page_num))
        return True
    
    print("Crawling[contest=%s][page=%s]" % (contest_str, str(page_num)))

    sleep_time = 1

    while True:

        submissionResponse = requests.get(requestURL)
        
        if sleep_time > 100:
            break
        elif submissionResponse.status_code == 200:
            submissionResponse = submissionResponse.json()
            break
        elif submissionResponse.status_code == 429:
            print('Next wait time..' + str(sleep_time))
            time.sleep(sleep_time)
            sleep_time *= 2
        else:
            print('Error Code=%s' % (submissionResponse.status_code))
            break

    if(len(submissionResponse) < 1): return False
    user_num = submissionResponse['user_num']
    if page_num > user_num / 25 + 1: return False
    
    IO_Helper.writeJSON(target_file, submissionResponse)
    return True

def crawlSubmission_raw(contest, page_end):

    starttime = time.perf_counter()

    contest_str = str(contest)
    
    logger = Logger.getLogger(contest_str + "_submission")
    
    found_new_record = False
    
    submissionURL = "https://leetcode.com/api/submissions/%s"
    submissionURLCN = "https://leetcode-cn.com/api/submissions/%s"

    logger.info("Crawling raw files [contest=%s] " % contest_str)

    
    Ranking_Folder = 'Contest_Ranking/' + contest_str + '/'
    outputLocation = 'Contest_Submission/' + contest_str + '/raw/'
    if not os.path.exists(outputLocation): os.makedirs(outputLocation)
    
    file_name_crawled_raw = outputLocation + 'crawled_rawfiles.json'

    # JSON record indicating whether file is crawled or not
    
    raw_files_crawled_JSON = IO_Helper.loadJSON(file_name_crawled_raw)
    # print(raw_files_crawled_JSON)

    # crawling up to 20 page

    for page in range(1, page_end):
        page_str = str(page)
        time.sleep(1)
        # try:
        Ranking_Page_file = Ranking_Folder + page_str + '.json'
        Ranking_Page_JSON = {}
        Ranking_Page_JSON = IO_Helper.loadJSON(Ranking_Page_file)
        
        submissions = Ranking_Page_JSON['submissions']
        total_rank = Ranking_Page_JSON['total_rank']
        questions = Ranking_Page_JSON['questions']
        # questions_filename = 'Contest_Submission/' + contest_str + '/questions.json'
        
        # IO_Helper.writeJSON(questions_filename, questions)

        size = len(submissions)
        submissionCounter = 0
        # print('size=' + str(size))

        for submission in submissions:
            submissionCounter += 1
            for question_id in submission:
                submission_id = str(submission[question_id]['submission_id'])
                data_region = str(submission[question_id]['data_region'])
                crawl_submission_raw(contest_str, page, submission_id, data_region)
        

        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     for submission in submissions:
        #         submissionCounter += 1
        #         for question_id in submission:
        #             submission_id = str(submission[question_id]['submission_id'])
        #             data_region = str(submission[question_id]['data_region'])
        #             executor.submit(crawl_submission_raw, contest_str, page, submission_id, data_region)
    
    finishtime = time.perf_counter()
    print('finished in %d seconds' % (finishtime - starttime))
                
                # submissionRequestURL = submissionURL
                # if data_region == 'CN': submissionRequestURL = submissionURLCN
                # submissionRequestURL = submissionRequestURL % submission_id

                # logger.info("Crawling raw file [contest %s][page %s][counter %d][raw file %s][region %s][%.1f%%]" % (contest_str, page, submissionCounter, 
                #     submission_id, data_region, (page + submissionCounter / size) / 21 * 100))

                # # print(submission_id)
                # if submission_id in raw_files_crawled_JSON: 
                #     logger.info("Already crawled file [filename=%s].. [status=%s]" % (submission_id, raw_files_crawled_JSON[submission_id]))
                #     continue
        
                # raw_file_name = submission_id


                # sleep_time = 1
                # # logger.info(submissionRequestURL)
                
                # flag = True
                # while True:
                #     submissionResponse = requests.get(submissionRequestURL)
                #     if sleep_time > 32: 
                #         logger.info('Request URL= ' + str(submissionRequestURL))
                #         logger.info('Response Text= ' + str(submissionResponse.text))
                #         flag = False
                #         break
                #     elif submissionResponse.status_code == 200: 
                #         submissionResponse = submissionResponse.json()
                #         break
                #     elif submissionResponse.status_code == 401:
                #         logger.info('Satus Code= ' + str(submissionResponse.status_code))
                #         logger.info('Target does not exist')
                #         flag = False
                #         break
                #     else:
                #         logger.info('Satus Code= ' + str(submissionResponse.status_code))
                #         logger.info('Next wait time..' + str(sleep_time))
                #         time.sleep(sleep_time)
                #         sleep_time *= 2
                
                # if not flag: 
                #     logger.info("[raw file %s] not available" % submission_id)
                #     if submissionResponse.status_code == 401:
                #         raw_files_crawled_JSON[raw_file_name] = 'file not found'
                #     else: 
                #         raw_files_crawled_JSON[raw_file_name] = 'error'
                #     IO_Helper.writeJSON(file_name_crawled_raw, raw_files_crawled_JSON)
                #     continue
                
                # submission_raw_filename = outputLocation + str(submission_id) + '.json'
                # raw_files_crawled_JSON[raw_file_name] = 'successfully crawled'
                # IO_Helper.writeJSON(submission_raw_filename, submissionResponse)
                # IO_Helper.writeJSON(file_name_crawled_raw, raw_files_crawled_JSON)  

def crawl_submission_raw(contest_str, page, submission_id, data_region):

    submissionURL = "https://leetcode.com/api/submissions/%s"
    submissionURL_CN = "https://leetcode-cn.com/api/submissions/%s"

    submissionRequestURL = submissionURL
    if data_region == 'CN': submissionRequestURL = submissionURL_CN
    submissionRequestURL = submissionRequestURL % submission_id

    

    # print(submission_id)
    outputLocation = 'Contest_Submission/' + contest_str + '/raw/'
    submission_raw_filename = outputLocation + str(submission_id) + '.json'

    if os.path.exists(submission_raw_filename): 
        print("Crawled raw file[contest=%s][page=%s][raw_file=%s][region=%s]" % (contest_str, page, submission_id, data_region))
        return
    
    print("Crawling raw file[contest=%s][page=%s][raw_file=%s][region=%s]" % (contest_str, page, submission_id, data_region))
    # if submission_id in raw_files_crawled_JSON: 
    #     logger.info("Already crawled file [filename=%s]" % (submission_id))
    #     return

    raw_file_name = submission_id

    sleep_time = 1
    
    flag = True
    while True:
        submissionResponse = requests.get(submissionRequestURL)
        if sleep_time > 32: 
            logger.info('Request URL= ' + str(submissionRequestURL))
            # logger.info('Response Text= ' + str(submissionResponse.text))
            flag = False
            break
        elif submissionResponse.status_code == 200: 
            submissionResponse = submissionResponse.json()
            break
        elif submissionResponse.status_code == 401:
            # logger.info('Satus Code= ' + str(submissionResponse.status_code))
            # logger.info('Target does not exist')
            flag = False
            break
        else:
            # logger.info('Satus Code= ' + str(submissionResponse.status_code))
            print('Next wait time..' + str(sleep_time))
            time.sleep(sleep_time)
            sleep_time *= 2
    
    if not flag: 
        logger.info("[raw file %s] not available" % submission_id)
        # if submissionResponse.status_code == 401:
        #     raw_files_crawled_JSON[raw_file_name] = 'file not found'
        # else: 
        #     raw_files_crawled_JSON[raw_file_name] = 'error'
        # IO_Helper.writeJSON(file_name_crawled_raw, raw_files_crawled_JSON)
        # continue
        return
    
    
    # raw_files_crawled_JSON[raw_file_name] = 'successfully crawled'
    IO_Helper.writeJSON(submission_raw_filename, submissionResponse)
    # IO_Helper.writeJSON(file_name_crawled_raw, raw_files_crawled_JSON)  


if __name__ == '__main__':
    crawl_user_info_raw_US('xianglaniunan')
    # crawl_user_info_raw_CN('zerotrac2')
