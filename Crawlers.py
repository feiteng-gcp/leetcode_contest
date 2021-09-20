import os, requests, json, pathlib, subprocess, pytz, time, stat, collections
from datetime import datetime
import logging, IO_Helper, traceback
import logging.config
import Logger
from os import path

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
    return url

def fetchContestRankingPage(contest):#, CNRegion = False, biweeklyContest = False):

    contest_str = str(contest)
    logger = Logger.getLogger(contest_str + "_ranking")
    
    data = {}
    
    start_page = 1
    end_page = 1000   # default to 1000 pages

    
    
    cur_folder = str(pathlib.Path().resolve())
    target_folder = cur_folder + '/Contest_Ranking/' + contest_str + '/'

    user_num = 0

    url = rankingURL(contest_str)

    for page_num in range(start_page, end_page + 1):

        # if(page_num % 10 == 0): logger.info('on page %d' % page_num)
        if contest_str == '1' or contest_str == '62': requestURL = url % page_num
        else: requestURL = url % (contest_str, page_num)

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        target_file = target_folder + str(page_num) + '.json'

        logger.info("Crawling ranking [contest.. %s] [page %s] json" % (contest_str, str(page_num)))
        if os.path.exists(target_file): 
            logger.info("Has record of.." + target_file)
            continue

        sleep_time = 1
        while True:
            submissionResponse = requests.get(requestURL, headers = {'User-agent':'robot 0.0'})
            print(submissionResponse.text)
            if sleep_time > 100:
                break
            elif submissionResponse.status_code == 200:
                submissionResponse = submissionResponse.json()
                break
            else:
                # logging.info(submissionResponse.text)
                logger.info('Next wait time..' + str(sleep_time))
                time.sleep(sleep_time)
                sleep_time *= 2


        if(len(submissionResponse) < 1): break
        user_num = submissionResponse['user_num']
        if page_num > user_num / 25 + 1: break
        with open(target_file, 'w') as outputFile:
            json.dump(submissionResponse, outputFile)
    
    logger.info("Finished crawling json files..")
    # logging.shutdown()    

def crawlSubmission_raw(contest, page_end):


    contest_str = str(contest)
    # print('Now crawling raw files for contest..%s' % (contest_str))
    logger = Logger.getLogger(contest_str + "_submission")
    # print(logger)

    logger.info('Now crawling raw files for contest..%s' % (contest_str))
    logger.debug('Now crawling raw files for contest..%s' % (contest_str))
    
    found_new_record = False
    
    # record_content[contest] = collections.defaultdict(dict)

    cur_folder = str(pathlib.Path().resolve())

    submissionURL = "https://leetcode.com/api/submissions/%s"
    submissionURLCN = "https://leetcode-cn.com/api/submissions/%s"

    logger.info("Crawling raw files... %s " % contest_str)

    
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
        questions_filename = 'Contest_Submission/' + contest_str + '/questions.json'
        
        IO_Helper.writeJSON(questions_filename, questions)

        size = len(submissions)
        submissionCounter = 0
        # print('size=' + str(size))
        for submission in submissions:
            submissionCounter += 1
            for question_id in submission:
                submission_id = str(submission[question_id]['submission_id'])
                data_region = str(submission[question_id]['data_region'])

                
                submissionRequestURL = submissionURL
                if data_region == 'CN': submissionRequestURL = submissionURLCN
                submissionRequestURL = submissionRequestURL % submission_id

                logger.info("Crawling raw file [contest %s][page %s][counter %d][raw file %s][region %s][%.0f%%]" % (contest_str, page, submissionCounter, 
                    submission_id, data_region, (submissionCounter / size) * 100))

                # print(submission_id)
                if submission_id in raw_files_crawled_JSON: 
                    logger.info("Already crawled file [filename=%s].. [status=%s]" % (submission_id, raw_files_crawled_JSON[submission_id]))
                    continue
        
                raw_file_name = submission_id


                sleep_time = 1
                # logger.info(submissionRequestURL)
                
                flag = True
                while True:
                    submissionResponse = requests.get(submissionRequestURL)
                    if sleep_time > 32: 
                        logger.info('Request URL= ' + str(submissionRequestURL))
                        logger.info('Response Text= ' + str(submissionResponse.text))
                        flag = False
                        break
                    elif submissionResponse.status_code == 200: 
                        submissionResponse = submissionResponse.json()
                        break
                    elif submissionResponse.status_code == 401:
                        logger.info('Satus Code= ' + str(submissionResponse.status_code))
                        logger.info('Target does not exist')
                        break
                    else:
                        logger.info('Satus Code= ' + str(submissionResponse.status_code))
                        logger.info('Next wait time..' + str(sleep_time))
                        time.sleep(sleep_time)
                        sleep_time *= 2
                
                if not flag: 
                    logger.info("[raw file %s] not available" % submission_id)
                    if submissionResponse.status_code == 401:
                        raw_files_crawled_JSON[raw_file_name] = 'file not found'
                    else 
                        raw_files_crawled_JSON[raw_file_name] = 'error'
                    IO_Helper.writeJSON(file_name_crawled_raw, raw_files_crawled_JSON)
                    continue
                
                submission_raw_filename = outputLocation + str(submission_id) + '.json'
                raw_files_crawled_JSON[raw_file_name] = 'successfully crawled'
                IO_Helper.writeJSON(submission_raw_filename, submissionResponse)
                IO_Helper.writeJSON(file_name_crawled_raw, raw_files_crawled_JSON)  
    
if __name__ == '__main__':
    crawlSubmission_raw(89, 21)