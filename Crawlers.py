import os, requests, json, pathlib, subprocess, pytz, time, stat
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
        if contest_str == '1' or contest_str == '62': curURL = url % page_num
        else: curURL = url % (contest_str, page_num)

        # try:
        # if file exists pass
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        target_file = target_folder + str(page_num) + '.json'
        if os.path.exists(target_file): 
            print("Has record of.." + target_file)
            continue

        # print(curURL)
        resp = requests.get(curURL)
        # print(resp)
        str_response = resp.json()
        
        user_num = str_response['user_num']

        if page_num > user_num / 25 + 1: break
        if(len(str_response) < 1): break

        with open(target_file, 'a') as outputFile_:
            json.dump(str_response, outputFile_)
        # except Exception as err:
        #     print(err)
        #     break
        
def crawlSubmissions(contest, page_end):

    # logging.info('parsing..')
    logging.basicConfig(
        level=logging.INFO,
        handlers=
        [
            logging.FileHandler('logging/' + contest + '.log'),
            logging.StreamHandler()
        ]
    )

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
    for i in range(1, page_end):
        time.sleep(1)
        # try:
        Ranking_Page = Ranking_Folder + str(i) + '.json'
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
            for k in submission:
                # if i % 20 == 0: 
                logging.info("[%s][Contest=%s] Crawling page.. %d user.. %d question num.. %s"  % (datetime.now(pytz.timezone('America/New_York')), contestName, i, user, k))
                # try:
                uniqueID = str(userrank) +  '_' + username + '_' + str(k)
                if uniqueID in processedID: 
                    logging.info(".......Submission exists")
                    continue
                processedID[uniqueID] = 1
                kth_submission = submission[k]
                submission_id = kth_submission['submission_id']
                
                submissionRequestURL = submissionURL

                if data_region == 'CN': submissionRequestURL = submissionURLCN

                submissionRequestURL = submissionRequestURL % submission_id

                sleep_time = 1
                while True:
                    submissionResponse = requests.get(submissionRequestURL)
                    # logging.info(submissionResponse.status_code)
                    if submissionResponse.status_code == 200: 
                        submissionResponse = submissionResponse.json()
                        break
                    else:
                        logging.info(submissionResponse.text)
                        print('next wait time..' + str(sleep_time))
                        time.sleep(sleep_time)
                        sleep_time *= 2

                    
                # logging.info(submissionResponse)

                # logging.info('Response = ')
                # logging.info(submissionResponse)
                coding_content =  submissionResponse['code']
                coding_language = submissionResponse['lang']

                if coding_language not in codingSuffix: codingSuffix[coding_language] = coding_language
                
                fileLocation = outputLocation + coding_language + '/' + str(k)
                # logging.info(fileLocation)
                if not os.path.exists(fileLocation):
                    os.makedirs(fileLocation)

                # save as contest - code language - [username][code content]
                filename = fileLocation + '/' + str(userrank) + '_' + username + '.' + codingSuffix[coding_language]
                if os.path.exists(filename): continue
                file = open(filename, 'w', encoding='utf-8')
                file.write(coding_content)
                file.close()
                # except Exception as err:
                #     print(err)
                #     pass
            with open(processedJSON, 'w') as outputFile:
                json.dump(processedID, outputFile)        


    logging.shutdown()