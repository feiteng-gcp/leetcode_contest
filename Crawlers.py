import os, requests, json, pathlib, subprocess, pytz, time, stat, collections
from datetime import datetime
import logging

def fetchContestRankingPage(contest):#, CNRegion = False, biweeklyContest = False):


    urlOne = "https://leetcode.com/contest/api/ranking/warm-up-contest/?pagination=%d"
    urlOld = "https://leetcode.com/contest/api/ranking/leetcode-weekly-contest-%s/?pagination=%d"
    url = "https://leetcode.com/contest/api/ranking/weekly-contest-%s/?pagination=%d"
    CNurl = "https://leetcode-cn.com/contest/api/ranking/weekly-contest-%s/?pagination=%d&region=local"
    url62 = "https://leetcode.com/contest/api/ranking/weekly-contest-by-app-academy/?pagination=%d"
    biweeklyURL = 'https://leetcode.com/contest/api/ranking/biweekly-contest-%s/?pagination=%d'
    CNBiweeklyURL = 'https://leetcode-cn.com/contest/api/ranking/biweekly-contest-%s/?pagination=%d&region=local'

    contest_str = str(contest)
    # contest_int = int(contest_str)


    # if contest_str == '16A' or contest_str == '16B' or contest_str == '18A' or contest_str == '18B': url = urlOld
    # elif contest_str == '1': url = urlOne
    # elif contest_str == '62': url = url62
    # elif contest_int <= 57: url = urlOld

    # if biweeklyContest: url = biweeklyURL
    # if CNRegion: url = CNurl
    # if CNRegion and biweeklyContest: url = CNBiweeklyURL
    data = {}
    
    start = 1
    end = 500   # default to 500 pages

    submissionURL = "https://leetcode.com/api/submissions/%d"
    # submissionURLCN = "https://leetcode-cn.com/api/submissions/%d"

    codingSuffix = {"cpp":"cpp",
                    "java":"java",
                    "python3":"py",
                    "python":"py",
                    "csharp":"cs",
                    "javascript":"js",
                    "golang":"go",
                    "rust":"rs",
                    "c":"c"
    }

    
    print("Start crawling for contest.. %s " % (contest_str))
    
    cur_folder = str(pathlib.Path().resolve())

    target_folder = cur_folder + '/Contest_Ranking/' + contest_str + '/'

    user_num = 0

    for page_num in range(start, end + 1):

        if(page_num % 10 == 0): print('on page %d' % page_num)
        if contest_str == '1' or contest_str == '62': requestURL = url % page_num
        else: requestURL = url % (contest_str, page_num)

        # try:
        # if file exists pass
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        target_file = target_folder + str(page_num) + '.json'
        if os.path.exists(target_file): 
            print("Has record of.." + target_file)
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
                print('next wait time..' + str(sleep_time))
                time.sleep(sleep_time)
                sleep_time *= 2


        try:
            if page_num > user_num / 25 + 1: break
            if(len(submissionResponse) < 1): break
            user_num = submissionResponse['user_num']
        except Exception as err:
            print(err)
            break
        with open(target_file, 'a') as outputFile_:
            json.dump(submissionResponse, outputFile_)
    
        
def crawlSubmissions(contest, page_end, record_content):

    found_new_record = False
    record_content[contest] = collections.defaultdict(dict)
    # logging.info('parsing..')
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=
        [
            logging.FileHandler('logging/' + contest + '.log'),
            logging.StreamHandler()
        ]
    )

    # record_content = {}# collections.defaultdict(dict)

    codingSuffix = {"cpp":"cpp",
                    "java":"java",
                    "python3":"py",
                    "python":"py",
                    "csharp":"cs",
                    "javascript":"js",
                    "golang":"go",
                    "rust":"rs",
                    "c":"c"
    }


    contestName = str(contest)
    cur_folder = str(pathlib.Path().resolve())
    submissionURL = "https://leetcode.com/api/submissions/%d"
    submissionURLCN = "https://leetcode-cn.com/api/submissions/%d"

    logging.info("Crawling submitted codes... %s " % contestName)

    # JSON_Location = 'C:/Users/lifeiteng/projects/visualizer/getRank/Contest JSON/' + contestName + '/'
    Ranking_Folder = cur_folder + '/Contest_Ranking/' + contestName + '/'
    outputLocation = cur_folder + '/Contest_Submission/' + contestName + '/'
    if not os.path.exists(outputLocation):
        os.makedirs(outputLocation)
    processedJSON = outputLocation + 'crawled.json'
    if not os.path.exists(processedJSON):
        f = open(processedJSON, 'w')
        f.write('{}')
        f.close()
    processedID = {}
    with open(processedJSON) as file:
        processedID = json.load(file)
    # assuming 500 pages, usually around 200
    for page in range(1, page_end):
        page_str = str(page)
        time.sleep(1)
        # try:
        Ranking_Page = Ranking_Folder + page_str + '.json'
        Ranking_Page_JSON = {}
        with open(Ranking_Page) as file:
            Ranking_Page_JSON = json.load(file)
        # except Exception as err:
        #     logging.info(err)
        #     break

        submissions = Ranking_Page_JSON['submissions']
        total_rank = Ranking_Page_JSON['total_rank']

        for user in range(len(total_rank)):

            line = total_rank[user]

            submission = submissions[user]
            data_region = line['data_region']
            username = line['username']
            userrank = line['rank']
            for question_num in submission:
                # try:
                uniqueID = str(userrank) +  '_' + username + '_' + str(question_num)
                cur_time = datetime.now(pytz.timezone('America/New_York'))
                if question_num not in record_content[contest]:
                    record_content[contest][question_num] = 0
                record_content[contest][question_num] += 1
                if uniqueID in processedID: 
                    logging.info("[%s][Contest=%s][page=%d][question=%s] submission exists" % (cur_time, contestName, page, question_num))
                    
                    continue
                # if i % 20 == 0: 
                logging.info("[%s][Contest=%s][Crawling page=%d][user=%d] question num.. %s"  % (cur_time, contestName, page, user, question_num))
                found_new_record = True
                processedID[uniqueID] = 1
                kth_submission = submission[question_num]
                submission_id = kth_submission['submission_id']
                
                submissionRequestURL = submissionURL

                if data_region == 'CN': submissionRequestURL = submissionURLCN

                submissionRequestURL = submissionRequestURL % submission_id

                sleep_time = 1
                while True:
                    submissionResponse = requests.get(submissionRequestURL)
                    # logging.info(submissionResponse.status_code)
                    if sleep_time > 100:
                        break
                    elif submissionResponse.status_code == 200: 
                        submissionResponse = submissionResponse.json()
                        break
                    else:
                        logging.info(submissionResponse.text)
                        print(submissionResponse)
                        print('next wait time..' + str(sleep_time))
                        time.sleep(sleep_time)
                        sleep_time *= 2
                try:
                    coding_content =  submissionResponse['code']
                    coding_language = submissionResponse['lang']
                    

                    if coding_language not in codingSuffix: codingSuffix[coding_language] = coding_language

                    
                    # print(record_content)
                    fileLocation = outputLocation + coding_language + '/' + str(question_num)
                    # logging.info(fileLocation)
                    if not os.path.exists(fileLocation):
                        os.makedirs(fileLocation)

                    # save as contest - code language - [username][code content]
                    filename = fileLocation + '/' + str(userrank) + '_' + username + '.' + codingSuffix[coding_language]
                    if os.path.exists(filename): continue
                    file = open(filename, 'w', encoding='utf-8')
                    file.write(coding_content)
                    file.close()
                except Exception as err:
                    print(err)
                    pass
            with open(processedJSON, 'w') as outputFile:
                json.dump(processedID, outputFile)        
            
    logging.shutdown()
    return found_new_record
