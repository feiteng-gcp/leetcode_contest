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

        # try:
        # if file exists pass
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        target_file = target_folder + str(page_num) + '.json'
        if os.path.exists(target_file): continue

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
        try:
            contest_JSON_File = rank_folder + contest + '/1.json'
            lastModified  = os.path.getmtime(contest_JSON_File)
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
            
            lastModified = datetime.fromtimestamp(lastModified).strftime('%Y/%m/%d')
            text += str(lastModified) + '|'
            rowDict[contest] = text
            # contestTimeDict[contest_finish_time] = contest
        except Exception as err:
            print("error msg... %s" % err)
            pass


    banner = '**Code compare results generated by [JPLag](https://github.com/jplag/jplag)**\n\n' \
             'All comments welcomed\n\n' \
             '|Contest|Question||||Last Crawled|\n' \
             '|-|-|-|-|-|-|'

    MDFileLocation = 'index.md'
    f = open(MDFileLocation, 'w')
    f.write(banner)
    contest_list = rowDict.keys()
    # sorted(list, key = lambda x : (int(x)), reverse=True)
    sorted_list = sorted(contest_list, key = lambda x : (int(x)), reverse = True)
    print(sorted_list)
    for key in sorted_list:# sorted(rowDict.keys(), reverse = True):
        # contestKey = contestTimeDict[key]
        # print(contestKey)
        f.write(rowDict[str(key)])
    f.close()

def writeToHTML():
    contestNames = []
    for folder in os.scandir('JPLAGResult/'):
        if folder.is_dir() and folder.name != '.git':
            contestNames.append(folder.name)

    rowDict = {}
    contestTimeDict = {}

    rank_folder = 'Contest_Ranking/'
    jplag_folder = 'JPLAGResult/'

    HTML_Head = """
    <!DOCTYPE html>
    <head>
    <meta charset="UTF-8">
    <title>Table</title>

    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.1/css/jquery.dataTables.min.css">

    <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>

    <script type="text/javascript" src="https://cdn.datatables.net/1.11.1/js/jquery.dataTables.min.js"></script>

    <script type="text/javascript">
        $(document).ready(function() {
            $('#example').DataTable();
        } );
    </script>

</head>
<body>
    """

    curTime = datetime.now(pytz.timezone('America/New_York'))
    cur_time = curTime.strftime('%Y %b %d %H:%M %p %z')
    banner = "<div><h4>Last Updated: " +  cur_time + "</h4></div><div>"
    HTML_Head_2 = """
    
    <table id="example" class="display" style="width:90%;font-size: x-small; margin:25px">
        <thead>
            <tr>
                <th>Contest</th>
                <th>Question</th>
                <th colspan=3>Language</th>
                <th>Last Crawled Time</th>
            </tr>
        </thead>
        <tbody>
        """

    HTML_Tail = """
        </tbody>
    </table>
    </div>
</body>
</html>
"""

    HTML_Body = ""

    for contest in sorted(contestNames, key = lambda x : (int(x)), reverse = True):
        
        try:
            
            contest_JSON_File = rank_folder + contest + '/1.json'
            lastModified  = os.path.getmtime(contest_JSON_File)
            lastModified = datetime.fromtimestamp(lastModified, pytz.timezone('America/New_York')).strftime('%Y %b %d %H:%M %p %z')
            jplag_result_path = jplag_folder +  contest

            questionList = []
            for folder in os.scandir(jplag_result_path + '/cppResult'):
                questionList.append(folder.name)

            HTML_Body += "<tr><td style='text-align:center' rowspan=" + str(len(questionList)) + ">" + str(contest) + "</td>"
            
            contest = str(contest)
            codingLanguages = ['cpp', 'java', 'python3']
            linkBase = 'https://feiteng-gcp.github.io/leetcode_contest/JPLAGResult/'

            linkBase += contest + '/'

            text = '\n|' + contest + '|'
            for question in sorted(questionList, key = lambda x : (int(x)), reverse = True): 
                question = str(question)
                HTML_Body += "<td style='text-align:center'>" + question + "</td>"
                text += question
                for codingLanguage in codingLanguages:
                    tmpLink = linkBase + codingLanguage + 'Result/' + question + '/index.html'
                    text += ' [' + codingLanguage + '](' + tmpLink + ')'
                    HTML_Body += "<td style='text-align:center' >" + "<a href='" + tmpLink + "'>" + codingLanguage + "</a></td>"
                text += '|'
                HTML_Body += "<td style='text-align:center' >" + lastModified + "</td></tr>"    

            
            
            
            text += str(lastModified) + '|'
            rowDict[contest] = text
            # contestTimeDict[contest_finish_time] = contest
        except Exception as err:
            # print("error msg... %s" % err)
            pass


    banner += '<p>Code compare results generated by <a href="https://github.com/jplag/jplag">JPLag</a></p><p>All comments welcomed</p>'

    HTML_FileLocation = 'index.html'
    f = open(HTML_FileLocation, 'w')
    f.write(HTML_Head + banner + HTML_Head_2 + HTML_Body + HTML_Tail)
    # contest_list = rowDict.keys()
    # # sorted(list, key = lambda x : (int(x)), reverse=True)
    # sorted_list = sorted(contest_list, key = lambda x : (int(x)), reverse = True)
    # print(sorted_list)
    # for key in sorted_list:# sorted(rowDict.keys(), reverse = True):
    #     # contestKey = contestTimeDict[key]
    #     # print(contestKey)
    #     f.write(rowDict[str(key)])
    f.close()




if __name__ == '__main__':

    debug = False
    page_end = 20   # check for top 500 people
    while True:
        try:
            if not debug: contest = loadContest().strip()
            if not debug: contest_int = (int)(contest)


            print(contest)
            
            if not debug: fetchContestRankingPage(contest)
            if not debug: parseSubmissions(contest, page_end)
            
            if not debug: jplag(contest)

            if not debug: update_indexMD()
            writeToHTML()
            if debug: break


            if not debug: commit_and_pushtoGithub('JPLAGResult/' + contest)
            if not debug: commit_and_pushtoGithub('index.html')

            if not debug: contest_int = contest_int + 1


            # writeContest(contest_int)
        except Exception as err:
            # retry it..
            pass
            

        # if page_end < 500: break   


