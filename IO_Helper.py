import os, requests, json, pathlib, subprocess, pytz, time, stat, collections
from datetime import datetime
import logging, Logger, traceback, configparser, Crawlers


def loadConfig():
    config = configparser.ConfigParser()
    config.read('assets/config.ini')
    return config

def loadContestMetaData(flag=False):
    config = loadConfig()
    filename = config['FILES']['CONTEST_METADATA_FILENAME'].strip()
    if flag: Crawlers.updateMetaData(filename)
    return loadJSON(filename)

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
    f = open(file_name, 'w', encoding='utf-8')
    f.write(file_content)
    f.close()

def loadJSON(file_name):
    # rootLogger = logging.getLogger()
    # rootLogger.info(file_name)
    
    if os.path.exists(file_name):
        f = open(file_name, 'r', encoding='utf-8')
        content = json.load(f)
        f.close()
        return content
    else: return {}

def writeJSON(file_name, file_content):
    # rootLogger = logging.getLogger()
    # rootLogger.info('Writing to json..[filename=%s]' % file_name)
    with open(file_name, 'w') as f:
        json.dump(file_content, f)
    f.close()


def jplag(contest):
    
    contest_str = str(contest)
    contest_submission_folder = 'Contest_Submission/' + contest_str + '/parsed-by-language/'
    question_dict = load_question_info(contest_str)
    # for question_num in question_dict:
    #     print(question_dict[question_num])

    languageFolder = "Contest_Submission/" + contest_str + "/parsed-by-language/"
    languageList = os.listdir(languageFolder)
    print(languageList)
    
    
    languagedict = {
            # 'c': 'c/c++',
            'cpp': 'c/c++',
            'csharp': 'c#-1.2',
            'java': 'java19',
            'python': 'python3',
            # 'javascript' : 'text'
                    }

    command1 = 'java -jar jplag-2.12.1-SNAPSHOT-jar-with-dependencies.jar -l '
    resultFolder = ' -r ./JPLAGResult/' + contest_str + '/'
    sourceFolder = ' -s "Contest_Submission/'

    for coding_language in languageList:
        jplag_language = 'text'
        if coding_language in languagedict: jplag_language = languagedict[coding_language]
        else: continue
        for question_num in question_dict:
            title_slug = question_dict[question_num]['title_slug']
            eachCommand = command1 + jplag_language + \
                resultFolder + coding_language  + '/' + title_slug + '/' + \
                sourceFolder + contest_str + '/parsed-by-language/' + coding_language + '/' + title_slug + '/"'
            os.system(eachCommand)    

# def jplag_():
#     title_slug = question_dict[question_num]['title_slug']
#     eachCommand = command1 + jplag_language + \
#         resultFolder + coding_language  + '/' + title_slug + '/' + \
#         sourceFolder + contest_str + '/parsed-by-language/' + coding_language + '/' + title_slug + '/"'
#     os.system(eachCommand)    



# def writeToHTML():

#     contestNames = []
#     for folder in os.scandir('JPLAGResult/'):
#         if folder.is_dir() and folder.name != '.git':
#             contestNames.append(folder.name)
#     print("Writing to HTML... Contest = ")
#     print(contestNames)
#     rowDict = {}
#     contestTimeDict = {}

#     rank_folder = 'Contest_Ranking/'
#     jplag_folder = 'JPLAGResult/'

#     HTML_Head = """
#     <!DOCTYPE html>
#     <head>
#     <meta charset="UTF-8">
#     <title>Table</title>

#     <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.1/css/jquery.dataTables.min.css">

#     <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>

#     <script type="text/javascript" src="https://cdn.datatables.net/1.11.1/js/jquery.dataTables.min.js"></script>

#     <script type="text/javascript">
#         $(document).ready(function() {
#             $('#example').DataTable();
#         } );
#     </script>

# </head>
# <body>
#     """

#     curTime = datetime.now(pytz.timezone('America/New_York'))
#     cur_time = curTime.strftime('%Y %b %d %H:%M %p %z')
#     banner = "<div><h4><a href='https://github.com/feiteng-gcp'>Last Updated</a>: " +  cur_time + "</h4></div><div>"
#     HTML_Head_2 = """
    
#     <table id="example" class="display" style="width:90%;font-size: x-small; margin:25px">
#         <thead>
#             <tr>
#                 <th>Contest</th>
#                 <th>Question</th>
#                 <th colspan=3>Language</th>
#                 <th>Last Crawled Time</th>
#             </tr>
#         </thead>
#         <tbody>
#         """

#     HTML_Tail = """
#         </tbody>
#     </table>
#     </div>
# </body>
# </html>
# """

#     HTML_Body = ""

#     for contest in sorted(contestNames, key = lambda x : (int(x)), reverse = True):
        
#         try:
            
#             contest_JSON_File = rank_folder + contest + '/1.json'
#             lastModified  = os.path.getmtime(contest_JSON_File)
#             lastModified = datetime.fromtimestamp(lastModified, pytz.timezone('America/New_York')).strftime('%Y %b %d %H:%M %p %z')
#             jplag_result_path = jplag_folder +  contest

#             questionList = []
#             for folder in os.scandir(jplag_result_path + '/cppResult'):
#                 questionList.append(folder.name)

#             HTML_Body += "<tr><td style='text-align:center' rowspan=" + str(len(questionList)) + ">" + str(contest) + "</td>"
            
#             contest = str(contest)
#             codingLanguages = ['cpp', 'java', 'python3']
#             linkBase = 'https://storage.googleapis.com/jplagresult/JPLAGResult/'

#             linkBase += contest + '/'

#             text = '\n|' + contest + '|'
#             for question in sorted(questionList, key = lambda x : (int(x)), reverse = True): 
#                 question = str(question)
#                 HTML_Body += "<td style='text-align:center'>" + question + "</td>"
#                 text += question
#                 for codingLanguage in codingLanguages:
#                     tmpLink = linkBase + codingLanguage + 'Result/' + question + '/index.html'
#                     text += ' [' + codingLanguage + '](' + tmpLink + ')'
#                     HTML_Body += "<td style='text-align:center' >" + "<a href='" + tmpLink + "'>" + codingLanguage + "</a></td>"
#                 text += '|'
#                 HTML_Body += "<td style='text-align:center' >" + lastModified + "</td></tr>\n"    

            
            
            
#             text += str(lastModified) + '|'
#             rowDict[contest] = text
#             # contestTimeDict[contest_finish_time] = contest
#         except Exception as err:
#             # print("error msg... %s" % err)
#             pass


#     banner += '<p>Code compare results generated by <a href="https://github.com/jplag/jplag">JPLag</a></p><p>All comments welcomed</p>'

#     HTML_FileLocation = 'index.html'
#     f = open(HTML_FileLocation, 'w')
#     f.write(HTML_Head + banner + HTML_Head_2 + HTML_Body + HTML_Tail)
#     # contest_list = rowDict.keys()
#     # # sorted(list, key = lambda x : (int(x)), reverse=True)
#     # sorted_list = sorted(contest_list, key = lambda x : (int(x)), reverse = True)
#     # print(sorted_list)
#     # for key in sorted_list:# sorted(rowDict.keys(), reverse = True):
#     #     # contestKey = contestTimeDict[key]
#     #     # print(contestKey)
#     #     f.write(rowDict[str(key)])
#     f.close()            


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

def load_question_info(contest):
    contest_str = str(contest)
    rank_file = "Contest_Ranking/" + contest_str + "/" + "1.json"
    rank_info = loadJSON(rank_file)

    question_dict = collections.defaultdict(dict)
    question_info = rank_info['questions']
    for each_question in question_info:

        question_dict[str(each_question['question_id'])] = {
            'title' : each_question['title'],
            'title_slug': each_question['title_slug']
        }
    return question_dict

def parseContest(contest):
    
    contest_str = str(contest)
    logger = Logger.getLogger(contest_str + "_parsing")
    rankingFolder = "Contest_Ranking/" + contest_str + "/"
    submissionFolder = "Contest_Submission/" + contest_str
    raw_submissionFolder = submissionFolder + "/raw/"

    # for each submission, write submitted to file
    # format [rank=%rank][username].[coding_language]]
    #

    question_dict = load_question_info(contest_str)
     # collections.defaultdict(dict)
    page_end = 21

    suffix = {
            'python':'py',
            'csharp':'cs',
            'javascript' : 'js'
            }

    for page in range(1, page_end):
        print('Parsing[Contest=%s][page=%s]' % (contest_str, str(page)))
        rank_file = rankingFolder + str(page) + ".json"
        rank_info = loadJSON(rank_file)
        # print(rank_info)
        submission = rank_info['submissions']
        # question_info = rank_info['questions']
        # for each_question in question_info:
        #     # print(each_question['question_id'])
        #     question_dict[str(each_question['question_id'])] = {
        #         'title' : each_question['title'],
        #         'title_slug': each_question['title_slug']
        #     }
        # print(question_dict)


        user_ranking_info = rank_info['total_rank']
        size = len(submission)
        # size = 1
        for idx in range(size):
            # print(idx)
            # print(submission[idx])
            # print(user_ranking_info[idx])
            username = user_ranking_info[idx]['username']
            userrank = user_ranking_info[idx]['rank']
            for each_submission in submission[idx]:
                submission_detail = submission[idx][each_submission]
                question_id = str(submission_detail['question_id'])
                submission_id = str(submission_detail['submission_id'])
                try:
                    # not all files are crawled, handle them
                    submission_content = loadJSON(raw_submissionFolder + submission_id + '.json')
                    submitted_code_content = submission_content['code']
                    # print(submitted_code_content)
                    coding_language = submission_content['lang']
                    if coding_language == 'python3': coding_language = 'python'
                    if coding_language == 'c': coding_language = 'cpp'
                    language_suffix = coding_language
                    if coding_language in suffix: language_suffix = suffix[coding_language]

                    user_file = '[%s][%s][submission-id=%s].%s' % (userrank ,username, submission_id, language_suffix)
                    # print(user_file)
                    # group by same coding language
                    # print('question_id=' + str(question_id))
                    target_folder = submissionFolder + '/parsed-by-language/' + coding_language + '/' + question_dict[question_id]['title_slug']
                    # print('target_folder=' + target_folder)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    
                    user_file_path = target_folder + '/' + user_file
                    # print('user_file_path=' + user_file_path)
                    writeFile(user_file_path, submitted_code_content)
                except Exception as err:
                    traceback.print_exc()
                    pass

def getLastCrawledTime(contest):
    contest_str = str(contest)
    crawled_ranking_file = "Contest_Ranking/%s/1.json" % (contest_str)
    lastModified_info  = os.path.getmtime(crawled_ranking_file)
    return datetime.fromtimestamp(lastModified_info, pytz.timezone('America/New_York')).strftime('%Y %b %d %H:%M %p %z')

# def writeRecord():
#     jplag_folder = "JPLAGResult/"
#     finished_contests = os.listdir(jplag_folder)
#     record = []
#     languagedict = {
#             'cpp': 'c/c++',
#             'csharp': 'c#-1.2',
#             'java': 'java19',
#             'python': 'python3',
#             }

#     for contest_str in sorted(finished_contests, key = lambda x : (int(x)), reverse = True):
#         last_crawled_time = getLastCrawledTime(contest_str)
#         question_dict = load_question_info(contest_str)
#         for question_num in question_dict:
#             title = question_dict[question_num]['title']
#             title_slug = question_dict[question_num]['title_slug']
#             for coding_language in languagedict:
#                 local_dir = "JPLAGResult/%s/%s/%s/" % (contest_str, coding_language, title_slug)
#                 if not os.path.exists(local_dir): continue
#                 contest_line_item = []
#                 contest_line_item.append(contest_str)
#                 link = 'https://storage.googleapis.com/jplagresult/JPLAGResult/%s/%s/%s/index.html' % (contest_str, coding_language, title_slug)
#                 leetcode_link = 'https://leetcode.com/problems/%s' % (title_slug)
#                 text = title
#                 contest_line_item.append('<a href="%s">%s</a>' % (leetcode_link, title))
#                 contest_line_item.append('<a href="%s">%s</a>' % (link, coding_language))
#                 contest_line_item.append(last_crawled_time)
#                 record.append(contest_line_item)

#     writeJSON('compare_record.json', record)
    # print(record)

def writeRecord():
    jplag_folder = "JPLAGResult/"
    finished_contests = os.listdir(jplag_folder)
    record = {}
    record['data'] = []
    languagedict = {
            'cpp': 'c/c++',
            'csharp': 'c#-1.2',
            'java': 'java19',
            'python': 'python3',
            }

    Contest_Metadata = loadContestMetaData()

    for contest_str in sorted(finished_contests, key = lambda x : (Contest_Metadata[x]['startTime']), reverse = True):
        last_crawled_time = getLastCrawledTime(contest_str)
        question_dict = load_question_info(contest_str)
        for question_num in question_dict:
            title = question_dict[question_num]['title']
            title_slug = question_dict[question_num]['title_slug']
            for coding_language in languagedict:
                local_dir = "JPLAGResult/%s/%s/%s/" % (contest_str, coding_language, title_slug)
                if not os.path.exists(local_dir): continue
                contest_line_item = {}
                contest_line_item['contest']=contest_str
                link = 'https://storage.googleapis.com/jplagresult/JPLAGResult/%s/%s/%s/index.html' % (contest_str, coding_language, title_slug)
                leetcode_link = 'https://leetcode.com/problems/%s' % (title_slug)
                text = title
                contest_line_item['title']='<a href="%s">%s</a>' % (leetcode_link, title)
                contest_line_item['coding_language']='<a href="%s">%s</a>' % (link, coding_language)
                contest_line_item['last_modified']=last_crawled_time
                record['data'].append(contest_line_item)

    writeJSON('compare_record_.json', record)

def parse_and_runJPLag(contest):
    # parseContest(contest)
    # jplag(contest)
    writeRecord()


if __name__ == '__main__':
    writeRecord_()
    # parseContest(65)
    # jplag(65)




