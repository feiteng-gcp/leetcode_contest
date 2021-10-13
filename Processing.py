import os, requests, json, pathlib, subprocess, pytz, time, stat, collections, hashlib, IO_Helper
from datetime import datetime
from checksumdir import dirhash
import logging, Logger, traceback
import concurrent.futures


def write_question_internal_ratings(CONTEST_METADATA, logger):
    # update_question_metadata()
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        Question_Metadata_filename = 'Question_Metadata.json'
        Question_Metadata = IO_Helper.loadJSON(Question_Metadata_filename)
        
        question_slug_ID = {}
        for question_frontendID in Question_Metadata:
            question_info = Question_Metadata[question_frontendID]
            question_title_slug = question_info['question_slug']
            question_slug_ID[question_title_slug] = question_frontendID


        question_internal_rating = {}
        question_internal_rating['data'] = []
        for contest_title_slug in CONTEST_METADATA:
                target_file = 'Contest_Ranking/' + contest_title_slug + '/1.json'
                submission_page = IO_Helper.loadJSON(target_file)
                for questions in submission_page['questions']:
                    question_title_slug = questions['title_slug']
                    question_frontendID = question_slug_ID[question_title_slug]

                    logger.info('calculating for [Question=%s]' % question_title_slug)
                    target_file = 'Question_Ratings_raw/' + question_title_slug + '.json'
                    file_content = IO_Helper.loadJSON(target_file)
                    leetcode_link = 'https://leetcode.com/problems/%s' % (question_title_slug)
                    question_link = '<a href="%s">%s</a>' % (leetcode_link, question_title_slug)
                    internal_rating = '#n/a'
                    # if question_title_slug in INTERNAL_RATING_RECORD:
                    # internal_rating = calcRating(file_content['data'])
                    process = executor.submit(calcRating, file_content['data'])
                    internal_rating = process.result()

                    
                    rating_base_link = 'http://feiteng-gcp.github.io/leetcode_contest/ratings_distribution.html?%s' % question_title_slug
                    rating_link = '<a href="%s">%s</a>' % (rating_base_link, str(internal_rating))

                    question_internal_rating['data'].append({
                        'frontend_id' : question_frontendID,
                        'title' : question_link,
                        'title_slug' : question_title_slug,
                        'rating' : rating_link,
                    })
                    question_internal_rating_filename = 'question_internal_rating_web.json'
                    IO_Helper.writeJSON(question_internal_rating_filename, question_internal_rating)
    # IO_Helper.commit_and_pushtoGithub(question_internal_rating_filename)

    finish = time.perf_counter()
    print(f'finished in {finish-start} seconds')

def calcRating(ratings):
    # print(ratings)
    avg = 0
    count = 0
    for rating in ratings:
        if rating > 0:
            avg += rating
            count += 1
    if count == 0: return '#n/a'
    return avg // count


def update_question_metadata():
    print('Updating meta data..')
    import requests, json
    url = 'https://leetcode.com/api/problems/algorithms/'
    CSRF_Token = '77HhPMor1cJWx7fEIZCrUkYvODrQCEf3QdcHUKSexKhpbRayWMtrREWiAsviKHls'
    COOKIE = 'csrftoken=' + CSRF_Token
    headers = {
        'referer': 'https://leetcode.com/accounts/login/',
        'cookie' : COOKIE,
        'x-csrftoken' : CSRF_Token
    }

    resp = json.loads(requests.get(url, headers = headers).text)

    data = {}
    for item in resp['stat_status_pairs']:
        map = item['stat']
        question_id = map['question_id']
        question__title = map['question__title']
        frontend_question_id = map['frontend_question_id']
        question_slug  = map['question__title_slug']
        data[str(frontend_question_id)] = {
            'question_id' : question_id,
            'question_title': question__title,
            'question_slug' : question_slug
        }

    with open('Question_Metadata.json', 'w') as file:
        json.dump(data, file)    



def get_question_internal_ratings_raw(CONTEST_METADATA, logger):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for contest_title_slug in CONTEST_METADATA:
            
            submission_page_file = 'Contest_Ranking/' + contest_title_slug + '/1.json'
            if not os.path.exists(submission_page_file): continue

            submission_page = IO_Helper.loadJSON(submission_page_file)
            # print(submission_page)
            for questions in submission_page['questions']:
                question_title_slug = questions['title_slug']
                target_file = 'Question_Ratings_raw/' + question_title_slug + '.json'
                if os.path.exists(target_file): continue
                logger.info('Getting rating for [Contest=%s][Question=%s]' % (contest_title_slug, question_title_slug))
                # if question_title_slug in INTERNAL_RATING_RECORD: continue
                file_name = 'Passed_User/' + question_title_slug + '.json'
                # print(file_name)
                user_list = IO_Helper.loadJSON(file_name)
                user_list_len = len(user_list)
                ratings = {}
                ratings['data'] = []
                counter = 0
                for user_info in user_list:
                    # logger.info('[Contest=%s][Question=%s][User=%s][Progress=%.2f%%]' % (contest_title_slug, question_title_slug, user_info['user_slug'], counter / user_list_len * 100))
                    # user_rating = get_user_rating(user_info, contest_title_slug, logger)
                    user_rating = executor.submit(get_user_rating, user_info, contest_title_slug, logger)
                    
                    # print('[Contest=%s][question=%s][username=%s][user_rating=%s]' % (contest_title_slug, question_title_slug,user_info['user_slug'], str(user_rating)))
                    # if user_rating >= 0: ratings.append(user_rating)
                    ratings['data'].append(user_rating.result())
                    counter += 1
                    # if counter > 3: break

                # average_rating = sum(ratings) // len(ratings)
                # INTERNAL_RATING_RECORD[question_title_slug] = ratings #average_rating
                IO_Helper.writeJSON(target_file, ratings)    

def get_question_internal_ratings(CONTEST_METADATA, INTERNAL_RATING_RECORD_FILENAME, 
    INTERNAL_RATING_RECORD, logger):
    # if question_title_slug in INTERNAL_RATING_RECORD: return
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for contest_title_slug in CONTEST_METADATA:
            logger.info('Getting rating for [Contest=%s]' % (contest_title_slug))
            target_file = 'Contest_Ranking/' + contest_title_slug + '/1.json'
            # print(target_file)
            submission_page = IO_Helper.loadJSON(target_file)
            # print(submission_page)
            for questions in submission_page['questions']:
                question_title_slug = questions['title_slug']
                if question_title_slug in INTERNAL_RATING_RECORD: continue
                file_name = 'Passed_User/' + question_title_slug + '.json'
                print(file_name)
                user_list = IO_Helper.loadJSON(file_name)
                user_list_len = len(user_list)
                ratings = []
                counter = 0
                for user_info in user_list:
                    # logger.info('[Contest=%s][Question=%s][User=%s][Progress=%.2f%%]' % (contest_title_slug, question_title_slug, user_info['user_slug'], counter / user_list_len * 100))
                    # user_rating = get_user_rating(user_info, contest_title_slug, logger)
                    user_rating = executor.submit(get_user_rating, user_info, contest_title_slug, logger)
                    
                    print('[Contest=%s][question=%s][username=%s][user_rating=%s]' % (contest_title_slug, question_title_slug,user_info['user_slug'], str(user_rating)))
                    # if user_rating >= 0: ratings.append(user_rating)
                    ratings.append(user_rating.result())
                    counter += 1
                    # if counter > 3: break

                # average_rating = sum(ratings) // len(ratings)
                INTERNAL_RATING_RECORD[question_title_slug] = ratings #average_rating
                IO_Helper.writeJSON(INTERNAL_RATING_RECORD_FILENAME, INTERNAL_RATING_RECORD)
        # break
    


def get_user_rating(USERINFO, CONTEST_TITLE_SLUG, logger):
    
    USERNAME = USERINFO['user_slug']
    USER_REGION = USERINFO['user_region']
    filename = 'User_Rating_Parsed/' + USERNAME + '.json'
    parse_user_rating(USERNAME, USER_REGION, filename)
    USER_RATING_RECORD = IO_Helper.loadJSON(filename)
    
    # print(filename)
    # print(USER_RATING_RECORD)
    # return

    if CONTEST_TITLE_SLUG in USER_RATING_RECORD:
    
        # logger.info('Already processed rating for User=%s contest=%s' % (USERNAME, CONTEST_TITLE_SLUG))
        # user_rating = USER_RATING_RECORD[USERNAME][CONTEST_TITLE_SLUG]
        # # logger.info(USER_RATING_RECORD[USERNAME])
        # if user_rating == None: USER_RATING_RECORD[USERNAME][CONTEST_TITLE_SLUG] = 1500
        return USER_RATING_RECORD[CONTEST_TITLE_SLUG]
    
    # 
    # logger.info('Getting rating[username=%s][USER_REGION=%s]' % (USERNAME, USER_REGION))

    # if USERNAME not in USER_RATING_REMECORD:
    #     USER_RATING_RECORD[USERNA] = {}

    # try:
    #     if USER_REGION == 'US': get_user_rating_US(USERNAME, USER_RATING_RECORD)
    #     else: get_user_rating_CN(USERNAME, USER_RATING_RECORD)
        
    #     IO_Helper.writeJSON(filename, USER_RATING_RECORD)
    #     return USER_RATING_RECORD[CONTEST_TITLE_SLUG]
    # except Exception as err:
    logger.info('Error loading rating for [username=%s][user-region=%s][Contest=%s]' % (USERNAME, USER_REGION, CONTEST_TITLE_SLUG))
    return -1

def parse_user_rating(USERNAME, USER_REGION, filename):
    try:
        print('Parsing [Username=%s][region=%s][File=%s]' % (USERNAME, USER_REGION, filename))
        USER_RATING_RECORD = IO_Helper.loadJSON(filename)
        if USER_REGION == 'US': parse_user_rating_US(USERNAME, USER_RATING_RECORD)
        else: parse_user_rating_CN(USERNAME, USER_RATING_RECORD)
        IO_Helper.writeJSON(filename, USER_RATING_RECORD)
    except:
        traceback.print_exc()

def parse_user_rating_US(USERNAME, USER_RATING_RECORD):
    try:
        file_name = 'User_Rating_Raw/' + USERNAME + '.json'
        file_content = IO_Helper.loadJSON(file_name)
        contest_ratings = file_content['data']['userContestRankingHistory']
        for item in contest_ratings:
            title_slug = item['contest']['titleSlug']
            rating = item['rating']
            USER_RATING_RECORD[title_slug] = rating
    except:
        traceback.print_exc()
    


def parse_user_rating_CN(USERNAME, USER_RATING_RECORD):
    try:
        file_name = 'User_Rating_Raw/' + USERNAME + '.json'
        if not os.path.exists(file_name): return
        file_content = IO_Helper.loadJSON(file_name)
        ratings_list = json.loads(file_content['data']['userContestRanking']['ratingHistory'])
        contest_list = json.loads(file_content['data']['userContestRanking']['contestHistory'])

        # counter = 0
        size1 = len(ratings_list)
        for idx in range(size1):
            title_slug = contest_list[idx]['title_slug']
            rating = ratings_list[idx]
            # print('[Username=%s][contest=%s][rating=%s]' % (USERNAME, title_slug, rating))
            if rating == None: rating = 1500 #default rating
            USER_RATING_RECORD[title_slug] = rating
    except:
        traceback.print_exc()

def get_contest_question_pass_users(CONTEST_QUESTION_PASS_RECORD_FILENAME, contest_title_slug, 
    CONTEST_QUESTION_PASS_RECORD, logger):
    # if contest_title_slug in CONTEST_QUESTION_PASS_RECORD:
    #     print('Already processed Contest=%s' % contest_title_slug)
    #     return
    try:
        
        folder = "Contest_Ranking/" + contest_title_slug + "/"
        question_dict = {}
        submission_record = {}
        # submission_record[question_title_slug] = [users who submitted successfully]

        first_file = folder + "1.json"
        if not os.path.exists(first_file): 
            # print('[Contest=%s] does not exist' % contest_title_slug)
            return True

        
        # print('loading [file=%s]' % first_file)
        file_content = IO_Helper.loadJSON(first_file)
        # print(file_content)
        questions_list = file_content['questions']
            # print(questions_list)
        

        # print(questions_list)
        all_processed = True

        for question in questions_list:
            question_title_slug = question['title_slug']
            file_name = 'Passed_User/' + question_title_slug + '.json'
            if not os.path.exists(file_name):
                all_processed = False

        if all_processed: 
            print('Processed all questions in [Contest=%s]' % contest_title_slug)
            return True
        print('Now processing [Contest=%s]' % contest_title_slug)

        for page in range(1, 501):
            # print('Processing [page=%s] in [Contest=%s]' % (str(page), contest_title_slug))
            path = folder + str(page) + ".json"
            # print(path)
            if not os.path.exists(path): break
            # print(path)
            file_content = IO_Helper.loadJSON(path)

            submissions_list = file_content['submissions']
            questions_list = file_content['questions']
            user_rank_list = file_content['total_rank']

            for question in questions_list:
                question_id_str = str(question['question_id'])
                question_dict[question_id_str] = {
                    'question_title' : question['title'],
                    'question_title_slug' : question['title_slug'],
                }

            size = len(user_rank_list)
            for i in range(size):
                submission = submissions_list[i]
                user_info = user_rank_list[i]
                user_slug = user_info['user_slug']
                user_region = user_info['data_region']
                for question_key in submission:
                    question_title_slug = question_dict[question_key]['question_title_slug']
                    # file_name = 'Passed_User/' + question_title_slug + '.json'
                    # if os.path.exists(file_name): continue
                    if question_title_slug not in submission_record: submission_record[question_title_slug] = []
                    submission_record[question_title_slug].append(
                    {
                        'user_slug':user_slug,
                        'user_region' : user_region
                    })    
                    
        for question_title_slug in submission_record:
            file_name = 'Passed_User/' + question_title_slug + '.json'
            print(file_name)
        # CONTEST_QUESTION_PASS_RECORD[contest_title_slug] = submission_record
            IO_Helper.writeJSON(file_name, submission_record[question_title_slug])
        # CONTEST_QUESTION_PASS_RECORD[contest_title_slug] = 1
        # IO_Helper.write_append_JSON(CONTEST_QUESTION_PASS_RECORD_FILENAME, CONTEST_QUESTION_PASS_RECORD)
        return True
    except Exception as err:
        traceback.print_exc()

def get_All_user_count():
    Contest_MetaData = IO_Helper.loadContestMetadata()
    User_Rating_record = IO_Helper.loadUserRating(collections.defaultdict(dict))
    base_folder = 'Contest_Ranking/'
    user_dict = set()
    for contest_title_slug in Contest_MetaData:
        target_folder = base_folder + contest_title_slug
        contest_user_dict = set()
        for file in os.listdir(target_folder):
            full_path = os.path.join(target_folder, file)
            # print(full_path)
            file_content = IO_Helper.loadJSON(full_path)
            # print(file_content)
            user_rank_list = file_content['total_rank']
            for user_info in user_rank_list:
                user_slug = user_info['user_slug']
                # print(user_slug)
                user_dict.add(user_slug)
                contest_user_dict.add(user_slug)
        print('contest=%s usercount=%s' % (contest_title_slug, len(contest_user_dict)))
    print(len(user_dict))

def get_all_user_submission_count(USERNAME):
    base_folder = 'User_Submission/'

    data = {
        'operationName': "getUserProfile",
        # 'query': "query getUserProfile($username: String!) {\n  allQuestionsCount {\n    difficulty\n    count\n    __typename\n  }\n  matchedUser(username: $username) {\n    username\n    socialAccounts\n    githubUrl\n    contributions {\n      points\n      questionCount\n      testcaseCount\n      __typename\n    }\n    profile {\n      realName\n      websites\n      countryName\n      skillTags\n      company\n      school\n      starRating\n      aboutMe\n      userAvatar\n      reputation\n      ranking\n      __typename\n    }\n    submissionCalendar\n    submitStats: submitStatsGlobal {\n      acSubmissionNum {\n        difficulty\n        count\n        submissions\n        __typename\n      }\n      totalSubmissionNum {\n        difficulty\n        count\n        submissions\n        __typename\n      }\n      __typename\n    }\n    badges {\n      id\n      displayName\n      icon\n      creationDate\n      __typename\n    }\n    upcomingBadges {\n      name\n      icon\n      __typename\n    }\n    activeBadge {\n      id\n      __typename\n    }\n    __typename\n  }\n}\n",
        'query' : "query getUserProfile($username: String!) {\n  matchedUser(username: $username) {\n submitStats: submitStatsGlobal {\n      totalSubmissionNum {\n        difficulty\n        count\n        submissions\n        }}}}",
        'variables': '{username: "' + USERNAME + '"}'
    }

if __name__ == '__main__':
    writeRecord(loadJSON('Contest_MetaData.json'))
    # parseContest(65)
    # jplag(143)
    # print(os.getcwd())




# 