import os, requests, json, pathlib, subprocess, pytz, time, stat, collections
from datetime import datetime
import logging

def loadFile(file_name, default_content):
    try:
        f = open(file_name, 'r')
        content = f.readline()
        f.close()
    except Exception as err:
        print('ERRRRRR')
        print(err)
        content = default_content
        pass
    return content

def writeFile(file_name, file_content):
    f = open(file_name, 'w')
    f.write(file_content)
    f.close()

def loadJSON(file_name):
    # rootLogger = logging.getLogger()
    # rootLogger.info(file_name)
    
    try:
        f = open(file_name, 'r')
        content = json.load(f)
        return content

    except Exception as err:
        print(err)
        pass
    return {}

def writeJSON(file_name, file_content):
    # rootLogger = logging.getLogger()
    # rootLogger.info('Writing to json..[filename=%s]' % file_name)
    with open(file_name, 'w') as f:
        json.dump(file_content, f)
    f.close()


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

def writeToHTML():

    contestNames = []
    for folder in os.scandir('JPLAGResult/'):
        if folder.is_dir() and folder.name != '.git':
            contestNames.append(folder.name)
    print("Writing to HTML... Contest = ")
    print(contestNames)
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
    banner = "<div><h4><a href='https://github.com/feiteng-gcp'>Last Updated</a>: " +  cur_time + "</h4></div><div>"
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
            linkBase = 'https://storage.googleapis.com/jplagresult/JPLAGResult/'

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
                HTML_Body += "<td style='text-align:center' >" + lastModified + "</td></tr>\n"    

            
            
            
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


def commit_and_pushtoGithub(file):

    curTime = datetime.now(pytz.timezone('America/New_York'))
    cur_time = curTime.strftime('%Y %b %d %H:%M %p %z')
    commit_message = 'auto committed on .. ' + cur_time
    print('Starting to push..')

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

def loadSubmissionRecord(fileName, defaultOutput):
    json_load = defaultOutput
    try:
        f = open(fileName, 'r')
        json_load = json.load(f)
        f.close()
    except Exception:
        print(Exception)
        pass
    return json_load

def writeRecord(submission_record, submission_record_file):
    # print(submission_record)
    print('writing submission record to file..')
    file = open(submission_record_file, 'w')
    json.dump(submission_record, file)
    file.close()
    file = open('Submission_record.md', 'w')
    banner = "|"
    file.write('|Contest|Q1|Q2|Q3|Q4|Total|\n|-|-|-|-|-|-|\n')    
    for contest in submission_record:
        total_count = 0
        banner += '%s|' % (contest)
        for question_num in submission_record[contest]:
            count = submission_record[contest][question_num]
            total_count += count
            banner += '%d|' % (count)
        banner += str(total_count) + '|\n'
    file.write(banner)
    file.close()

def countAllSubmissions():
    folderName = "Contest_Submission/"
    record = collections.defaultdict(dict)
    for path, subdirs, files in os.walk(folderName):
        for name in files:
            filePath = os.path.join(path, name)
            filePath = filePath.replace("\\", "/")
            print(filePath)
            split = filePath.split("/")
            print(split)
            if len(split) > 3:
                contest = split[1]
                coding_language = split[2]
                question_num = split[3]
                if contest not in record: record[contest] = {}
                if question_num not in record[contest]:
                    record[contest][question_num] = {}
                if coding_language not in record[contest]:
                    record[contest][question_num][coding_language] = 0
                record[contest][question_num][coding_language] += 1
            # print(split)
    banner = '|Contest|Question Num|Coding Language|Count|\n|-|-|-|-|\n'
    for contest in record:
        for question_num in record[contest]:
            total = 0
            for coding_language in record[contest][question_num]:
                count = record[contest][question_num][coding_language]
                total += count
                banner += '|%s|%s|%s|%s|\n' % (str(contest), str(question_num), coding_language, str(count))
            banner += '|%s|Total|#|%s|\n' % (str(contest),str(total))


    file = open('submission_record.md', 'w')
    file.write(banner)
    file.close()