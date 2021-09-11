import os, requests, json, pathlib, subprocess, pytz, time, stat
from datetime import datetime

import Crawlers, IO_Helper, uploadToGCP

if __name__ == '__main__':

    relativePath = str(pathlib.Path().resolve())
    # print(relativePath)
    local = False
    if relativePath.startswith('C:'):
        local = True
    page_end = 2   # check for top 500 people
    submission_record_file = 'submission_record'
    submission_record = IO_Helper.loadSubmissionRecord(submission_record_file, {})
    while True:
        
        contest = IO_Helper.loadContest().strip()
        contest_int = (int)(contest)

        # if not debug: 
        Crawlers.fetchContestRankingPage(contest)
        # if not debug: 
        found_new_crawl = Crawlers.crawlSubmissions(contest, page_end, submission_record)
        
        if found_new_crawl and not local:
            IO_Helper.jplag(contest)
            uploadToGCP.uploadFolder('JPLAGResult/' + contest)
            IO_Helper.writeToHTML()
            IO_Helper.commit_and_pushtoGithub('index.html')

        contest_int = contest_int + 1
        IO_Helper.writeContest(contest_int)
        IO_Helper.writeRecord(submission_record, submission_record_file)
    