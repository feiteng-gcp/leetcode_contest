import os, requests, json, pathlib, subprocess, pytz, time, stat, collections
from datetime import datetime
import logging, IO_Helper
import logging.config

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

    logger = logging.getLogger("Crawl Log")

    contest_str = str(contest)

    data = {}
    
    start_page = 1
    end_page = 1000   # default to 500 pages

    logger.info("Start crawling for contest.. %s " % (contest_str))
    
    cur_folder = str(pathlib.Path().resolve())
    target_folder = cur_folder + '/Contest_Ranking/' + contest_str + '/'

    user_num = 0

    url = rankingURL(contest)

    for page_num in range(start_page, end_page + 1):

        if(page_num % 10 == 0): logger.info('on page %d' % page_num)
        if contest_str == '1' or contest_str == '62': requestURL = url % page_num
        else: requestURL = url % (contest_str, page_num)

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        target_file = target_folder + str(page_num) + '.json'

        if os.path.exists(target_file): 
            logger.info("Has record of.." + target_file)
            continue

        sleep_time = 1
        while True:
            submissionResponse = requests.get(requestURL)
            # logging.info(submissionResponse.status_code)
            if sleep_time > 100:
                break
            elif submissionResponse.status_code == 200:
                submissionResponse = submissionResponse.json()
                break
            else:
                logging.info(submissionResponse.text)
                logger.info('Next wait time..' + str(sleep_time))
                time.sleep(sleep_time)
                sleep_time *= 2


        try:
            if page_num > user_num / 25 + 1: break
            if(len(submissionResponse) < 1): break
            user_num = submissionResponse['user_num']
        except Exception as err:
            logger.debug(err)
            break
        with open(target_file, 'a') as outputFile_:
            json.dump(submissionResponse, outputFile_)
    
        
# def crawlSubmissions(contest, page_end, record_content):

#     found_new_record = False
#     record_content[contest] = collections.defaultdict(dict)
#     # logging.info('parsing..')
#     logging.basicConfig(
#         level=logging.DEBUG,
#         handlers=
#         [
#             logging.FileHandler('logging/Crawling.log'),
#             logging.StreamHandler()
#         ]
#     )

#     # record_content = {}# collections.defaultdict(dict)

#     codingSuffix = {"cpp":"cpp",
#                     "java":"java",
#                     "python3":"py",
#                     "python":"py",
#                     "csharp":"cs",
#                     "javascript":"js",
#                     "golang":"go",
#                     "rust":"rs",
#                     "c":"c"
#     }


#     contestName = str(contest)
#     cur_folder = str(pathlib.Path().resolve())
#     submissionURL = "https://leetcode.com/api/submissions/%d"
#     submissionURLCN = "https://leetcode-cn.com/api/submissions/%d"

#     logging.info("Crawling submitted codes... %s " % contestName)

#     # JSON_Location = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest JSON/' + contestName + '/'
#     Ranking_Folder = cur_folder + '/Contest_Ranking/' + contestName + '/'
#     outputLocation = cur_folder + '/Contest_Submission/' + contestName + '/'
#     if not os.path.exists(outputLocation):
#         os.makedirs(outputLocation)
#     processedJSON = outputLocation + 'crawled.json'
#     if not os.path.exists(processedJSON):
#         f = open(processedJSON, 'w')
#         f.write('{}')
#         f.close()
#     processedID = {}
#     with open(processedJSON) as file:
#         processedID = json.load(file)
#     # assuming 500 pages, usually around 200
#     for page in range(1, page_end):
#         page_str = str(page)
#         time.sleep(1)
#         # try:
#         Ranking_Page = Ranking_Folder + page_str + '.json'
#         Ranking_Page_JSON = {}
#         with open(Ranking_Page) as file:
#             Ranking_Page_JSON = json.load(file)
#         # except Exception as err:
#         #     logging.info(err)
#         #     break

#         submissions = Ranking_Page_JSON['submissions']
#         total_rank = Ranking_Page_JSON['total_rank']

#         for user in range(len(total_rank)):

#             line = total_rank[user]

#             submission = submissions[user]
#             data_region = line['data_region']
#             username = line['username']
#             userrank = line['rank']
#             for question_num in submission:
#                 # try:
#                 uniqueID = str(userrank) +  '_' + username + '_' + str(question_num)
#                 cur_time = datetime.now(pytz.timezone('America/New_York'))
#                 if question_num not in record_content[contest]:
#                     record_content[contest][question_num] = 0
#                 record_content[contest][question_num] += 1
#                 if uniqueID in processedID: 
#                     logging.info("[%s][Contest=%s][page=%d][question=%s] submission exists" % (cur_time, contestName, page, question_num))
                    
#                     continue
#                 # if i % 20 == 0: 
#                 logging.info("[%s][Contest=%s][Crawling page=%d][user=%d] question num.. %s"  % (cur_time, contestName, page, user, question_num))
#                 found_new_record = True
#                 processedID[uniqueID] = 1
#                 kth_submission = submission[question_num]
#                 submission_id = kth_submission['submission_id']
                
#                 submissionRequestURL = submissionURL

#                 if data_region == 'CN': submissionRequestURL = submissionURLCN

#                 submissionRequestURL = submissionRequestURL % submission_id

#                 sleep_time = 1
#                 while True:
#                     submissionResponse = requests.get(submissionRequestURL)
#                     # logging.info(submissionResponse.status_code)
#                     if sleep_time > 100:
#                         break
#                     elif submissionResponse.status_code == 200: 
#                         submissionResponse = submissionResponse.json()
#                         break
#                     else:
#                         logging.info(submissionResponse.text)
#                         print(submissionResponse)
#                         print('next wait time..' + str(sleep_time))
#                         time.sleep(sleep_time)
#                         sleep_time *= 2
#                 try:
#                     coding_content =  submissionResponse['code']
#                     coding_language = submissionResponse['lang']
                    

#                     if coding_language not in codingSuffix: codingSuffix[coding_language] = coding_language
#                     coding_language = codingSuffix[coding_language]
                    
#                     # print(record_content)
#                     fileLocation = outputLocation + coding_language + '/' + str(question_num)
#                     # logging.info(fileLocation)
#                     if not os.path.exists(fileLocation):
#                         os.makedirs(fileLocation)

#                     # save as contest - code language - [username][code content]
#                     filename = fileLocation + '/' + str(userrank) + '_' + username + '.' + coding_language
#                     if os.path.exists(filename): continue
#                     file = open(filename, 'w', encoding='utf-8')
#                     file.write(coding_content)
#                     file.close()
#                 except Exception as err:
#                     print(err)
#                     pass
#             with open(processedJSON, 'w') as outputFile:
#                 json.dump(processedID, outputFile)        
            
#     # logging.shutdown()
#     print(record_content)
#     return found_new_record


def crawlSubmission_raw(contest, page_end):

    contest_str = str(contest)
    log_path = "logging/crawling_raw/{0}.log".format(contest_str)
    logging.config.fileConfig('logging.conf', defaults={'logfilename':log_path})
    logger = logging.getLogger(log_path)

    logger.info('Now crawling raw files for contest..%s' % (contest_str))
    
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

        for submission in submissions:
            for question_id in submission:
                submission_id = str(submission[question_id]['submission_id'])
                data_region = str(submission[question_id]['data_region'])

                
                submissionRequestURL = submissionURL
                if data_region == 'CN': submissionRequestURL = submissionURLCN
                submissionRequestURL = submissionRequestURL % submission_id

                logger.info("Crawling..[page %s][question %s][raw file %s]" % (page, question_id, submission_id))

                # print(submission_id)
                if submission_id in raw_files_crawled_JSON: 
                    logger.info("[filename=%s] exists in system" % submission_id) 
                    continue
        
                raw_file_name = submission_id


                sleep_time = 1
                # logger.info(submissionRequestURL)
                
                while True:
                    submissionResponse = requests.get(submissionRequestURL)
                    if sleep_time > 100:
                        break
                    elif submissionResponse.status_code == 200: 
                        submissionResponse = submissionResponse.json()
                        break
                    else:
                        logger.info('Next wait time..' + str(sleep_time))
                        time.sleep(sleep_time)
                        sleep_time *= 2
                    
                submission_raw_filename = outputLocation + str(submission_id) + '.json'
                raw_files_crawled_JSON[raw_file_name] = '1'
                
                IO_Helper.writeJSON(submission_raw_filename, submissionResponse)
                IO_Helper.writeJSON(file_name_crawled_raw, raw_files_crawled_JSON)
    