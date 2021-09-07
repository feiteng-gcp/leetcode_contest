import os, requests, json, pathlib, subprocess, pytz, time, stat
from datetime import datetime


# for each contest
# loop through each page, will get this json
# {
# time: 1587875867.2136621,
# is_past: true,
# submissions: [],
# questions: [],
# total_rank: [],
# user_num: 11684
# }



def fetchContestRankingPage(contest):#, CNRegion = False, biweeklyContest = False):


    urlOne = "https://leetcode.com/contest/api/ranking/warm-up-contest/?pagination=%d"
    urlOld = "https://leetcode.com/contest/api/ranking/leetcode-weekly-contest-%s/?pagination=%d"
    url = "https://leetcode.com/contest/api/ranking/weekly-contest-%s/?pagination=%d"
    CNurl = "https://leetcode-cn.com/contest/api/ranking/weekly-contest-%s/?pagination=%d&region=local"
    url62 = "https://leetcode.com/contest/api/ranking/weekly-contest-by-app-academy/?pagination=%d"
    biweeklyURL = 'https://leetcode.com/contest/api/ranking/biweekly-contest-%s/?pagination=%d'
    CNBiweeklyURL = 'https://leetcode-cn.com/contest/api/ranking/biweekly-contest-%s/?pagination=%d&region=local'

    contest_str = str(contest)

    if contest_str == '16A' or contest_str == '16B' or contest_str == '18A' or contest_str == '18B': url = urlOld
    elif contest_str == '1': url = urlOne
    elif contest_str == '62': url = url62
    elif contest_str <= '57': url = urlOld

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
                    "rust":"rs"
    }

    
    print("Start crawling for contest.. %s " % (contest_str))
    
    cur_folder = str(pathlib.Path().resolve())

    target_folder = cur_folder + '/Contest_Ranking/' + contest_str + '/'

    user_num = 0

    for page_num in range(start, end + 1):

        if(page_num % 10 == 0): print('on page %d' % page_num)
        if contest_str == '1' or contest_str == '62': curURL = url % page_num
        else: curURL = url % (contest_str, page_num)

        try:
            # if file exists pass
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            target_file = target_folder + str(page_num) + '.json'
            if os.path.exists(target_file): continue

            resp = requests.get(curURL)
            str_response = resp.json()
            user_num = str_response['user_num']

            if page_num > user_num / 25 + 1: break
            if(len(str_response) < 1): break

            with open(target_file, 'a') as outputFile_:
                json.dump(str_response, outputFile_)
        except Exception as err:
            print(err)
            break

def parseSubmissions(contest, page_end):

    # print('parsing..')

    codingSuffix = {"cpp":"cpp",
                    "java":"java",
                    "python3":"py",
                    "python":"py",
                    "csharp":"cs",
                    "javascript":"js",
                    "golang":"go",
                    "rust":"rs"
    }


    contestName = str(contest)
    cur_folder = str(pathlib.Path().resolve())
    submissionURL = "https://leetcode.com/api/submissions/%d"
    submissionURLCN = "https://leetcode-cn.com/api/submissions/%d"

    print("Crawling submitted codes... %s " % contestName)

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
        try:
            Ranking_Page = Ranking_Folder + str(i) + '.json'
            Ranking_Page_JSON = {}
            with open(Ranking_Page) as file:
                Ranking_Page_JSON = json.load(file)
        except Exception as err:
            print(err)
            break

        submissions = Ranking_Page_JSON['submissions']
        total_rank = Ranking_Page_JSON['total_rank']

        for user in range(len(total_rank)):

            line = total_rank[user]

            submission = submissions[user]
            data_region = line['data_region']
            username = line['username']
            userrank = line['rank']
            for k in submission:
                print("[Contest=%s] Crawling submitted codes.. %d user.. %d submission.. %s"  % (contestName, i, user, k))
                try:
                    uniqueID = str(userrank) +  '_' + username + '_' + str(k)
                    if uniqueID in processedID: continue
                    processedID[uniqueID] = 1
                    kth_submission = submission[k]
                    submission_id = kth_submission['submission_id']
                    
                    submissionRequestURL = submissionURL

                    if data_region == 'CN': submissionRequestURL = submissionURLCN

                    submissionRequestURL = submissionRequestURL % submission_id

                    submissionResponse = requests.get(submissionRequestURL)
                    submissionResponse = submissionResponse.json()

                    coding_content =  submissionResponse['code']
                    coding_language = submissionResponse['lang']
                    
                    fileLocation = outputLocation + coding_language + '/' + str(k)
                    # print(fileLocation)
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
                    break
        with open(processedJSON, 'w') as outputFile:
            json.dump(processedID, outputFile)


def loadContest():
    f = open('contest', 'r')
    contest = f.readline()
    f.close()
    return contest

def writeContest(content):
    f = open('contest', 'w')
    f.write(str(content))
    f.close()


def commit_and_pushtoGithub(file):

    nyTime = pytz.timezone('America/New_York')
    nyTime = pytz.timezone('America/New_York')
    curTime = datetime.now(nyTime)
    cur_time = curTime.strftime('%Y %b %d %H:%M %p %z')
    commit_message = 'auto committed on .. ' + cur_time
    print('Trying to push..')

    push_successful = True
    try:

        subprocess.call(['git', 'add', file])
        subprocess.call(['git', 'commit' ,'-m', commit_message])
    # set your remote origin to https://<USERNAME>:<TOKEN>@github.com/USERNAME/PROJECT.git
    # or use subprocess.call(['git push', MYREPO])
    # where MYREPO = https://<USERNAME>:<TOKEN>@github.com/USERNAME/PROJECT.git
        subprocess.call(['git' ,'push'])
    except Exception as error:
        push_successful = False
        print(error)
        pass

    if push_successful:
        print("Successful..")

def jplag(contest):
    
    str_contest = str(contest)

    cur_folder = str(pathlib.Path().resolve()) + '/Contest_Submission/'
    contest_submission_folder = cur_folder + str_contest
    questionList = []
    for folder in os.scandir(contest_submission_folder + '/cpp'):
        questionList.append(folder.name)

    # questionList = [str(q) for q in questionList]
    languageList = ['java', 'cpp', 'python3']
    languageRef = ['java19', 'c/c++', 'python3']

    command1 = 'java -jar jplag-2.12.1-SNAPSHOT-jar-with-dependencies.jar -l '
    resultFolder = ' -r ./JPLAGResult/' + str_contest + '/'
    sourceFolder = ' -s "Contest_Submission/'

    for question in questionList:
        for i in range(0, 3):
            eachCommand = command1 + languageRef[i] + resultFolder + languageList[i] + 'Result/' + question + sourceFolder + str_contest + '/' + languageList[i] + '/' + question + '"'
            # print(changeDirectory + eachCommand)
            os.system(eachCommand)
    
def update_indexMD():
    contestNames = []
    for folder in os.scandir('JPLAGResult/'):
        # path = os.path.abspath(folder) + '/'
        # print(path)
        if folder.is_dir() and folder.name != '.git':
            contestNames.append(folder.name)

    rowDict = {}
    contestTimeDict = {}

    rank_folder = 'Contest_Ranking/'
    jplag_folder = 'JPLAGResult/'

    for contest in contestNames:
        # print('...contest=' + contest)
        
            
        # get contest crawl time
        contest_JSON_File = rank_folder + contest + '/1.json'
        lastModified  = os.path.getmtime(contest_JSON_File)
        # lastModified = time.ctime(file_stats[stat.ST_MTIME])

        # print(lastModified)

        # contest_finish_time = 0
        # with open(contest_JSON_File) as file:
        #     str_response = json.load(file)
        #     contest_finish_time = str_response['time']
        # if contest.startswith('CN'): continue
        jplag_result_path = jplag_folder +  contest

        questionList = []
        for folder in os.scandir(jplag_result_path + '/cppResult'):
            questionList.append(folder.name)

        contest = str(contest)
        codingLanguages = ['cpp', 'java', 'python3']
        linkBase = 'https://feiteng-gcp.github.io/leetcode_contest/JPLAGResult/'

        linkBase += contest + '/'

        text = '\n|' + contest + '|'
        for question in questionList:
            question = str(question)
            text += question
            for codingLanguage in codingLanguages:
                tmpLink = linkBase + codingLanguage + 'Result/' + question + '/index.html'
                text += ' [' + codingLanguage + '](' + tmpLink + ')'
            text += '|'
        # lastModified = os.path.getctime(JPLagResultFolder + '/' + contest)
        lastModified = datetime.fromtimestamp(lastModified).strftime('%Y/%m/%d')
        text += str(lastModified) + '|'
        rowDict[contest] = text
        # contestTimeDict[contest_finish_time] = contest
        # except Exception as err:
        #     print("error msg... %s" % err)
        #     pass


    banner = '**Code compare results generated by [JPLag](https://github.com/jplag/jplag)**\n\n' \
             'All comments welcomed\n\n' \
             '|Contest|Question||||Last Crawled|\n' \
             '|-|-|-|-|-|-|'

    MDFileLocation = 'index.md'
    f = open(MDFileLocation, 'w')
    f.write(banner)
    for key in sorted(rowDict.keys(), reverse = True):
        # contestKey = contestTimeDict[key]
        # print(contestKey)
        f.write(rowDict[key])
    f.close()




if __name__ == '__main__':

    page_end = 20   # check for top 500 people
    while True:
        contest = loadContest().strip()
        contest_int = (int)(contest)


        print(contest)
        
        fetchContestRankingPage(contest)
        parseSubmissions(contest, page_end)
        
        jplag(contest)

        update_indexMD()


        commit_and_pushtoGithub('JPLAGResult/' + contest)
        commit_and_pushtoGithub('index.md')

        contest_int = contest_int + 1

        writeContest(contest_int)

        # if page_end < 500: break   


