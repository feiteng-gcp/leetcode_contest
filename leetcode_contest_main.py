import os, requests, json, pathlib, subprocess, pytz, time, stat
from datetime import datetime

import Crawlers, IO_Helper, uploadToGCP

if __name__ == '__main__':

    debug = True
    page_end = 20   # check for top 500 people
    submission_record_file = 'submission_record'
    submission_record = IO_Helper.loadSubmissionRecord(submission_record_file, {})
    while True:
        # try:
        contest = IO_Helper.loadContest().strip()
        contest_int = (int)(contest)


        print(contest)
        
        # if not debug: 
        Crawlers.fetchContestRankingPage(contest)
        # if not debug: 
        found_new_crawl = Crawlers.crawlSubmissions(contest, page_end, submission_record)
        
        if found_new_crawl:
            IO_Helper.jplag(contest)
            uploadToGCP.uploadFolder('JPLAGResult/' + contest)
            IO_Helper.writeToHTML()
            IO_Helper.commit_and_pushtoGithub('index.html')
            
        if debug: 
            print('finished..')
            # break

        # if not debug: 
        

        # if not debug: 
        

        # print(submission_record)

        contest_int = contest_int + 1
        IO_Helper.writeContest(contest_int)
        IO_Helper.writeRecord(submission_record, submission_record_file)
        
        
        # except Exception as err:
        #     print(err)
        #     pass
            

        # if page_end < 500: break   


